"""Pipeline reproducible del bloque 05.

Ejecuta desde la raíz del repositorio:
    python notebooks/practicas/05-pipeline-pedidos-nebula.py
"""
from pathlib import Path

import pandas as pd

ROOT = Path(__file__).resolve().parents[2]
DATA = ROOT / "datasets" / "pandas"
CANAL_VALIDOS = {"web", "app", "partner"}


def cargar_pedidos() -> pd.DataFrame:
    return pd.read_csv(
        DATA / "pedidos_nebula.csv", sep=";", encoding="utf-8",
        dtype={"pedido_id": "string", "cliente_id": "string", "canal": "string"},
        na_values=["", "NA", "sin dato"],
    )


def limpiar(pedidos_raw: pd.DataFrame) -> tuple[pd.DataFrame, pd.DataFrame]:
    pedidos = pedidos_raw.copy()
    pedidos["fecha_pedido"] = pd.to_datetime(
        pedidos["fecha_pedido"], format="%Y-%m-%d", errors="coerce", utc=True
    )
    pedidos["fecha_extraccion"] = pd.to_datetime(pedidos["fecha_extraccion"], utc=True)
    for columna in ["importe_bruto", "descuento"]:
        pedidos[columna] = pd.to_numeric(
            pedidos[columna].str.replace(",", ".", regex=False), errors="coerce"
        )
    pedidos["descuento"] = pedidos["descuento"].fillna(0)

    # Regla acordada: ante varias exportaciones del mismo pedido, conservar la más reciente.
    pedidos = pedidos.sort_values("fecha_extraccion").drop_duplicates("pedido_id", keep="last")
    es_valido = (
        pedidos["fecha_pedido"].notna()
        & pedidos["importe_bruto"].ge(0)
        & pedidos["canal"].isin(CANAL_VALIDOS)
    )
    rechazos = pedidos.loc[~es_valido].assign(motivo="fecha, importe o canal inválido")
    validos = pedidos.loc[es_valido & pedidos["estado"].eq("pagado")].copy()
    validos["importe_neto"] = validos["importe_bruto"] - validos["descuento"]
    return validos, rechazos


def main() -> None:
    raw = cargar_pedidos()
    print(f"Filas raw: {len(raw)}; duplicados de pedido: {raw['pedido_id'].duplicated().sum()}")
    validos, rechazos = limpiar(raw)
    clientes = pd.read_csv(DATA / "clientes_nebula.csv", sep=";", dtype="string")
    assert clientes["cliente_id"].is_unique
    assert validos["pedido_id"].is_unique
    assert validos["importe_neto"].ge(0).all()
    enriquecidos = validos.merge(
        clientes, on="cliente_id", how="left", validate="many_to_one", indicator=True
    )
    resumen = enriquecidos.groupby("canal", as_index=False).agg(
        pedidos=("pedido_id", "nunique"), ingresos_netos=("importe_neto", "sum")
    )
    assert resumen["ingresos_netos"].sum() == validos["importe_neto"].sum()
    print(f"Rechazos técnicos: {len(rechazos)}; pedidos pagados válidos: {len(validos)}")
    print("\nIngresos por canal:")
    print(resumen.to_string(index=False))
    print("\nCobertura de clientes:")
    print(enriquecidos["_merge"].value_counts().to_string())


if __name__ == "__main__":
    main()
