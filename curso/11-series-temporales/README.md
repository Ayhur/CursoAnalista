# Bloque 11 - Series temporales

## Propósito

Analizar pedidos diarios de una aplicación, distinguir patrones temporales de cambios reales y construir previsiones útiles para planificar capacidad e inventario. El objetivo no es memorizar modelos: es definir, validar y comunicar una predicción que otra persona pueda cuestionar.

## Caso continuo: pedidos diarios de Lumen

Lumen es una aplicación de comercio local. Operaciones debe decidir cada lunes cuántos repartidores reservar para los 14 días siguientes. La métrica es `pedidos_completados_diarios`; cada observación es un día en la zona horaria de Madrid. El bloque parte de este caso y conserva su contrato, datos disponibles y riesgos a lo largo de todas las lecciones.

## Lecciones

1. [Contrato de previsión y calidad temporal](lecciones/01-indice-temporal-y-calidad.md)
2. [Tendencia, estacionalidad, calendario y rupturas](lecciones/02-componentes-de-una-serie.md)
3. [Lags, autocorrelación y ventanas móviles](lecciones/03-lags-y-previsiones-base.md)
4. [Baselines y un modelo sencillo](lecciones/04-validacion-temporal-y-comunicacion.md)
5. [Validación walk-forward y fuga de futuro](lecciones/05-validacion-walk-forward-y-fugas.md)
6. [Métricas de previsión y coste de error](lecciones/06-metricas-de-prevision.md)
7. [Intervalos de predicción y calibración](lecciones/07-intervalos-y-calibracion.md)
8. [Rupturas, monitorización y operación](lecciones/08-rupturas-y-monitorizacion.md)
9. [Laboratorio reproducible de demanda](lecciones/09-laboratorio-demanda.md)

## Práctica

Plantea [una previsión de demanda](../../ejercicios/temario-11/aplicacion/prevision-demanda.md), ejecuta el [laboratorio reproducible](../../notebooks/practicas/11-prevision-demanda.py) y compara con [la solución razonada](../../soluciones/temario-11/prevision-demanda.md).
