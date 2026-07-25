"""Laboratorio reproducible del bloque 02.

Ejecuta: python notebooks/practicas/02-auditoria-pedidos.py
También puede copiarse por bloques en Google Colab.
"""


PEDIDOS_DEMO = [
    {"id": "p-101", "canal": "web", "estado": "confirmado", "importe": 120.50},
    {"id": "p-102", "canal": "app", "estado": "confirmado", "importe": "40"},
    {"id": "p-103", "canal": "web", "estado": "confirmado", "importe": 0},
    {"id": "p-104", "canal": "web", "estado": "cancelado", "importe": 30},
    {"id": "p-105", "canal": "partner", "estado": "confirmado"},
    {"id": "p-106", "canal": "app", "estado": "confirmado", "importe": "no disponible"},
]


def validar_pedido(pedido):
    """Devuelve una copia normalizada de un pedido confirmado válido.

    Contrato: exige id, canal, estado confirmado e importe convertible a float y positivo.
    Lanza ValueError para un evento que el informe no puede sumar.
    """
    for campo in ("id", "canal", "estado", "importe"):
        if campo not in pedido:
            raise ValueError(f"falta el campo {campo}")
    if pedido["estado"] != "confirmado":
        raise ValueError("estado distinto de confirmado")
    try:
        importe = float(pedido["importe"])
    except (TypeError, ValueError) as error:
        raise ValueError("importe no numérico") from error
    if importe <= 0:
        raise ValueError("importe no positivo")
    return {**pedido, "importe": importe}


def auditar_pedidos(pedidos, limite_revision=100):
    """Resume pedidos válidos e incidencias sin modificar la lista de entrada."""
    resumen = {"validos": 0, "total": 0.0, "por_canal": {}, "ids_revision": [], "incidencias": []}
    for pedido in pedidos:
        try:
            valido = validar_pedido(pedido)
        except ValueError as error:
            resumen["incidencias"].append({"id": pedido.get("id", "sin_id"), "motivo": str(error)})
            continue
        resumen["validos"] += 1
        resumen["total"] += valido["importe"]
        canal = valido["canal"]
        resumen["por_canal"][canal] = resumen["por_canal"].get(canal, 0.0) + valido["importe"]
        if valido["importe"] >= limite_revision:
            resumen["ids_revision"].append(valido["id"])
    return resumen


def ejecutar_pruebas():
    """Casos normal, borde e inválidos: el laboratorio no sigue si cambian las reglas."""
    assert auditar_pedidos([])["total"] == 0.0
    assert validar_pedido({"id": "x", "canal": "web", "estado": "confirmado", "importe": "25.5"})["importe"] == 25.5
    assert auditar_pedidos([{"id": "x", "canal": "web", "estado": "confirmado", "importe": 100}])["ids_revision"] == ["x"]
    try:
        validar_pedido({"id": "x", "canal": "web", "estado": "confirmado", "importe": 0})
        raise AssertionError("el cero no debe aceptarse")
    except ValueError:
        pass


def main():
    ejecutar_pruebas()
    resumen = auditar_pedidos(PEDIDOS_DEMO)
    print(f"Pedidos válidos confirmados: {resumen['validos']}")
    print(f"Importe confirmado: {resumen['total']:.2f} EUR")
    print(f"Por canal: {resumen['por_canal']}")
    print(f"Pedidos para revisión: {resumen['ids_revision']}")
    print(f"Incidencias: {len(resumen['incidencias'])}")
    for incidencia in resumen["incidencias"]:
        print(f"- {incidencia['id']}: {incidencia['motivo']}")


if __name__ == "__main__":
    main()
