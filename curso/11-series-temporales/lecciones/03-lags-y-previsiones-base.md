# Lags, autocorrelación y ventanas móviles

## Objetivos y prerrequisitos

Usarás valores pasados para describir dependencia temporal sin introducir información futura.

Un **lag** es un valor retrasado: `pedidos_t-1` es ayer y `pedidos_t-7` es el mismo día de la semana anterior. La **autocorrelación** resume cuánto se parece la serie a sí misma tras uno o varios retrasos. Una ACF alta en el lag 7 sugiere patrón semanal, no causalidad ni permiso para copiar siete días sin evaluar.

Una media móvil de 7 días suaviza ruido al promediar solo observaciones anteriores. Para predecir el 10 de marzo, su ventana puede usar del 3 al 9, nunca del 11 al 16. La regla evita una fuga de futuro muy común cuando se calculan ventanas sobre toda la tabla.

Ejemplo: si Lumen tuvo 102 pedidos ayer, 118 hace una semana y una media móvil de 110, esos tres números pueden alimentar modelos distintos. Cada variable contiene una hipótesis: continuidad inmediata, patrón semanal o nivel suavizado.

El horizonte importa: prever mañana y prever seis meses son problemas distintos. Declara qué información estaba disponible en el momento de hacer cada previsión; usar datos futuros por accidente produce resultados irreales. En la siguiente lección convertirás estas referencias en baselines comparables.

## Resumen

Lags y ventanas describen dependencia; no prueban que una acción cause pedidos. Sigue con [baselines y un modelo sencillo](04-validacion-temporal-y-comunicacion.md).
