#!/usr/bin/env python3
"""Genera fallbacks SVG para los diagramas Mermaid visibles en GitHub Mobile.

GitHub web renderiza Mermaid, pero algunos visores móviles muestran el bloque como
código. Este script conserva la fuente Mermaid dentro de ``details`` y coloca una
imagen SVG delante, de modo que el diagrama se vea en ambos entornos.
"""

from __future__ import annotations

import argparse
import hashlib
import html
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
COURSE = ROOT / "curso"
ASSETS = ROOT / "recursos" / "diagramas-moviles"
MERMAID = re.compile(r"```mermaid\n(?P<body>.*?)\n```", re.DOTALL)
NODE = re.compile(
    r"(?P<id>[A-Za-z0-9_]+)(?:\[(?P<square>[^]]+)\]|\((?P<round>[^)]+)\)|\{(?P<curly>[^}]+)\})"
)
EDGE = re.compile(
    r"(?P<source>[A-Za-z0-9_]+)(?:\[[^]]+\]|\([^)]+\)|\{[^}]+\})?\s*--?>\s*"
    r"(?:\|(?P<label>[^|]+)\|\s*)?(?P<target>[A-Za-z0-9_]+)"
)


def normalise_label(label: str) -> str:
    return re.sub(r"<br\s*/?>", " — ", label, flags=re.IGNORECASE).strip(' "')


def parse(source: str) -> tuple[list[str], dict[str, str], list[tuple[str, str, str]]]:
    order: list[str] = []
    labels: dict[str, str] = {}
    for match in NODE.finditer(source):
        node = match.group("id")
        label = next(value for value in (match.group("square"), match.group("round"), match.group("curly")) if value is not None)
        labels[node] = normalise_label(label)
        if node not in order:
            order.append(node)
    edges: list[tuple[str, str, str]] = []
    for match in EDGE.finditer(source):
        source_id, target_id = match.group("source"), match.group("target")
        for node in (source_id, target_id):
            if node not in labels:
                labels[node] = node
                order.append(node)
        edges.append((source_id, target_id, (match.group("label") or "").strip()))
    return order or ["fallback"], labels or {"fallback": "Diagrama Mermaid"}, edges


def ranks(order: list[str], edges: list[tuple[str, str, str]]) -> list[list[str]]:
    children = {node: [] for node in order}
    pending = {node: 0 for node in order}
    for source, target, _ in edges:
        children[source].append(target)
        pending[target] += 1
    rank = {node: 0 for node in order}
    queue = [node for node in order if pending[node] == 0]
    processed: set[str] = set()
    while queue:
        node = queue.pop(0)
        processed.add(node)
        for child in children[node]:
            rank[child] = max(rank[child], rank[node] + 1)
            pending[child] -= 1
            if pending[child] == 0:
                queue.append(child)
    for node in order:
        if node not in processed:
            parents = [rank[source] for source, target, _ in edges if target == node and source in processed]
            rank[node] = max(parents, default=0) + (1 if parents else 0)
    grouped: dict[int, list[str]] = {}
    for node in order:
        grouped.setdefault(rank[node], []).append(node)
    return [grouped[level] for level in sorted(grouped)]


def wrap(label: str, width: int = 24) -> list[str]:
    words, lines, current = label.split(), [], ""
    for word in words:
        candidate = f"{current} {word}".strip()
        if current and len(candidate) > width:
            lines.append(current)
            current = word
        else:
            current = candidate
    if current:
        lines.append(current)
    return lines[:3] or [label[:width]]


def svg(source: str) -> str:
    order, labels, edges = parse(source)
    levels = ranks(order, edges)
    width, margin, box_h = 960, 36, 78
    height = max(190, 72 + len(levels) * 132)
    positions: dict[str, tuple[float, float, float]] = {}
    for level, nodes in enumerate(levels):
        count = len(nodes)
        box_w = min(250, max(145, (width - margin * 2 - (count - 1) * 18) / count))
        total = count * box_w + (count - 1) * 18
        start = (width - total) / 2
        y = 34 + level * 132
        for index, node in enumerate(nodes):
            positions[node] = (start + index * (box_w + 18), y, box_w)
    parts = [
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}" role="img">',
        '<title>Diagrama del curso</title><defs><marker id="arrow" markerWidth="10" markerHeight="10" refX="8" refY="3" orient="auto"><path d="M0,0 L0,6 L9,3 z" fill="#667085"/></marker></defs>',
        '<rect width="100%" height="100%" rx="12" fill="#ffffff"/>',
    ]
    for source_id, target_id, label in edges:
        sx, sy, sw = positions[source_id]
        tx, ty, tw = positions[target_id]
        start_x, start_y = sx + sw / 2, sy + box_h
        end_x, end_y = tx + tw / 2, ty
        parts.append(f'<path d="M {start_x:.1f} {start_y:.1f} L {end_x:.1f} {end_y:.1f}" stroke="#667085" stroke-width="2" fill="none" marker-end="url(#arrow)"/>')
        if label:
            parts.append(f'<text x="{(start_x + end_x) / 2:.1f}" y="{(start_y + end_y) / 2 - 5:.1f}" text-anchor="middle" font-family="Arial, sans-serif" font-size="14" fill="#475467">{html.escape(label[:34])}</text>')
    for node in order:
        x, y, box_w = positions[node]
        parts.append(f'<rect x="{x:.1f}" y="{y:.1f}" width="{box_w:.1f}" height="{box_h}" rx="10" fill="#EAF2F8" stroke="#1D5D84" stroke-width="2"/>')
        lines = wrap(labels[node])
        offset = y + box_h / 2 - (len(lines) - 1) * 10
        for index, line in enumerate(lines):
            parts.append(f'<text x="{x + box_w / 2:.1f}" y="{offset + index * 20:.1f}" text-anchor="middle" font-family="Arial, sans-serif" font-size="16" fill="#12355B">{html.escape(line)}</text>')
    return "\n".join(parts + ["</svg>", ""])


def asset_name(markdown: Path, number: int) -> str:
    stem = markdown.relative_to(ROOT).with_suffix("").as_posix().replace("/", "--")
    digest = hashlib.sha1(f"{markdown}:{number}".encode()).hexdigest()[:8]
    return f"{stem}-{number:02d}-{digest}.svg"


def transform(markdown: Path, check: bool) -> tuple[int, bool]:
    text = markdown.read_text(encoding="utf-8")
    changed = False
    count = 0

    def replacement(match: re.Match[str]) -> str:
        nonlocal changed, count
        count += 1
        before = text[max(0, match.start() - 300):match.start()]
        if "<!-- mobile-diagram: rendered fallback -->" in before:
            return match.group(0)
        name = asset_name(markdown, count)
        asset = ASSETS / name
        if not check:
            asset.parent.mkdir(parents=True, exist_ok=True)
            asset.write_text(svg(match.group("body")), encoding="utf-8")
        relative = Path(__import__('os').path.relpath(asset, markdown.parent)).as_posix()
        label = next(iter(parse(match.group("body"))[1].values()), "diagrama")
        changed = True
        return (
            "<!-- mobile-diagram: rendered fallback -->\n"
            f"![Diagrama: {label}]({relative})\n\n"
            "<details>\n<summary>Ver código Mermaid editable</summary>\n\n"
            f"{match.group(0)}\n"
            "</details>"
        )

    updated = MERMAID.sub(replacement, text)
    if check:
        expected = len(MERMAID.findall(text))
        visible = text.count("<!-- mobile-diagram: rendered fallback -->")
        image_paths = re.findall(r"!\[Diagrama:[^]]+\]\(([^)]+\.svg)\)", text)
        missing_assets = [markdown.parent / image_path for image_path in image_paths if not (markdown.parent / image_path).resolve().exists()]
        return expected, expected == visible and not missing_assets
    if changed:
        markdown.write_text(updated, encoding="utf-8")
    return count, True


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true", help="Falla si falta un fallback móvil")
    args = parser.parse_args()
    files = sorted(COURSE.glob("[0-9][0-9]-*/lecciones/*.md"))
    diagrams, valid = 0, True
    for file in files:
        count, okay = transform(file, args.check)
        diagrams += count
        valid = valid and okay
    if args.check and not valid:
        raise SystemExit("Faltan fallbacks SVG: ejecuta scripts/construir_diagramas_moviles.py")
    print(f"Diagramas procesados: {diagrams}")


if __name__ == "__main__":
    main()
