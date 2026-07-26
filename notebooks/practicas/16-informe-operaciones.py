"""Laboratorio del bloque 16: SQLite -> controles -> libro Excel.

Instala dependencias en Colab o local: pip install pandas openpyxl
El ejemplo crea una base didáctica local. En producción la conexión, credenciales
y tabla vendrían de un sistema con permisos de solo lectura.
"""

from __future__ import annotations

import argparse
import logging
import sqlite3
from datetime import datetime, timezone
from pathlib import Path

import pandas as pd
from openpyxl import load_workbook
from openpyxl.styles import Font, PatternFill

ROOT = Path(__file__).resolve().parents[2]
DATABASE = ROOT / "datasets" / "temario-16" / "operaciones.sqlite"
OUTPUT = ROOT / "salidas"


def crear_base_si_falta() -> None:
    DATABASE.parent.mkdir(parents=True, exist_ok=True)
    with sqlite3.connect(DATABASE) as conexion:
        conexion.execute(
            """CREATE TABLE IF NOT EXISTS operaciones (
                operacion_id TEXT PRIMARY KEY, fecha_utc TEXT NOT NULL,
                estado TEXT NOT NULL, importe_eur REAL, canal TEXT NOT NULL,
                es_prueba INTEGER NOT NULL DEFAULT 0
            )"""
        )
        if conexion.execute("SELECT COUNT(*) FROM operaciones").fetchone()[0] == 0:
            conexion.executemany(
                "INSERT INTO operaciones VALUES (?, ?, ?, ?, ?, ?)",
                [
                    ("op-001", "2026-07-13T08:00:00Z", "pagada", 120.0, "web", 0),
                    ("op-002", "2026-07-14T09:30:00Z", "rechazada", 80.0, "app", 0),
                    ("op-003", "2026-07-15T10:00:00Z", "pagada", 50.0, "web", 0),
                    ("op-004", "2026-07-16T14:15:00Z", "devuelta", 30.0, "partner", 0),
                    ("op-005", "2026-07-17T12:20:00Z", "pendiente", 25.0, "app", 0),
                    ("op-test", "2026-07-18T10:00:00Z", "pagada", 1.0, "web", 1),
                ],
            )


def cargar(inicio: str, fin: str) -> pd.DataFrame:
    sql = """
    SELECT operacion_id, fecha_utc, estado, importe_eur, canal, es_prueba
    FROM operaciones
    WHERE fecha_utc >= :inicio AND fecha_utc < :fin
    """
    with sqlite3.connect(DATABASE) as conexion:
        return pd.read_sql_query(sql, conexion, params={"inicio": inicio, "fin": fin})


def validar(datos: pd.DataFrame, inicio: str, fin: str) -> pd.DataFrame:
    controles = []
    requeridas = {"operacion_id", "fecha_utc", "estado", "importe_eur", "canal", "es_prueba"}
    controles.append(("columnas requeridas", requeridas.issubset(datos.columns), ", ".join(sorted(requeridas - set(datos.columns)))))
    controles.append(("IDs únicos", not datos["operacion_id"].duplicated().any(), str(datos["operacion_id"].duplicated().sum())))
    datos["fecha_utc"] = pd.to_datetime(datos["fecha_utc"], utc=True)
    inicio_dt, fin_dt = pd.Timestamp(inicio, tz="UTC"), pd.Timestamp(fin, tz="UTC")
    dentro = datos["fecha_utc"].ge(inicio_dt).all() and datos["fecha_utc"].lt(fin_dt).all()
    controles.append(("fechas dentro de [inicio, fin)", dentro, f"{datos['fecha_utc'].min()} — {datos['fecha_utc'].max()}"))
    pagadas = datos.query("es_prueba == 0 and estado == 'pagada'")
    controles.append(("importe pagado no nulo", pagadas["importe_eur"].notna().all(), str(pagadas["importe_eur"].isna().sum())))
    return pd.DataFrame(controles, columns=["control", "superado", "detalle"])


def generar_libro(datos: pd.DataFrame, controles: pd.DataFrame, inicio: str, fin: str) -> Path:
    salida = OUTPUT / f"operaciones_{inicio}_a_{fin}.xlsx"
    OUTPUT.mkdir(exist_ok=True)
    elegibles = datos.query("es_prueba == 0").copy()
    # Excel no conserva la zona horaria en sus fechas. La declaramos en el
    # nombre y exportamos ISO 8601 para no convertir silenciosamente UTC a la
    # zona local de quien abre el libro.
    elegibles["fecha_utc"] = elegibles["fecha_utc"].dt.strftime("%Y-%m-%dT%H:%M:%SZ")
    pagadas = elegibles.query("estado == 'pagada'").copy()
    rechazados = elegibles.query("estado != 'pagada'").copy()
    rechazados["motivo_exclusion_total"] = "estado distinto de pagada"
    resumen = pd.DataFrame(
        {
            "indicador": ["Intentos elegibles", "Operaciones pagadas", "Importe cobrado EUR"],
            "valor": [len(elegibles), len(pagadas), pagadas["importe_eur"].sum()],
        }
    )
    por_canal = pagadas.groupby("canal", as_index=False)["importe_eur"].sum().rename(columns={"importe_eur": "importe_pagado_eur"})
    metadatos = pd.DataFrame(
        {
            "campo": ["inicio_inclusivo_utc", "fin_exclusivo_utc", "generado_utc", "fuente", "estado_controles"],
            "valor": [inicio, fin, datetime.now(timezone.utc).isoformat(), "SQLite didáctica: operaciones", "APTO" if controles["superado"].all() else "BLOQUEADO"],
        }
    )
    with pd.ExcelWriter(salida, engine="openpyxl") as writer:
        resumen.to_excel(writer, sheet_name="Resumen", index=False, startrow=0)
        por_canal.to_excel(writer, sheet_name="Resumen", index=False, startrow=len(resumen) + 3)
        elegibles.to_excel(writer, sheet_name="Detalle", index=False)
        rechazados.to_excel(writer, sheet_name="Rechazados", index=False)
        controles.to_excel(writer, sheet_name="Conciliacion", index=False)
        metadatos.to_excel(writer, sheet_name="Metadatos", index=False)
    libro = load_workbook(salida)
    for hoja in libro.worksheets:
        hoja.freeze_panes = "A2"
        hoja.auto_filter.ref = hoja.dimensions
        for celda in hoja[1]:
            celda.font = Font(bold=True, color="FFFFFF")
            celda.fill = PatternFill("solid", fgColor="1D5D84")
        for columna in hoja.columns:
            letra = columna[0].column_letter
            hoja.column_dimensions[letra].width = min(42, max(12, max(len(str(c.value or "")) for c in columna) + 2))
    libro.save(salida)
    return salida


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--inicio", default="2026-07-13")
    parser.add_argument("--fin", default="2026-07-20")
    args = parser.parse_args()
    logging.basicConfig(level=logging.INFO, format="%(levelname)s %(message)s")
    crear_base_si_falta()
    datos = cargar(args.inicio, args.fin)
    controles = validar(datos, args.inicio, args.fin)
    if not controles["superado"].all():
        logging.error("Informe bloqueado:\n%s", controles.to_string(index=False))
        raise SystemExit(2)
    ruta = generar_libro(datos, controles, args.inicio, args.fin)
    logging.info("Informe generado: %s", ruta)


if __name__ == "__main__":
    main()
