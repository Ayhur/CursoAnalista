# Solución razonada - Investigar la caída de checkout de Nébula

## 1. Pregunta y perfil

Pregunta: «¿cómo cambia la conversión `compras / visitas` de la semana 05-05 a 11-05 frente a la referencia, en total y por plataforma, en filas agregadas por fecha/plataforma/canal?». Antes de calcularla comprobaría que las columnas esperadas existen, que `(fecha, plataforma, canal)` no se repite y que visitas/compras no son nulas, negativas ni inconsistentes. También revisaría la cobertura diaria y el significado de los eventos.

## 2. Comparación de tasas

El laboratorio suma compras y visitas antes de dividir. Su salida muestra que la caída se concentra en Android, mientras web permanece aproximadamente estable. La respuesta debe copiar los denominadores que imprima su ejecución: el porcentaje sin compras y visitas no permite saber si el cambio puede estar sostenido por muy poco tráfico.

El procedimiento es:

```text
tasa(periodo, plataforma) = suma(compras) / suma(visitas)
```

No es correcto sacar el promedio de los porcentajes diarios ni sumar porcentajes de canales.

## 3. Observación extrema y explicaciones

La fila de Android/ads del 08-05 tiene visitas positivas y compras cero. Puede reflejar un checkout que falla, una exportación incompleta del evento `compra`, tráfico automatizado o un canal mal atribuido. Ninguna de esas opciones se decide desde este CSV. La fila se conserva, se marca en la nota y se compara el resumen con y sin ella solo como análisis de sensibilidad; no se elimina para «normalizar» el resultado.

## 4. Hipótesis y próxima comprobación

Una hipótesis de producto es que una versión reciente afectó al formulario Android. Una hipótesis de calidad es que el evento de compra dejó de enviarse desde esa plataforma o canal. Pediría el desglose de errores del formulario, versión de aplicación y pagos confirmados por la pasarela para el mismo periodo. Si los pagos siguen estables y el evento cae, gana plausibilidad el problema de tracking; si caen los pagos y aumentan errores, gana plausibilidad una incidencia real.

## 5. Actualización responsable

> La conversión observada entre 05-05 y 11-05 es menor que en la referencia y el patrón se concentra en Android. El cálculo usa compras y visitas agregadas por fecha, plataforma y canal; una fila de Android/ads del 08-05 registra compras cero y se mantiene pendiente de verificación. Estos datos no identifican la causa. Ingeniería contrastará pagos confirmados, errores de formulario y cambios de tracking antes de recomendar una intervención.

Esta actualización es útil porque describe, delimita y asigna una comprobación; no convierte una coincidencia temporal en culpabilidad.
