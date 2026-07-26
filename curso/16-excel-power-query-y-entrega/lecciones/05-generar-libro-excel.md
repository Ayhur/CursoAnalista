# 5. Generar un libro Excel verificable

## Objetivo

Construirás un archivo que sirva para leer y revisar, no solo para descargar filas. `DataFrame.to_excel` escribe una tabla; una biblioteca como `openpyxl` permite aplicar formato, congelar encabezados, crear varias hojas y proteger contra modificaciones accidentales.

## Diseño antes del código

El libro semanal de Norte Operaciones tendrá cinco hojas: `Resumen`, `Detalle`, `No_pagadas`, `Conciliacion` y `Metadatos`. Esta separación evita que el resumen esconda excepciones y permite a cada audiencia empezar por la hoja adecuada. **No_pagadas** no significa «rechazadas»: separa explícitamente un cobro fallido, uno pendiente y uno devuelto.

<!-- mobile-diagram: rendered fallback -->
![Diagrama: Datos validados](../../../recursos/diagramas-moviles/curso--16-excel-power-query-y-entrega--lecciones--05-generar-libro-excel-01-542b05cc.svg)

<details>
<summary>Ver código Mermaid editable</summary>

```mermaid
flowchart LR
 A[Datos validados] --> B[Resumen ejecutivo]
 A --> C[Detalle filtrable]
 A --> D[No pagadas y motivo]
 B --> E[Conciliación]
 C --> E
 D --> E
 E --> F[Metadatos de entrega]
```
</details>

La hoja de metadatos registra fecha de generación, parámetros, fuente, versión del script y controles ejecutados. No es una garantía de veracidad: es el punto de partida para que alguien reconstruya una cifra.

## Ejemplo de generación

```python
from pathlib import Path
import pandas as pd
from openpyxl import load_workbook
from openpyxl.styles import Font, PatternFill

ruta = Path("salidas/informe_operaciones_2026-07-13.xlsx")
with pd.ExcelWriter(ruta, engine="openpyxl") as escritor:
    resumen.to_excel(escritor, sheet_name="Resumen", index=False)
    detalle.to_excel(escritor, sheet_name="Detalle", index=False)
    no_pagadas.to_excel(escritor, sheet_name="No_pagadas", index=False)
    controles.to_excel(escritor, sheet_name="Conciliacion", index=False)
    metadatos.to_excel(escritor, sheet_name="Metadatos", index=False)

libro = load_workbook(ruta)
for hoja in libro.worksheets:
    hoja.freeze_panes = "A2"
    hoja.auto_filter.ref = hoja.dimensions
    for celda in hoja[1]:
        celda.font = Font(bold=True, color="FFFFFF")
        celda.fill = PatternFill("solid", fgColor="1D5D84")
libro.save(ruta)
```

El formato sigue al significado: `importe_eur` usa moneda; `fecha_utc` usa un formato de fecha/hora y un nombre que declare la zona; las columnas se ajustan con límite razonable para que no aparezcan hojas ilegibles. Evita fórmulas críticas ocultas; si introduces una, documenta fórmula, rango y control independiente.

## Conciliación y lectura humana

En `Conciliacion`, compara al menos: filas extraídas, pruebas excluidas, filas elegibles, pagos, no pagos, identificadores distintos y total pagado de dos cálculos. La identidad `elegibles = pagadas + no_pagadas` debe cuadrar antes de entregar. Para dinero se concilian **céntimos enteros**; no una comparación aproximada de coma flotante. Muestra resultado, umbral y acción: «diferencia = 0 → entregar; diferencia ≠ 0 → bloquear y revisar».

Los registros no pagados conservan estado y motivo: `rechazada` = autorización o cobro fallido; `pendiente` = resultado no definitivo; `devuelta` = pago revertido. Clasificar no es filtrar: una fila excluida del total puede seguir siendo imprescindible para explicar una tasa o una incidencia.

## Errores frecuentes

Un archivo con formato bonito puede ser inutilizable si: cambia la columna de fecha a texto, trunca decimales, exporta filas personales no necesarias, sobrescribe el informe anterior o titula “Total” a una suma que mezcla monedas. El laboratorio crea títulos, instrucciones visibles, tablas estructuradas, formato monetario, cabeceras consistentes y controles fallidos resaltados. `Metadatos` se protege contra cambios accidentales, pero esa protección no sustituye los permisos de acceso. El nombre de archivo debe incluir periodo y momento de generación, por ejemplo `operaciones_2026-07-13_a_2026-07-20_generado_2026-07-20T0815Z.xlsx`.

## Resumen

Un libro profesional comunica resultado, detalle, excepciones y evidencia. Formatear no es maquillar: reduce errores de interpretación y facilita una revisión que pueda fallar de manera visible.

**Fuente primaria:** [documentación de `DataFrame.to_excel`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.to_excel.html) y [tutorial de openpyxl](https://openpyxl.readthedocs.io/en/stable/tutorial.html).
