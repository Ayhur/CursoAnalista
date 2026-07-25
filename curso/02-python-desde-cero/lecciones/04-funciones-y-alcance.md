# Funciones y alcance

## Objetivos y prerrequisitos

Aprenderás a encapsular una regla reutilizable, diferenciar entrada y salida y evitar depender de variables ocultas. Requiere condiciones y bucles.

## Dar nombre a una transformación

Una **función** es un fragmento de código con un nombre, entradas y una salida. Evita copiar la misma regla en diez lugares y hace que el análisis se pueda revisar por partes.

```python
def clasificar_importe(importe):
    if importe >= 100:
        return "alto"
    return "habitual"

clasificar_importe(120)
```

`importe` es un **parámetro**: el nombre que la función usa para recibir un dato. `return` devuelve un resultado. Una función útil responde una pregunta concreta: “dado un importe, ¿qué etiqueta corresponde según esta regla?”.

## Alcance: qué nombres existen dónde

Los nombres creados dentro de una función normalmente solo existen durante esa llamada. Esto se llama **alcance**. Es una protección: una función debería depender de sus entradas, no de una variable lejana cuyo valor puede cambiar sin avisar.

```python
limite = 100

def es_alto(importe, limite):
    return importe >= limite
```

Aunque parece repetitivo pasar `limite`, deja visible el supuesto. En un análisis, los supuestos invisibles son difíciles de auditar.

## Caso IT y límite

Una función puede estandarizar una comprobación de eventos: clasificar una duración de carga como lenta o aceptable. Pero no convierte el umbral en verdad universal: 2 segundos puede ser aceptable en una página y grave durante un pago. Documenta de dónde sale el umbral.

## Resumen y práctica

- Las funciones nombran transformaciones repetibles.
- Parámetros hacen visibles las entradas; `return` entrega la salida.
- Evitar dependencias ocultas facilita revisar y probar.

Reescribe el cálculo de “pedido alto” como función y pruébalo con 99, 100 y 101. Después estudia [errores y depuración](05-errores-y-depuracion.md).
