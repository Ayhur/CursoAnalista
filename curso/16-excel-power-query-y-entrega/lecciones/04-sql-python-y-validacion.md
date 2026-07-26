# 4. Consultar y validar datos desde Python

## Objetivo

Extraerás datos de una base con una consulta de solo lectura, parámetros y controles. Una **consulta parametrizada** separa la instrucción SQL de los valores como fechas; evita construir texto SQL mezclando datos externos y hace visible qué periodo se pidió.

## Antes de programar: contrato de extracción

Para el informe semanal define: variable objetivo = importes cobrados; grano = un intento de cobro; periodo = desde el lunes 00:00 UTC inclusive hasta el lunes siguiente exclusivo; fuente = tabla `operaciones`; exclusión = pruebas internas; salida = resumen, detalle y no pagadas. Sin este contrato, el código puede ser correcto y responder otra pregunta.

<!-- mobile-diagram: rendered fallback -->
![Diagrama: Parámetros: inicio y fin](../../../recursos/diagramas-moviles/curso--16-excel-power-query-y-entrega--lecciones--04-sql-python-y-validacion-01-612e8e93.svg)

<details>
<summary>Ver código Mermaid editable</summary>

```mermaid
flowchart TD
 A[Parámetros: inicio y fin] --> B[SQL de solo lectura]
 B --> C[DataFrame]
 C --> D[Controles: esquema, periodo y unicidad]
 D --> E{¿Controles superados?}
 E -->|sí| F[Generar entrega]
 E -->|no| G[Detener y registrar incidencia]
```
</details>

Detener es una salida válida. Generar un Excel con una extracción incompleta solo porque el script no produjo una excepción es peor que avisar de una incidencia.

## Ejemplo mínimo

```python
import sqlite3
import pandas as pd

consulta = """
SELECT operacion_id, fecha_utc, estado, importe_centimos, canal
FROM operaciones
WHERE fecha_utc >= :inicio AND fecha_utc < :fin
  AND es_prueba = 0
"""

with sqlite3.connect("operaciones.sqlite") as conexion:
    datos = pd.read_sql_query(
        consulta, conexion,
        params={"inicio": "2026-07-13", "fin": "2026-07-20"},
    )
```

El laboratorio usa `importe_centimos`: `12000` equivale a 120,00 EUR. El nombre hace visible que SQL y Python trabajan con enteros para conciliar; la conversión a euros se reserva para el libro que leerá una persona.

`read_sql_query` crea un DataFrame —una tabla en memoria con filas y columnas— a partir de la consulta. SQLite es útil para aprender porque es local; en un entorno empresarial el conector puede ser PostgreSQL u otro motor. Las credenciales no se escriben dentro del script ni se suben al repositorio: se inyectan mediante variables de entorno o un gestor de secretos y se usan con un usuario de solo lectura.

## Controles que responden a riesgos

- **Esquema:** ¿están las columnas necesarias y sus tipos son interpretables?
- **Periodo:** ¿la fecha mínima y máxima están dentro de los límites declarados?
- **Unicidad:** ¿`operacion_id` se repite cuando el grano promete una fila por intento?
- **Completitud:** ¿hay nulos en identificador, fecha, estado o importe?
- **Conciliación:** ¿las filas extraídas, pruebas excluidas, elegibles, pagos y no pagos encajan entre sí? ¿El importe de pagos calculado en el DataFrame coincide exactamente, en céntimos, con una segunda consulta SQL?
- **Exclusiones:** ¿cuántas filas de prueba, devoluciones o estados desconocidos quedaron fuera y por qué?

Un control debe fallar correctamente. Si faltase `operacion_id`, intentar contar duplicados produciría un `KeyError` técnico y ocultaría el problema real. Primero se comprueba el esquema; si faltan columnas, el laboratorio genera un control fallido con los nombres ausentes, bloquea la entrega y no ejecuta los controles que dependen de ellas. Un `assert` o una excepción de dominio clara puede impedir la entrega, pero el informe de controles debe explicar qué corregir.

Para dinero, la base didáctica guarda `importe_centimos` como entero: 12 000 representa 120,00 EUR. Así, tanto Pandas como SQL suman enteros y la conciliación exige igualdad exacta. El Excel final muestra euros para lectura; en una base empresarial usarías un tipo decimal apropiado o centavos enteros, no `float` como fuente de verdad.

## Límite técnico y ético

Parametrizar valores no habilita parametrizar arbitrariamente nombres de tabla o permisos. No ejecutes escrituras (`DELETE`, `UPDATE`) desde un informe; limita columnas y filas al mínimo necesario y evita exportar identificadores personales si el destinatario no los requiere.

**Comprobación:** si el total cae a cero porque cambió el nombre de un estado, ¿qué control lo detectaría y qué debería hacer el proceso?

**Fuente primaria:** [pandas `read_sql_query`](https://pandas.pydata.org/docs/reference/api/pandas.read_sql_query.html).
