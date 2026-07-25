# Solución razonada - Caso Lumen

## 1. Contratos mínimos

**Activación 14d v1.0:** cuenta de prueba elegible con `source_connected` y después `report_published` dentro de 14 días / cuenta de prueba con `workspace_created`; excluir demos, empleados y bots; fuente backend deduplicada por `event_id`; propietario Producto. No mide satisfacción ni retención.

**Retención S4 v1.0:** cuentas de la cohorte que emiten un evento de valor en días 22–28 / cuentas de esa cohorte con cuatro semanas completas; fuente eventos canónicos; propietario Customer Success. No equivale a renovación contractual.

**Churn de logos mensual v1.0:** cancelaciones contractuales efectivas / cuentas activas al inicio del mes; no incluir downgrade; fuente de facturación; propietario Finanzas. No mide pérdida de uso en cuentas que no cancelaron.

## 2. Funnel

El funnel es 100 espacios / 48 conexiones = 48 %; 40 informes publicados únicos / 48 conexiones = 83,3 %; activación final = 40 %. Los cuatro reintentos hacen que haya 44 filas, pero no 44 cuentas ni 44 operaciones. El primer descenso relevante es antes de conectar fuente: 52 cuentas no llegan a una confirmación de backend. No prueba que el formulario sea el culpable: puede ser proveedor, permisos, tráfico de menor intención, error técnico o cobertura rota. `click_connect_source` es señal de intención y diagnóstico, no una conexión.

## 3. Métricas

Retención S4 = 28 / 100 = **28 %**. CAC de cuentas de prueba = 24 000 / 120 = **200 EUR por prueba**. Churn de logos = 22 / 550 = **4 %**. No llamamos 200 EUR «CAC de pago» porque faltan atribución y conversión de prueba a cliente; mezclar ambos denominadores inventaría rentabilidad.

## 4. Evento y pruebas

`report_published` necesita como mínimo `event_id`, `occurred_at` UTC, `received_at`, `account_id`, `user_id` cuando exista, `schema_version`, `plan_tier` y `source=backend`. No se manda título ni contenido del informe. Una prueba reenvía la misma operación con idéntico `event_id` y exige un recuento único. Otra entrega el evento 24 horas tarde y verifica que se asigna a `occurred_at` y se recalcula la cohorte afectada.

## 5. Decisión y guardrails

La decisión de una semana es abrir investigación del flujo de conexión por proveedor, versión y código de error, y corregir el fallo verificable más frecuente. Guardrails: cobertura de `account_id` y tasa de error/tiempo de conexión; además, no elevar clics a costa de conexiones fallidas. Antes de culpar a UX, pediría logs de backend, conciliación entre fuentes creadas y conexiones, segmentación por canal y versión, y muestras cualitativas de cuentas bloqueadas.

## 6. Cambio gobernado

La propuesta v2 documenta propósito, diferencias, consumidores y plan de migración. Producto, Datos, Ingeniería y Privacidad la aprueban; se prueba el esquema y se monitoriza con SLA. Se publica v2, se marca v1 como deprecada, se avisa a dashboards, se ofrece una fecha límite y solo se detiene v1 cuando los consumidores se migraron. Se conserva el catálogo histórico para que las tendencias sigan interpretándose correctamente.
