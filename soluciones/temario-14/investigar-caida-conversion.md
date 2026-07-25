# Solución razonada - Investigar una caída de conversión en Lumen

## 1. Pregunta y DAG

Un estimando válido es: “efecto medio de mostrar B en vez de A sobre la probabilidad de reserva a 7 días, por visita elegible Android, entre el 8 y 21 de junio, con corte el 29 de junio”. El contrafactual es la reserva que la misma visita habría tenido viendo A; no se observa directamente.

La campaña puede afectar tanto la probabilidad de ver B si el despliegue o canal la condicionó como la reserva; es confusor. Plataforma también puede serlo si B y rendimiento cambian por sistema. Un mal control sería el número de errores dentro del formulario si B puede producir esos errores: ocurre después del tratamiento y bloquearía parte del mecanismo de B.

## 2. Operación primero

Primero se comprueba la laguna de Android 8.3: conteo de eventos fuente, frescura, cambios de esquema y duplicados. La alerta se abre como incidente de datos, propietario ingeniería de tracking, y se escala a producto solo si la métrica recalculada sigue baja con datos completos durante dos ventanas comparables. El criterio de cierre debe indicar causa, intervalo afectado, corrección o backfill y enlace a la consulta versionada.

## 3. Diseño e incertidumbre

Antes/después mezcla formulario, campaña y fallo de tracking. Un A/B con asignación aleatoria por visita elegible, guardrails y análisis por intención de tratar es la opción preferida. Si es imposible, un país no desplegado podría servir para diferencias en diferencias solo tras mostrar tendencias previas paralelas, exposición comparable a campaña y ausencia de otros cambios.

Para bootstrap se remuestrean usuarios o visitas independientes dentro de cada variante; se calcula `p(B)-p(A)` en, por ejemplo, 2.000 réplicas, y se reportan percentiles junto a denominadores. No elimina confusión ni el fallo de instrumentación. Una sensibilidad útil compara incluir/excluir el tráfico de afiliación con etiqueta tardía y ventanas de 7/14 días; un veredicto que cambia se comunica como frágil.

## 4. Escala

```sql
SELECT event_date, platform, event_name, count(DISTINCT user_id) AS usuarios
FROM read_parquet('eventos/event_date=*/platform=*/*.parquet', hive_partitioning = true)
WHERE event_date BETWEEN DATE '2026-06-08' AND DATE '2026-06-14'
  AND platform = 'android'
  AND event_name IN ('visit', 'booking_confirmed')
GROUP BY 1, 2, 3;
```

Fecha es buena partición si las consultas casi siempre acotan periodo. No se particiona por usuario: proliferarían archivos y carpetas pequeños. La consulta aún debe validar que `booking_confirmed` es atribuible a una visita dentro del horizonte definido; contar eventos no equivale automáticamente a conversión.

## 5. Fuente externa y geografía

El contrato API registra proveedor, licencia, URL, parámetros, versión, fecha, ciudad, zona horaria, cursor y hash de lote. Ante 429 aplica espera indicada o backoff acotado; ante 4xx no recuperable para y revisa la petición. La clave vive fuera del repositorio. Meteorología se une por fecha y ciudad documentadas y se interpreta como contexto, no como demostración causal.

Si las coordenadas vienen en EPSG:4326 están en grados; para distancia local se transforma a un CRS proyectado apropiado. En un mapa se agregan zonas, se aplican mínimos de recuento y se restringe el acceso: una cuadrícula precisa de reservas puede revelar comportamiento individual.

## Criterio de calidad

La respuesta es buena si separa: dato fiable, patrón observado, estimación causal y decisión. No basta con decir “hacer un A/B” ni con añadir más tecnología a una consulta semánticamente incorrecta.
