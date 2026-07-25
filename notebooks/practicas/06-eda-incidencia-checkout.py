"""Laboratorio reproducible del bloque 06: EDA de una caída de checkout.

Ejecutar desde la raíz del repositorio:
    python notebooks/practicas/06-eda-incidencia-checkout.py
"""

from __future__ import annotations

import csv
from collections import defaultdict
from datetime import date
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
DATASET = ROOT / "datasets" / "nebula_checkout_mayo.csv"
ACTUAL_INICIO = date(2025, 5, 5)
ACTUAL_FIN = date(2025, 5, 11)


def cargar() -> list[dict[str, object]]:
    with DATASET.open(encoding="utf-8", newline="") as archivo:
        filas = []
        for fila in csv.DictReader(archivo):
            filas.append(
                {
                    "fecha": date.fromisoformat(fila["fecha"]),
                    "plataforma": fila["plataforma"],
                    "canal": fila["canal"],
                    "visitas": int(fila["visitas"]),
                    "compras": int(fila["compras"]),
                }
            )
    return filas


def tasa(filas: list[dict[str, object]]) -> tuple[int, int, float]:
    visitas = sum(int(fila["visitas"]) for fila in filas)
    compras = sum(int(fila["compras"]) for fila in filas)
    return compras, visitas, compras / visitas if visitas else 0.0


def periodo(fila: dict[str, object]) -> str:
    return "actual" if ACTUAL_INICIO <= fila["fecha"] <= ACTUAL_FIN else "referencia"


def main() -> None:
    filas = cargar()
    claves = [(f["fecha"], f["plataforma"], f["canal"]) for f in filas]
    print("PERFIL DEL ARCHIVO")
    print(f"Filas: {len(filas)} | columnas: fecha, plataforma, canal, visitas, compras")
    print(f"Cobertura: {min(f['fecha'] for f in filas)} a {max(f['fecha'] for f in filas)}")
    print(f"Duplicados por fecha/plataforma/canal: {len(claves) - len(set(claves))}")
    print(f"Rangos: visitas {min(f['visitas'] for f in filas)}-{max(f['visitas'] for f in filas)}; "
          f"compras {min(f['compras'] for f in filas)}-{max(f['compras'] for f in filas)}")

    grupos: dict[tuple[str, str], list[dict[str, object]]] = defaultdict(list)
    for fila in filas:
        grupos[(periodo(fila), str(fila["plataforma"]))].append(fila)

    print("\nTASAS PONDERADAS (compras / visitas)")
    for clave in sorted(grupos):
        compras, visitas, conversion = tasa(grupos[clave])
        print(f"{clave[0]:10} {clave[1]:8}: {compras:3}/{visitas:5} = {conversion:.2%}")

    for nombre in ("referencia", "actual"):
        subconjunto = [fila for fila in filas if periodo(fila) == nombre]
        compras, visitas, conversion = tasa(subconjunto)
        print(f"{nombre:10} total   : {compras:3}/{visitas:5} = {conversion:.2%}")

    alertas = [fila for fila in filas if fila["visitas"] > 0 and fila["compras"] == 0]
    print("\nALERTA DE CALIDAD / PRODUCTO")
    for fila in alertas:
        print(f"{fila['fecha']} | {fila['plataforma']}/{fila['canal']}: "
              f"{fila['visitas']} visitas y 0 compras. No borrar: contrastar pagos y tracking.")

    print("\nCONCLUSION RESPONSABLE")
    print("El archivo permite observar una caída concentrada en Android. No permite elegir entre "
          "incidencia de checkout, cambio de mezcla o tracking incompleto; solicitar errores y pagos confirmados.")


if __name__ == "__main__":
    main()
