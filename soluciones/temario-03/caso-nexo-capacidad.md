# Solución razonada - Capacidad y crecimiento de Nexo

## 1. Conversiones y agregación

| Ciudad | Semana 1 | Semana 2 |
| --- | ---: | ---: |
| A | `100 / 1.000 = 10 %` | `132 / 1.100 = 12 %` |
| B | `720 / 9.000 = 8 %` | `891 / 9.900 = 9 %` |

La conversión global de semana 1 es `(100 + 720) / (1.000 + 9.000) = 8,2 %`; la de semana 2 es `(132 + 891) / (1.100 + 9.900) = 9,3 %`. La media simple sería 9 % y 10,5 %, respectivamente. No es la métrica global porque trata A y B como si aportaran igual número de visitas. La tasa agregada debe sumar pedidos y visitas primero.

## 2. Señal de demanda y señal de servicio

B pasa de 720 a 891 pedidos: `+171 pedidos`, o `171/720 = 23,75 %`. Su p90 pasa de 50 a 63 min: `+13 min`, o `26 %`. La demanda crece, pero la cola de servicio empeora todavía más. La decisión no debería ser celebrar el crecimiento aislado: conviene comprobar capacidad de tarde, zonas y cobertura de repartidores antes de escalar la campaña.

## 3. Centro y extremo

La media es `(28+30+31+35+39+82)/6 = 40,83 min`; la mediana ordenada es `(31+35)/2 = 33 min`. Para una promesa de servicio usaría p90 o percentiles sobre una muestra suficiente, porque protege a los clientes de la cola; la mediana comunica experiencia típica. El valor 82 debe investigarse por pedido, meteorología, zona, incidencia o error de tracking. Borrarlo sin trazabilidad sesgaría el servicio hacia una apariencia mejor.

## 4. Capacidad

`1.023 × 24 = 24.552 minutos`. Dividido entre 480 son `51,15`: al menos 52 repartidores-equivalentes si todos esos minutos son trabajo efectivo y se pueden repartir perfectamente. Fallan, entre otros, el supuesto de 24 min constante y el de 480 min íntegramente disponibles: tráfico, pausas, reequilibrio y geografía cambian la capacidad. Es una línea base, no una planificación final.

## 5. Crecimiento no es causalidad

Una formulación honesta es: "Los pedidos confirmados de A y B juntos pasaron de 820 en semana 1 a 1.023 en semana 2, un aumento de 24,8 % frente a la semana anterior". El 21 % no es el cálculo de pedidos conjuntos. Aun con el porcentaje correcto, una campaña puede coincidir con festivos, cambios de precio, mejor tracking o estacionalidad. Para atribuir causalidad haría falta un grupo de comparación o un experimento bien diseñado.

## 6. Contrato diario

Una fila por `fecha local, ciudad` (grano diario-ciudad) puede incluir `visitas`, `pedidos_confirmados`, `ingresos_eur`, `p50_entrega_min`, `p90_entrega_min`, `repartidores_horas`, `fecha_extraccion` y `cobertura_tracking`. Declararía zona horaria `Europe/Madrid` y alerta si p90 supera 60 min con al menos 100 pedidos. Cero pedidos significa que hubo observación y no ocurrieron pedidos; valor ausente significa que no se conoce el dato, por ejemplo por caída del sistema. Nunca deben agregarse igual.

## Qué no concluye el caso

Estos cálculos no prueban que campaña, ciudad o repartidores causen el cambio. Tampoco garantizan que el patrón semanal continúe. El siguiente paso es conservar los datos a grano pedido, segmentar la cola y comparar semanas equivalentes.
