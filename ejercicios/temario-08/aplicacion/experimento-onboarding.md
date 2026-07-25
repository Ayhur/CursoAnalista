# Ejercicio aplicado — ¿Lanzamos el onboarding B?

Nexo ha ejecutado un A/B de onboarding durante dos semanas. La unidad es un usuario nuevo web en España; la métrica primaria es crear proyecto y tarea en 24 h. El archivo [onboarding_nexo_agregado.csv](../../../datasets/experimentos/onboarding_nexo_agregado.csv) contiene el resultado diario agregado.

Resumen ya auditado: A tuvo 2.800 usuarios asignados, 2.760 expuestos y 552 activados; B tuvo 2.800 asignados, 2.745 expuestos y 594 activados. En B hubo una actualización menor de interfaz el día 9, aplicada también a A. El equipo predefinió un MDE de +1 pp, α=0,05, potencia 80 % y estas guardrails: errores no más de +0,2 pp, p90 de carga no más de +2 minutos y cancelación a 7 días no peor en más de +0,3 pp.

El laboratorio calcula una aproximación de diferencia, intervalo y prueba. Úsalo, pero no entregues solo sus números.

## Entrega

1. Escribe el contrato: población, unidad, denominador, exposición y métrica primaria.
2. Calcula tasas A/B, diferencia absoluta en pp y diferencia relativa. ¿Qué muestra cada medida?
3. Describe dos comprobaciones de calidad antes de interpretar causalidad y explica por qué no excluirías automáticamente a usuarios B no expuestos.
4. Interpreta el intervalo y p-valor que obtengas: escribe una afirmación permitida y otra prohibida.
5. Propón un tamaño económico para +1 pp con 100.000 nuevos usuarios/mes y 4 € de margen esperado por activación. Declara el supuesto que lo hace incierto.
6. Redacta una recomendación de máximo 120 palabras que incluya acción, incertidumbre, guardrails y siguiente revisión. No existe una única decisión correcta: se evalúa el razonamiento.

## Rúbrica breve

- 30 %: contrato y denominadores correctos;
- 25 %: efecto e incertidumbre interpretados sin falsas afirmaciones;
- 25 %: calidad, guardrails y límites causales;
- 20 %: recomendación proporcional, económica y accionable.

Consulta la [solución razonada](../../../soluciones/temario-08/experimento-onboarding.md) solo después de intentarlo.
