# Solución - Gastos personales

```python
movimientos = [
    {"categoria": "comida", "importe": 34.5},
    {"categoria": "transporte", "importe": 20},
    {"categoria": "comida", "importe": 72},
    {"categoria": "ocio", "importe": 18},
    {"categoria": "hogar", "importe": 110},
]

total = 0
por_categoria = {}

for movimiento in movimientos:
    categoria = movimiento["categoria"]
    importe = movimiento["importe"]
    total += importe
    por_categoria[categoria] = por_categoria.get(categoria, 0) + importe

mayores_de_100 = [
    categoria for categoria, importe in por_categoria.items() if importe > 100
]

print(total)
print(por_categoria)
print(mayores_de_100)
```

Si un importe fuese texto, Python no podría sumarlo directamente a un número. En un caso real habría que validar y convertir el tipo antes de calcular.
