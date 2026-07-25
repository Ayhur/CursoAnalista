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
from reportlab.platypus import PageBreak, Paragraph, Preformatted, SimpleDocTemplate, Spacer

ROOT = Path(__file__).resolve().parents[1]
COURSE_DIR = ROOT / "curso"
DIST_MD = ROOT / "dist" / "markdown"
DIST_PDF = ROOT / "dist" / "pdf"


def chapter_paths() -> list[Path]:
    return sorted(path for path in COURSE_DIR.glob("[0-9][0-9]-*/README.md"))


def clean_markdown(text: str) -> str:
    """Normaliza contenido destinado a la concatenación y al PDF."""
    return text.replace("\r\n", "\n").strip() + "\n"


def write_consolidated_markdown(chapters: list[Path]) -> Path:
    DIST_MD.mkdir(parents=True, exist_ok=True)
    output = DIST_MD / "temario-completo.md"
    parts = ["# Temario completo - Curso de Analista de Datos con Python\n"]
    for chapter in chapters:
        parts.append(clean_markdown(chapter.read_text(encoding="utf-8")))
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
                story.append(Preformatted("\n".join(code_lines), styles_map["code"]))
                code_lines = []
            in_code = not in_code
            continue
        if in_code:
            code_lines.append(line)
            continue
        if not line.strip():
            flush_list()
            story.append(Spacer(1, 3))
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
        build_pdf(clean_markdown(chapter.read_text(encoding="utf-8")), DIST_PDF / f"{slug}.pdf")
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
