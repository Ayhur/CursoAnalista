# Caso Lumen: funnel, cohorte y decisión

## Situación

Lumen quiere decidir dónde invertir la próxima semana. En una cohorte madura de 100 cuentas de prueba: 72 crearon espacio, 48 conectaron fuente, 40 publicaron un informe dentro de 14 días y 28 tuvieron actividad de valor en semana 4. El gasto atribuible de captación fue 24 000 EUR; entraron 120 cuentas de prueba. De 30 cancelaciones observadas, 8 son downgrades a plan gratuito y 22 cancelaciones contractuales de cuentas que estaban activas al inicio del mes (550).

Los eventos `source_connected` provienen del backend. `report_published` tiene 44 filas, pero cuatro comparten `event_id` con otra fila: son reintentos. El equipo de ventas pide contar `click_connect_source` como conexión para «mostrar progreso».

## Entrega

1. Escribe contratos resumidos para activación 14d, retención S4 y churn de logos: entidad, numerador, denominador, ventana, exclusiones, fuente, versión y una limitación.
2. Calcula los pasos y conversiones del funnel después de deduplicar. Explica cuál es el primer cuello de botella y por qué no demuestra causa.
3. Calcula retención S4, CAC de cuentas de prueba y churn de logos. Indica por qué CAC no es todavía CAC de cliente de pago.
4. Diseña los campos obligatorios de `report_published` y una prueba de deduplicación/retraso.
5. Propón una decisión de una semana, dos guardrails y la evidencia que pedirías antes de atribuir la pérdida a UX.
6. Describe el proceso de aprobación y deprecación si se quiere sustituir `report_published` por una versión v2.

No uses el clic como sustituto de una conexión confirmada. Consulta la [solución razonada](../../../soluciones/temario-10/aplicacion/funnel-cohorte-y-decision.md) solo tras justificar tus supuestos.
