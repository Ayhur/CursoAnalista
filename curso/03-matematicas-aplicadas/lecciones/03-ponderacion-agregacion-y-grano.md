# 03. Ponderación, agregación y el grano del dato

## Objetivo

Sabrás elegir el denominador y el peso de un resumen. El **grano** indica qué representa una fila: un pedido, un día, una ciudad o un cliente. Agregar sin saberlo puede duplicar o diluir información.

## La falsa media de tasas

Nexo compara conversión por ciudad:

| Ciudad | Visitas | Pedidos | Conversión |
| --- | ---: | ---: | ---: |
| A | 100 | 15 | 15 % |
| B | 10.000 | 800 | 8 % |

La media simple `(15 % + 8 %) / 2 = 11,5 %` trata ambas ciudades como si tuvieran igual exposición. La conversión global correcta es `815 / 10.100 = 8,07 %`. Una **media ponderada** multiplica cada valor por un **peso** adecuado y divide por la suma de pesos: `(0,15×100 + 0,08×10.000) / 10.100`.

```mermaid
flowchart LR
  A[Filas de pedidos] --> B[Grano: un pedido]
  B --> C[Agrupar por ciudad y semana]
  C --> D[Contar pedidos y visitas]
  D --> E[Dividir sumas compatibles]
  E --> F[Tasa agregada defendible]
```

La regla práctica es sumar primero numeradores y denominadores compatibles y dividir después. Promediar porcentajes casi nunca sustituye esa operación.

## Agregar responde una pregunta nueva

De pedidos individuales a ciudad/día cambiamos de grano. El total de ingresos se suma, pero el tiempo de entrega no debe sumarse: puede promediarse o expresarse como percentil. Una tabla diaria tampoco debe unirse a una tabla por pedido sin comprobar cardinalidad; repetir una fila diaria en cada pedido multiplicaría su facturación.

Define antes: población (pedidos confirmados), filtro (sin pruebas internas), periodo (semana 20), agrupación (ciudad) y función (`sum`, `count`, `mean`, percentil). Esa especificación será después el contrato de una métrica en el bloque 10.

## Ponderar no es maquillar

El peso debe corresponder al mecanismo que se resume. Para conversión se pondera por visitas; para tiempo promedio por pedidos entregados; para una encuesta representativa pueden existir pesos muestrales definidos por investigación. Ponderar por ingresos para resumir tiempo de entrega cambia la pregunta a "tiempo medio de un euro facturado", que quizá no interesa.

### Ejemplo: media de promedios diarios

Dos días tienen 20 pedidos a 20 min y 200 pedidos a 40 min. La media simple de sus medias es 30 min; la media por pedido es `(20×20 + 200×40)/220 = 38,2 min`. Si se planifican repartidores con 30 min, faltará capacidad.

## Errores y comprobación

- Un total puede crecer porque hay más filas duplicadas, no porque hay más pedidos: compara claves únicas.
- Un promedio sin número de casos oculta su fiabilidad.
- Agregar puede ocultar diferencias de segmento; desagrega cuando cambia la acción.

1. ¿Cuál es el grano de una tabla con una fila por pedido?
2. ¿Qué peso usarías para combinar tasas de cancelación por ciudad?
3. ¿Qué función usarías para resumir ingresos y cuál para p90 de entrega?

Continúa con [funciones y modelos](04-funciones-y-modelos.md).
