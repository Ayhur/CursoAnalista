# Laboratorio reproducible de demanda

## Objetivos y prerrequisitos

Aplicarás el contrato temporal, tres baselines, validación ordenada y métricas de error sobre el caso de Lumen.

El script [11-prevision-demanda.py](../../../notebooks/practicas/11-prevision-demanda.py) genera de forma determinista 90 días de pedidos diarios con patrón semanal y una ruptura documentada. Divide pasado y futuro, compara naïve, seasonal naïve y media móvil, y calcula MAE, RMSE, MAPE, sMAPE y MASE.

No trates la salida como una respuesta universal: inspecciona qué baseline gana y explica por qué. Cambia la fecha de corte o la ruptura para observar que una métrica global puede ocultar días críticos. Escribe en tu entrega qué información estaría disponible realmente antes de predecir.

## Entregable

Resuelve la [práctica de demanda](../../../ejercicios/temario-11/aplicacion/prevision-demanda.md), conserva los resultados esperados y contrasta tu razonamiento con la [solución](../../../soluciones/temario-11/prevision-demanda.md).
