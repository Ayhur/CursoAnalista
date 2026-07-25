# Evaluación y coste de errores

## Objetivos y prerrequisitos

Elegirás métricas según el tipo de resultado y la consecuencia de cada fallo.

Para cantidades, MAE expresa error medio absoluto y RMSE penaliza más fallos grandes. Para clasificación, precisión pregunta cuántos avisos fueron correctos; recall, cuántos casos reales detectaste. No hay métrica universal: en fraude, perder un caso puede costar mucho; en una campaña cara, contactar falsos positivos también.

El umbral de probabilidad transforma un modelo en una acción. Ajustarlo cambia precisión, recall, capacidad operativa y equidad. Evalúa por segmentos relevantes y en datos futuros, no solo una métrica global.

## Resumen

La mejor métrica refleja la decisión y sus costes, no el número más alto de una tabla.
