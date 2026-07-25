# Ejercicio - Priorizar churn en Lumen

## Contexto

Cada lunes Lumen puede revisar manualmente 20 cuentas activas. Quiere anticipar cancelaciones dentro de los 30 días siguientes. La tabla de ejemplo contiene una fila por cuenta el día de corte; las etiquetas `churn_30d` son históricas y no existirían todavía el lunes real.

## Entrega

Redacta una respuesta breve y razonada. Puedes usar el [dataset](../../../datasets/lumen_churn_ejemplo.csv) y ejecutar el [laboratorio](../../../notebooks/practicas/12-priorizacion-churn.py).

1. Escribe el contrato predictivo: unidad, población, fecha de corte, horizonte, target, tres features permitidas y acción posterior.
2. Clasifica estas columnas como permitida, fuga o «necesita aclaración»: `sesiones_7d`, `fecha_cancelacion`, `tickets_cerrados_en_los_30_dias_siguientes`, `factura_impagada`, `motivo_de_cancelacion`.
3. Explica por qué el baseline «predecir continuidad siempre» puede lograr accuracy alta y, aun así, no servir para la cola de atención.
4. Si el equipo puede revisar cinco cuentas del dataset, indica qué política de umbral usarías y qué métrica priorizarías. No respondas solo con «0,5».
5. La cola de cinco tiene 4 VP y 1 FP; fuera de ella hay 2 FN y 13 VN. Calcula precision, recall y F1. Di qué información adicional necesitas para juzgar si es rentable.
6. Propón dos controles de monitorización y un riesgo de sesgo, privacidad o interpretación que revisarías antes de operar el sistema.

Consulta la [solución razonada](../../../soluciones/temario-12/priorizar-churn.md) solo después de intentarlo.
