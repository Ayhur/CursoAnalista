# Solución razonada — Experimento de onboarding

## 1. Contrato

La población es usuarios nuevos de web en España durante el periodo definido, excluyendo empleados y pruebas. La unidad de asignación y análisis es usuario, no sesión. El denominador principal debe ser usuarios **asignados elegibles** (en un análisis ITT); el evento de exposición se conserva para auditar que la variante llegó correctamente. Activación es crear proyecto y tarea en las 24 horas posteriores a la asignación/exposición según el contrato fijado. Hay que conservar la misma regla para A y B.

## 2. Magnitud

Con los datos asignados, A = 552/2.800 = **19,71 %** y B = 594/2.800 = **21,21 %**. La diferencia absoluta es **+1,50 pp**; la relativa es aproximadamente **+7,6 %** sobre A. Los puntos porcentuales dicen cuántas activaciones adicionales hay por cada 100 elegibles; el relativo contextualiza frente a la base, pero no debe presentarse solo.

## 3. Calidad y exposición

Primero revisaría que 2.800/2.800 es una asignación prevista, que no existen usuarios duplicados y que fecha, país y dispositivo no revelan desequilibrios graves. Después compararía exposición: A 98,6 % y B 98,0 % son cercanas, pero cualquier diferencia debe investigarse. No excluiría automáticamente B no expuestos: la no exposición puede estar causada por un error de carga relacionado con dispositivo o conexión; eliminarlos tras asignación puede romper la comparación aleatoria. ITT responde al efecto de ofrecer B.

## 4. Incertidumbre

La aproximación del laboratorio sitúa el efecto alrededor de +1,5 pp. Un intervalo de confianza describe los efectos compatibles con estos datos y el procedimiento, no la probabilidad subjetiva de que el efecto esté dentro. Si el intervalo incluye cero, no hay precisión suficiente para descartar ausencia de mejora; tampoco se demuestra que ambas variantes sean equivalentes. Un p-valor no es la probabilidad de que H0 sea cierta ni el valor económico de B.

## 5. Economía

Un efecto de +1 pp con 100.000 usuarios mensuales equivale a unas 1.000 activaciones extra. A 4 € de margen esperado por activación supone aproximadamente **4.000 €/mes** de valor bruto esperado. Es incierto porque activar no garantiza retención, compra ni margen; debe comprobarse la cadena posterior y descontar coste de desarrollo, soporte y daños.

## 6. Recomendación modelo

> Recomiendo completar la muestra predefinida y no lanzar globalmente todavía. B mejora la activación observada en 1,50 pp (21,21 % frente a 19,71 %), que supera el MDE puntual de 1 pp, pero la decisión depende de su intervalo y de que los guardrails permanezcan dentro de límite. Mantendría el análisis ITT, auditaría la exposición ligeramente menor de B y revisaría errores, p90 de carga y cancelación a siete días. Si al cierre se confirma una mejora de al menos 1 pp sin deterioro relevante, propondría un ramp-up al 10 % con rollback y revisión semanal.

La solución no afirma causalidad fuera de población, periodo y correcta aleatorización. Tampoco usa “no significativo” como sinónimo de “sin efecto”.
