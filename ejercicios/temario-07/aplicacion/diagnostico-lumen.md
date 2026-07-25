# Caso aplicado — Diagnóstico visual de Lumen

## Situación

Lumen registra, durante una semana, visitas, inicios de checkout y pagos finalizados. El lunes se publicó la versión 4.2. El equipo pide una decisión para la reunión del viernes.

| Día | Plataforma | Visitas | Inicio checkout | Pago |
| --- | --- | ---: | ---: | ---: |
| Lun | móvil | 5.000 | 1.000 | 760 |
| Mar | móvil | 5.200 | 980 | 700 |
| Mié | móvil | 5.100 | 970 | 690 |
| Jue | móvil | 5.300 | 1.020 | 720 |
| Vie | móvil | 5.000 | 1.010 | 710 |
| Lun | escritorio | 4.000 | 820 | 660 |
| Mar | escritorio | 4.100 | 850 | 680 |
| Mié | escritorio | 4.050 | 830 | 665 |
| Jue | escritorio | 4.200 | 860 | 690 |
| Vie | escritorio | 4.100 | 840 | 675 |

La semana anterior móvil tenía una conversión visita→pago de 18,0% y escritorio de 16,5%. El equipo de instrumentación avisa que el evento `payment_success` se retrasó dos horas el miércoles, pero se recuperó antes del cierre diario.

## Entregable

Prepara una nota para producto, no una galería de gráficos. Debe incluir:

1. El contrato de la métrica principal: fórmula, población, periodo, denominador y fuente hipotética.
2. Dos gráficos que harías, con tipo, ejes, título que exprese hallazgo y anotaciones necesarias. Explica por qué cada uno responde una pregunta distinta.
3. Cálculo de conversión móvil y escritorio de la semana con los datos disponibles. Indica qué comparación con la semana anterior es válida y cuál requiere cautela.
4. Un funnel por plataforma. Calcula conversión visita→inicio, inicio→pago y visita→pago; identifica el paso a investigar.
5. Una recomendación accionable, una alternativa no causal y una comprobación de calidad antes de atribuir la caída a 4.2.
6. El contrato de un panel de dashboard: propietario, actualización, umbral, acción y limitación.

No necesitas ejecutar código, pero puedes usar el [laboratorio](../../../notebooks/practicas/07-visualizacion-lumen.py). Consulta la [solución](../../../soluciones/temario-07/diagnostico-lumen.md) solo después de razonar.
