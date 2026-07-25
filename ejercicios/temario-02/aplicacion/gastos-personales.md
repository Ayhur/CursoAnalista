# Ejercicio aplicado - Auditoría de pedidos de Lumen

## Situación

Lumen quiere publicar el importe diario de pedidos confirmados. La fuente entrega esta lista de eventos; no todos pueden entrar en el total.

```python
pedidos = [
    {"id": "p-201", "canal": "web", "estado": "confirmado", "importe": 75},
    {"id": "p-202", "canal": "app", "estado": "confirmado", "importe": "25.50"},
    {"id": "p-203", "canal": "web", "estado": "cancelado", "importe": 80},
    {"id": "p-204", "canal": "web", "estado": "confirmado", "importe": 0},
    {"id": "p-205", "canal": "partner", "estado": "confirmado"},
]
```

## Entrega

1. Escribe `validar_pedido(pedido)` que acepte solo pedidos con `id`, `canal`, estado `confirmado` e importe convertible a `float` mayor que cero. Debe devolver una **copia** normalizada con importe numérico o lanzar `ValueError` con un motivo claro.
2. Escribe `auditar_pedidos(pedidos, limite_revision=100)` que devuelva un diccionario con `total`, `por_canal`, `ids_revision` e `incidencias`.
3. Un pedido válido entra en `ids_revision` cuando su importe es mayor o igual al límite. Incluye una prueba para un importe exactamente igual a 100.
4. Añade `assert` para: lista vacía, importe de texto convertible, importe cero y el límite de 100.
5. Escribe tres líneas de interpretación: total esperado, número de incidencias y por qué no debes sumar los pedidos excluidos como cero.

## Salida esperada para los datos dados

```text
total: 100.5
por_canal: {'web': 75.0, 'app': 25.5}
ids_revision: []
incidencias: 3
```

No necesitas usar Pandas ni capturar todas las excepciones. La calidad se evalúa por contrato explícito, casos límite y explicación de las exclusiones. Consulta la [solución razonada](../../../soluciones/temario-02/gastos-personales.md) únicamente después de intentarlo.
