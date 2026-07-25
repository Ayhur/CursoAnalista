# Solución razonada - Auditoría de pedidos de Nébula

## 1. Contrato

La población son pedidos con estado `pagado` creados en junio. El grano final es un pedido y `pedido_id` debe ser único. Ingreso neto es `importe_bruto - descuento`, en EUR. La cifra no representa margen ni devuelve ajustes posteriores a la extracción; por eso no se debe presentar como beneficio.

## 2. Perfil y limpieza

Una solución empieza verificando `shape`, `dtypes`, nulos, `pedido_id.duplicated()` y categorías de `estado` y `canal`. Son controles distintos: el primero detecta tamaño inesperado, el segundo conversiones peligrosas, el tercero ausencia, el cuarto una posible violación de grano y los dos últimos valores fuera del contrato.

```python
raw = pd.read_csv("datasets/pandas/pedidos_nebula.csv", sep=";", dtype="string")
pedidos = raw.copy()
pedidos["fecha_pedido"] = pd.to_datetime(
    pedidos["fecha_pedido"], format="%Y-%m-%d", errors="coerce", utc=True
)
for c in ["importe_bruto", "descuento"]:
    pedidos[c] = pd.to_numeric(pedidos[c].str.replace(",", ".", regex=False), errors="coerce")
pedidos["fecha_extraccion"] = pd.to_datetime(pedidos["fecha_extraccion"], utc=True)
```

La fecha `fecha-mal`, el importe `-5,00` y el canal `tienda` no se borran por tener nulos: se etiquetan como rechazos porque incumplen reglas diferentes. Un `dropna()` eliminaría también datos potencialmente recuperables y no dejaría evidencia del motivo.

## 3. Duplicados y métrica

`P-1002` no es un duplicado técnico idéntico: cambia el descuento y la extracción. Se conserva la versión de `2026-06-30T09:00:00Z` por una regla explícita de «última extracción prevalece». Antes de llevarla a producción habría que confirmar con pagos que una extracción posterior es una corrección y no un reintento de entrega.

Tras deduplicar, filtrar `pagado` y las reglas de calidad, los pedidos válidos son `P-1001`, `P-1002` y `P-1005`. Sus ingresos netos son 29,90 EUR, 39,90 EUR y 60,00 EUR. Por tanto el resumen esperado es web: 1 pedido y 29,90 EUR; app: 1 pedido y 39,90 EUR; partner: 1 pedido y 60,00 EUR. Total: **129,80 EUR**.

```python
resumen = validos.groupby("canal", as_index=False).agg(
    pedidos=("pedido_id", "nunique"), ingresos_netos=("importe_neto", "sum")
)
assert resumen["ingresos_netos"].sum() == validos["importe_neto"].sum()
```

## 4. Merge y linaje

La unión correcta es `left`, porque un pedido válido sin cliente sigue siendo un ingreso observado. `validate="many_to_one"` protege que la dimensión clientes tenga una ficha por `cliente_id`; `indicator=True` revela que `C-99` queda `left_only`. En ingresos se conserva y se declara cobertura incompleta. En segmentación no se finge que pertenece a un segmento: se informa el porcentaje no clasificado.

Registro de linaje: fuente `pedidos_nebula.csv` y `clientes_nebula.csv`, extraídas el 30 de junio; conversiones controladas de fecha e importes; se conserva la última extracción por `pedido_id` y se rechazan fecha/importe/canal inválidos; total de 129,80 EUR reconciliado, con un pedido sin dimensión de cliente y sin ajuste de devoluciones.
