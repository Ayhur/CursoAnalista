# Pasos de Power Query

## Objetivo

Transformar dos CSV en una tabla refrescable sin editar el archivo de origen. Una fila de `operaciones-brutas.csv` representa un intento de cobro; no confundas cliente con operación.

## Importar con parámetros

1. En Excel usa **Datos → Obtener datos → Desde archivo → Desde texto/CSV** y selecciona `operaciones-brutas.csv`.
2. Confirma el separador `;`. Elige **Transformar datos**, no «Cargar», para inspeccionar primero los pasos.
3. Crea dos parámetros de texto llamados `RutaOperaciones` y `RutaClientes` con las rutas locales de los archivos. Pega [consulta-operaciones.m](consulta-operaciones.m) en **Editor avanzado**. Los parámetros evitan que la ruta quede enterrada en una secuencia de clics.
4. Revisa que `id_operacion` sea texto, `fecha_hora` fecha/hora, `importe` moneda con configuración regional española y `es_prueba` entero. Si `op-001` se convierte a número o `120,00` queda como texto, detente: aún no tienes una tabla fiable.

## Leer los pasos, no solo pulsar actualizar

La consulta promueve cabeceras, asigna tipos, filtra `es_prueba = 0`, importa clientes, combina por `cliente_id` y clasifica la exclusión del total. **Combinar** añade atributos del cliente a una operación; no debe aumentar el número de operaciones. Si creciera de cinco a diez filas, investigaría una clave duplicada en clientes antes de continuar.

Al actualizar, compara el resultado con [resultado-esperado.csv](resultado-esperado.csv): hay cinco filas, dos pagadas y 170,00 EUR cobrados. `devuelta` y `pendiente` aparecen en la tabla, pero no se clasifican como rechazo ni entran en ese total.

## Refresco y error deliberado

Renombra temporalmente la columna `importe` del CSV y actualiza. El error demuestra que el esquema es un contrato. Devuelve el nombre original, actualiza y registra qué paso dependía de él. No uses «quitar errores» para silenciar el problema.

## Comprobación

Explica qué operación cambia si conviertes el `Left Outer` de clientes en `Inner`. ¿Perderías una operación sin cliente? ¿Sería una decisión de limpieza, una exclusión válida o un incidente de calidad?

