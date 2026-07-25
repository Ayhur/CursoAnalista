# 02 - Seleccionar, tipar y limpiar sin ocultar pérdidas

## Objetivo y prerrequisitos

Transformarás el extracto de Nébula en una tabla utilizable sin confundir una corrección técnica con una decisión de negocio. Partimos del DataFrame `pedidos_raw` de la lección anterior.

## Seleccionar es formular una condición

`pedidos["canal"]` devuelve una Series. `pedidos[["pedido_id", "canal"]]` conserva un DataFrame. Para seleccionar con intención hay dos herramientas: `loc` usa etiquetas y una condición; `iloc` usa posiciones numéricas para inspección, no para reglas de negocio.

```python
pedidos = pedidos_raw.copy()
pagados = pedidos.loc[pedidos["estado"].eq("pagado")].copy()
ejemplo = pedidos.iloc[:3, :4]
```

La máscara `pedidos["estado"].eq("pagado")` es una Serie de `True`/`False`, una respuesta por fila. Antes de filtrar, cuenta los estados. «Pagado» no equivale siempre a «cobrado», «facturado» ni «sin devolución»: aquí es una definición operativa que debe figurar en el contrato.

## Tipos, fechas y nulos: convertir sin inventar

Los tipos (`dtypes`) determinan qué operaciones son válidas. Para Nébula la fecha llega como texto y el importe usa coma decimal:

```python
pedidos["fecha_pedido"] = pd.to_datetime(
    pedidos["fecha_pedido"], format="%Y-%m-%d", errors="coerce", utc=True
)
pedidos["importe_bruto"] = pd.to_numeric(
    pedidos["importe_bruto"].str.replace(",", ".", regex=False), errors="coerce"
)
pedidos["descuento"] = pd.to_numeric(
    pedidos["descuento"].str.replace(",", ".", regex=False), errors="coerce"
).fillna(0)
```

`errors="coerce"` convierte una conversión imposible en ausente (`NaN` o `NaT`); es una alarma medible, no una reparación. Por ejemplo, una fecha inválida no debe convertirse silenciosamente en la fecha de hoy. Después clasificamos el motivo y conservamos las filas rechazadas:

```python
es_valido = (
    pedidos["pedido_id"].notna()
    & pedidos["fecha_pedido"].notna()
    & pedidos["importe_bruto"].ge(0)
    & pedidos["canal"].isin(["web", "app", "partner"])
)
rechazos = pedidos.loc[~es_valido].assign(motivo="regla_basica")
pedidos_validos = pedidos.loc[es_valido].copy()
```

## Copias y duplicados tienen significado

`copy()` comunica que el resultado será una tabla independiente. Evita modificar de manera inesperada un subconjunto de `pedidos_raw` y evita depender de comportamientos de vista/copia que han evolucionado en Pandas. La regla práctica: conserva `raw`, crea pasos con nombres y asigna con `.loc` sobre el DataFrame que posees.

Un **duplicado técnico** es una fila idéntica repetida por una exportación. Un **duplicado de negocio** son dos filas que comparten `pedido_id` aunque otro campo cambie; puede representar reintento, corrección o corrupción. No se tratan igual:

```python
duplicados_tecnicos = pedidos.duplicated(keep=False)
duplicados_negocio = pedidos.duplicated("pedido_id", keep=False)
print(pedidos.loc[duplicados_negocio].sort_values("pedido_id"))
```

Eliminar con `drop_duplicates("pedido_id")` sin inspección puede quedarse con la primera versión arbitraria. En el laboratorio se conserva la fila más reciente por `fecha_extraccion`, una regla que debe validarse con el área dueña de la fuente.

## Resumen y comprobación

- `loc` expresa reglas con nombres; `iloc` inspecciona posiciones.
- Convertir con `coerce` hace visibles los errores; no equivale a aceptar la fila.
- `raw`, tabla válida y rechazos son artefactos distintos que permiten auditar.

1. ¿Qué información perderías al ejecutar `dropna()` sobre toda la tabla?
2. ¿Por qué dos filas con el mismo `pedido_id` requieren una conversación de negocio antes de eliminarlas?

Sigue con [transformación y agregación](03-transformacion-y-agregacion.md).
