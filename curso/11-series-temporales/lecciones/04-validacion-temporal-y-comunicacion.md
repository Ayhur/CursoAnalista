# Baselines y un modelo sencillo

## Objetivos y prerrequisitos

Compararás referencias honestas antes de elegir un modelo más elaborado.

Un baseline responde “¿qué lograríamos sin sofisticación?”. Para Lumen compara: naïve (repetir ayer), seasonal naïve (repetir el mismo día de la semana anterior) y media móvil de siete días. Son modelos explícitos, reproducibles y difíciles de superar cuando hay fuerte patrón semanal.

Como modelo sencillo adicional, una regresión con tendencia y variables de día de semana puede estimar nivel y estacionalidad. No es automáticamente mejor: solo se conserva si mejora de forma estable al baseline y su coste/interpretación compensa. Métodos como ETS, ARIMA o modelos de aprendizaje automático se estudian después de dominar esta comparación.

Ejemplo: si la media móvil gana en semanas tranquilas pero pierde sistemáticamente los viernes, la referencia estacional puede ser preferible. No elijas por una única semana ni por una gráfica atractiva.

El siguiente paso es evaluar respetando la flecha del tiempo. Continúa con [validación walk-forward y fuga de futuro](05-validacion-walk-forward-y-fugas.md).

Plantea la [previsión de demanda](../../../ejercicios/temario-11/aplicacion/prevision-demanda.md). En modelos posteriores aprenderás predicción supervisada, pero conservarás esta regla: validación coherente con el momento de decisión.
