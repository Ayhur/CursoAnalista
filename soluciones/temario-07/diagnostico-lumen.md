# Solución razonada — Diagnóstico visual de Lumen

## 1. Contrato de métrica

La métrica principal es conversión visita→pago: `100 × pagos finalizados únicos / sesiones`. Población: sesiones autenticadas de Lumen; grano: día y plataforma; periodo: lunes a viernes de la semana de 4.2; fuente hipotética: tabla diaria derivada de `events_v3`. El denominador no son inicios de checkout: esa sería otra tasa y otra pregunta.

## 2. Gráficos y mensaje

El primer gráfico es una **línea de conversión diaria por plataforma**: fecha en X, conversión (%) en Y, dos líneas con etiquetas directas y una anotación de “despliegue 4.2”. Título: “La conversión móvil cae tras 4.2 mientras escritorio se mantiene; validar checkout y tracking”. Muestra evolución y contraste, no causalidad.

El segundo es un **funnel por plataforma** con visitas, inicios y pagos, cada uno con número y porcentaje respecto al paso anterior. Responde dónde se pierde el volumen. Un gráfico circular de plataformas no responde ninguna de estas preguntas y oculta denominadores.

## 3. Cálculo e interpretación

Móvil: visitas = 25.600; pagos = 3.580; conversión = `3.580 / 25.600 = 13,98%` (≈ 14,0%). Escritorio: visitas = 20.450; pagos = 3.370; conversión = `3.370 / 20.450 = 16,48%` (≈ 16,5%). Frente a la semana anterior, móvil cae aproximadamente 4,0 puntos porcentuales; escritorio se mantiene prácticamente igual.

La comparación es descriptivamente útil porque usa la misma fórmula, pero necesita cautela: no conocemos mezcla de canales, países, cambios de tráfico ni la completitud de eventos. El retraso de dos horas del miércoles no afecta al cierre diario según el aviso, pero debe verificarse con recuento de eventos y zona horaria antes de usar ese día como evidencia fuerte.

## 4. Funnel

Móvil: inicio/visita = `4.980 / 25.600 = 19,45%`; pago/inicio = `3.580 / 4.980 = 71,89%`; pago/visita = 13,98%. Escritorio: inicio/visita = `4.200 / 20.450 = 20,54%`; pago/inicio = `3.370 / 4.200 = 80,24%`; pago/visita = 16,48%.

La diferencia más clara está entre inicio y pago (≈ -8,4 pp en móvil). Priorizaría revisar el checkout móvil y sus eventos. No concluiría aún que 4.2 causó la caída: puede ser un cambio de mix de usuarios, de pagos rechazados o de instrumentación.

## 5. Recomendación y control

Abriría una incidencia con Producto, Ingeniería y Datos: reproducir checkout móvil en 4.2, contrastar eventos `payment_attempt` y `payment_success` con el proveedor de pagos y preparar reversión si se confirma impacto. Una explicación alternativa es que aumentó el tráfico de una campaña con usuarios menos propensos a pagar; se comprueba desglosando por canal y comparando composición. También revisaría duplicados, retrasos, versiones de evento y que visitas/pagos tengan la misma zona horaria.

## 6. Panel de seguimiento

Panel: conversión móvil visita→pago diaria frente a media móvil de 7 días; propietaria Product Analytics; actualización diaria 09:00 UTC; alerta si cae más de 1 pp con al menos 5.000 sesiones; acción: crear incidencia de checkout y validar tracking; límite: la alerta detecta asociación, no causalidad, y debe mostrar `n`, cambios de tracking y composición por canal.
