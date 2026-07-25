"""Laboratorio autónomo del bloque 13: trazabilidad y calidad de activación.

Ejecuta: python notebooks/practicas/13-activacion-reproducible.py
No usa paquetes externos ni datos reales. Simula un posible fallo de tracking:
Android 4.2 reporta menos reservas, por lo que la tasa observada no demuestra
por sí sola que el producto haya empeorado.
"""

from collections import defaultdict
from datetime import date, timedelta


CORTE = date(2026, 5, 6)
VENTANA_DIAS = 7


def crear_cuentas():
    """Una fila por cuenta; esta es la población, no una tabla de eventos."""
    cuentas = []
    for indice in range(32):
        plataforma = "android" if indice % 2 == 0 else "ios"
        version = "4.2" if indice >= 16 else "4.1"
        alta = date(2026, 4, 1) + timedelta(days=indice % 20)
        cuentas.append(
            {
                "account_id": f"a-{indice:02}",
                "alta": alta,
                "plataforma": plataforma,
                "version_app": version,
                "es_interna": indice == 31,
            }
        )
    return cuentas


def crear_reservas_reportadas(cuentas):
    """Genera reservas; falta parte de Android 4.2 como simulación de tracking roto."""
    eventos = []
    for indice, cuenta in enumerate(cuentas):
        activa_realmente = indice % 5 != 0
        perdida_de_tracking = cuenta["plataforma"] == "android" and cuenta["version_app"] == "4.2" and indice % 3 == 0
        if activa_realmente and not perdida_de_tracking:
            eventos.append({"account_id": cuenta["account_id"], "fecha": cuenta["alta"] + timedelta(days=2)})
    return eventos


def activacion_por_segmento(cuentas, eventos):
    reservas = {evento["account_id"] for evento in eventos}
    resumen = defaultdict(lambda: {"elegibles": 0, "activadas": 0})
    for cuenta in cuentas:
        observada = (CORTE - cuenta["alta"]).days >= VENTANA_DIAS
        if cuenta["es_interna"] or not observada:
            continue
        clave = (cuenta["plataforma"], cuenta["version_app"])
        resumen[clave]["elegibles"] += 1
        resumen[clave]["activadas"] += cuenta["account_id"] in reservas
    return resumen


def main():
    cuentas = crear_cuentas()
    eventos = crear_reservas_reportadas(cuentas)
    print(f"Corte: {CORTE.isoformat()} | ventana: {VENTANA_DIAS} días")
    print(f"Cuentas fuente: {len(cuentas)} | eventos reserva reportados: {len(eventos)}")
    print("\nTasa observada por plataforma y versión")
    for clave, fila in sorted(activacion_por_segmento(cuentas, eventos).items()):
        tasa = fila["activadas"] / fila["elegibles"]
        print(f"{clave[0]:7} {clave[1]}: {fila['activadas']}/{fila['elegibles']} = {tasa:.1%}")
    print("\nInterpretación: la diferencia observada no prueba un problema de producto.")
    print("Siguiente control: comparar reserva_creada con la fuente transaccional por versión.")


if __name__ == "__main__":
    main()
