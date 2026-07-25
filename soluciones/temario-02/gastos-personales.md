# Solución razonada - Auditoría de pedidos de Lumen

La solución separa validar de agregar. Así, una incidencia no modifica el total y se conserva evidencia para investigar la fuente.

```python
def validar_pedido(pedido):
    """Normaliza un pedido confirmado válido o informa por qué no lo es."""
    for campo in ("id", "canal", "estado", "importe"):
        if campo not in pedido:
            raise ValueError(f"falta el campo {campo}")
    if pedido["estado"] != "confirmado":
        raise ValueError("el pedido no está confirmado")
    try:
        importe = float(pedido["importe"])
    except (TypeError, ValueError) as error:
        raise ValueError("importe no numérico") from error
    if importe <= 0:
        raise ValueError("importe no positivo")
    return {**pedido, "importe": importe}


def auditar_pedidos(pedidos, limite_revision=100):
    resumen = {"total": 0.0, "por_canal": {}, "ids_revision": [], "incidencias": []}
    for pedido in pedidos:
        try:
            valido = validar_pedido(pedido)
        except ValueError as error:
            resumen["incidencias"].append({"id": pedido.get("id", "sin_id"), "motivo": str(error)})
            continue
        resumen["total"] += valido["importe"]
        canal = valido["canal"]
        resumen["por_canal"][canal] = resumen["por_canal"].get(canal, 0.0) + valido["importe"]
        if valido["importe"] >= limite_revision:
            resumen["ids_revision"].append(valido["id"])
    return resumen
```

## Pruebas de la regla

```python
assert auditar_pedidos([])["total"] == 0.0
assert validar_pedido({"id": "x", "canal": "web", "estado": "confirmado", "importe": "25.5"})["importe"] == 25.5
assert auditar_pedidos([{"id": "x", "canal": "web", "estado": "confirmado", "importe": 100}])["ids_revision"] == ["x"]

try:
    validar_pedido({"id": "x", "canal": "web", "estado": "confirmado", "importe": 0})
    raise AssertionError("un importe cero no debe ser válido")
except ValueError:
    pass
```

Para los datos del enunciado el total es `100.5`, hay dos canales y tres incidencias: un cancelado, un cero y un importe ausente. No se asignan ceros a esas incidencias porque «cero» significaría un pedido confirmado sin valor, una afirmación distinta de «no podemos usar este evento». Si negocio quisiera medir cancelaciones, convendría otro contador con contrato propio.

## Variación y límite

La función acepta un `limite_revision` opcional para no ocultar el umbral. Si el contrato cambiara para admitir reembolsos negativos, no bastaría con reemplazar `<= 0`: habría que redefinir total, estado y comunicación de forma explícita.
