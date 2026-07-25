# Lags, referencias y previsiones base

## Objetivos y prerrequisitos

Usarás valores pasados como referencia y evaluarás una previsión contra alternativas simples.

Un **lag** es un valor retrasado: ventas de ayer o del mismo día de la semana anterior. Una previsión ingenua que repite el último valor, o una estacional que repite la semana anterior, es un baseline obligatorio. Si un modelo más complejo no mejora esa referencia, añade coste sin valor.

El horizonte importa: prever mañana y prever seis meses son problemas distintos. Declara qué información estaba disponible en el momento de hacer cada previsión; usar datos futuros por accidente produce resultados irreales.

## Resumen

Una previsión se evalúa frente a un baseline y un horizonte, no por lo convincente que parezca la curva.
