"""Laboratorio reproducible del bloque 03.

Ejecutar: python notebooks/practicas/03-matematicas-nexo.py
No requiere paquetes externos. Primero muestra los resultados y después invita a
modificar los datos para comprobar qué cambia y qué permanece.
"""

from statistics import mean, median


def porcentaje(numerador, denominador):
    """Devuelve None cuando una tasa no está definida."""
    return None if denominador == 0 else 100 * numerador / denominador


def mostrar_tasa(nombre, numerador, denominador):
    valor = porcentaje(numerador, denominador)
    if valor is None:
        print(f"{nombre}: no definida (denominador 0)")
    else:
        print(f"{nombre}: {numerador}/{denominador} = {valor:.2f} %")


semana_1 = {"A": (1000, 100), "B": (9000, 720)}  # visitas, pedidos
semana_2 = {"A": (1100, 132), "B": (9900, 891)}

print("=== Conversiones ===")
for ciudad, (visitas, pedidos) in semana_1.items():
    mostrar_tasa(f"Semana 1, ciudad {ciudad}", pedidos, visitas)
for ciudad, (visitas, pedidos) in semana_2.items():
    mostrar_tasa(f"Semana 2, ciudad {ciudad}", pedidos, visitas)

v1 = sum(visitas for visitas, _ in semana_1.values())
p1 = sum(pedidos for _, pedidos in semana_1.values())
v2 = sum(visitas for visitas, _ in semana_2.values())
p2 = sum(pedidos for _, pedidos in semana_2.values())
mostrar_tasa("Global semana 1", p1, v1)
mostrar_tasa("Global semana 2", p2, v2)
print(f"Crecimiento conjunto: {p2 - p1:+d} pedidos; {porcentaje(p2 - p1, p1):.2f} %")

tiempos = [28, 30, 31, 35, 39, 82]
print("\n=== Tiempos de entrega de B (min) ===")
print(f"Valores: {tiempos}")
print(f"Media: {mean(tiempos):.2f}; mediana: {median(tiempos):.2f}")
print("El 82 no se borra: se investiga como posible incidencia o error de registro.")

pedidos_por_zona = [120, 80, 100]
minutos_por_pedido = [22, 30, 26]
minutos_por_zona = [p * t for p, t in zip(pedidos_por_zona, minutos_por_pedido)]
print("\n=== Operación vectorial por zona ===")
print(f"Minutos por zona: {minutos_por_zona}; total: {sum(minutos_por_zona)}")

minutos_estimados = 24 * p2
repartidores_equivalentes = minutos_estimados / 480
print("\n=== Modelo de capacidad ===")
print(f"{p2} pedidos × 24 min/pedido = {minutos_estimados} min")
print(f"{repartidores_equivalentes:.2f} repartidores-equivalentes de 480 min")
print("Supuesto: 24 min/pedido y disponibilidad completa; no prueba causalidad ni garantiza capacidad real.")
