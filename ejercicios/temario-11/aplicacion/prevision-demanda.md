# Práctica - Planificar pedidos diarios de Lumen

Operaciones de Lumen debe reservar repartidores para los próximos 14 días. La tabla diaria contiene estos campos: `fecha`, `pedidos_completados`, `campaña_activa`, `stock_disponible` y `version_tracking`. Se predice el domingo a las 23:59 para actuar el lunes.

1. Escribe el contrato de previsión: objetivo, unidad, frecuencia, granularidad, horizonte, fecha de corte, información permitida y decisión que apoya.
2. El 6 de enero no aparece en la fuente. Explica tres significados posibles y qué comprobación harías antes de rellenarlo con cero.
3. Propón qué lags, variable de calendario y ventana móvil usarías, indicando por qué ninguno puede usar información posterior al corte.
4. Compara cuándo usarías naïve, seasonal naïve y media móvil de siete días. Propón un modelo sencillo adicional y el requisito para conservarlo.
5. Dibuja o describe una validación walk-forward para octubre, noviembre y diciembre. Identifica dos fugas de información plausibles.
6. Para un día real de 0 pedidos y previsión de 10, explica qué ocurre con MAE, RMSE y MAPE. Indica qué métrica priorizarías si faltar repartidores tiene un coste alto.
7. Formula una previsión de escenario bajo/central/alto y un plan de monitorización ante una campaña nueva o una rotura de stock.
8. Ejecuta el [laboratorio](../../../notebooks/practicas/11-prevision-demanda.py) y entrega el baseline ganador, sus métricas y una limitación que impediría lanzarlo sin revisión humana.
