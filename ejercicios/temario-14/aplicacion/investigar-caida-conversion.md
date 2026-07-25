# Laboratorio - Investigar una caída de conversión en Lumen

## Situación

El 8 de junio Lumen activó el formulario B para Android. La conversión visita a reserva a 7 días pasó de 4,8 % a 3,6 %. Ese día también empezó una campaña de afiliación; el equipo de datos detectó que la versión Android 8.3 dejó de enviar `booking_confirmed` durante 70 minutos. Hay eventos Parquet particionados por día y plataforma, y se propone añadir una API meteorológica por ciudad.

No se pide “encontrar la causa” con los datos disponibles. Se pide producir un plan de investigación defendible.

## Entregables

1. Escribe el estimando: tratamiento, resultado, unidad, población, fecha de corte y contrafactual.
2. Dibuja o describe un DAG con campaña, plataforma, formulario y reserva. Indica un confusor y un mal control posible.
3. Prioriza el primer diagnóstico de la alerta y redacta tres pasos concretos de runbook, con responsable y criterio de escalado.
4. Explica por qué la comparación antes/después no identifica el efecto de B. Propón A/B y, si no es posible, un diseño cuasiexperimental con un supuesto comprobable.
5. Diseña un bootstrap: unidad de remuestreo, estadística, número aproximado de réplicas e interpretación. Da una sensibilidad que podría cambiar la recomendación.
6. Escribe una consulta DuckDB que filtre siete días de Android y lea solo las columnas necesarias. Justifica la partición elegida y un riesgo de archivos pequeños.
7. Diseña el contrato de una API paginada: procedencia, cursor, 429, reintentos y secreto. Explica cómo unirías meteorología sin usarla como prueba causal.
8. Indica el CRS de entrada, una precaución al medir distancia y una regla de privacidad para publicar un mapa.

Consulta la [solución razonada](../../../soluciones/temario-14/investigar-caida-conversion.md) solo al terminar.
