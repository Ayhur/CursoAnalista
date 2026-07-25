# Solución razonada - Bloque 00: activación de Lumen

No existe una única recomendación correcta. Esta solución muestra el nivel de precisión esperado y deja visibles los límites.

## 1. Pregunta y tipo de análisis

> Entre usuarios únicos que instalaron Lumen en Android del 1 al 7 de julio y tienen siete días completos de observación, ¿qué porcentaje completó su primera reserva en los siete días posteriores, comparado con instalaciones Android equivalentes del 1 al 7 de junio en la versión 4.1? ¿La diferencia se concentra en un paso del onboarding, en una versión o en un canal, y qué evidencia necesita Producto antes de decidir una reversión temporal?

Primero procede un análisis **descriptivo y diagnóstico exploratorio**. Hay una diferencia observada, pero aún no una base para atribuir una causa o predecir el efecto de revertir.

## 2. Hechos, hipótesis y comprobaciones

| Hecho observado | Hipótesis que podría explicarlo | Evidencia o comprobación |
| --- | --- | --- |
| 290/1.000 activaron en 4.2 frente a 380/1.000 en 4.1 | El selector de fecha de Android falla en 4.2 | Revisar errores, sesiones que abandonan el selector y reproducir el flujo en dispositivos/versiones afectadas |
| La caída se observa tras el 1 de julio | La campaña desde el 3 de julio trae usuarios con menor intención | Comparar dentro de cada canal y revisar la mezcla de adquisición antes/después |
| El conteo de reservas parece menor | `reserva_completada` dejó de enviarse o cambió de nombre | Contrastar con registros de pago/reserva del backend y revisar despliegue de tracking |
| La comparación es entre semanas distintas | Hay calendario, festivo o disponibilidad de espacios diferente | Comparar semanas equivalentes, disponibilidad y posibles cambios operativos |

La tabla no afirma que todas las hipótesis sean igual de probables. Ordena qué evidencia tiene más valor y evita convertir una secuencia temporal en causalidad.

## 3. Contrato de `activación_7d`

| Campo | Definición propuesta |
| --- | --- |
| Decisión | Priorizar investigación, reversión o cambio de onboarding Android |
| Numerador | Usuarios únicos elegibles con la primera `reserva_completada` ocurrida como máximo 7 x 24 horas después de su instalación |
| Denominador | Usuarios únicos elegibles con `app_instalada` durante el periodo de cohorte |
| Exclusiones | Empleados, cuentas de prueba, fraude conocido y reinstalaciones identificadas |
| Grano | Una instalación elegible por usuario; se cuenta como máximo una activación por instalación |
| Ventana y corte | Siete días desde instalación, zona horaria Europe/Madrid acordada; no incluir cohortes que no hayan completado siete días al corte |
| Fuente y calidad | Eventos de cliente más reservas confirmadas en backend; Datos revisa duplicados, eventos ausentes y cambio de esquema |
| Segmentos | Versión de app, Android/iOS, canal y país solo si el tamaño permite interpretar |
| Propietario | Responsable de producto; Data Engineering avisa cambios de tracking |
| Protección | Tasa de cancelación a siete días y contactos a soporte por cada 100 reservas |

Una respuesta equivalente es válida si hace explícitas reglas comparables. «Reservas / instalaciones» sin estas condiciones no alcanza el contrato.

## 4. Por qué la diferencia no prueba causalidad

Primero, 4.2 y 4.1 se observan en periodos distintos: puede haber cambiado la mezcla de campañas, la disponibilidad o el calendario. Segundo, el evento de reserva puede estar incompleto en 4.2, lo que produciría una caída aparente. También faltaría comprobar que los grupos son comparables y que la ventana de siete días está completa para ambos.

Una reversión puede ser una decisión prudente de contención, pero no convierte por sí misma el diagnóstico anterior en prueba causal. Para estimar causalidad se necesitaría un diseño más controlado, como una prueba aleatoria o una comparación apropiada, tema que se trabajará más adelante.

## 5. Recomendación proporcionada y seguimiento

Una recomendación defendible sería: **no declarar aún una causa; en las próximas horas comprobar tracking contra backend y reproducir el flujo Android. Si ambos confirman un fallo grave del selector y el coste de continuar es alto, revertir temporalmente con un ticket documentado; si no, mantener 4.2 mientras se segmenta por canal y se prepara una comparación más controlada.**

El nivel de certeza es bajo a medio porque solo conocemos una comparación agregada antes/después. Durante siete días tras la acción, Producto y Datos revisarán diariamente activación a 7 días de cohortes maduras, cancelaciones y contactos a soporte; si activación no se recupera o las métricas de protección empeoran, se reabrirá la hipótesis y la decisión.

## Rúbrica (10 puntos)

| Criterio | Puntos | Evidencia de dominio |
| --- | ---: | --- |
| Pregunta y decisión | 2 | Incluye población, resultado, ventana, comparación y decisión real |
| Hipótesis y evidencia | 2 | Separa hechos de explicaciones; incluye al menos tres hipótesis y una comprobación por cada una |
| Contrato de métrica | 3 | Define numerador, denominador, exclusiones, grano, ventana/corte, fuente, propietario y protección |
| Causalidad y límites | 1.5 | Explica por qué la comparación no demuestra causa y no sobrerreclama |
| Recomendación y seguimiento | 1.5 | Propone acción proporcional, condición de reversión y medición posterior |

Una entrega excelente puede recomendar investigar antes de revertir o revertir de forma temporal. Lo que no es aceptable es afirmar una causa sin comprobación, contar una métrica sin contrato o recomendar una acción sin forma de evaluar sus consecuencias.
