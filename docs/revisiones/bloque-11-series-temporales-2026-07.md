# Revisión catedrática - Bloque 11: Series temporales

## Diagnóstico previo

La versión anterior explicaba calendario, componentes, baselines y validación en cuatro lecciones y tres páginas PDF. Era una introducción correcta, pero no permitía construir ni evaluar una previsión reproducible. Faltaban contrato de previsión, ACF/lags/ventanas, métricas, intervalos, calibración, rupturas, práctica técnica y una representación visual correcta de componentes paralelos.

## Decisión de rediseño

Se conserva el enfoque de analista y se amplía a nueve lecciones mediante un caso continuo: pedidos diarios de Lumen. Se añaden tres baselines, un modelo sencillo como referencia conceptual, validación walk-forward, fugas, métricas y operación. El laboratorio usa datos sintéticos con semilla fija; no pretende estimar una demanda real.

## Riesgos y límites explícitos

- El script no implementa todavía ACF gráfica, intervalos calibrados ni un modelo ETS/ARIMA; las lecciones los explican y sitúan como extensión profesional.
- Las métricas del laboratorio se usan como demostración; un lanzamiento real debe evaluar múltiples cortes, segmentación y costes operativos.
- La ruptura de stock simulada muestra por qué un patrón histórico puede dejar de ser válido, no un método causal para cuantificarla.
