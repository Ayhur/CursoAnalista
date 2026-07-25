"""Laboratorio reproducible del bloque 01. Ejecutar desde la raíz del repositorio."""
from __future__ import annotations

import csv
import json
from collections import Counter, defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
DATA = ROOT / "datasets" / "temario-01"


def read_orders() -> list[dict[str, str]]:
    with (DATA / "pedidos.csv").open(encoding="utf-8", newline="") as file:
        return list(csv.DictReader(file, delimiter=";"))


def euros(value: str) -> float:
    return float(value.replace(",", "."))


orders = read_orders()
print(f"Filas leídas en pedidos: {len(orders)}; grano declarado: un pedido por fila.")

ids = [row["pedido_id"] for row in orders]
duplicates = [key for key, count in Counter(ids).items() if count > 1]
missing_dates = [row["pedido_id"] for row in orders if not row["creado_en_utc"]]
allowed_channels = {"web", "app", "partner"}
unknown_channels = sorted({row["canal"] for row in orders} - allowed_channels)
print("Duplicados de pedido_id:", duplicates)
print("Pagados sin fecha UTC:", missing_dates)
print("Canales fuera del contrato:", unknown_channels)

# Deduplicar por ID para una métrica de pedidos, conservando primera evidencia y registrando incidencia.
unique_orders: dict[str, dict[str, str]] = {}
for row in orders:
    unique_orders.setdefault(row["pedido_id"], row)

known_paid = [
    row for row in unique_orders.values()
    if row["estado"] == "pagado" and row["creado_en_utc"]
]
print("Pedidos pagados con fecha conocida:", len(known_paid))
print("Ingreso defendible para el corte:", sum(euros(row["total_eur"]) for row in known_paid))

with (DATA / "lineas_pedido.csv").open(encoding="utf-8", newline="") as file:
    lines = list(csv.DictReader(file, delimiter=";"))

# Simulación visible de join: el total de pedido se repite por cada línea.
by_order = {row["pedido_id"]: row for row in unique_orders.values()}
joined = [{**line, "total_pedido": by_order[line["pedido_id"]]["total_eur"]} for line in lines]
wrong_total = sum(euros(row["total_pedido"]) for row in joined)
right_total = sum(euros(row["total_eur"]) for row in known_paid)
print(f"Join pedidos × líneas: {len(joined)} filas; grano: una línea de pedido.")
print(f"Suma INCORRECTA de total_pedido tras join: {wrong_total:.2f} €")
print(f"Suma CORRECTA en pedidos pagados y fechados: {right_total:.2f} €")

units = defaultdict(int)
for line in lines:
    units[line["producto_id"]] += int(line["cantidad"])
print("Unidades por producto:", dict(units))

with (DATA / "pedido-ejemplo.json").open(encoding="utf-8") as file:
    payload = json.load(file)
print("JSON convertido conceptualmente a 1 pedido y", len(payload["items"]), "líneas.")
