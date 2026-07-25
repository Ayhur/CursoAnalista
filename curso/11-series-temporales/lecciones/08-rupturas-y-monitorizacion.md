# Rupturas, monitorización y operación

## Objetivos y prerrequisitos

Identificarás cambios que pueden invalidar patrones históricos y diseñarás una respuesta operativa ante errores de previsión.

Una **ruptura estructural** es un cambio por el que la relación aprendida deja de ser estable: cambio de precio, falta de stock, expansión de zonas, campaña, nueva versión de producto o cambio de tracking. No se corrige borrando el punto “raro”; se registra el evento, se evalúa el impacto y se decide si el modelo necesita reentrenamiento o una regla temporal.

Monitoriza error por horizonte, cobertura de intervalos, datos ausentes, frescura y sesgo por día de semana. Una alerta debe indicar umbral, dueño y acción: “si el MAE de siete días supera 20 pedidos dos semanas, revisar calendario, stock y extracción”. Alertar sin responsable crea ruido, no control.

## Resumen

Prever es un proceso operativo: datos, modelo, error, aprendizaje y ajuste. Continúa con el [laboratorio reproducible](09-laboratorio-demanda.md).
