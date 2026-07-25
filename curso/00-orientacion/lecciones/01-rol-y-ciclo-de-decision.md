# El rol del analista y el ciclo de decisión

## Objetivos y punto de partida

Al terminar podrás distinguir una decisión de un cálculo y describir el trabajo de un analista sin reducirlo a “hacer gráficos”. No necesitas saber qué es una base de datos ni programar.

## El problema que resuelve el análisis

Una empresa de reparto observa menos pedidos que el mes anterior. La directora debe decidir si cambia una campaña, corrige una incidencia en la aplicación o no hace nada porque la variación es normal. Mirar un número aislado no responde esa decisión: hace falta saber **qué cambió, para quién, respecto a qué referencia y con qué confianza**.

Un **analista de datos** transforma una necesidad de decisión en evidencia revisable. Su producto final no es una tabla ni un gráfico: es una recomendación que explica qué se sabe, qué no se sabe y qué conviene comprobar después.

## Del encargo a la acción

Antes de hablar de herramientas, mira este recorrido. Responde a la pregunta: “¿cómo se evita saltar de una impresión a una conclusión?”

```mermaid
flowchart LR
  A[Decisión pendiente] --> B[Pregunta concreta]
  B --> C[Datos y comprobaciones]
  C --> D[Interpretación]
  D --> E[Recomendación]
  E --> F[Medir resultado]
  F --> A
```

El ciclo es deliberadamente circular. Una recomendación no cierra el trabajo: genera una acción cuya consecuencia debe medirse. Si la campaña cambia, habrá que volver a comprobar pedidos, margen y posibles efectos no deseados.

## Ejemplo trabajado

Petición inicial: “las ventas van mal”.

Una respuesta precipitada sería abrir un gráfico mensual y proponer bajar precios. Una respuesta analítica empieza preguntando: “¿qué decisión está sobre la mesa?”. Supongamos que la decisión es redistribuir 20 000 euros de publicidad. Entonces la pregunta puede ser: “¿Qué canal explica la caída de pedidos de junio frente al promedio de marzo a mayo, y cuál mantiene margen suficiente para recibir inversión?”

La pregunta obliga a definir después “pedido”, “canal”, “margen” y los periodos. Aún no demuestra que un canal **cause** la caída; solo delimita qué evidencia buscar.

## Límite importante: describir no es explicar causas

Que los pedidos hayan bajado después de una campaña no prueba que la campaña sea la causa. Puede haber estacionalidad, un fallo técnico, cambios de precio o clientes distintos. El análisis descriptivo dice qué ocurrió; una explicación causal exige comparaciones y diseño más cuidadoso, que se estudiará más adelante.

## Resumen y comprobación

- El analista ayuda a decidir con evidencia trazable.
- Una cifra es un indicio, no una conclusión.
- El trabajo continúa después de recomendar: hay que medir el resultado.

Pregúntate: ¿qué decisión cambiaría si el análisis mostrara que la caída procede solo de usuarios nuevos? ¿Qué dato adicional pedirías antes de recomendar bajar precios?

Sigue con [preguntas, hipótesis, evidencia y métricas](02-preguntas-hipotesis-y-evidencia.md) y después resuelve el [ejercicio del bloque](../../../ejercicios/temario-00/comprension/preguntas.md).
