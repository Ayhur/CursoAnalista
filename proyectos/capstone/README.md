# Capstone - Analisis de principio a fin

## Reto y resultado

Construye una entrega que ayude a decidir algo realista: conversion de un producto, demanda, retencion, eficiencia operativa o desigualdad de servicio. Puedes usar datos publicos con licencia o datos simulados claramente etiquetados. No se evalua que la empresa sea real: se evalua que la pregunta, evidencia y limite sean honestos.

## Proyecto minimo guiado

Si no tienes tema, usa *Nimbo*. Se entrega una recomendacion sobre el embudo de alta de comercios. La pregunta es: "en que paso conviene investigar primero la activacion de comercios iniciados en abril?". Define activacion como publicar un menu dentro de siete dias, trabaja con una tabla de eventos simulada y declara que no puedes inferir causalidad.

## Hitos, entregables y criterio de terminado

| Hito | Entregable | Listo cuando |
| --- | --- | --- |
| 1. Contrato | pregunta, decision, metrica, ventana, poblacion, fuente/licencia | un revisor puede explicar que decision cambia con el resultado |
| 2. Datos | diccionario, procedencia, grano, chequeos de calidad y privacidad | problemas, exclusiones y tratamiento estan en el registro |
| 3. Analisis | notebook o script y tabla/grafico central | se ejecuta desde una instruccion limpia o se declara la limitacion |
| 4. Argumento | README ejecutivo, interpretacion, limite y siguiente prueba | no confunde asociacion con causalidad |
| 5. Entrega | licencia, presentacion de cinco diapositivas y guion | rubrica >= 70/100, sin fallo critico y defensa de cinco minutos |

## Entregables obligatorios

1. README ejecutivo con pregunta, decision, hallazgo, recomendacion, limites y ejecucion.
2. Diccionario de datos, procedencia/licencia y evaluacion de calidad.
3. Analisis reproducible en Python y/o SQL; incluir dependencias o instrucciones del entorno.
4. Metricas definidas y visualizaciones que muestren denominador, unidad, poblacion y ventana.
5. Registro de decisiones: que se cambio, por que, con que evidencia y que alternativa se descarto.
6. Presentacion para publico no tecnico y guion de cinco minutos.

## Estructura sugerida

```text
mi-capstone/
  README.md
  LICENSE
  data/README.md
  docs/diccionario-datos.md
  docs/registro-decisiones.md
  notebooks/01_analisis.ipynb
  outputs/
  requirements.txt
```

Parte de las [plantillas](plantillas/README.md) y comprueba la [rubrica](../../evaluaciones/rubricas/capstone.md) al terminar cada hito, no solo al final.

## Limites y seguridad

No publiques PII, secretos, tokens, rutas locales ni datos sin permiso de redistribucion. Un resultado observacional no demuestra que una accion cause un resultado. Si no puedes compartir datos, comparte esquema, datos sinteticos o instrucciones autorizadas y explica exactamente que no se puede reproducir.
