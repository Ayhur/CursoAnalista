# Lección 06 - Laboratorio: investigar la caída de checkout

## Objetivo

Ejecutarás un análisis exploratorio completo, desde el perfil hasta una nota de decisión, sobre un archivo pequeño y auditable.

## Datos y contrato

Abre `datasets/nebula_checkout_mayo.csv`. Cada fila es una combinación diaria de fecha, plataforma y canal. `visitas` cuenta visitas al checkout y `compras` pagos completados atribuidos al mismo corte diario. Es un dataset didáctico: no representa usuarios individuales ni prueba causalidad.

Ejecuta desde la raíz del repositorio:

```bash
python notebooks/practicas/06-eda-incidencia-checkout.py
```

El script usa solo la biblioteca estándar de Python para que pueda correrse sin instalar paquetes. El código muestra el perfil, tasas correctamente ponderadas por visitas, comparaciones por plataforma y una alerta de calidad. Después reescribe una parte con Pandas para quien quiera practicar el flujo habitual.

## Secuencia de trabajo

1. Lee el contrato y comprueba las columnas, fechas, duplicados y rangos.
2. Calcula la tasa total sumando compras y visitas.
3. Separa referencia y semana actual; compara total y plataforma.
4. Examina el día de conversión cero y formula al menos dos explicaciones.
5. Redacta el hallazgo con una limitación y una siguiente comprobación.

No hay una causa «oculta» que debas adivinar. La respuesta correcta identifica qué muestran los datos y qué información externa sería necesaria para pasar de sospecha a causa.

## Entrega mínima

Tu respuesta al [ejercicio aplicado](../../../ejercicios/temario-06/aplicacion/investigar-caida.md) debe incluir una tabla de tasas con denominadores, dos hipótesis rivales, tratamiento justificado de la observación extrema y una actualización responsable al equipo. Consulta la [solución razonada](../../../soluciones/temario-06/investigar-caida.md) solo después de intentarlo.
