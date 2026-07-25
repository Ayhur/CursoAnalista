# Caso integrador - Capacidad y crecimiento de Nexo

## Situación

Nexo opera en dos ciudades. Cada fila siguiente es un resumen diario; no es un pedido individual. El equipo estudia si debe reforzar el turno de tarde y si la mejora de conversión compensa el empeoramiento del servicio.

| Ciudad | Periodo | Visitas | Pedidos | Ingresos EUR | Mediana entrega min | p90 min |
| --- | --- | ---: | ---: | ---: | ---: | ---: |
| A | Semana 1 | 1.000 | 100 | 2.000 | 26 | 42 |
| B | Semana 1 | 9.000 | 720 | 14.400 | 31 | 50 |
| A | Semana 2 | 1.100 | 132 | 2.640 | 27 | 48 |
| B | Semana 2 | 9.900 | 891 | 17.820 | 34 | 63 |

Además, los tiempos de entrega de seis pedidos de B en la tarde de semana 2 fueron `28, 30, 31, 35, 39, 82` minutos. El equipo estima 24 minutos de trabajo por pedido y cada repartidor dispone de 480 minutos de turno.

## Entrega esperada

Escribe una nota de decisión de una página, con cálculos y supuestos visibles. No uses el laboratorio hasta resolverlo a mano.

1. Calcula conversión de cada ciudad y semana. Calcula la conversión global de cada semana agregando numeradores y denominadores. Compara con la media simple de conversiones y explica cuál responde a la conversión total.
2. Para B, calcula el crecimiento de pedidos de semana 1 a 2, en pedidos y porcentaje. Calcula el cambio de p90 en minutos y porcentaje. ¿Qué dos señales deben entrar en la decisión?
3. Calcula media y mediana de los seis tiempos. Explica qué resumen usarías en una promesa de servicio y qué investigarías antes de eliminar 82.
4. Estima repartidores-equivalentes para los 1.023 pedidos de semana 2 con el modelo `minutos = 24 × pedidos`. Expón dos supuestos del modelo que podrían fallar.
5. El director afirma: "Nexo crece un 21 % y por tanto la campaña causó el crecimiento". Corrige la frase: especifica base, periodo y por qué la causalidad no queda demostrada.
6. Diseña una tabla diaria mínima para la semana 3: columnas, grano, zona horaria y una métrica de alerta. Explica qué diferencia hay entre cero pedidos y dato ausente.

Consulta la [solución razonada](../../../soluciones/temario-03/caso-nexo-capacidad.md) después de intentarlo. También puedes ejecutar el [laboratorio](../../../notebooks/practicas/03-matematicas-nexo.py).
