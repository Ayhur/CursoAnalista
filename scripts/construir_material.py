#!/usr/bin/env python3
"""Genera Markdown consolidado y PDFs descargables del curso."""

from __future__ import annotations

import argparse
import html
import re
from pathlib import Path

from reportlab.lib.colors import HexColor
from reportlab.lib.enums import TA_CENTER
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import cm
from reportlab.platypus import Flowable, Paragraph, Preformatted, SimpleDocTemplate, Spacer

ROOT = Path(__file__).resolve().parents[1]
COURSE_DIR = ROOT / "curso"
DIST_MD = ROOT / "dist" / "markdown"
DIST_PDF = ROOT / "dist" / "pdf"


class MermaidFlow(Flowable):
    """Dibuja en PDF una parte segura y semántica de los flowcharts Mermaid."""

    node_pattern = re.compile(r"(?P<id>[A-Za-z0-9_]+)\[(?P<label>[^]]+)\]")
    edge_pattern = re.compile(
        r"(?P<source>[A-Za-z0-9_]+)(?:\[[^]]+\])?\s*-->\s*(?:\|(?P<label>[^|]+)\|\s*)?(?P<target>[A-Za-z0-9_]+)"
    )

    def __init__(self, source: str):
        super().__init__()
        self.labels: dict[str, str] = {}
        self.order: list[str] = []
        for match in self.node_pattern.finditer(source):
            node_id = match.group("id")
            label = re.sub(r"<br\s*/?>", " - ", match.group("label"), flags=re.IGNORECASE)
            self.labels[node_id] = label
            if node_id not in self.order:
                self.order.append(node_id)
        self.edges = []
        for match in self.edge_pattern.finditer(source):
            source_id, target_id = match.group("source"), match.group("target")
            if source_id not in self.labels:
                self.labels[source_id] = source_id
                self.order.append(source_id)
            if target_id not in self.labels:
                self.labels[target_id] = target_id
                self.order.append(target_id)
            self.edges.append((source_id, target_id, match.group("label") or ""))
        if not self.order:
            self.labels = {"fallback": "Diagrama no compatible"}
            self.order = ["fallback"]
        self.ranks = self._ranks()
        self.height = max(2.4 * cm, (len(self.ranks) * 1.65 + 0.5) * cm)

    def _ranks(self):
        """Agrupa nodos por nivel sin inventar una cadena para las ramas.

        Kahn resuelve los grafos acíclicos (el caso habitual). Si hay un ciclo,
        conserva sus nodos en un nivel estable y permite que la arista de retorno
        se dibuje hacia arriba: es preferible a iterar sin fin o falsificarlo.
        """
        children = {node: [] for node in self.order}
        pending = {node: 0 for node in self.order}
        for source, target, _ in self.edges:
            children[source].append(target)
            pending[target] += 1

        rank = {node: 0 for node in self.order}
        queue = [node for node in self.order if pending[node] == 0]
        processed = set()
        while queue:
            node = queue.pop(0)
            processed.add(node)
            for child in children[node]:
                rank[child] = max(rank[child], rank[node] + 1)
                pending[child] -= 1
                if pending[child] == 0:
                    queue.append(child)

        # Los ciclos no tienen una jerarquía dirigida válida. Se sitúan de
        # forma determinista tras sus predecesores ya resueltos, sin introducir
        # niveles vacíos ni forzar una relación inexistente entre hermanos.
        for node in self.order:
            if node not in processed:
                parent_ranks = [
                    rank[source]
                    for source, target, _ in self.edges
                    if target == node and source in processed
                ]
                rank[node] = max(parent_ranks, default=0) + (1 if parent_ranks else 0)

        levels = {}
        for node in self.order:
            levels.setdefault(rank[node], []).append(node)
        return [levels[level] for level in sorted(levels)]

    def wrap(self, available_width, available_height):
        self.width = available_width
        return available_width, self.height

    def draw(self):
        canvas = self.canv
        box_height = 0.68 * cm
        positions = {}
        for level, nodes in enumerate(self.ranks):
            count = len(nodes)
            if not count:
                continue
            box_width = min(5.0 * cm, max(2.5 * cm, (self.width - (count + 1) * 0.35 * cm) / count))
            y = self.height - (level + 1) * 1.5 * cm
            for index, node in enumerate(nodes):
                x = (self.width - (count * box_width + (count - 1) * 0.35 * cm)) / 2 + index * (box_width + 0.35 * cm)
                positions[node] = (x, y, box_width, box_height)
        for source, target, edge_label in self.edges:
            if source not in positions or target not in positions:
                continue
            sx, sy, sw, _ = positions[source]
            tx, ty, tw, th = positions[target]
            start_x, start_y = sx + sw / 2, sy
            end_x, end_y = tx + tw / 2, ty + th
            canvas.setStrokeColor(HexColor("#667085"))
            canvas.line(start_x, start_y, end_x, end_y)
            canvas.line(end_x, end_y, end_x - 3, end_y + 5)
            canvas.line(end_x, end_y, end_x + 3, end_y + 5)
            if edge_label:
                canvas.setFillColor(HexColor("#475467"))
                canvas.setFont("Helvetica", 6.5)
                canvas.drawCentredString((start_x + end_x) / 2, (start_y + end_y) / 2, edge_label[:28])
        for node in self.order:
            x, y, box_width, box_height = positions[node]
            canvas.setFillColor(HexColor("#EAF2F8"))
            canvas.setStrokeColor(HexColor("#1D5D84"))
            canvas.roundRect(x, y, box_width, box_height, 4, fill=1, stroke=1)
            canvas.setFillColor(HexColor("#12355B"))
            canvas.setFont("Helvetica", 8.5)
            canvas.drawCentredString(x + box_width / 2, y + 0.24 * cm, self.labels[node][:56])


def chapter_paths() -> list[Path]:
    return sorted(path for path in COURSE_DIR.glob("[0-9][0-9]-*/README.md"))


def block_markdown(chapter: Path) -> str:
    """Consolida el índice del bloque y sus lecciones en orden pedagógico."""
    lessons_dir = chapter.parent / "lecciones"
    sources = [chapter]
    if lessons_dir.exists():
        sources.extend(sorted(lessons_dir.glob("*.md")))
    return "\n".join(clean_markdown(source.read_text(encoding="utf-8")) for source in sources)


def clean_markdown(text: str) -> str:
    """Normaliza contenido destinado a la concatenación y al PDF."""
    return text.replace("\r\n", "\n").strip() + "\n"


def write_consolidated_markdown(chapters: list[Path]) -> Path:
    DIST_MD.mkdir(parents=True, exist_ok=True)
    output = DIST_MD / "temario-completo.md"
    parts = ["# Temario completo - Curso de Analista de Datos con Python\n"]
    for chapter in chapters:
        parts.append(block_markdown(chapter))
    output.write_text("\n".join(parts), encoding="utf-8")
    return output


def styles() -> dict[str, ParagraphStyle]:
    base = getSampleStyleSheet()
    return {
        "title": ParagraphStyle("CourseTitle", parent=base["Title"], fontName="Helvetica-Bold", fontSize=24, leading=29, textColor=HexColor("#12355B"), alignment=TA_CENTER, spaceAfter=18),
        "h1": ParagraphStyle("CourseH1", parent=base["Heading1"], fontName="Helvetica-Bold", fontSize=18, leading=23, textColor=HexColor("#12355B"), spaceBefore=16, spaceAfter=10),
        "h2": ParagraphStyle("CourseH2", parent=base["Heading2"], fontName="Helvetica-Bold", fontSize=14, leading=18, textColor=HexColor("#1D5D84"), spaceBefore=12, spaceAfter=7),
        "body": ParagraphStyle("CourseBody", parent=base["BodyText"], fontName="Helvetica", fontSize=10.5, leading=15, spaceAfter=7),
        "bullet": ParagraphStyle("CourseBullet", parent=base["BodyText"], fontName="Helvetica", fontSize=10.5, leading=14, leftIndent=14, firstLineIndent=-8, spaceAfter=4),
        "code": ParagraphStyle("CourseCode", fontName="Courier", fontSize=8.5, leading=11, backColor=HexColor("#F2F4F7"), borderPadding=7, spaceBefore=5, spaceAfter=9),
    }


def inline_markdown(value: str) -> str:
    escaped = html.escape(value)
    escaped = re.sub(r"`([^`]+)`", r"<font name='Courier'>\1</font>", escaped)
    escaped = re.sub(r"\*\*([^*]+)\*\*", r"<b>\1</b>", escaped)
    escaped = re.sub(r"\[([^]]+)\]\(([^)]+)\)", r"<link href='\2' color='#1D5D84'>\1</link>", escaped)
    return escaped


def markdown_to_story(text: str, styles_map: dict[str, ParagraphStyle]) -> list:
    story: list = []
    in_code = False
    code_language = ""
    code_lines: list[str] = []
    list_buffer: list[str] = []

    def flush_list() -> None:
        nonlocal list_buffer
        for item in list_buffer:
            story.append(Paragraph("- " + inline_markdown(item), styles_map["bullet"]))
        list_buffer = []

    for raw_line in text.splitlines():
        line = raw_line.rstrip()
        if line.startswith("```"):
            flush_list()
            if in_code:
                if code_language == "mermaid":
                    story.append(MermaidFlow("\n".join(code_lines)))
                    story.append(Spacer(1, 8))
                else:
                    story.append(Preformatted("\n".join(code_lines), styles_map["code"]))
                code_lines = []
                code_language = ""
            else:
                code_language = line[3:].strip().lower()
            in_code = not in_code
            continue
        if in_code:
            code_lines.append(line)
            continue
        if not line.strip():
            flush_list()
            story.append(Spacer(1, 3))
            continue
        if line.startswith("<!-- mobile-diagram:") or line.startswith("![Diagrama:"):
            continue
        if line in {"<details>", "</details>"} or line.startswith("<summary>"):
            continue
        if line.startswith("# "):
            flush_list()
            story.append(Paragraph(inline_markdown(line[2:]), styles_map["title"]))
        elif line.startswith("## "):
            flush_list()
            story.append(Paragraph(inline_markdown(line[3:]), styles_map["h1"]))
        elif line.startswith("### "):
            flush_list()
            story.append(Paragraph(inline_markdown(line[4:]), styles_map["h2"]))
        elif re.match(r"^[-*] ", line):
            list_buffer.append(line[2:])
        elif re.match(r"^\d+\. ", line):
            flush_list()
            story.append(Paragraph(inline_markdown(line), styles_map["bullet"]))
        elif line.startswith("> "):
            flush_list()
            story.append(Paragraph(inline_markdown(line[2:]), styles_map["body"]))
        elif line.startswith("|") or line.startswith("---"):
            # Las tablas se conservan en Markdown; el PDF inicial prioriza texto legible.
            continue
        else:
            flush_list()
            story.append(Paragraph(inline_markdown(line), styles_map["body"]))
    flush_list()
    if in_code:
        raise ValueError("Hay un bloque de código sin cerrar")
    return story


def add_page_number(canvas, doc) -> None:
    canvas.saveState()
    canvas.setFont("Helvetica", 8)
    canvas.setFillColor(HexColor("#667085"))
    canvas.drawString(1.8 * cm, 1.2 * cm, "Curso de Analista de Datos con Python")
    canvas.drawRightString(A4[0] - 1.8 * cm, 1.2 * cm, f"Página {doc.page}")
    canvas.restoreState()


def build_pdf(markdown: str, output: Path) -> None:
    output.parent.mkdir(parents=True, exist_ok=True)
    document = SimpleDocTemplate(
        str(output), pagesize=A4,
        rightMargin=1.8 * cm, leftMargin=1.8 * cm, topMargin=1.8 * cm, bottomMargin=1.8 * cm,
        title="Curso de Analista de Datos con Python",
        author="Ayhur",
    )
    document.build(markdown_to_story(markdown, styles()), onFirstPage=add_page_number, onLaterPages=add_page_number)


def build_all() -> None:
    chapters = chapter_paths()
    if not chapters:
        raise SystemExit("No se encontraron capítulos en curso/")
    for chapter in chapters:
        slug = chapter.parent.name
        build_pdf(block_markdown(chapter), DIST_PDF / f"{slug}.pdf")
    full_markdown = write_consolidated_markdown(chapters)
    build_pdf(full_markdown.read_text(encoding="utf-8"), DIST_PDF / "temario-completo.pdf")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--all", action="store_true", help="Genera todos los PDFs y el Markdown consolidado")
    args = parser.parse_args()
    if args.all:
        build_all()
    else:
        parser.error("Usa --all")


if __name__ == "__main__":
    main()
