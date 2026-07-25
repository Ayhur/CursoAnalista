# Temario completo - Curso de Analista de Datos con Python

# Bloque 00 - Orientación y pensamiento analítico

## Propósito

Antes de escribir una consulta, abrir Python o crear un gráfico, un analista debe saber qué decisión está ayudando a tomar. Este bloque enseña a convertir una preocupación de negocio en una investigación revisable: una pregunta concreta, una hipótesis que puede fallar, evidencia adecuada, una recomendación prudente y un plan de seguimiento.

El hilo conductor es un caso de producto IT: **Lumen**, una app de reservas de espacios de trabajo, detecta que menos personas que instalan la app completan su primera reserva. Leo acompañará a producto e ingeniería desde el aviso inicial hasta la decisión y su medición posterior.

## Resultados observables

Al completar el bloque podrás:

- distinguir descripción, diagnóstico, predicción y prescripción, y saber qué no permite concluir cada uno;
- redactar un brief analítico que otra persona pueda ejecutar y revisar;
- separar hechos observados, hipótesis y evidencia;
- definir una métrica con evento, denominador, exclusiones, grano, ventana, fuente y decisión asociada;
- estudiar desde el móvil dejando un registro reproducible de tus respuestas y supuestos.

## Ruta de aprendizaje

1. [El rol del analista, tipos de análisis y ciclo de decisión](lecciones/01-rol-y-ciclo-de-decision.md)
2. [Preguntas, hipótesis, evidencia y contrato de métrica](lecciones/02-preguntas-hipotesis-y-evidencia.md)
3. [Método de estudio, brief y trabajo reproducible](lecciones/03-metodo-de-estudio-y-diagnostico.md)

## Prerrequisitos y práctica móvil

No necesitas programación ni vocabulario técnico. Desde el móvil puedes leer las lecciones, copiar la [plantilla de brief](plantillas/brief-analitico.md) en una nota y responder el ejercicio. Cuando dispongas de ordenador, repetirás este mismo razonamiento con datos en los bloques siguientes.

## Evaluación del bloque

Completa el [caso integrador de Lumen](../../ejercicios/temario-00/comprension/preguntas.md) sin mirar la solución. Después compáralo con la [solución razonada y rúbrica](../../soluciones/temario-00/preguntas.md). No se evalúa acertar una causa inventada: se evalúa formular una investigación y una decisión defendibles.

# El rol del analista, tipos de análisis y ciclo de decisión

## Resultado observable y punto de partida

Al terminar podrás recibir una frase como «la activación ha caído» y convertirla en un recorrido de investigación. Distinguirás cuatro tipos de análisis sin confundir una descripción con una causa o una recomendación. No necesitas saber programar: una **app** es un programa que una persona usa en su teléfono; un **evento** será una acción que la app registra, como instalarla o completar una reserva.

## Caso continuo: la caída de activación de Lumen

Lumen permite reservar puestos de trabajo. El lunes, la responsable de producto escribe: «La activación ha bajado; arregladlo». Antes de actuar faltan datos importantes.

Llamaremos **activación** a que una persona nueva llega a realizar la primera acción de valor del producto. En Lumen, de momento, esa acción será completar una primera reserva. Esta definición es una elección de negocio, no una propiedad mágica del software: más adelante se formalizará para que todos cuenten lo mismo.

El encargo útil no es «mirar los datos». Es decidir entre opciones con coste: ¿priorizar una incidencia de ingeniería en el formulario?, ¿cambiar el texto de bienvenida?, ¿pausar una campaña que atrae usuarios poco adecuados?, ¿esperar porque la caída es solo una variación normal? El analista hace visible qué evidencia haría preferible una opción.

## Del brief al seguimiento

Este flujo responde a «¿qué debe ocurrir entre una alarma y una decisión responsable?».

```mermaid
flowchart LR
  A[Brief: caída de activación] --> B[Pregunta y métrica]
  B --> C[Hipótesis alternativas]
  C --> D[Comprobar evidencia]
  D --> E[Recomendación con límite]
  E --> F[Acción de producto]
  F --> G[Seguimiento y aprendizaje]
```

El seguimiento vuelve a abrir una pregunta, aunque lo representemos como el final de este recorrido para conservar un diagrama legible en PDF. Si Lumen simplifica una pantalla, debe comprobar después si sube la activación **sin** empeorar cancelaciones, soporte o ingresos. Una recomendación no cierra el análisis; crea una nueva situación que hay que observar.

## Cuatro preguntas, cuatro tipos de análisis

La misma caída puede estudiarse con preguntas distintas. La tabla no es una escalera automática: cada tipo necesita evidencia diferente.

| Tipo | Pregunta de Lumen | Entrega útil | Lo que no permite afirmar por sí solo |
| --- | --- | --- | --- |
| Descriptivo | ¿Cuánto cambió la activación y en qué fechas? | Serie, segmentos y definición de la medida | Por qué cambió ni qué hacer |
| Diagnóstico | ¿En qué paso, dispositivo o canal se concentra la caída? | Hipótesis priorizadas y comprobaciones | Que un factor observado sea la causa |
| Predictivo | ¿Cuántas activaciones esperamos la próxima semana si continúa el patrón? | Estimación con incertidumbre | Que una acción concreta produzca el resultado |
| Prescriptivo | ¿Qué opción conviene ejecutar dadas las evidencias, costes y riesgos? | Recomendación, condiciones y seguimiento | Que sea óptima o causalmente demostrada sin experimento |

En lectura rápida, el análisis **descriptivo** responde «qué pasó»; el **diagnóstico** pregunta «dónde y con qué explicaciones plausibles»; el **predictivo** estima «qué podría pasar»; y el **prescriptivo** propone «qué conviene hacer, bajo qué condiciones y cómo sabremos si funcionó». Ninguno autoriza por sí solo a afirmar causalidad.

### Ejemplo trabajado

La primera comprobación muestra que la activación pasó de 38% a 29% entre dos semanas comparables. Eso es **descriptivo**. Al separar por plataforma, la caída aparece sobre todo en Android y coincide con una actualización. Eso es **diagnóstico exploratorio**: orienta a revisar el formulario y los registros de error, pero aún no prueba que la actualización sea la causa. Si Lumen estima el número de activaciones de la semana siguiente para dimensionar soporte, está haciendo una **predicción**. Si decide revertir la actualización temporalmente porque el riesgo de perder usuarios es alto y medirá el efecto, está haciendo una **prescripción** bajo incertidumbre.

### Contraejemplos que evitan errores caros

- «Android cayó después de la actualización; por tanto, la actualización causó la caída». Es una hipótesis plausible, no una prueba. También pudo cambiar la mezcla de campañas o dejar de registrarse un evento.
- «El modelo predice 600 activaciones; por tanto, cambiar el botón dará 600». Una predicción de demanda no mide el efecto causal de un cambio de interfaz.
- «Recomiendo cambiar el texto porque parece claro». Una recomendación sin métrica de éxito, coste o plan de reversión es una opinión, no una decisión analítica.

## El producto real del analista

Un gráfico puede ser una evidencia, pero no es el producto final. Una entrega profesional deja una cadena que otra persona puede revisar:

- **Decisión:** qué se puede hacer y quién decide.
- **Pregunta:** qué comparación responderá esa decisión.
- **Evidencia:** qué registros, periodos y comprobaciones la sostienen.
- **Interpretación:** qué muestra el resultado y qué permanece incierto.
- **Recomendación:** acción, coste, riesgo y criterio de seguimiento.

Esta cadena protege tanto a Lumen como al analista: evita que una cifra bonita se convierta en una afirmación que los datos no permiten.

## Resumen y comprobación

- Describir, diagnosticar, predecir y prescribir responden preguntas distintas.
- Una asociación observada puede priorizar una investigación, pero no demuestra causalidad.
- Toda acción debe tener una métrica de seguimiento y una posible condición de reversión.

Comprueba tu comprensión: si la activación baja solo en Android, ¿qué dos explicaciones alternativas investigarías antes de culpar al formulario? ¿Qué dato distinguiría una caída real de un fallo de medición?

En la siguiente lección convertirás la alarma de Lumen en una pregunta comprobable y un contrato de métrica. Después resuelve el [caso integrador](../../../ejercicios/temario-00/comprension/preguntas.md).

# Preguntas, hipótesis, evidencia y contrato de métrica

## Resultado observable y prerrequisitos

Al terminar redactarás una pregunta analítica y el contrato completo de una métrica de activación. Usarás el caso de Lumen de la lección anterior. Una **métrica** es una regla repetible para medir algo; un **KPI** es una métrica elegida para seguir un objetivo importante. No toda cifra merece ser KPI.

## De una preocupación a una pregunta comprobable

«Queremos que más personas usen la aplicación» expresa una intención, no una investigación. Una pregunta comprobable especifica, como mínimo:

- **Población:** ¿de qué personas o casos hablamos?
- **Resultado:** ¿qué acción o valor observaremos?
- **Ventana temporal:** ¿cuánto tiempo tiene cada persona para lograrlo?
- **Comparación:** ¿frente a qué fecha, segmento o versión?
- **Decisión:** ¿qué acción puede cambiar la respuesta?

Para Lumen: «Entre las personas que instalan la versión 4.2 de Lumen, ¿qué porcentaje completa una primera reserva dentro de siete días, comparado con la versión 4.1, y en qué paso del flujo se concentra la diferencia para decidir si revertimos el cambio?».

La pregunta no presupone que la versión sea culpable. Ese detalle permite que la evidencia contradiga la sospecha inicial.

## Hecho, hipótesis y evidencia: mantener las piezas separadas

Una **hipótesis** es una explicación provisional que podría ser falsa; por ejemplo: «el selector de fecha de Android impide avanzar». Un **hecho observado** sería: «en Android, el 31% llega a `reserva_iniciada`, frente al 43% antes de la versión». La **evidencia** es la información que puede apoyar, matizar o refutar la hipótesis: registros de error, repetición del flujo, una comparación con iOS o una prueba controlada.

Este diagrama responde a «¿cómo evitar que una sospecha se disfrace de conclusión?».

```mermaid
flowchart TB
  A[Hecho: baja la activación Android] --> B[Hipótesis: falla selector]
  B --> C[Predicción observable]
  C --> D[Registros, prueba y comparación]
  D --> E[Decisión: ¿la evidencia encaja?]
  E -->|sí, con límites| F[Priorizar corrección]
  E -->|no o incompleta| G[Revisar hipótesis y medición]
```

La ruta «sí» no elimina los límites: quizá el cambio coincide con una campaña. Por eso la recomendación debe indicar el nivel de seguridad y qué se medirá tras actuar.

## Contrato completo de métrica

Decir «la activación es 29%» es insuficiente. Dos personas pueden llegar a números distintos si una cuenta instalaciones y otra cuentas, o si una incluye empleados de Lumen. Un **contrato de métrica** documenta las reglas antes de discutir el resultado.

| Campo | Contrato de activación de Lumen | Por qué evita errores |
| --- | --- | --- |
| Nombre y decisión | Activación a 7 días; decidir si investigar/revertir cambios de onboarding | Conecta medida y acción |
| Evento numerador | Usuarios únicos con `reserva_completada` dentro de 7 días tras instalar | Dice qué éxito cuenta |
| Denominador | Usuarios únicos con `app_instalada` en la versión y periodo definidos | Evita dividir por una población distinta |
| Exclusiones | Empleados, cuentas de prueba, fraudes detectados y reinstalaciones identificadas | Evita inflar o sesgar la tasa |
| Grano | Una fila lógica por usuario e instalación elegible | Impide contar varias reservas como varias personas |
| Ventana y fecha de corte | 7 días desde instalación; solo instalaciones con 7 días completos al corte | Evita comparar cohortes inmaduras |
| Fuente y calidad | Eventos de la app y tabla de usuarios; comprobar duplicados, zona horaria y eventos faltantes | Hace el número auditable |
| Segmentos autorizados | Versión, sistema operativo y canal de adquisición | Permite localizar el problema sin inventar segmentos |
| Propietario y revisión | Producto es propietario; Datos revisa cambios de tracking antes de publicar | Define responsabilidad |
| Métricas de protección | Cancelación en 7 días y contactos a soporte por reserva | Evita optimizar activación a costa de la experiencia |

Para que el contrato también pueda leerse sin una tabla, conserva esta lista de control:

- Cuenta como éxito el evento `reserva_completada` dentro de siete días; cuenta como entrada cada instalación elegible.
- Excluye empleados, pruebas, fraude conocido y reinstalaciones identificadas; cada unidad es una instalación elegible por usuario.
- Espera a que cada cohorte complete siete días y documenta zona horaria, fuente y comprobaciones de duplicados o eventos ausentes.
- Segmenta por versión, sistema operativo y canal; Producto es propietario y Datos revisa cambios de tracking.
- Junto a activación, vigila cancelaciones y contactos a soporte para no mejorar un número a costa de la experiencia.

En notación sencilla:

`activación_7d = usuarios elegibles con primera reserva en 7 días / usuarios elegibles que instalaron`

La fórmula no sustituye el contrato. Sin exclusiones, grano y ventana, dos fracciones con el mismo nombre pueden significar cosas opuestas.

## Ejemplo trabajado: decidir con un contrato

El 8 de julio, Lumen compara instalaciones del 1 al 7 de junio (versión 4.1) con instalaciones del 1 al 7 de julio (versión 4.2). Espera hasta el 15 de julio para que todos tengan siete días completos. Tras excluir empleados y reinstalaciones, calcula 380 activados de 1.000 elegibles (38%) frente a 290 de 1.000 (29%).

La diferencia describe una señal prioritaria, pero todavía hay preguntas: ¿el evento `reserva_completada` siguió enviándose? ¿cambió el canal de adquisición? ¿la caída aparece también en iOS? El contrato no responde por sí solo; garantiza que esas preguntas parten del mismo objeto medido.

## Error frecuente: optimizar una métrica huérfana

Si Lumen premia solo «reservas creadas», podría añadir una reserva automática que después se cancela. La tasa parecería mejor mientras el usuario recibe una experiencia peor. Por eso una métrica principal necesita métricas de protección y una decisión explícita. Esto se verá con más profundidad en el bloque de métricas y producto.

Otro error es cambiar el contrato después de ver el resultado para hacerlo favorable. Si la definición debe cambiar por una mejora legítima de tracking, se versiona: se conserva la definición anterior, se indica desde qué fecha rige la nueva y se evita comparar series incompatibles como si fueran iguales.

## Resumen y comprobación

- Una pregunta comprobable incluye población, resultado, ventana, comparación y decisión.
- Hecho, hipótesis y evidencia cumplen papeles distintos; una correlación no prueba una causa.
- Una métrica profesional necesita más que una fórmula: evento, denominador, exclusiones, grano, ventana, fuente y uso.

Antes de avanzar, intenta explicar por qué «usuarios activos: 10.000» no es aún un resultado interpretable. Después usa la [plantilla de brief](../plantillas/brief-analitico.md) y resuelve el [caso integrador](../../../ejercicios/temario-00/comprension/preguntas.md).

# Método de estudio, brief y trabajo reproducible

## Resultado observable y prerrequisitos

Sabrás estudiar una lección desde el móvil y dejar un brief que otra persona pueda continuar. No hace falta instalar nada. Un **brief** es una nota breve que fija el problema, la decisión, las reglas de medida y los límites antes de investigar; no es un informe final ni una orden de confirmar una sospecha.

## Estudiar para poder aplicar, no solo reconocer

Leer «activación = 29%» puede hacer que el concepto parezca familiar. Poder usarlo exige recuperar la idea sin mirar y defender una decisión. Para cada lección, alterna:

1. **Comprender:** lee el ejemplo y señala palabras nuevas.
2. **Recuperar:** cierra la página y explica con tus palabras qué se mide y por qué.
3. **Aplicar:** resuelve una variación pequeña sin consultar la solución.
4. **Contrastar:** compara con la solución, corrige el razonamiento y anota qué supuesto omitiste.

Desde el móvil puedes copiar la plantilla en una aplicación de notas y escribir en frases cortas. No necesitas escribir código todavía. Cuando tengas ordenador, un **notebook** será una página que mezcla explicación, código ejecutable y resultados; empezarás desde cero en el bloque de Python.

## El brief mínimo que hace el análisis continuable

Una investigación no es reproducible porque use una herramienta moderna. Es **reproducible** cuando otra persona puede entender qué se preguntó, qué información se usó, qué reglas se aplicaron y por qué se recomendó actuar. El siguiente mapa responde a «¿qué debe conservarse para revisar el caso de Lumen?».

```mermaid
flowchart LR
  A[Decisión y contexto] --> B[Pregunta e hipótesis]
  B --> C[Contrato de métrica]
  C --> D[Fuentes y comprobaciones]
  D --> E[Resultado y límites]
  E --> F[Acción y seguimiento]
```

Si alguien recibe solo un gráfico final, no puede comprobar si se incluyeron cuentas de prueba, si la comparación tenía la misma ventana o si la recomendación fue prudente. La [plantilla reutilizable](../plantillas/brief-analitico.md) guarda los seis eslabones.

## Ejemplo: un brief inicial para Lumen

Un inicio honesto podría decir:

> **Decisión:** Producto decidirá el viernes si revierte temporalmente el onboarding 4.2 en Android. **Pregunta:** comparar activación a siete días de instalaciones 4.2 frente a 4.1, por sistema operativo y paso del flujo. **Hipótesis alternativas:** error en selector de fecha, cambio de mezcla de campañas o evento de reserva no registrado. **Límite inicial:** una comparación antes/después no demuestra causalidad. **Seguimiento:** si se revierte, medir activación, cancelación y contactos a soporte durante una semana comparable.

Fíjate en lo que no hace: no afirma que el selector «es la causa» y no borra explicaciones alternativas. Un brief puede empezar con incógnitas; su trabajo es hacerlas visibles.

## Usar AI como tutor, no como piloto automático

La AI puede adaptar ejemplos y hacer preguntas, pero no convierte una respuesta convincente en evidencia. Una petición útil para Leo sería: «No sé qué es un denominador. Explícame la activación de Lumen usando tres personas ficticias; después pídeme que defina a quién excluiría». Después verifica el ejemplo cambiando valores y explica por qué cambia el resultado.

No pegues datos personales, credenciales ni información privada de una empresa en una herramienta pública. Cuando más adelante uses código, conserva la fuente y los pasos; cuando uses AI, conserva también la pregunta importante y verifica cualquier consulta o conclusión antes de compartirla.

## Diagnóstico y siguiente ruta

Tener formación matemática ayuda, pero no permite saltarse las decisiones de medida. Una tasa puede estar bien calculada y responder una pregunta equivocada. Si ya dominas porcentajes, usa los ejemplos para repasar y dedica tiempo a los conceptos nuevos: población, evento, grano, ventana y evidencia.

Después de completar el ejercicio, continúa con el [bloque 01](../../01-fundamentos-datos/README.md). Allí aprenderás qué es un archivo, una tabla, una fila y una columna: las piezas que después permitirán implementar el contrato de métrica con datos reales.

## Resumen y comprobación

- Estudiar implica recuperar, aplicar y corregir, no solo leer.
- Un brief conserva decisión, pregunta, contrato, evidencia, límites y seguimiento.
- AI es útil para practicar si mantienes el control de los datos y verificas las conclusiones.

Pregúntate: ¿qué tendría que escribir Lumen en el brief si el sistema deja de registrar `reserva_completada`? ¿Por qué un número calculado correctamente podría seguir siendo una mala base para decidir?

# Bloque 01 - Fundamentos de datos: desde archivos hasta calidad

## Propósito

Antes de programar o abrir una base de datos, Leo debe entender qué representa un dato, cómo se organiza la información y por qué una cifra aparentemente correcta puede conducir a una decisión equivocada. Este bloque no presupone que sepas qué es CSV, JSON, una tabla o una clave.

## Resultado de salida

Al terminar podrás abrir un archivo sencillo y explicar qué información contiene, distinguir una tabla de un documento JSON, identificar el grano de un conjunto de datos, proponer controles de calidad y reconocer límites de privacidad y sesgo.

## Lecciones

1. [Qué es un dato, un archivo y una tabla](lecciones/01-archivo-tabla-y-grano.md).
2. [Filas, columnas, tipos y relaciones](lecciones/02-filas-columnas-y-relaciones.md).
3. [CSV, JSON, Excel, Parquet y bases de datos](lecciones/03-formatos-y-almacenamiento.md).
4. [Calidad, ausencia, sesgo, privacidad y ética](lecciones/04-calidad-y-uso-responsable.md).

## Práctica

Realiza [la auditoría de calidad](../../ejercicios/temario-01/comprension/auditoria-calidad.md) después de la lección 4 y compárala con [la solución razonada](../../soluciones/temario-01/auditoria-calidad.md).

# 01.1 Qué es un dato, un archivo y una tabla

## Objetivos

Entender qué es un dato antes de hablar de herramientas; distinguir una información suelta de un conjunto organizado; y reconocer qué representa una fila de una tabla.

## Empieza por una situación cotidiana

Imagina una tienda que quiere saber qué productos se venden más. Cada vez que una persona compra algo, la tienda puede guardar información: fecha, producto, importe y forma de pago. Cada una de esas piezas es un **dato**: una representación de algo que ocurrió en el mundo real.

La información se guarda en un **archivo**, igual que una fotografía o una nota de texto. Un archivo tiene nombre, contenido y un formato que indica cómo se organiza. No hay magia: un archivo de datos es una manera de guardar información para poder leerla, compartirla o analizarla después.

Una de las formas más comunes de organizar datos es una **tabla**. Una tabla se parece a una hoja de cálculo: tiene columnas que describen qué tipo de información guardamos y filas que recogen casos concretos.

```text
fecha       | producto | importe | canal
2026-01-03  | teclado  | 45.99   | web
2026-01-04  | ratón    | 19.90   | tienda
2026-01-04  | teclado  | 45.99   | web
```

En este ejemplo, la primera fila de datos representa una compra concreta. La columna `producto` responde qué se compró; `importe`, cuánto costó. La tabla no “sabe” qué significa un teclado: nosotros le damos significado a las columnas.

## El grano: la pregunta que evita errores grandes

El **grano** indica qué representa exactamente una fila. Aquí, una fila representa una compra, no un cliente ni un producto. Esta frase parece pequeña, pero evita errores muy caros: si se cuenta una fila como si fuera una persona, un cliente que compra tres veces se contará como tres clientes.

```mermaid
flowchart TD
    A[Pregunta: qué se quiere analizar] --> B[Definir qué representa una fila]
    B --> C[Elegir columnas necesarias]
    C --> D[Construir o leer la tabla]
    D --> E[Calcular sin confundir entidades]
```

Antes de cualquier análisis, completa siempre esta frase: “cada fila de este conjunto representa…”. Si no puedes completarla, no empieces a sumar ni a calcular promedios.

## Ejemplo IT

Una aplicación registra eventos. Una tabla puede tener una fila por clic, otra por sesión y otra por usuario. Son tablas distintas con granos distintos. Contar clics no responde cuántos usuarios usaron la aplicación; contar sesiones tampoco responde directamente cuántas personas pagaron.

## Error frecuente

Pensar que una tabla es “la realidad”. Una tabla es un modelo parcial. Puede no incluir compras hechas por teléfono, usuarios anónimos o devoluciones. Siempre pregunta qué no está en los datos.

## Comprobación

Para una academia online, escribe el grano de tres tablas posibles: una de alumnos, una de inscripciones y una de visualizaciones de vídeo. ¿Por qué no deben mezclarse sin una relación explícita?

# 01.2 Filas, columnas, tipos y relaciones

## Objetivos

Aprender a leer una tabla con precisión: distinguir filas y columnas, reconocer tipos básicos de datos y entender por qué una clave permite relacionar tablas sin duplicar significado.

## Filas y columnas no son solo una forma visual

Una **fila** contiene información de un caso. Una **columna** guarda el mismo tipo de atributo para muchos casos. En una tabla de compras, `importe` debería contener números; en una tabla de usuarios, `fecha_registro` debería contener fechas. El tipo de información determina qué operaciones tienen sentido.

No tiene sentido calcular la media de `ciudad`; sí puede tener sentido contar cuántos usuarios hay por ciudad. No tiene sentido ordenar alfabéticamente un importe para encontrar la venta mayor; sí tiene sentido convertirlo a número y compararlo.

```mermaid
flowchart LR
    A[Fila: una compra] --> B[fecha]
    A --> C[producto]
    A --> D[importe]
    A --> E[cliente_id]
    E --> F[Relación con tabla de clientes]
```

## Tipos que encontrarás al empezar

- **Texto:** nombre de producto, ciudad, comentario.
- **Número:** importe, cantidad, edad, latencia.
- **Fecha y hora:** momento de registro, compra o despliegue.
- **Booleano:** verdadero/falso; por ejemplo, `es_cliente`.
- **Categoría:** conjunto limitado de etiquetas, como plan `gratis`, `pro` o `empresa`.

Un número puede representar cosas distintas: un identificador `cliente_id=1042` parece número, pero no debes calcular su media. Es una etiqueta técnica, no una cantidad.

## Claves y relaciones

Una **clave** es una columna que permite identificar o conectar información. Si `cliente_id` identifica de forma única a cada cliente, se llama clave primaria de la tabla de clientes. La misma columna puede aparecer en la tabla de compras para indicar quién realizó cada compra; allí actúa como clave foránea o referencia.

```mermaid
flowchart LR
    A[CLIENTES: cliente_id, nombre, ciudad] -->|un cliente realiza muchas compras| B[COMPRAS: compra_id, cliente_id, importe, fecha]
```

La relación dice: un cliente puede realizar muchas compras; una compra pertenece a un cliente. Esta información es esencial al combinar tablas. Si una tabla de clientes tiene accidentalmente dos filas para el mismo `cliente_id`, una unión puede duplicar importes sin que el error sea evidente.

## Error frecuente

Confundir un identificador con una medida. `pedido_id` y `cliente_id` sirven para identificar; no para hacer promedios. También es un error asumir que una columna “única” realmente lo es sin comprobar duplicados y nulos.

## Comprobación

Diseña las columnas mínimas de una tabla de tickets de soporte. ¿Qué representa cada fila? ¿Qué columna conectaría un ticket con un cliente? ¿Cuál parece numérica pero no debe tratarse como medida?

# 01.3 CSV, JSON, Excel, Parquet y bases de datos

## Objetivos

Saber qué problema resuelve cada formato básico y elegir una forma razonable de guardar o recibir información sin memorizar una lista de siglas.

## CSV: una tabla escrita como texto

Un archivo **CSV** significa *Comma-Separated Values*: valores separados por comas. Es un archivo de texto que representa una tabla. La primera línea suele contener los nombres de las columnas; cada línea posterior es una fila.

```text
fecha,producto,importe
2026-01-03,teclado,45.99
2026-01-04,ratón,19.90
```

CSV es sencillo de abrir, compartir y leer con Python, Excel o un editor de texto. Su simplicidad también tiene límites: no guarda bien tipos complejos, fórmulas, varias hojas ni una estructura dentro de otra. Además, hay que acordar separador, codificación, formato de fecha y separador decimal.

## JSON: una ficha que puede contener otras fichas

**JSON** significa *JavaScript Object Notation*. Es texto estructurado mediante pares `campo: valor`. A diferencia de un CSV, puede guardar objetos dentro de objetos y listas. Es frecuente en APIs, configuraciones y eventos de aplicaciones.

```json
{
  "pedido_id": 1001,
  "cliente": {
    "nombre": "Leo",
    "ciudad": "Madrid"
  },
  "productos": ["teclado", "ratón"],
  "importe": 65.89
}
```

El JSON anterior es una ficha de pedido. No es una tabla, aunque se pueda transformar en una. Para analizar muchos pedidos, normalmente tendrás que decidir qué campos extraer y cómo convertir listas u objetos anidados en columnas o tablas relacionadas.

```mermaid
flowchart LR
    A[Archivo CSV] --> B[Tabla plana: filas y columnas]
    C[Archivo JSON] --> D[Ficha con objetos y listas]
    B --> E[Python, Excel o SQL]
    D --> F[Leer y normalizar antes de analizar]
```

## Excel, Parquet y bases de datos

**Excel** es una aplicación y un formato de libro de trabajo; es útil para revisión manual, cálculos ligeros y comunicación. No es ideal como fuente única de procesos repetibles si múltiples personas lo editan sin control.

**Parquet** es un formato optimizado para datos tabulares grandes. Guarda columnas de forma eficiente y conserva tipos mejor que CSV. Normalmente lo usarás mediante Python, Spark, DuckDB o un warehouse, no editándolo a mano.

Una **base de datos** organiza información para que aplicaciones y personas puedan consultarla con reglas de acceso, relaciones y actualizaciones. SQL es un lenguaje para consultar muchas bases relacionales; MongoDB almacena documentos similares a JSON; DynamoDB se diseña alrededor de claves y patrones de acceso.

## Cómo elegir sin obsesionarte

Empieza preguntando: ¿necesito una tabla simple que cualquiera pueda abrir? CSV. ¿Recibo una respuesta con estructuras anidadas de una API? JSON. ¿Trabajo con muchos datos tabulares repetidamente? Parquet o una base de datos. ¿Necesito revisar manualmente algo pequeño? Excel puede ser adecuado.

La elección no elimina el deber de conocer grano, calidad y significado.

## Comprobación

Explica a otra persona la diferencia entre CSV y JSON sin usar las palabras “plano” ni “anidado”. Después indica cuál esperarías recibir de una API meteorológica y por qué.

# 01.4 Calidad, ausencia, sesgo, privacidad y uso responsable

## Objetivos

Revisar un conjunto de datos antes de analizarlo, interpretar ausencias sin borrarlas por costumbre y reconocer que una decisión basada en datos también puede causar daño.

## Calidad como condición de confianza

La calidad no significa que un dataset sea perfecto. Significa que conocemos si es adecuado para una decisión concreta. Una tabla de compras puede ser suficiente para estimar ingresos diarios y no serlo para saber satisfacción de clientes.

```mermaid
flowchart TD
    A[Pregunta de negocio] --> B[Datos disponibles]
    B --> C[Comprobar grano y cobertura]
    C --> D[Validar valores y relaciones]
    D --> E[Investigar ausencias y sesgos]
    E --> F{¿Apto para esta decisión?}
    F -->|Sí, con límites| G[Analizar y comunicar]
    F -->|No| H[Corregir, obtener datos o cambiar pregunta]
```

Cinco controles iniciales son especialmente útiles:

- **Completitud:** ¿faltan valores necesarios para la pregunta?
- **Validez:** ¿los valores respetan reglas, unidades y formatos?
- **Consistencia:** ¿la misma idea está registrada de la misma forma?
- **Unicidad:** ¿existen duplicados indebidos?
- **Actualidad:** ¿el dato llega a tiempo para la decisión?

## Los nulos cuentan una historia

Un valor ausente no es automáticamente un error. Puede significar “no se aplica”, “no se midió”, “falló el sistema” o “la persona prefirió no responder”. Borrar todas las filas con nulos puede eliminar justo a la población con la que tienes un problema.

Por ejemplo, si el campo `ingresos` falta sobre todo en usuarios que abandonan un formulario, la ausencia es información sobre fricción. Antes de imputar o eliminar, mide dónde faltan datos, desde cuándo y en qué segmentos.

## Sesgo, privacidad y propósito

Un dataset puede representar peor a grupos que usan menos una aplicación, tienen conectividad limitada o no están incluidos en la fuente. Un modelo entrenado con esos datos puede amplificar esa desigualdad. El analista debe declarar cobertura, exclusiones y riesgos, no tratarlos como una nota al pie.

La privacidad comienza antes de abrir un archivo: recoge solo los datos necesarios, evita copiar identificadores personales en notebooks, limita acceso y define cuánto tiempo se conservan. Que un sistema permita acceder a una columna no significa que sea legítimo usarla para cualquier objetivo.

## Caso práctico

Una empresa quiere comparar uso por ciudad, pero el 30 % de usuarios no informa ciudad y ese porcentaje es mayor en móvil. Concluir que “móvil usa menos el producto en ciertas ciudades” sin estudiar la ausencia puede ser falso. Primero se investiga el formulario, la geolocalización, el consentimiento y los segmentos afectados.

## Comprobación

Elige una de las cinco dimensiones de calidad y describe: un error concreto, cómo lo detectarías, qué decisión podría dañar y cuál sería una respuesta prudente.

# Bloque 02 - Python desde cero

## Propósito

Aprender a leer, escribir y depurar programas pequeños antes de usar bibliotecas de análisis. El objetivo no es memorizar sintaxis: es expresar una regla de negocio de forma clara y verificable.

## Lecciones

1. [Ejecutar código, valores y variables](lecciones/01-entorno-valores-y-variables.md)
2. [Listas, diccionarios y datos sencillos](lecciones/02-colecciones-y-datos-sencillos.md)
3. [Decisiones y repeticiones](lecciones/03-condiciones-y-bucles.md)
4. [Funciones y alcance](lecciones/04-funciones-y-alcance.md)
5. [Errores y depuración](lecciones/05-errores-y-depuracion.md)
6. [Estilo y práctica guiada](lecciones/06-estilo-y-practica-gastos.md)

## Prerrequisitos

Haber leído los bloques 00 y 01. Basta con saber que un dato debe tener significado y que una regla analítica debe poder revisarse.

## Práctica

Abre el [notebook de gastos personales](../../notebooks/practicas/02-gastos-personales.ipynb) o [ejecútalo en Google Colab](https://colab.research.google.com/github/Ayhur/CursoAnalista/blob/main/notebooks/practicas/02-gastos-personales.ipynb). También puedes resolver [el ejercicio](../../ejercicios/temario-02/aplicacion/gastos-personales.md). Las [soluciones](../../soluciones/temario-02/gastos-personales.md) se consultan al terminar.

# Ejecutar código, valores y variables

## Objetivos y prerrequisitos

Aprenderás qué hace un programa, cómo ejecutar una celda de notebook y cómo guardar un resultado con un nombre. No necesitas experiencia previa.

## Código que transforma valores

Un programa es una lista de instrucciones que transforma información. En un análisis, esa información puede ser el importe de una compra, una fecha o una respuesta de usuario. Un **valor** es una pieza concreta de información: `1200`, `"web"` o `True` (verdadero).

En Google Colab, un notebook muestra una celda de código y su resultado. Ejecuta primero esto y cambia después un único valor:

```python
ventas = 1200
objetivo = 1500
cumplimiento = ventas / objetivo
print(cumplimiento)
```

Una **variable** es un nombre que referencia un valor. Aquí `cumplimiento` guarda el resultado `0.8`. El signo `=` no pregunta si dos cosas son iguales: asigna el valor de la derecha al nombre de la izquierda.

## Tipos: la forma del dato importa

Python distingue números enteros (`3`), decimales (`3.5`), texto (`"Madrid"`), booleanos (`True` o `False`) y ausencia representada por `None`. El tipo condiciona qué operaciones tienen sentido: sumar `3 + 5` es válido; sumar `"3" + "5"` une texto y produce `"35"`.

Esta secuencia responde a “¿por qué revisar el tipo antes de calcular?”

```mermaid
flowchart LR
  A[Valor recibido] --> B[Comprobar tipo]
  B --> C[Aplicar operación]
  C --> D[Revisar resultado]
```

El paso de comprobar evita, por ejemplo, tratar un importe escrito como texto como si fuera dinero calculable.

## Error habitual

`ventas = ventas + 100` parece una igualdad matemática imposible. En programación significa “toma el valor actual de ventas, súmale 100 y guarda el nuevo resultado bajo el mismo nombre”. Usarlo sin cuidado puede ocultar el valor original; cuando importe, conserva ambos nombres: `ventas_iniciales` y `ventas_actualizadas`.

## Resumen y comprobación

- Una celda ejecuta instrucciones y muestra un resultado.
- Una variable etiqueta un valor; no es una caja mágica independiente.
- El tipo determina qué cálculo es válido.

Prueba `type(ventas)` y `type("1200")`. Explica por qué se diferencian. Continúa con [colecciones](02-colecciones-y-datos-sencillos.md).

# Listas, diccionarios y datos sencillos

## Objetivos y prerrequisitos

Sabrás agrupar varios valores y representar una compra sencilla antes de conocer las tablas de Pandas. Requiere variables y tipos básicos.

## Cuando un valor no basta

Una lista guarda una secuencia ordenada. Por ejemplo, los importes de tres pedidos:

```python
importes = [12.50, 18.00, 7.20]
primer_importe = importes[0]
```

Los corchetes indican una **lista** y el índice empieza en cero: `importes[0]` es el primer elemento. Esto sorprende al principio, así que no intentes “corregirlo”: compruébalo imprimiendo el resultado.

Un **diccionario** asocia una clave con un valor. Es útil para una observación con campos nombrados:

```python
pedido = {"canal": "web", "importe": 42.50, "pagado": True}
print(pedido["importe"])
```

La clave evita depender de una posición. Una lista de diccionarios puede representar varias compras pequeñas; más adelante Pandas convertirá esa estructura en una tabla.

## Relación con datos reales

Una API —un mecanismo para que programas intercambien información— suele devolver listas y diccionarios similares. Eso no elimina la necesidad de validar: que un campo se llame `importe` no garantiza que sea numérico, completo o esté expresado en la misma moneda.

## Límite y práctica

`pedido["descuento"]` provoca un error si esa clave no existe. No inventes un cero sin preguntar qué significa que falte: podría significar “sin descuento”, “dato desconocido” o “campo no recogido”.

Resume con tus palabras la diferencia entre lista y diccionario y continúa con [condiciones y bucles](03-condiciones-y-bucles.md).

# Decisiones y repeticiones

## Objetivos y prerrequisitos

Aplicarás una regla distinta según un dato y repetirás una comprobación sobre varios pedidos. Requiere listas y diccionarios.

## Condiciones: expresar una regla

Una condición permite que el programa elija. `if` pregunta por una expresión que da `True` o `False`:

```python
importe = 120
if importe >= 100:
    categoria = "pedido alto"
else:
    categoria = "pedido habitual"
```

La sangría no es decoración: las líneas desplazadas pertenecen a la rama de la condición. La regla debe coincidir con una definición de negocio. Pregunta si exactamente 100 debe contarse como alto antes de decidir entre `>` y `>=`.

## Bucles: repetir sin copiar código

Un bucle `for` visita cada elemento de una colección. El siguiente acumula importes y muestra la idea de agregación que luego hará Pandas:

```python
total = 0
for importe in [12.5, 18.0, 7.2]:
    total = total + importe
print(total)
```

Este flujo responde a “¿qué ocurre para cada dato de entrada?”

```mermaid
flowchart LR
  A[Un importe] --> B[Comprobar regla]
  B --> C[Actualizar resultado]
  C --> D[Siguiente importe]
```

El programa repite el mismo criterio; no decide de forma inteligente qué regla usar. La calidad de la conclusión depende de que la regla y los datos sean apropiados.

## Error habitual

No modifiques una lista mientras la recorres salvo que entiendas las consecuencias: puedes saltarte elementos. Para aprender, crea una lista nueva para los resultados o revisa primero el tamaño y contenido de la original.

## Resumen

Las condiciones expresan criterios y los bucles los aplican repetidamente. Sigue con [funciones](04-funciones-y-alcance.md).

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

# Errores y depuración

## Objetivos y prerrequisitos

Sabrás leer el mensaje de error, formular una hipótesis mínima y comprobarla sin cambiar diez cosas a la vez. Requiere haber ejecutado código sencillo.

## Un error también es evidencia

Cuando Python no puede continuar, muestra un mensaje con una última línea relevante. `NameError` suele indicar que un nombre no existe; `TypeError`, que se intentó una operación incompatible; `KeyError`, que falta una clave del diccionario. El mensaje no sustituye la comprensión, pero delimita qué revisar.

Ejemplo:

```python
importe = "42.50"
importe + 10
```

El problema no es que Python “falle”: `importe` contiene texto, no un número. La corrección solo debe hacerse si la regla de origen confirma que ese texto representa un importe válido:

```python
importe_numerico = float(importe)
```

## Método de depuración

Este flujo responde a “¿cómo investigar sin adivinar?”

```mermaid
flowchart TB
  A[Leer última línea del error] --> B[Reducir a ejemplo pequeño]
  B --> C[Inspeccionar valor y tipo]
  C --> D[Formular una causa]
  D --> E[Aplicar un cambio y volver a ejecutar]
```

Reducir el ejemplo evita mezclar varios problemas. Usa `print(valor)` y `type(valor)` antes de cambiar código. Si la causa es un dato inesperado, no la tapes con una conversión automática: registra cuántos casos hay y decide qué significan.

## Error habitual: silenciar en lugar de entender

`try/except` permite manejar errores, pero capturarlos todos y continuar puede ocultar importes inválidos o pedidos perdidos. Úsalo para casos esperados y registra qué ocurrió. Un análisis correcto que descarta silenciosamente el 20 % de los datos no es fiable.

## Resumen

Depurar es un proceso de evidencia: leer, aislar, inspeccionar, probar. Continúa con [estilo y práctica](06-estilo-y-practica-gastos.md).

# Estilo y práctica guiada

## Objetivos y prerrequisitos

Aplicarás las piezas del bloque en un problema pequeño y aprenderás a escribir código que otra persona pueda leer. Requiere todas las lecciones anteriores.

## Legibilidad es una propiedad analítica

Un programa de análisis no se evalúa solo por “funciona hoy”. Debe dejar claro qué representa cada valor y qué regla se aplicó. Usa nombres como `gasto_por_categoria`, no `x`; evita repetir números mágicos como `100` sin explicar su significado; separa carga de datos, transformación y resultado.

Un ejemplo legible:

```python
LIMITE_REVISAR = 100

def categorias_sobre_limite(movimientos, limite):
    total_por_categoria = {}
    for movimiento in movimientos:
        categoria = movimiento["categoria"]
        importe = movimiento["importe"]
        total_por_categoria[categoria] = total_por_categoria.get(categoria, 0) + importe
    return [categoria for categoria, total in total_por_categoria.items() if total > limite]
```

Antes de reutilizarlo en una empresa, define cómo se tratan devoluciones, moneda, movimientos duplicados y valores ausentes. El código implementa una decisión; no decide por ti qué es correcto.

## Comprobaciones mínimas

Prueba casos normales y casos límite: lista vacía, importe exactamente 100, importe negativo y un texto donde debería haber número. Escribir esos ejemplos antes de confiar en el resultado es una forma simple de prueba.

## Ejercicio de cierre

Resuelve la [práctica de gastos](../../../ejercicios/temario-02/aplicacion/gastos-personales.md) y compara tu razonamiento con las [soluciones](../../../soluciones/temario-02/gastos-personales.md) solo al terminar. Si solo tienes móvil, escribe primero el pseudocódigo en texto: entradas, pasos y salidas.

## Puente al siguiente bloque

Python permite operar con estructuras pequeñas. En NumPy y Pandas aplicarás operaciones parecidas a miles de valores y tablas, pero conservarás las mismas preguntas: ¿qué representa cada dato?, ¿qué regla se aplica?, ¿cómo se comprueba?

# Bloque 03 - Matemáticas aplicadas al análisis

## Propósito y ruta adaptable

Conectar herramientas matemáticas con decisiones de negocio y análisis. Si manejas porcentajes, medias ponderadas, funciones y vectores, usa las explicaciones generales como repaso; las aplicaciones, los límites y la interpretación no son opcionales.

## Lecciones

1. [Magnitudes, porcentajes y tasas](lecciones/01-magnitudes-porcentajes-y-tasas.md)
2. [Promedios, ponderación y agregación](lecciones/02-promedios-ponderacion-y-agregacion.md)
3. [Funciones, vectores y matrices](lecciones/03-funciones-vectores-y-matrices.md)
4. [Tiempo, crecimiento y comparaciones](lecciones/04-tiempo-crecimiento-y-comparaciones.md)

## Resultado esperado

Podrás calcular y comunicar un cambio sin mezclar unidades, elegir una agregación defendible y cuestionar comparaciones aparentemente obvias.

# Magnitudes, porcentajes y tasas

## Objetivos y prerrequisitos

Sabrás separar cambio absoluto, cambio relativo y puntos porcentuales. La aritmética básica es suficiente; si ya dominas fórmulas, céntrate en los ejemplos y errores de interpretación.

## Una cifra necesita unidad y referencia

Pasar de 100 a 120 pedidos supone un cambio absoluto de 20 pedidos y un crecimiento relativo del 20 %: `(120 - 100) / 100`. Ambas cifras son correctas, pero responden preguntas distintas. El cambio absoluto ayuda a estimar capacidad; el relativo permite comparar grupos de tamaño distinto.

Una tasa relaciona cantidades: por ejemplo, 30 compras de 1 000 visitas son una tasa de conversión del 3 %. No digas “subió un 2 %” si pasó de 3 % a 5 %: aumentó **2 puntos porcentuales** y aproximadamente un 66,7 % relativo. Esa diferencia cambia la percepción de impacto.

Este recorrido responde a “¿qué debe declararse antes de comparar un número?”

```mermaid
flowchart LR
  A[Valor y unidad] --> B[Referencia]
  B --> C[Cambio absoluto]
  B --> D[Cambio relativo o tasa]
  C --> E[Interpretación]
  D --> E
```

La referencia puede ser ayer, el objetivo, otro segmento o el mismo mes del año anterior; elegirla es una decisión analítica, no una operación automática.

## Ejemplo y contraejemplo

Una app pasa de 10 a 20 conversiones: +10 conversiones y +100 %. Otra pasa de 10 000 a 10 100: +100 conversiones pero +1 %. Presentar solo porcentaje hace enorme el primer cambio; presentar solo conteo oculta que el segundo afecta a más clientes. Comunica ambos cuando importen.

Un descenso del 20 % después de un aumento del 20 % no vuelve al inicio: `100 × 1,2 × 0,8 = 96`. Los porcentajes se aplican a bases distintas.

## Resumen y práctica

- Declara unidad, población y referencia.
- Distingue porcentaje, tasa y punto porcentual.
- El tamaño de la base cambia la interpretación.

Calcula el cambio absoluto, relativo y en puntos porcentuales si una conversión pasa de 4 % a 5 %. Luego sigue con [ponderación](02-promedios-ponderacion-y-agregacion.md).

# Promedios, ponderación y agregación

## Objetivos y prerrequisitos

Aprenderás cuándo un promedio resume un conjunto y cuándo lo distorsiona. Requiere comprender porcentajes y tasas.

## Un promedio siempre combina observaciones

La media aritmética suma valores y divide por su número. Es útil para importes comparables, pero una media de tasas puede ser engañosa si cada grupo tiene un tamaño distinto. Si el país A convierte 8 de 10 visitas (80 %) y B convierte 1 000 de 10 000 (10 %), la media simple de 45 % no describe la conversión conjunta. La respuesta correcta suma éxitos y oportunidades: `1008 / 10010`, aproximadamente 10,1 %.

Eso es una **media ponderada**: cada tasa pesa según su denominador. No es un detalle de fórmula; evita tomar decisiones de inversión basadas en segmentos pequeños y extremos.

## Agregar cambia el grano

Antes de sumar o promediar, pregunta qué representa una fila. Si cada fila es un pedido, sumar importes da ingresos por pedido. Si cada fila es un usuario mensual, sumar ingresos puede duplicar clientes que compraron varias veces. El nivel al que se describe un dato se llama **grano** y se estudió en el bloque 01.

## Error habitual: promedio de promedios

Un dashboard muestra conversión diaria y calcula la media de siete porcentajes. Puede ser válido si cada día tiene el mismo tráfico; si no, conviene dividir compras totales entre visitas totales. Conserva numerador y denominador: permiten revisar y reponderar.

## Resumen

El promedio no es neutral: depende de qué observaciones se incluyan y cuánto pesa cada una. Continúa con [funciones, vectores y matrices](03-funciones-vectores-y-matrices.md).

# Funciones, vectores y matrices

## Objetivos y prerrequisitos

Comprenderás las ideas matemáticas que harán legibles NumPy y Pandas: una función transforma entradas; un vector reúne valores; una matriz organiza muchos vectores.

## Transformar entradas en salidas

Una **función** expresa una relación: dado número de clientes y precio, devuelve ingresos. `ingresos(clientes, precio) = clientes × precio`. No afirma que ambas variables sean independientes ni que subir precio no cambie clientes: solo define el cálculo bajo unos supuestos.

Un **vector** es una lista ordenada de valores de la misma clase, por ejemplo las ventas de tres días: `[120, 140, 110]`. Una **matriz** organiza muchas filas de valores: cada fila podría ser un día y cada columna pedidos, ingresos y devoluciones. En código, un array de NumPy permitirá aplicar un cálculo a todos los elementos sin escribir un bucle manual.

## Relación con el análisis

Los objetos matemáticos no sustituyen el significado. Dos columnas con mil números pueden formar una matriz, pero no por ello es razonable sumarlas si una contiene euros y otra minutos. La estructura permite calcular; el contexto decide si el cálculo responde una pregunta válida.

## Resumen y puente

Funciones hacen explícitas transformaciones; vectores y matrices permiten representar muchas observaciones. En el bloque 04 aprenderás a manejarlos eficientemente con NumPy.

# Tiempo, crecimiento y comparaciones

## Objetivos y prerrequisitos

Sabrás elegir una comparación temporal defendible y distinguir nivel, variación y crecimiento acumulado. Requiere porcentajes.

## El tiempo no siempre avanza de forma comparable

Comparar junio con mayo puede ser útil, pero una tienda de viajes puede tener una estacionalidad fuerte: junio suele diferir de mayo por razones repetidas cada año. Compara también con junio del año anterior y con una referencia acordada. La elección depende de la decisión: planificación anual, respuesta a una incidencia o seguimiento semanal.

El crecimiento compuesto encadena cambios: si una métrica crece 10 % dos meses, el factor es `1,1 × 1,1 = 1,21`, no 1,20. Para comunicarlo, muestra periodo inicial, final y fórmula, no una etiqueta vaga de “crecimiento”.

## Límite: una serie no demuestra causalidad

Que una métrica cambie tras una acción no identifica por sí mismo la causa. El tiempo puede coincidir con campañas, festivos, cambios de mercado o problemas de medición. Las comparaciones temporales son evidencia descriptiva que requiere contexto, segmentos y, cuando sea necesario, experimentos.

## Cierre del bloque

Las matemáticas aplicadas sirven para no confundir escalas, promedios ni referencias. Antes de automatizar con NumPy o Pandas, pregunta siempre: ¿qué mide este número, sobre qué población y frente a qué comparación?

Aplica el bloque en la [práctica de tasas y promedios](../../../ejercicios/temario-03/aplicacion/tasas-y-promedios.md) antes de leer su solución.

# Bloque 04 - NumPy y cálculo vectorizado

## Propósito

Usar arrays para representar datos numéricos y aplicar cálculos sobre colecciones completas. NumPy prepara el modelo mental de Pandas, pero no reemplaza la comprensión del significado de cada número.

## Lecciones

1. [Arrays y cálculo vectorizado](lecciones/01-arrays-y-vectorizacion.md)
2. [Selección, máscaras y forma](lecciones/02-seleccion-mascaras-y-forma.md)
3. [Broadcasting, simulación y reproducibilidad](lecciones/03-broadcasting-simulacion-y-reproducibilidad.md)

# Arrays y cálculo vectorizado

## Objetivos y prerrequisitos

Sabrás crear un array numérico y aplicar un cálculo a todos sus elementos. Requiere entender listas y vectores de los bloques 02 y 03.

## De una lista a un array

Un **array** es una estructura para valores organizados, normalmente del mismo tipo, que permite operaciones numéricas eficientes. En Python se importa NumPy con un alias convencional:

```python
import numpy as np
ventas = np.array([120, 140, 110])
ventas_con_iva = ventas * 1.21
```

La última línea no multiplica la lista como texto ni requiere un `for`: aplica la operación elemento a elemento. Eso se llama **vectorización**. Expresa “aplica la misma regla a cada venta”, una intención fácil de revisar.

Este flujo responde a “¿qué ocurre cuando la regla llega a una colección completa?”

```mermaid
flowchart LR
  A[Array de ventas] --> B[Regla vectorizada]
  B --> C[Array transformado]
  C --> D[Suma, media o filtro]
```

## Límite analítico

Que una operación sea rápida no la hace correcta. Multiplicar por 1,21 solo procede si todos los valores comparten moneda, representan importes sin IVA y la regla de negocio aplica a todos. Vectorizar una mala regla propaga el error más deprisa.

## Resumen

Un array reúne números; la vectorización aplica una operación a cada uno. En la siguiente lección seleccionarás subconjuntos sin perder de vista el criterio usado.

# Selección, máscaras y forma

## Objetivos y prerrequisitos

Aprenderás a elegir elementos por posición o condición y a interpretar la forma de un array. Requiere arrays básicos.

## Preguntar una condición a cada elemento

Una **máscara booleana** contiene `True` o `False` para cada posición. Es la traducción de una pregunta: “¿esta venta supera 100?”

```python
ventas = np.array([80, 125, 210])
es_alta = ventas > 100
ventas[es_alta]  # array([125, 210])
```

La máscara es valiosa porque hace visible el criterio. Antes de filtrar pedidos “altos”, define por qué 100 es el límite y revisa cuántos elementos quedan fuera.

La **forma** (`shape`) describe dimensiones. Un array de tres ventas tiene forma `(3,)`; una matriz de dos días y tres métricas puede tener `(2, 3)`. La forma no da significado a filas y columnas: debes documentarlo.

## Error habitual

Una máscara de longitud distinta al array no se puede aplicar correctamente. Más grave aún: una máscara correcta técnicamente puede estar desalineada conceptualmente si proviene de otro periodo o de clientes ordenados de forma distinta.

## Resumen

Seleccionar es formular un criterio. Comprueba siempre forma, orden y significado antes de combinar arrays.

# Broadcasting, simulación y reproducibilidad

## Objetivos y prerrequisitos

Comprenderás cómo NumPy combina dimensiones compatibles y por qué una simulación debe poder repetirse. Requiere forma y arrays.

## Broadcasting sin magia

**Broadcasting** es la regla por la que NumPy aplica un vector compatible a una matriz sin copiarlo manualmente. Si una matriz contiene ventas por día y canal, restar la media de cada canal puede centrar sus columnas. No memorices casos: imprime `shape` y comprueba qué dimensión representa cada valor antes de operar.

## Simular para explorar, no para fabricar evidencia

Puedes generar números aleatorios para practicar o evaluar un método. Una **semilla** fija el punto de partida del generador y permite repetir el mismo ejemplo:

```python
generador = np.random.default_rng(42)
muestra = generador.normal(loc=100, scale=15, size=5)
```

El 42 no hace la simulación más verdadera; hace el resultado reproducible. Una muestra simulada sirve para aprender o estudiar escenarios, no para afirmar qué hicieron clientes reales.

## Cierre y ejercicio

NumPy permite transformar, seleccionar y resumir números de forma concisa. Antes de Pandas, resuelve una práctica: crea ventas, aplica una máscara y explica qué supuesto contiene el umbral. Documenta semilla y forma. El mismo criterio se aplicará a tablas reales.

# Bloque 05 - Pandas: manipulación de datos

## Propósito

Preparar datos tabulares con trazabilidad. Pandas no “arregla” datos por sí solo: permite expresar y validar decisiones sobre ellos.

## Lecciones

1. [DataFrames, importación y perfilado](lecciones/01-dataframes-importacion-y-perfilado.md)
2. [Selección, tipos y limpieza](lecciones/02-seleccion-tipos-y-limpieza.md)
3. [Columnas derivadas y agregaciones](lecciones/03-transformacion-y-agregacion.md)
4. [Uniones y cardinalidad](lecciones/04-uniones-y-cardinalidad.md)
5. [Validación y trazabilidad](lecciones/05-validacion-y-trazabilidad.md)
6. [Caso integrado de pedidos](lecciones/06-caso-integrado-pedidos.md)

## Práctica

Resuelve [la limpieza de pedidos](../../ejercicios/temario-05/aplicacion/limpieza-pedidos.md) y después consulta [la solución razonada](../../soluciones/temario-05/limpieza-pedidos.md).

# DataFrames, importación y perfilado

## Objetivos y prerrequisitos

Sabrás abrir una tabla con Pandas e inspeccionarla antes de modificarla. Requiere los bloques de datos y Python.

Un **DataFrame** es una tabla en memoria: filas (observaciones) y columnas (variables) con nombres. Un archivo CSV puede guardar una tabla, pero abrirlo no garantiza que cada columna tenga el tipo ni el significado esperado.

```python
import pandas as pd
pedidos = pd.read_csv("pedidos.csv")
pedidos.head()
pedidos.info()
```

`head()` muestra ejemplos; `info()` enseña número de filas, columnas, tipos y valores no nulos. Compleméntalos con `describe()`, revisión de categorías y comprobación del grano: ¿una fila representa un pedido, una línea de pedido o un usuario?

Este flujo responde a “¿qué debe ocurrir antes de calcular?”

```mermaid
flowchart LR
 A[Importar] --> B[Ver ejemplos]
 B --> C[Comprobar grano y tipos]
 C --> D[Medir nulos y duplicados]
 D --> E[Decidir transformación]
```

Un error habitual es llamar “ventas” a una columna sin verificar moneda, impuestos o devoluciones. El perfilado abre preguntas; no las responde automáticamente.

Sigue con [selección, tipos y limpieza](02-seleccion-tipos-y-limpieza.md).

# Selección, tipos y limpieza

## Objetivos y prerrequisitos

Seleccionarás columnas y filas, convertirás tipos explícitamente y tratarás problemas sin borrar información a ciegas.

Seleccionar una columna responde una pregunta concreta: `pedidos["importe"]`. Filtrar filas aplica un criterio visible: `pedidos[pedidos["estado"] == "pagado"]`. Antes de filtrar, cuenta qué se excluye y por qué; “pagado” puede ser una definición distinta a “pedido creado”.

Los valores importados como texto requieren conversión controlada:

```python
pedidos["importe"] = pd.to_numeric(pedidos["importe"], errors="coerce")
pedidos["fecha"] = pd.to_datetime(pedidos["fecha"], errors="coerce")
```

`coerce` convierte valores inválidos en ausentes. Es útil porque no inventa una cifra, pero obliga a medir y decidir qué hacer con esos ausentes. No elimines nulos por costumbre: pueden concentrarse en un canal y sesgar el resultado.

## Resumen

Limpiar es convertir una regla de calidad en código verificable. Continúa con [transformación y agregación](03-transformacion-y-agregacion.md).

# Columnas derivadas y agregaciones

## Objetivos y prerrequisitos

Crearás medidas derivadas y resumirás una tabla sin perder de vista el grano.

Una columna derivada expresa una regla: `importe_neto = importe - descuento`. Documenta si el descuento ya incluye impuestos y qué sucede cuando falta. `groupby` agrupa filas y aplica una agregación:

```python
ventas_canal = pedidos.groupby("canal", as_index=False).agg(
    pedidos=("pedido_id", "nunique"),
    ingresos=("importe_neto", "sum")
)
```

`nunique` cuenta identificadores únicos; `count` cuenta valores no nulos. Elegir uno u otro cambia la métrica. Un promedio de importe también puede ocultar la distribución, por lo que conviene acompañarlo de volumen y percentiles cuando la decisión lo requiera.

## Límite

Agregar convierte muchas filas en pocas. Es útil para comparar canales, pero puede ocultar diferencias por país, dispositivo o periodo. Conserva la tabla de origen y registra cada agregación.

Sigue con [uniones y cardinalidad](04-uniones-y-cardinalidad.md).

# Uniones y cardinalidad

## Objetivos y prerrequisitos

Combinarás tablas comprobando qué clave conecta las filas y cuántas coincidencias son válidas.

Una unión (`merge`) cruza dos tablas mediante una **clave**, por ejemplo `cliente_id`. Antes de ejecutarla declara la cardinalidad: uno a uno, uno a muchos o muchos a uno. Muchos a muchos puede ser correcto, pero multiplica combinaciones y requiere una justificación explícita.

```python
pedidos_con_clientes = pedidos.merge(
    clientes, on="cliente_id", how="left", validate="many_to_one"
)
```

`validate="many_to_one"` convierte un supuesto en una comprobación: muchos pedidos pueden corresponder a un cliente, pero cada pedido no debe encontrar dos fichas de cliente. Tras unir, compara filas, claves sin coincidencia y totales monetarios.

## Error habitual

Ver una columna nueva y asumir que la unión funcionó. Si `clientes` tiene duplicados por error, cada pedido puede repetirse y los ingresos se inflan. La sintaxis válida no demuestra una relación válida.

Continúa con [validación y trazabilidad](05-validacion-y-trazabilidad.md).

# Validación y trazabilidad

## Objetivos y prerrequisitos

Definirás controles simples que convierten una transformación en un paso revisable.

Tras cada paso relevante guarda observaciones: número de filas, claves únicas, porcentaje de nulos y totales de negocio. Una validación puede ser una aserción:

```python
assert pedidos["pedido_id"].is_unique
assert pedidos["importe_neto"].notna().all()
```

No uses una aserción para ocultar un problema. Si falla, inspecciona los registros y decide si el supuesto era incorrecto o si hay un defecto de datos. Registra filtros, versión de la fuente y fecha de extracción: ese rastro permite reproducir el análisis.

## Resumen

Validar no es un último adorno; acompaña a cada transformación. Aplica ahora todo el ciclo en el [caso integrado](06-caso-integrado-pedidos.md).

# Caso integrado de pedidos

## Objetivos y prerrequisitos

Usarás el flujo completo para responder una pregunta simple: “¿qué canal aporta ingresos netos y cuántos pedidos válidos hay?”.

Primero formula el contrato: una fila es un pedido; solo se incluyen estados pagados; importe neto excluye descuento; el periodo es el mes analizado. Después perfila, convierte tipos, mide registros inválidos, crea la columna neta y agrupa por canal. Finalmente compara el total agrupado con el total de pedidos filtrados.

El resultado debe incluir una limitación: si hay pedidos devueltos después de la extracción, los ingresos no representan todavía margen final. Ese tipo de frase es parte del análisis, no una excusa.

Resuelve la [limpieza de pedidos](../../../ejercicios/temario-05/aplicacion/limpieza-pedidos.md) y revisa la solución razonada. El siguiente bloque explorará lo que estos resúmenes sugieren, sin convertirlos de inmediato en causalidad.

# Bloque 06 - Análisis exploratorio de datos

## Propósito

Explorar datos para descubrir patrones, anomalías y preguntas nuevas sin confundir exploración con demostración causal.

## Lecciones

1. [Preguntas y perfil exploratorio](lecciones/01-preguntas-y-perfil-exploratorio.md)
2. [Distribuciones, segmentos y valores extremos](lecciones/02-distribuciones-segmentos-y-outliers.md)
3. [Relaciones, correlación y explicaciones rivales](lecciones/03-relaciones-correlacion-y-causalidad.md)
4. [Registro de hallazgos y decisiones](lecciones/04-registro-de-hallazgos.md)

## Práctica

Resuelve [la investigación de una caída](../../ejercicios/temario-06/aplicacion/investigar-caida.md) antes de mirar [la guía de solución](../../soluciones/temario-06/investigar-caida.md).

# Preguntas y perfil exploratorio

## Objetivos y prerrequisitos

Convertirás un conjunto de datos en preguntas de exploración y comprobarás si la fuente puede responderlas. Requiere manejo básico de Pandas.

El análisis exploratorio, o **EDA**, es una investigación abierta pero disciplinada. No empieza con “haz todos los gráficos”; empieza con una pregunta como “¿en qué segmento se concentra la caída de pedidos?” y con un perfil de grano, periodo, cobertura, nulos y duplicados.

```mermaid
flowchart LR
 A[Pregunta] --> B[Perfil de fuente]
 B --> C[Comparar segmentos]
 C --> D[Hallazgo]
 D --> E[Comprobar plausibilidad]
 E --> F[Nueva pregunta o reporte]
```

El hallazgo genera una hipótesis, no un veredicto. Si faltan datos de dispositivo, no concluyas que no importa: concluye que la fuente no permite evaluarlo.

## Resumen

El EDA limita el espacio de dudas con evidencia visible. Sigue con [distribuciones y segmentos](02-distribuciones-segmentos-y-outliers.md).

# Distribuciones, segmentos y valores extremos

## Objetivos y prerrequisitos

Interpretarás cómo se reparte una medida y decidirás cuándo investigar valores extremos en vez de eliminarlos.

Una **distribución** muestra cómo se repiten los valores. Además de una media, observa mediana, dispersión, asimetría y percentiles. En importes de pedido, unos pocos pedidos empresariales pueden elevar la media aunque la mayoría de clientes gaste poco.

Segmentar divide observaciones por una característica relevante: canal, país, dispositivo o cohorte. Una tendencia global puede esconder un canal en caída y otro en crecimiento. El segmento se elige por una hipótesis de negocio, no porque haya columnas disponibles.

Un **outlier** es un valor inusual respecto al resto; no es sinónimo de error. Puede ser una compra fraudulenta, un cliente clave, una moneda mal parseada o una unidad distinta. Conserva la evidencia, clasifica la causa y documenta la regla si decides excluirlo.

## Resumen

Describe la distribución antes de resumirla y explica cualquier exclusión. Continúa con [relaciones y causalidad](03-relaciones-correlacion-y-causalidad.md).

# Relaciones, correlación y explicaciones rivales

## Objetivos y prerrequisitos

Distinguirás asociación observada, explicación posible y evidencia causal.

Dos medidas pueden moverse juntas. Una **correlación** resume asociación lineal, pero no identifica por qué ocurre. Las visitas y las ventas pueden subir por una campaña; el precio y las devoluciones pueden variar porque se venden productos distintos. Una tercera variable, un cambio de medición o puro azar pueden explicar la relación.

Antes de recomendar una acción, formula explicaciones rivales y busca qué dato las distinguiría. Un experimento o un diseño causal puede aportar mejor evidencia; el EDA prepara esa investigación.

## Error habitual

Ordenar una tabla por dos columnas y afirmar una causa porque el patrón “parece claro”. La visualización ayuda a detectar preguntas; no elimina confusión, sesgo de selección ni estacionalidad.

## Resumen

Una asociación es un punto de partida. Registra qué observaste y qué sería necesario para sostener una explicación.

# Registro de hallazgos y decisiones

## Objetivos y prerrequisitos

Aprenderás a convertir una exploración en un artefacto revisable por producto, ingeniería o dirección.

Para cada hallazgo anota pregunta, fuente y periodo, filtros, método, resultado, interpretación, límites y siguiente acción. Un ejemplo: “La conversión móvil cayó 1,8 puntos desde la versión 4.2; el patrón aparece en Android y no en web; falta comprobar cambios de tracking y errores del formulario”.

No escribas “la versión causó la caída” si solo existe coincidencia temporal. La precisión del lenguaje protege al equipo de decidir demasiado pronto.

Resuelve la [investigación de una caída](../../../ejercicios/temario-06/aplicacion/investigar-caida.md). En el bloque siguiente aprenderás a elegir gráficos que hagan visible esta evidencia sin manipular la percepción.

# Bloque 07 - Visualización y comunicación

## Propósito

Elegir y construir visualizaciones que permitan comprender una decisión con rapidez, sin distorsionar los datos.

## Lecciones

1. [De la pregunta al tipo de gráfico](lecciones/01-pregunta-y-tipo-de-grafico.md)
2. [Diseño honesto y accesible](lecciones/02-diseno-honesto-y-accesible.md)
3. [De exploración a comunicación](lecciones/03-exploracion-y-narrativa.md)
4. [Dashboards y entregables profesionales](lecciones/04-dashboards-y-entregables.md)

## Ejercicio

Haz el [diagnóstico de gráficos](../../ejercicios/temario-07/comprension/elegir-grafico.md) y comprueba [los criterios](../../soluciones/temario-07/elegir-grafico.md).

# De la pregunta al tipo de gráfico

## Objetivos y prerrequisitos

Sabrás escoger una representación según la comparación que una decisión necesita. Requiere EDA básico.

Un gráfico no es una decoración de una tabla: es una forma de hacer visible una comparación. Pregunta primero si necesitas mostrar evolución, diferencias entre categorías, distribución o relación entre dos medidas.

```mermaid
flowchart LR
 A[Pregunta] --> B{Comparación}
 B -->|Tiempo| C[Línea]
 B -->|Categorías| D[Barras]
 B -->|Distribución| E[Histograma o caja]
 B -->|Relación| F[Dispersión]
 C --> G[Hallazgo y acción]
 D --> G
 E --> G
 F --> G
```

Una línea responde bien a “¿cómo cambió semanalmente la conversión?”. Unas barras ordenadas responden mejor a “¿qué canal tiene más pedidos?”. Un histograma muestra si un promedio es representativo. Un gráfico de dispersión ayuda a explorar asociación, no a afirmar causalidad.

## Error habitual

Elegir un gráfico porque “queda profesional”. Un gráfico circular con muchas categorías impide comparar; una línea sobre categorías sin orden temporal inventa continuidad. El gráfico correcto depende de la pregunta y del tipo de dato.

## Resumen

Declara la pregunta antes del gráfico. Continúa con [diseño honesto](02-diseno-honesto-y-accesible.md).

# Diseño honesto y accesible

## Objetivos y prerrequisitos

Aprenderás a etiquetar, escalar y colorear un gráfico sin exagerar diferencias ni excluir a parte de la audiencia.

Un gráfico honesto declara unidad, periodo, población y fuente cuando son necesarios. En barras que comparan magnitudes, empezar el eje en cero evita que diferencias pequeñas parezcan enormes. En líneas puede usarse otro rango si se explica y se busca estudiar variación, no tamaño absoluto.

El color debe codificar una diferencia con significado: versión A frente a B, cumplimiento frente a riesgo. No hagas que el único mensaje dependa de rojo y verde; añade etiquetas, contraste y patrones si el gráfico se va a reutilizar.

## Límite

La claridad no significa ocultar incertidumbre: si un valor procede de pocos usuarios o una estimación, muestra contexto, intervalo o nota metodológica. Simplificar es retirar ruido, no retirar condiciones que cambiarían una decisión.

## Resumen

Cada elección visual transmite una interpretación. Verifica escalas, etiquetas y accesibilidad antes de presentar.

# De exploración a comunicación

## Objetivos y prerrequisitos

Separarás un gráfico para investigar de uno para recomendar una decisión.

Durante exploración puedes producir muchos gráficos, probar segmentos y descubrir errores. Un gráfico explicativo reduce esa exploración a una afirmación revisable: título con hallazgo, comparación destacada, definición de métrica y límite relevante.

Por ejemplo, “La conversión móvil cayó 1,8 puntos desde la versión 4.2” es más informativo que “Conversión por semana”. Acompáñalo de población, ventana temporal y una nota: “asociación temporal; pendiente validar cambio de tracking”.

## Error habitual

Convertir el dashboard exploratorio en una diapositiva ejecutiva con veinte series y filtros. El receptor no puede saber qué mirar ni qué acción se propone. Una buena narrativa deja clara evidencia, recomendación y grado de confianza.

## Práctica

Reformula el título de un gráfico que solo diga “Ventas mensuales” y explica qué dato necesitas para justificar el nuevo mensaje.

# Dashboards y entregables profesionales

## Objetivos y prerrequisitos

Diseñarás un entregable que responda a una decisión y no solo muestre indicadores.

Un **dashboard** reúne métricas para seguimiento continuo; no sustituye un análisis cuando hay una decisión nueva. Cada panel debe indicar definición, actualización, propietario y acción esperada. Una presentación o ticket de Jira puede ser mejor para explicar una incidencia concreta: contexto, evidencia, recomendación, riesgos y siguiente paso.

Antes de entregar pregunta: ¿quién actúa?, ¿qué cambiaría si el dato varía?, ¿qué limitación debe conocer? Si no hay respuesta, probablemente sobra un gráfico o falta una pregunta.

Completa el [diagnóstico de gráficos](../../../ejercicios/temario-07/comprension/elegir-grafico.md). El bloque siguiente añadirá la incertidumbre que una visualización por sí sola no puede resolver.

# Bloque 08 - Estadística para decisiones

## Propósito

Medir incertidumbre, evaluar diferencias y comunicar resultados sin convertir una prueba estadística en una respuesta automática.

## Lecciones

1. [Describir variabilidad](lecciones/01-describir-variabilidad.md)
2. [Población, muestra y sesgo](lecciones/02-poblacion-muestra-y-sesgo.md)
3. [Probabilidad e incertidumbre](lecciones/03-probabilidad-e-incertidumbre.md)
4. [Intervalos y pruebas de hipótesis](lecciones/04-intervalos-y-pruebas.md)
5. [Experimentos A/B](lecciones/05-experimentos-ab.md)
6. [Tamaño de efecto y decisión](lecciones/06-tamano-de-efecto-y-decision.md)

## Práctica

Analiza [un experimento de onboarding](../../ejercicios/temario-08/aplicacion/experimento-onboarding.md) y revisa [la interpretación](../../soluciones/temario-08/experimento-onboarding.md).

# Describir variabilidad

## Objetivos y prerrequisitos

Sabrás resumir un conjunto sin esconder su dispersión. Requiere promedios y distribuciones.

La media responde “¿cuál es el promedio?”, pero no “¿cuánto varían los casos?”. Mediana, percentiles, rango y desviación estándar describen perspectivas distintas. En tiempos de carga, una media de dos segundos puede convivir con usuarios que esperan veinte; los percentiles altos suelen importar para experiencia real.

No elijas la medida que haga mejor la historia. Declara por qué la métrica representa la decisión: media para coste total esperado, mediana para cliente típico, percentil 95 para un compromiso de rendimiento.

## Resumen

Centro y variabilidad se interpretan juntos. Continúa con [población y muestra](02-poblacion-muestra-y-sesgo.md).

# Población, muestra y sesgo

## Objetivos y prerrequisitos

Distinguirás el conjunto sobre el que quieres decidir de los datos que realmente observaste.

La **población** es el conjunto de interés, por ejemplo todos los nuevos usuarios elegibles. Una **muestra** es una parte observada. Un **estadístico** resume la muestra; un parámetro describe la población. Muestras diferentes producen resultados diferentes: esa variabilidad no es un fallo, es la razón para comunicar incertidumbre.

El problema no se arregla solo con más filas. Si solo respondieron usuarios muy activos a una encuesta, hay **sesgo de selección**: la muestra puede ser grande y seguir sin representar a la población.

## Resumen

Pregunta siempre quién quedó dentro, quién fuera y por qué. Sigue con [probabilidad e incertidumbre](03-probabilidad-e-incertidumbre.md).

# Probabilidad e incertidumbre

## Objetivos y prerrequisitos

Usarás probabilidad como modelo de incertidumbre, no como promesa sobre un caso individual.

Una probabilidad expresa qué tan frecuente sería un resultado dentro de un modelo y unas condiciones. Si una conversión histórica es 10 %, no significa que cada décimo usuario vaya a comprar ni que el siguiente tenga 10 % “garantizado”. Depende de población, periodo, medición y estabilidad del proceso.

La incertidumbre aparece porque observamos una parte del proceso, existe variación y las mediciones pueden tener error. Separar esos componentes evita comunicar una cifra estimada como si fuera exacta.

## Resumen

Un modelo probabilístico necesita supuestos explícitos. Sigue con [intervalos y pruebas](04-intervalos-y-pruebas.md).

# Intervalos y pruebas de hipótesis

## Objetivos y prerrequisitos

Interpretarás un intervalo y un p-valor sin atribuirles un significado que no tienen.

Un intervalo de confianza ofrece un rango de valores compatibles con un método, datos y nivel de confianza bajo sus supuestos. Una prueba compara datos con una **hipótesis nula**, por ejemplo “no hay diferencia de conversión”. Un p-valor pequeño indica que los datos serían poco compatibles con esa hipótesis si el modelo fuera correcto.

No dice la probabilidad de que la hipótesis nula sea cierta, no mide importancia de negocio y no corrige sesgo, medición mala ni pruebas repetidas. Comunica efecto absoluto, relativo, intervalo y decisión propuesta.

```mermaid
flowchart LR
 A[Población] --> B[Muestra]
 B --> C[Estimación]
 C --> D[Intervalo]
 C --> E[Prueba]
 D --> F[Decisión con límite]
 E --> F
```

## Resumen

La inferencia cuantifica incertidumbre; no sustituye juicio ni diseño. Continúa con [experimentos A/B](05-experimentos-ab.md).

# Experimentos A/B

## Objetivos y prerrequisitos

Diseñarás la estructura mínima de un experimento antes de mirar su resultado.

Un experimento A/B asigna unidades elegibles a variantes para comparar una métrica. Define antes población, unidad de asignación, métrica principal, guardrails, duración, tamaño necesario y criterio de decisión. Si aleatorizas por usuario pero mides por sesión sin cuidado, puedes contar varias veces una experiencia.

No mires cada día hasta encontrar significación: ese comportamiento eleva falsos positivos. También vigila calidad del tracking, exposición real a la variante y efectos por segmentos relevantes.

## Límite

Un experimento válido estima efecto en la población y periodo estudiados; no garantiza el mismo efecto después de lanzar globalmente ni en otro mercado.

## Práctica

Analiza el [experimento de onboarding](../../../ejercicios/temario-08/aplicacion/experimento-onboarding.md) antes de leer su solución.

# Tamaño de efecto y decisión

## Objetivos y prerrequisitos

Vincularás una diferencia estadística con coste, beneficio, riesgo y recomendación.

Una diferencia minúscula puede resultar “significativa” con millones de usuarios y aun así no pagar el coste de ingeniería. Una diferencia grande con pocos datos puede ser prometedora pero incierta. Por eso una decisión profesional reúne tamaño absoluto, cambio relativo, intervalo, volumen afectado, guardrails y reversibilidad de la acción.

Ejemplo: +0,2 puntos de conversión puede significar miles de pedidos si hay mucho tráfico, pero no conviene lanzar si aumenta reclamaciones o si el intervalo incluye una pérdida importante. La recomendación debe declarar el umbral que hace que actuar merezca la pena.

## Cierre

Estadística no concede permiso automático para afirmar o lanzar. Ayuda a calibrar qué se sabe, qué riesgo queda y qué evidencia faltaría.

# Bloque 09 - SQL, NoSQL y almacenamiento

## Propósito

Entender cómo viven los datos en una empresa, consultar tablas con SQL y saber cuándo un modelo documental o clave-valor exige otro diseño.

## Lecciones

1. [Modelo relacional, tablas y grano](lecciones/01-modelo-relacional-y-grano.md)
2. [Seleccionar, filtrar y resumir con SQL](lecciones/02-sql-seleccion-filtro-y-agregacion.md)
3. [JOIN y validación de cardinalidad](lecciones/03-joins-y-cardinalidad.md)
4. [CTE, ventanas, fechas y nulos](lecciones/04-sql-analitico-y-mantenible.md)
5. [MongoDB y documentos](lecciones/05-mongodb-y-documentos.md)
6. [DynamoDB y patrones de acceso](lecciones/06-dynamodb-y-patrones-de-acceso.md)
7. [Warehouse, lakehouse y consultas asistidas](lecciones/07-arquitectura-y-consultas-asistidas.md)

## Práctica

Resuelve [la consulta de conversión](../../ejercicios/temario-09/aplicacion/consulta-conversion.md) y compara con [la solución](../../soluciones/temario-09/consulta-conversion.md).

# Modelo relacional, tablas y grano

## Objetivos y prerrequisitos

Comprenderás una base de datos relacional como un conjunto de tablas conectadas, antes de escribir una consulta.

Una base de datos guarda información para que programas y personas puedan consultarla de forma consistente. En el modelo **relacional**, una tabla representa una entidad o hecho: `clientes`, `pedidos` o `eventos`. Una fila es una observación y una clave identifica o conecta filas.

La pregunta principal antes de SQL es el **grano**: ¿una fila de `pedidos` representa un pedido completo o una línea de producto? Sumar importes después de unir tablas sin responderla puede duplicar ingresos.

```mermaid
flowchart LR
 A[CLIENTES: un cliente] -->|cliente_id| B[PEDIDOS: un pedido]
 B -->|pedido_id| C[LINEAS: un producto pedido]
```

El diagrama muestra relaciones uno a muchos: un cliente puede tener pedidos y un pedido varias líneas. La clave no es una decoración: define qué combinaciones son válidas.

## Resumen

SQL opera sobre tablas, pero el análisis depende de grano y claves. Sigue con [selección, filtro y agregación](02-sql-seleccion-filtro-y-agregacion.md).

# Seleccionar, filtrar y resumir con SQL

## Objetivos y prerrequisitos

Escribirás una consulta legible que responda una pregunta concreta y comprobarás qué filas excluye.

SQL es un lenguaje declarativo: describes qué resultado quieres, no los pasos internos exactos. Para contar pedidos pagados por canal:

```sql
SELECT canal, COUNT(*) AS pedidos
FROM pedidos
WHERE estado = 'pagado'
GROUP BY canal
ORDER BY pedidos DESC;
```

`WHERE` filtra filas antes de agrupar; `GROUP BY` define el nivel del resultado. `COUNT(*)` cuenta filas, pero `COUNT(DISTINCT pedido_id)` cuenta pedidos únicos. Elegir uno es una definición de métrica, no una preferencia sintáctica.

## Error habitual

Filtrar un periodo con texto o sin zona horaria explícita puede incluir o excluir registros inesperados. Inspecciona datos de borde y declara la ventana temporal.

## Resumen

Una consulta profesional hace visibles medida, población y grano. Continúa con [JOIN y cardinalidad](03-joins-y-cardinalidad.md).

# JOIN y validación de cardinalidad

## Objetivos y prerrequisitos

Combinarás tablas sin multiplicar accidentalmente registros.

Un `JOIN` une filas por una clave. `INNER JOIN` conserva coincidencias; `LEFT JOIN` conserva todas las filas izquierdas y muestra ausencia de coincidencia. Antes de unir, declara cardinalidad: uno a uno, uno a muchos o muchos a muchos.

```sql
SELECT p.pedido_id, c.pais
FROM pedidos p
LEFT JOIN clientes c ON p.cliente_id = c.cliente_id;
```

Si `clientes` contiene dos filas para el mismo `cliente_id`, cada pedido aparecerá dos veces. Comprueba recuento antes y después, claves duplicadas y nulos introducidos por la unión. Un SQL que ejecuta no prueba que el resultado sea válido.

## Resumen

La cardinalidad es un supuesto analítico que debes validar. Sigue con [SQL analítico](04-sql-analitico-y-mantenible.md).

# CTE, ventanas, fechas y nulos

## Objetivos y prerrequisitos

Escribirás consultas por pasos y compararás una fila con su contexto sin destruir el detalle.

Una CTE (`WITH`) da nombre a un resultado intermedio y mejora la revisión. Las funciones de ventana calculan sobre un grupo sin reducirlo: `ROW_NUMBER()` ordena pedidos por cliente, `SUM(...) OVER (...)` construye acumulados y `LAG()` compara con el valor anterior.

Las fechas necesitan una zona y una granularidad; los nulos no equivalen automáticamente a cero. Usa `COALESCE` solo cuando la regla de negocio diga qué significa la ausencia.

## Resumen

La consulta mantenible separa pasos, documenta supuestos y conserva el detalle necesario para validar.

# MongoDB y documentos

## Objetivos y prerrequisitos

Entenderás qué problema resuelve un documento flexible y qué preguntas siguen siendo analíticas.

Un documento puede guardar información anidada de una entidad, por ejemplo un pedido con dirección y líneas. MongoDB almacena colecciones de documentos y permite filtros y pipelines de agregación. Esta flexibilidad ayuda cuando la forma de los datos cambia o una aplicación lee el agregado completo.

No significa “sin modelo”. Debes definir identificadores, campos opcionales, versiones y cómo se agregan importes. Documentos duplicados o esquemas inconsistentes complican análisis histórico y comparaciones.

## AI asistiendo consultas

Una herramienta que genera un filtro o pipeline desde lenguaje natural produce un borrador. Revisa colección, filtros, periodos, campos sensibles, coste e interpretación del resultado antes de ejecutarlo o compartirlo.

## Resumen

NoSQL cambia el modelo de almacenamiento; no elimina definición de métrica ni validación.

# DynamoDB y patrones de acceso

## Objetivos y prerrequisitos

Comprenderás por qué algunas bases clave-valor se diseñan empezando por las consultas que una aplicación necesita.

DynamoDB organiza registros alrededor de una clave de partición y, opcionalmente, una clave de ordenación. Está pensado para accesos predecibles a gran escala: “dame los pedidos de este cliente ordenados por fecha”, no para unir libremente cualquier tabla después.

Antes de modelar, enumera patrones de acceso, volumen, frecuencia y orden requerido. Diseñar solo por “entidades bonitas” puede producir consultas caras o imposibles. Para análisis amplio se suele extraer a un warehouse o lakehouse.

## Resumen

El modelo operativo optimiza accesos conocidos; el modelo analítico optimiza preguntas y historia.

# Warehouse, lakehouse y consultas asistidas

## Objetivos y prerrequisitos

Relacionarás fuentes operacionales con el entorno donde se preparan datos para análisis.

Un sistema operacional registra transacciones para que la aplicación funcione. Un **warehouse** organiza datos históricos y modelados para consulta analítica; un **lakehouse** combina almacenamiento flexible con capacidades analíticas. La arquitectura suele extraer, transformar y documentar datos antes de dashboards, SQL o Python.

```mermaid
flowchart LR
 A[Aplicación y fuentes] --> B[Extracción]
 B --> C[Warehouse o lakehouse]
 C --> D[Modelos y controles]
 D --> E[SQL, Python y BI]
```

La AI puede acelerar un borrador de consulta, pero no conoce por defecto el grano, la semántica, permisos o coste. Contrasta siempre resultado, plan de consulta y definición de métrica.

Resuelve la [consulta de conversión](../../../ejercicios/temario-09/aplicacion/consulta-conversion.md) antes de consultar la solución.

# Bloque 10 - Métricas, KPIs y analítica de producto

## Propósito del bloque

Este bloque enseña a construir un sistema de medición para un producto o negocio tecnológico. No se trata de aprender una lista de siglas ni de abrir un dashboard: se trata de decidir qué representa valor, cómo medirlo de forma consistente, qué señales deben activar una investigación y cómo evitar que una métrica optimizada localmente perjudique al producto.

## Resultado de salida

Al terminar podrás tomar una pregunta como “queremos crecer” y convertirla en un árbol de métricas con definiciones, instrumentación, guardrails, segmentos y una decisión asociada. También sabrás revisar un funnel, una cohorte o un dashboard de Amplitude sin aceptar sus cifras ciegamente.

## Prerrequisitos

- Bloque 00: preguntas y decisiones.
- Bloques 05–08: datos tabulares, exploración y estadística básica.
- Bloque 09: comprensión básica de fuentes y consultas.

## Lecciones

1. [Dato, medida, métrica, indicador y KPI](lecciones/01-lenguaje-de-medicion.md).
2. [Contrato de una métrica: definición que otra persona puede repetir](lecciones/02-contrato-de-metrica.md).
3. [Objetivos, North Star, árboles y guardrails](lecciones/03-arquitectura-de-metricas.md).
4. [Baselines, objetivos, benchmarks, ratios y comparaciones](lecciones/04-baselines-y-comparaciones.md).
5. [Funnels: definición, instrumentación y diagnóstico de conversión](lecciones/05-funnels.md).
6. [Cohortes, retención, churn y segmentación](lecciones/06-cohortes-retencion.md).
7. [Adquisición, engagement, monetización y métricas de valor](lecciones/07-metricas-de-valor.md).
8. [Experimentación, Goodhart y decisiones bajo incertidumbre](lecciones/08-experimentacion-y-goodhart.md).
9. [Catálogo de métricas, tracking plan y Amplitude](lecciones/09-gobierno-y-amplitude.md).

## Práctica

Cuando termines las tres primeras lecciones, realiza [el ejercicio de árbol de métricas](../../ejercicios/temario-10/aplicacion/arbol-metricas.md). No abras [la solución](../../soluciones/temario-10/arbol-metricas.md) hasta haber definido tus propios supuestos.

# 10.1 Dato, medida, métrica, indicador y KPI

## Objetivos

Al terminar esta lección podrás diferenciar los cinco términos que más se confunden en una conversación de negocio y detectar por qué una frase como “la métrica ha subido” puede ser inútil si no está definida.

## El problema no es contar; es representar una realidad

Una empresa tecnológica produce muchas huellas: eventos de aplicación, pedidos, tickets de soporte, pagos, campañas y cambios de código. Ninguno de esos registros, por sí solo, responde una pregunta de negocio. El trabajo del analista consiste en convertirlos en una representación explícita y limitada de una realidad: quién hizo qué, cuándo, bajo qué condiciones y por qué nos importa.

Un **dato** es un valor registrado: `usuario_id=42`, `evento="checkout_completed"`, `importe=39.90`. Una **medida** es una operación elemental sobre datos, como contar eventos o sumar importes. Una **métrica** añade una definición reutilizable y un propósito: por ejemplo, “usuarios activos semanales”, calculados como usuarios únicos que realizan una acción de valor entre lunes y domingo. Un **indicador** interpreta una métrica respecto a un contexto: “la activación está 2 puntos por debajo del objetivo”. Un **KPI** es el indicador elegido para gobernar una prioridad importante y al que se asigna responsabilidad y seguimiento.

```mermaid
flowchart TD
    A[Datos crudos: eventos, pedidos, tickets] --> B[Medida: conteo o suma]
    B --> C[Métrica: definición reproducible]
    C --> D[Indicador: valor frente a contexto]
    D --> E[KPI: señal prioritaria para decidir]
    E --> F[Acción, aprendizaje y revisión]
```

La flecha no significa que toda medida acabe siendo un KPI. La mayoría no debería serlo. Si una organización convierte cada número visible en un KPI, nadie sabe qué priorizar y se optimizan cifras irrelevantes.

## Ejemplo: “usuarios activos” no es una métrica hasta que la definas

Supón que tres equipos presentan el mismo dashboard. Producto llama activo a quien abre la aplicación; Marketing llama activo a quien recibe un correo; Finanzas llama activo a quien paga. Los tres pueden estar usando datos correctos y aun así discutir sobre cifras incompatibles. El problema no es una fórmula: es una definición incompleta.

Una definición mínima de “usuario activo semanal” podría ser: “usuario identificado que completa al menos una acción de valor entre las 00:00 del lunes y las 23:59 del domingo, en la zona horaria del producto; se excluyen empleados, cuentas de prueba y eventos enviados por sistemas automáticos”. Ahora se puede calcular, discutir y cambiar de forma controlada.

## La métrica no debe sustituir la pregunta

Una métrica es buena cuando ayuda a tomar una decisión. “Número de clics” rara vez es una decisión completa. “Porcentaje de usuarios nuevos que completa el primer proyecto en 7 días, segmentado por plataforma” puede orientar si hay que revisar onboarding, compatibilidad móvil o adquisición.

Antes de aceptar una métrica, plantea estas preguntas:

1. ¿Qué comportamiento o resultado pretende representar?
2. ¿Quién entra en la población y quién no?
3. ¿Qué evento o fuente se considera evidencia?
4. ¿Qué ventana temporal y zona horaria aplican?
5. ¿Qué decisión cambiaría si la métrica mejora o empeora?

Si la quinta pregunta no tiene respuesta, probablemente estás ante una cifra decorativa o exploratoria, no ante un KPI.

## Errores frecuentes

- Llamar KPI a todo lo que aparece en un dashboard.
- Confundir volumen con valor: más registros no implica más clientes satisfechos.
- Comparar métricas con definiciones o periodos distintos.
- Usar una media global cuando segmentos diferentes tienen comportamientos opuestos.
- Olvidar que un dato puede ser correcto técnicamente y engañoso para la decisión.

## Comprobación

Clasifica estas frases: “importe de una transacción”, “ingresos mensuales por cliente activo”, “la retención está por debajo del mínimo aceptable”, “retención a 30 días es un KPI del objetivo de sostenibilidad”. Después explica qué información falta en cada una para que sea reproducible.

# 10.2 Contrato de una métrica: una definición que otra persona puede repetir

## Objetivos

Aprender a especificar una métrica como un contrato: una pieza de documentación y lógica que permite que producto, datos, finanzas y dirección hablen del mismo número.

## Por qué una fórmula no basta

Escribir `conversion = compras / visitas` parece claro hasta que aparecen preguntas reales: ¿visitas de quién? ¿una visita por sesión, dispositivo o usuario? ¿la compra debe ocurrir el mismo día? ¿se cuentan devoluciones? ¿qué ocurre si el tracking se duplicó durante dos horas? La fórmula es solo una parte de la definición.

Un contrato de métrica elimina ambigüedad antes de que el dashboard llegue a una reunión. Debe ser breve, pero suficiente para que otra persona pueda reproducirla sin interpretar intenciones.

```mermaid
flowchart LR
    A[Pregunta de negocio] --> B[Contrato de métrica]
    B --> C[Eventos y fuentes]
    C --> D[SQL, modelo o dashboard]
    D --> E[Valor observado]
    E --> F[Decisión y responsable]
    F --> B
```

El último retorno importa: una definición no es eterna. Si cambia el producto, el comportamiento de valor o la fuente, se revisa el contrato y se documenta el cambio. No se sobrescribe silenciosamente la historia.

## Los siete campos mínimos

1. **Nombre y propósito.** “Activación a 7 días” y la decisión que pretende informar.
2. **Fórmula.** Numerador, denominador, unidades y tratamiento de cero.
3. **Población.** Quién es elegible, exclusiones y regla de identidad.
4. **Grano.** Usuario, cuenta, pedido, sesión, evento o día.
5. **Ventana temporal.** Inicio, fin, zona horaria y posible retraso de datos.
6. **Fuentes y lógica.** Eventos, tablas, filtros, versión de modelo y reglas de calidad.
7. **Propietario y límites.** Quién responde por la definición y qué no representa la métrica.

## Ejemplo completo: activación de una aplicación B2B

**Propósito:** saber si usuarios nuevos alcanzan el primer resultado de valor durante su primera semana y decidir qué paso de onboarding debe mejorarse.

**Fórmula:** usuarios únicos que crean un proyecto y ejecutan su primera consulta dentro de los siete días siguientes al registro / usuarios nuevos elegibles registrados en el mismo periodo. La métrica se expresa como porcentaje.

**Población:** usuarios humanos con cuenta verificada; se excluyen empleados, sandboxes internas, bots y migraciones masivas. El identificador estable es `account_user_id`.

**Grano y ventana:** cada usuario aporta una vez a su cohorte de registro. El día cero es el día de registro en UTC. Se esperan siete días completos antes de cerrar una cohorte.

**Fuente:** tabla de usuarios para registro, eventos `project_created` y `query_executed` para el criterio de valor. Validaciones: no más de un 1 % de eventos sin identificador y reconciliación diaria con logs de backend.

**Límites:** medir activación no demuestra retención ni satisfacción. Un usuario puede completar la acción por curiosidad y no volver; por eso se acompaña de retención y métricas de calidad.

## Versionado y cambios

Si el producto cambia y ahora una integración automática crea proyectos por el usuario, la definición anterior deja de medir la misma conducta. Mantener la misma etiqueta sin documentarlo rompe comparaciones históricas. Decide entre conservar la versión antigua, crear una v2 o recalcular el histórico si existe una regla equivalente. La elección debe quedar registrada.

## Comprobación

Escribe el contrato de “tasa de conversión de prueba a pago”. Incluye una exclusión razonable, una decisión que informaría y una limitación que impediría interpretarla como salud total del producto.

# 10.3 Objetivos, North Star, árboles y guardrails

## Objetivos

Relacionar la estrategia de un producto con métricas operables sin caer en la trampa de gestionar una organización con una única cifra.

## De estrategia a sistema de medida

Un objetivo formula una dirección: “hacer que equipos pequeños obtengan valor recurrente del producto”. Una North Star Metric intenta resumir la entrega de valor de ese objetivo. No sustituye a la estrategia ni resume todas las obligaciones de la empresa; sirve como punto de coordinación.

Una North Star útil debe estar relacionada con valor para el cliente, ser medible con suficiente calidad, responder a acciones de equipos y no ser tan fácil de manipular que incentive un comportamiento dañino. “Usuarios registrados” suele ser demasiado superficial; “cuentas que completan un flujo de valor semanal” suele estar más cerca de la experiencia real, aunque exige una definición cuidadosa.

```mermaid
flowchart TD
    A[Objetivo: valor recurrente] --> B[North Star: cuentas con valor semanal]
    B --> C[Activación]
    B --> D[Adopción de funciones]
    B --> E[Retención]
    B --> F[Monetización sostenible]
    C --> G[Guardrails: calidad, soporte, fraude]
    D --> G
    E --> G
    F --> G
```

El árbol no es una cadena causal demostrada automáticamente. Es una hipótesis de negocio: debe contrastarse con análisis, experiencia de producto y experimentos. Su valor está en obligar a explicitar cómo se espera que una acción local contribuya al resultado global.

## Métricas de entrada y de resultado

Las métricas de resultado miran el efecto final: ingresos, retención o valor entregado. Son importantes, pero tardan en cambiar. Las métricas de entrada representan comportamientos o condiciones que un equipo puede influir antes: completar onboarding, tiempo hasta primer valor, cobertura de documentación o tasa de errores.

No elijas una métrica de entrada porque sea fácil de mover. El vínculo con el resultado debe ser plausible y medible. Por ejemplo, aumentar notificaciones enviadas puede mejorar una métrica de actividad a corto plazo y empeorar retención por fatiga.

## Guardrails: progreso sin daño oculto

Un guardrail es una métrica que limita una optimización. Si el objetivo es elevar conversión, guardrails habituales son tasa de devoluciones, tickets de soporte, latencia, fraude, cancelación o satisfacción. No son métricas secundarias: definen qué tipo de éxito es aceptable.

El fenómeno de Goodhart resume el riesgo: cuando una medida se convierte en objetivo, las personas encuentran maneras de mejorarla sin mejorar lo que pretendía representar. Un equipo puede impulsar activación añadiendo un paso obligatorio que dispara el evento de valor, aunque el usuario no haya recibido valor alguno. El árbol de métricas y los guardrails ayudan a detectar esta distorsión.

## Ejemplo de decisión

Un equipo observa menor activación en móvil. Su árbol sugiere revisar el tiempo hasta primer proyecto y el abandono en el permiso de notificaciones. Antes de rediseñar, segmenta por versión, dispositivo y canal; comprueba instrumentación; estima el tamaño de la caída; y decide si necesita un experimento o una corrección técnica. El árbol orienta la investigación, no reemplaza el análisis.

## Comprobación

Para una plataforma de cursos, propone una North Star, tres entradas y dos guardrails. Después describe una forma de manipular la North Star sin generar aprendizaje real y cómo lo detectaría un guardrail.

# 10.4 Baselines, objetivos, benchmarks, ratios y comparaciones

## Objetivos

Evitar conclusiones engañosas al comparar una métrica con un periodo, una población o una referencia inadecuados.

## Un número aislado casi nunca informa

Decir “la conversión es 4 %” no permite decidir. ¿Es 4 % frente a un objetivo de 3 % o de 8 %? ¿Sube respecto a la semana anterior? ¿La semana anterior tenía una campaña, una caída de tracking o un festivo? Toda métrica necesita una referencia: baseline histórico, objetivo acordado, benchmark externo comparable o grupo de control.

```mermaid
flowchart TD
    A[Valor observado] --> B{Referencia válida}
    B --> C[Histórico comparable]
    B --> D[Objetivo acordado]
    B --> E[Control o experimento]
    B --> F[Benchmark comparable]
    C --> G[Interpretación]
    D --> G
    E --> G
    F --> G
```

Un benchmark externo puede orientar, pero rara vez es una meta automática: modelo de negocio, mercado, madurez, definición y población pueden diferir. Es más riguroso usarlo para plantear preguntas que para declarar éxito o fracaso.

## Absoluto, relativo y normalizado

Una caída de 200 conversiones puede ser enorme para un producto pequeño y trivial para otro. Por eso se combinan recuentos absolutos, tasas, cambios porcentuales y, cuando procede, normalización por población o exposición. La tasa de conversión necesita denominador; los ingresos por usuario necesitan periodo y población; la disponibilidad necesita duración observada.

Evita comparar porcentajes cuando los denominadores son minúsculos. Pasar de 1 a 2 compras es un aumento del 100 %, pero no justifica el mismo lenguaje que pasar de 10 000 a 20 000. Comunica ambos valores.

## Segmentos y paradojas

La media global puede mejorar mientras todos los segmentos relevantes empeoran, si cambió la composición de la población. Divide por canal, plataforma, cohorte, región o plan cuando exista una razón de negocio. Pero no busques segmentos hasta encontrar uno “significativo”: define previamente cuáles son plausibles y documenta exploraciones adicionales.

## Comprobación

Una conversión mensual sube del 3 % al 4 %. Escribe cinco datos que pedirías antes de celebrar la mejora y una manera de comunicarla sin exageración.

# 10.5 Funnels: definición, instrumentación y diagnóstico de conversión

## Objetivos

Construir un funnel que represente un recorrido real del usuario y diagnosticar pérdidas sin confundir eventos técnicos con progreso de valor.

## Qué mide un funnel

Un funnel compara cuántas entidades pasan por una secuencia de pasos definidos. La entidad puede ser usuario, cuenta, pedido o sesión; escogerla cambia la respuesta. Un funnel de onboarding por usuario y un funnel de checkout por pedido no son intercambiables.

```mermaid
flowchart LR
    A[Visita elegible] --> B[Registro completado]
    B --> C[Configuración inicial]
    C --> D[Primer valor]
    D --> E[Pago o retención]
```

Cada flecha es una hipótesis sobre un recorrido. Define orden, ventana máxima, repetición de eventos, exclusiones y tratamiento de usuarios que entran a mitad del proceso. Si una persona completa pasos en varios dispositivos, necesitas una regla de identidad antes de calcular.

## Pérdida no significa causa

Que el mayor abandono ocurra entre B y C no demuestra que el formulario sea el problema. Puede haber tráfico de baja intención, una incompatibilidad de navegador, un cambio de precio o un evento que no se está registrando. El funnel localiza dónde investigar; logs, sesiones, segmentación, cualitativo o experimentos ayudan a explicar por qué.

## Instrumentación mínima

Para cada paso documenta nombre, condición de éxito, propiedades, cuándo se envía el evento y qué sistemas pueden generarlo. Distingue “botón pulsado” de “acción completada en backend”. El primer evento mide intención; el segundo confirma resultado. Ambos pueden ser útiles, pero responden preguntas distintas.

## Ejemplo de diagnóstico

Si la conversión cae solo en Android tras una versión, compara el funnel por versión de app, modelo de dispositivo y error técnico. Si el evento de “registro completado” cae pero las cuentas existen en base de datos, el problema puede ser instrumentación. La investigación responsable informa de ambas posibilidades antes de atribuir culpa al producto.

## Comprobación

Define un funnel de compra de suscripción. Indica entidad, pasos, ventana y un evento técnico que no usarías como criterio final de conversión.

# 10.6 Cohortes, retención, churn y segmentación

## Objetivos

Interpretar cuándo una población vuelve, se mantiene o abandona, y evitar comparar cohortes que no son equivalentes.

## La cohorte da contexto temporal

Una cohorte agrupa entidades que comparten una condición de entrada: por ejemplo, usuarios registrados en la misma semana o cuentas que activaron una funcionalidad. La retención pregunta qué proporción vuelve a realizar una acción definida después de esa entrada. Sin cohorte, una media de usuarios activos mezcla generaciones de producto, campañas y antigüedad.

```mermaid
flowchart TD
    A[Cohorte: registro semana 1] --> B[Actividad semana 1]
    B --> C[Retención semana 2]
    C --> D[Retención semana 4]
    D --> E[Investigación por segmento]
```

Define con precisión evento de entrada, evento de retorno, intervalo y tipo de retención. La retención clásica exige volver en un periodo concreto; la no acotada permite volver en o después de cierto día. Ambas son válidas si se nombran correctamente.

## Churn no es simplemente “no activo”

Churn puede referirse a cancelación contractual, inactividad durante un umbral o pérdida de ingresos. Un SaaS anual y una app gratuita no usan la misma definición. Declara el horizonte y la población: una cuenta que aún no tuvo oportunidad razonable de renovar no debe entrar en una tasa de cancelación.

## Segmentación con propósito

Segmenta cuando exista una hipótesis operativa: canales que traen usuarios de distinto valor, planes con onboarding distinto, países con diferencias regulatorias o cuentas con distintos tamaños. No uses segmentos como excusa para ocultar la métrica global; combina ambos niveles y declara denominadores.

## Comprobación

Compara dos cohortes con retención día 30 del 20 % y 25 %. Enumera información necesaria antes de afirmar que la segunda experiencia de onboarding es mejor.

# 10.7 Adquisición, engagement, monetización y valor

## Objetivos

Relacionar métricas de distintas etapas del producto sin convertirlas en una colección desconectada de siglas.

## El recorrido económico y de valor

Adquisición responde quién llega; activación responde quién obtiene primer valor; engagement responde con qué frecuencia y profundidad se usa; retención responde quién vuelve; monetización responde qué valor económico sostiene el servicio. No existe una secuencia universal, pero dibujar la relación evita optimizar una etapa contra otra.

```mermaid
flowchart LR
    A[Adquisición] --> B[Activación]
    B --> C[Engagement]
    C --> D[Retención]
    D --> E[Monetización]
    E --> F[Capacidad de reinversión]
```

DAU, WAU y MAU son recuentos de actividad; el cociente DAU/MAU se usa a veces como aproximación a frecuencia, pero solo es interpretable con una definición de actividad estable. ARPU, CAC y LTV ayudan a hablar de economía unitaria, pero dependen de costes, horizontes y atribución. No los presentes como verdades universales.

La métrica de valor más útil no siempre es ingreso. En un producto B2B puede ser informes entregados; en una plataforma educativa, actividades significativas completadas; en una infraestructura, tareas ejecutadas con éxito. El valor debe conectar una necesidad del usuario con una viabilidad de negocio.

## Comprobación

Elige un producto y propone una métrica de valor, una de engagement, una de monetización y una advertencia sobre la relación entre ellas.

# 10.8 Experimentación, Goodhart y decisiones bajo incertidumbre

## Objetivos

Usar métricas para evaluar cambios sin convertir una mejora puntual en una certeza ni incentivar comportamientos que dañen el producto.

## Antes del experimento

Define hipótesis, población, métrica primaria, guardrails, duración y criterio de decisión antes de mirar los resultados. Si la métrica cambia después de conocer los datos, aumentas la probabilidad de encontrar una historia convincente pero falsa.

La estadística ayuda a medir incertidumbre; no decide por sí sola. Una diferencia puede ser compatible con ruido, demasiado pequeña para justificar coste o perjudicial en un segmento. Comunica magnitud absoluta, relativa, intervalo, tamaño de muestra, duración y límites.

```mermaid
flowchart TD
    A[Hipótesis] --> B[Métrica primaria y guardrails]
    B --> C[Diseño y asignación]
    C --> D[Recogida de datos]
    D --> E[Estimación e incertidumbre]
    E --> F{¿Valor neto aceptable?}
    F -->|Sí| G[Desplegar y monitorizar]
    F -->|No| H[Aprender o iterar]
```

## Goodhart en la práctica

Una medida se degrada cuando las personas optimizan el indicador en vez del fenómeno. Ejemplos: forzar clics para elevar engagement, retrasar una cancelación para reducir churn del mes, o dividir un ticket para mejorar tiempo de primera respuesta. Los guardrails, auditorías cualitativas y métricas complementarias no eliminan el riesgo, pero lo hacen visible.

## Comprobación

Propón un experimento para elevar activación. Incluye métrica primaria, dos guardrails, decisión de parada y una posible forma de Goodhart.

# 10.9 Catálogo de métricas, tracking plan y Amplitude

## Objetivos

Comprender que la confianza en un dashboard depende de un sistema de gobierno: definiciones, eventos, propiedad, cambios y calidad.

## Catálogo de métricas

Un catálogo es el lugar donde se encuentran nombre, propósito, definición, fórmula, fuentes, propietario, versiones, dashboards y consumidores de una métrica. Evita que cada equipo reconstruya “usuarios activos” desde cero y permite investigar diferencias de forma trazable.

## Tracking plan

Antes de instrumentar, documenta qué eventos representan interacciones importantes, qué propiedades permiten segmentar y cómo se identifica a usuario, cuenta o dispositivo. Define también eventos prohibidos: no envíes PII innecesaria a herramientas de analítica. El plan debe incluir validación de cobertura y un proceso de cambio cuando el producto evolucione.

```mermaid
flowchart LR
    A[Decisión y métrica] --> B[Tracking plan]
    B --> C[Implementación]
    C --> D[Validación de eventos]
    D --> E[Amplitude o BI]
    E --> F[Dashboard y acción]
    F --> G[Catálogo y versión]
```

## Amplitude como ejemplo, no como sustituto del criterio

Amplitude permite trabajar con eventos, propiedades, funnels, cohorts, retención y dashboards. Eso no le concede autoridad sobre la definición: una visualización correcta sobre eventos mal instrumentados sigue siendo engañosa. Valida primero identidad, latencia, duplicados, eventos de servidor frente a cliente y cambios de versión.

Una práctica sana consiste en revisar cada métrica con tres capas: definición de negocio, lógica técnica y comportamiento observado. Si las tres no coinciden, el trabajo no está terminado.

## Comprobación

Escribe tres eventos y dos propiedades para medir activación de un producto. Indica qué dato no recogerías por privacidad y cómo comprobarías que el evento llega correctamente.

# Bloque 11 - Series temporales

## Propósito

Analizar pedidos diarios de una aplicación, distinguir patrones temporales de cambios reales y construir previsiones útiles para planificar capacidad e inventario. El objetivo no es memorizar modelos: es definir, validar y comunicar una predicción que otra persona pueda cuestionar.

## Caso continuo: pedidos diarios de Lumen

Lumen es una aplicación de comercio local. Operaciones debe decidir cada lunes cuántos repartidores reservar para los 14 días siguientes. La métrica es `pedidos_completados_diarios`; cada observación es un día en la zona horaria de Madrid. El bloque parte de este caso y conserva su contrato, datos disponibles y riesgos a lo largo de todas las lecciones.

## Lecciones

1. [Contrato de previsión y calidad temporal](lecciones/01-indice-temporal-y-calidad.md)
2. [Tendencia, estacionalidad, calendario y rupturas](lecciones/02-componentes-de-una-serie.md)
3. [Lags, autocorrelación y ventanas móviles](lecciones/03-lags-y-previsiones-base.md)
4. [Baselines y un modelo sencillo](lecciones/04-validacion-temporal-y-comunicacion.md)
5. [Validación walk-forward y fuga de futuro](lecciones/05-validacion-walk-forward-y-fugas.md)
6. [Métricas de previsión y coste de error](lecciones/06-metricas-de-prevision.md)
7. [Intervalos de predicción y calibración](lecciones/07-intervalos-y-calibracion.md)
8. [Rupturas, monitorización y operación](lecciones/08-rupturas-y-monitorizacion.md)
9. [Laboratorio reproducible de demanda](lecciones/09-laboratorio-demanda.md)

## Práctica

Plantea [una previsión de demanda](../../ejercicios/temario-11/aplicacion/prevision-demanda.md), ejecuta el [laboratorio reproducible](../../notebooks/practicas/11-prevision-demanda.py) y compara con [la solución razonada](../../soluciones/temario-11/prevision-demanda.md).

# Contrato de previsión y calidad temporal

## Objetivos y prerrequisitos

Definirás qué se predice, cuándo se predice y qué datos son legítimos antes de mirar un gráfico o elegir un modelo.

Una **serie temporal** es una medida observada en momentos ordenados. En Lumen una fila representa un día; la variable objetivo es el número de `pedidos_completados`; la frecuencia es diaria; la zona es `Europe/Madrid`; el horizonte son los 14 días siguientes; y la fecha de corte es el domingo a las 23:59. Operaciones decide cuántos repartidores reservar el lunes usando solo información anterior al corte.

Esto responde a la pregunta “¿qué contrato evita que una previsión sea una cifra sin contexto?”

```mermaid
flowchart LR
 A[Contrato: pedidos diarios] --> B[Fecha de corte]
 B --> C[Información disponible]
 C --> D[Horizonte de 14 días]
 D --> E[Decisión de capacidad]
```

El diagrama es una secuencia de decisión: no se puede usar una campaña conocida el miércoles para predecir el lunes anterior. El contrato hace visible el momento en que el dato se vuelve utilizable.

Antes de modelar, construye un calendario completo. Un día sin fila puede significar cero pedidos, una caída del sistema de captura o una fuente incompleta; son tres hechos distintos. Comprueba duplicados, zona horaria, horas de cambio estacional, cobertura, agregación y cambios de definición. Si desde julio “pedido completado” excluye pedidos parcialmente reembolsados, no compares niveles sin documentar la ruptura.

Ejemplo mínimo: si el 6 de enero no aparece en el archivo, no rellenas automáticamente con cero. Primero contrastas el registro operacional; solo después decides si es un cero real, un ausente o un día que debe excluirse.

## Resumen

Una serie fiable empieza por un contrato, un calendario y una métrica estable. Continúa con [tendencia, estacionalidad y rupturas](02-componentes-de-una-serie.md).

# Tendencia, estacionalidad, calendario y rupturas

## Objetivos y prerrequisitos

Separarás patrones sostenidos, repeticiones de calendario, ruido y cambios estructurales antes de atribuir una causa.

Una serie puede contener **tendencia** (movimiento de largo plazo), **estacionalidad** (patrón que se repite por día, semana o año), ciclos, ruido y rupturas. En Lumen los viernes pueden superar a los martes; noviembre puede contener un pico de campañas; y un cierre de zonas de reparto puede producir un cambio de nivel. Una caída de lunes a domingo puede ser normal; una caída frente al mismo lunes de semanas comparables merece investigación.

```mermaid
flowchart TD
 A[Pedidos diarios] --> B[Tendencia]
 A --> C[Estacionalidad semanal y anual]
 A --> D[Calendario y festivos]
 A --> E[Ruido, anomalías y rupturas]
 B --> F[Modelo y baseline]
 C --> F
 D --> F
 E --> G[Investigación y anotación]
```

Los componentes son ramas paralelas: no ocurren uno después de otro. Una descomposición puede ser **aditiva** si los efectos se suman aproximadamente (por ejemplo, +20 pedidos cada viernes) o **multiplicativa** si la amplitud crece con el nivel (por ejemplo, un 20 % más). Una transformación logarítmica puede ayudar en el segundo caso, pero no es una obligación ni admite ceros sin tratamiento explícito.

Descomponer no prueba causas. Un cambio de nivel puede coincidir con una campaña, una incidencia, un festivo, falta de stock o error de medición. Cruza eventos y segmentos antes de explicarlo; registra la ruptura para no entrenar un modelo que la interprete como estacionalidad permanente.

## Resumen

Compara contra referencias temporales adecuadas, no solo contra el periodo anterior. Sigue con [lags, autocorrelación y ventanas móviles](03-lags-y-previsiones-base.md).

# Lags, autocorrelación y ventanas móviles

## Objetivos y prerrequisitos

Usarás valores pasados para describir dependencia temporal sin introducir información futura.

Un **lag** es un valor retrasado: `pedidos_t-1` es ayer y `pedidos_t-7` es el mismo día de la semana anterior. La **autocorrelación** resume cuánto se parece la serie a sí misma tras uno o varios retrasos. Una ACF alta en el lag 7 sugiere patrón semanal, no causalidad ni permiso para copiar siete días sin evaluar.

Una media móvil de 7 días suaviza ruido al promediar solo observaciones anteriores. Para predecir el 10 de marzo, su ventana puede usar del 3 al 9, nunca del 11 al 16. La regla evita una fuga de futuro muy común cuando se calculan ventanas sobre toda la tabla.

Ejemplo: si Lumen tuvo 102 pedidos ayer, 118 hace una semana y una media móvil de 110, esos tres números pueden alimentar modelos distintos. Cada variable contiene una hipótesis: continuidad inmediata, patrón semanal o nivel suavizado.

El horizonte importa: prever mañana y prever seis meses son problemas distintos. Declara qué información estaba disponible en el momento de hacer cada previsión; usar datos futuros por accidente produce resultados irreales. En la siguiente lección convertirás estas referencias en baselines comparables.

## Resumen

Lags y ventanas describen dependencia; no prueban que una acción cause pedidos. Sigue con [baselines y un modelo sencillo](04-validacion-temporal-y-comunicacion.md).

# Baselines y un modelo sencillo

## Objetivos y prerrequisitos

Compararás referencias honestas antes de elegir un modelo más elaborado.

Un baseline responde “¿qué lograríamos sin sofisticación?”. Para Lumen compara: naïve (repetir ayer), seasonal naïve (repetir el mismo día de la semana anterior) y media móvil de siete días. Son modelos explícitos, reproducibles y difíciles de superar cuando hay fuerte patrón semanal.

Como modelo sencillo adicional, una regresión con tendencia y variables de día de semana puede estimar nivel y estacionalidad. No es automáticamente mejor: solo se conserva si mejora de forma estable al baseline y su coste/interpretación compensa. Métodos como ETS, ARIMA o modelos de aprendizaje automático se estudian después de dominar esta comparación.

Ejemplo: si la media móvil gana en semanas tranquilas pero pierde sistemáticamente los viernes, la referencia estacional puede ser preferible. No elijas por una única semana ni por una gráfica atractiva.

El siguiente paso es evaluar respetando la flecha del tiempo. Continúa con [validación walk-forward y fuga de futuro](05-validacion-walk-forward-y-fugas.md).

Plantea la [previsión de demanda](../../../ejercicios/temario-11/aplicacion/prevision-demanda.md). En modelos posteriores aprenderás predicción supervisada, pero conservarás esta regla: validación coherente con el momento de decisión.

# Validación walk-forward y fuga de futuro

## Objetivos y prerrequisitos

Validarás una previsión como se usaría en producción: entrenar con pasado y comprobar contra futuro todavía desconocido.

Una partición temporal no se baraja. En Lumen puedes entrenar hasta septiembre, validar octubre-noviembre, ajustar una única vez y reservar diciembre como prueba final. Para conocer estabilidad, el enfoque **walk-forward** avanza sucesivos cortes: se predice la semana siguiente, se compara con lo observado y se avanza.

```mermaid
flowchart LR
 A[Pasado: entrenamiento] --> B[Validación futura 1]
 B --> C[Validación futura 2]
 C --> D[Prueba final intacta]
```

Cada bloque está en orden temporal. La prueba final no decide parámetros ni umbrales; estima cómo habría rendido el proceso al desplegarlo.

Una **fuga de información** ocurre si una variable usa el futuro: una media móvil centrada, normalizar usando todos los meses o incluir un precio que se fijó después de la fecha de corte. Un resultado excepcionalmente bueno merece investigar fuga antes de celebrarlo.

## Resumen y práctica

La validación simula el momento de decisión. Sigue con [métricas de previsión](06-metricas-de-prevision.md).

# Métricas de previsión y coste de error

## Objetivos y prerrequisitos

Elegirás cómo medir un error de previsión según la decisión, la escala y el coste de equivocarse.

El error de un día es `real - predicción`. **MAE** promedia su valor absoluto y se interpreta en la unidad del negocio: “nos equivocamos 12 pedidos al día”. **RMSE** eleva errores al cuadrado antes de promediar y penaliza más fallos grandes; puede convenir si quedarse muy corto de capacidad es especialmente grave.

Las métricas porcentuales requieren cuidado. **MAPE** divide por el valor real: no está definido con ceros y sobrerreacciona ante valores pequeños. **sMAPE** reduce algunos problemas, pero también tiene comportamiento difícil cerca de cero. **MASE** escala el error frente a una previsión naïve y permite comparar series de distinto tamaño, siempre que el baseline sea válido.

Ejemplo: predecir 10 pedidos cuando hubo 0 hace que MAPE falle; MAE sigue diciendo 10 pedidos de error. Si reservar repartidores extra cuesta poco pero faltar capacidad cuesta mucho, una métrica media no basta: comunica también errores por debajo de la demanda y el coste operativo asociado.

## Resumen

No existe “la métrica ganadora” fuera de una decisión. Evalúa varias y explica por qué una domina el criterio de lanzamiento. Continúa con [intervalos y calibración](07-intervalos-y-calibracion.md).

# Intervalos de predicción y calibración

## Objetivos y prerrequisitos

Comunicarás incertidumbre de una previsión y comprobarás si el rango prometido se cumple con la frecuencia esperada.

Una previsión puntual de 120 pedidos no expresa todo lo que sabemos. Un **intervalo de predicción** podría comunicar “entre 95 y 145 pedidos con cobertura nominal del 80 %”, bajo el método y supuestos usados. Debe referirse a observaciones futuras, no solo a incertidumbre sobre una media histórica.

La **calibración** pregunta si los intervalos son honestos: de cien días con intervalos al 80 %, aproximadamente ochenta deberían contener el valor real a largo plazo. Cobertura baja indica rangos demasiado estrechos; cobertura muy alta puede indicar rangos inútilmente amplios. Revisa también si el fallo se concentra en viernes, festivos o campañas.

Para Lumen, operaciones puede planificar tres escenarios: bajo, central y alto. La decisión no es “creer” el número central, sino elegir capacidad compatible con el coste de sobre- y sub-reservar.

## Límite

Un intervalo no protege frente a un evento fuera de la historia, como cierre de una ciudad o campaña inédita. Es un rango condicionado a datos y supuestos, no una garantía.

## Resumen

Una previsión útil incluye incertidumbre verificable. Sigue con [rupturas y monitorización](08-rupturas-y-monitorizacion.md).

# Rupturas, monitorización y operación

## Objetivos y prerrequisitos

Identificarás cambios que pueden invalidar patrones históricos y diseñarás una respuesta operativa ante errores de previsión.

Una **ruptura estructural** es un cambio por el que la relación aprendida deja de ser estable: cambio de precio, falta de stock, expansión de zonas, campaña, nueva versión de producto o cambio de tracking. No se corrige borrando el punto “raro”; se registra el evento, se evalúa el impacto y se decide si el modelo necesita reentrenamiento o una regla temporal.

Monitoriza error por horizonte, cobertura de intervalos, datos ausentes, frescura y sesgo por día de semana. Una alerta debe indicar umbral, dueño y acción: “si el MAE de siete días supera 20 pedidos dos semanas, revisar calendario, stock y extracción”. Alertar sin responsable crea ruido, no control.

## Resumen

Prever es un proceso operativo: datos, modelo, error, aprendizaje y ajuste. Continúa con el [laboratorio reproducible](09-laboratorio-demanda.md).

# Laboratorio reproducible de demanda

## Objetivos y prerrequisitos

Aplicarás el contrato temporal, tres baselines, validación ordenada y métricas de error sobre el caso de Lumen.

El script [11-prevision-demanda.py](../../../notebooks/practicas/11-prevision-demanda.py) genera de forma determinista 90 días de pedidos diarios con patrón semanal y una ruptura documentada. Divide pasado y futuro, compara naïve, seasonal naïve y media móvil, y calcula MAE, RMSE, MAPE, sMAPE y MASE.

No trates la salida como una respuesta universal: inspecciona qué baseline gana y explica por qué. Cambia la fecha de corte o la ruptura para observar que una métrica global puede ocultar días críticos. Escribe en tu entrega qué información estaría disponible realmente antes de predecir.

## Entregable

Resuelve la [práctica de demanda](../../../ejercicios/temario-11/aplicacion/prevision-demanda.md), conserva los resultados esperados y contrasta tu razonamiento con la [solución](../../../soluciones/temario-11/prevision-demanda.md).

# Bloque 12 - Modelos predictivos para analistas

## Propósito

Usar modelos predictivos para estimar resultados, priorizar casos y apoyar decisiones. El objetivo no es maximizar una métrica aislada: es construir una predicción útil, válida y explicable.

## Lecciones

1. [Decidir si la predicción aporta valor](lecciones/01-caso-de-uso-y-objetivo.md)
2. [Datos, variables y fuga de información](lecciones/02-preparacion-y-fuga.md)
3. [Baselines y familias de modelos](lecciones/03-baselines-y-modelos.md)
4. [Evaluación y coste de errores](lecciones/04-evaluacion-y-coste-de-error.md)
5. [Interpretación, sesgo y uso responsable](lecciones/05-interpretacion-sesgo-y-uso-responsable.md)

## Práctica

Resuelve [el caso de churn](../../ejercicios/temario-12/aplicacion/priorizar-churn.md).

# Decidir si la predicción aporta valor

## Objetivos y prerrequisitos

Separarás una pregunta predictiva de una causal y definirás la decisión que una predicción puede mejorar.

Un modelo predictivo usa patrones históricos para estimar un resultado desconocido: probabilidad de abandono, demanda de mañana o importe esperado. Antes de modelar define quién recibirá la predicción, qué acción puede tomar y cuál es el coste de equivocarse.

Predecir riesgo de churn no demuestra por qué alguien abandonará ni qué oferta lo retendrá. Sirve para priorizar contacto; la eficacia de la intervención exige experimento o evidencia causal aparte.

```mermaid
flowchart LR
 A[Decisión] --> B[Objetivo medible]
 B --> C[Datos históricos]
 C --> D[Baseline y modelo]
 D --> E[Evaluación]
 E --> F[Acción y seguimiento]
```

## Resumen

Sin decisión y acción, una predicción puede ser interesante pero no valiosa. Sigue con [datos y fuga](02-preparacion-y-fuga.md).

# Datos, variables y fuga de información

## Objetivos y prerrequisitos

Definirás objetivo, momento de predicción y variables que estarían disponibles entonces.

La **variable objetivo** es lo que se quiere estimar; las variables de entrada describen información disponible antes del resultado. Una **fuga de información** ocurre cuando el modelo usa un dato que solo existe después: una cancelación registrada tras el momento en que querías predecir churn.

Separa entrenamiento, validación y prueba respetando tiempo cuando corresponda. Ajustar transformaciones solo con entrenamiento evita que información del futuro mejore artificialmente la evaluación.

## Error habitual

Crear una variable con “número de tickets resueltos” para predecir una baja cuando esos tickets se abren precisamente al iniciar la baja. Un resultado excelente puede ser señal de fuga, no de inteligencia.

## Resumen

La pregunta correcta es: “¿qué sabíamos en el instante de decidir?”.

# Baselines y familias de modelos

## Objetivos y prerrequisitos

Compararás un modelo con una referencia sencilla antes de usar complejidad adicional.

Un **baseline** puede ser predecir la media, repetir el último valor o clasificar siempre la clase mayoritaria. Si un modelo no lo supera de forma útil, no merece operación ni explicación adicional.

Regresión lineal estima una cantidad; regresión logística estima probabilidad de una clase; árboles capturan divisiones y relaciones no lineales. Ninguna familia es “mejor” sin contexto: más flexibilidad puede sobreajustar y reducir interpretabilidad.

## Resumen

Empieza simple y compara con una referencia honesta. Sigue con [evaluación y coste de error](04-evaluacion-y-coste-de-error.md).

# Evaluación y coste de errores

## Objetivos y prerrequisitos

Elegirás métricas según el tipo de resultado y la consecuencia de cada fallo.

Para cantidades, MAE expresa error medio absoluto y RMSE penaliza más fallos grandes. Para clasificación, precisión pregunta cuántos avisos fueron correctos; recall, cuántos casos reales detectaste. No hay métrica universal: en fraude, perder un caso puede costar mucho; en una campaña cara, contactar falsos positivos también.

El umbral de probabilidad transforma un modelo en una acción. Ajustarlo cambia precisión, recall, capacidad operativa y equidad. Evalúa por segmentos relevantes y en datos futuros, no solo una métrica global.

## Resumen

La mejor métrica refleja la decisión y sus costes, no el número más alto de una tabla.

# Interpretación, sesgo y uso responsable

## Objetivos y prerrequisitos

Comunicarás qué hace un modelo, dónde falla y qué controles necesita antes de automatizar acciones.

Explicar importancia de variables no demuestra causalidad. Una variable puede predecir churn porque está asociada a un canal, no porque modificarla resuelva el abandono. Examina calidad, representatividad, privacidad y posibles proxies de atributos sensibles.

Documenta población, fecha de entrenamiento, objetivo, variables, métricas, umbral, fallos esperados, responsable y monitorización. Si una predicción afecta a personas, conserva revisión humana y mecanismo para detectar daño desigual.

Resuelve el [caso de priorización de churn](../../../ejercicios/temario-12/aplicacion/priorizar-churn.md). El siguiente bloque enseña a entregar este trabajo de forma colaborable y reproducible.

# Bloque 13 - Herramientas y reproducibilidad

## Propósito

Trabajar como analista dentro de un equipo: convertir peticiones en entregables verificables, documentar decisiones y hacer que un análisis pueda repetirse.

## Lecciones

1. [De petición a ticket analítico](lecciones/01-ticket-analitico.md)
2. [Proyecto reproducible y Git](lecciones/02-proyecto-reproducible-y-git.md)
3. [Notebooks, scripts y revisiones](lecciones/03-notebooks-scripts-y-revision.md)
4. [Instrumentación, tracking plan y Amplitude](lecciones/04-instrumentacion-y-amplitude.md)
5. [BI, dashboards y definición de métricas](lecciones/05-bi-y-dashboards.md)
6. [Entrega, seguimiento y comunicación](lecciones/06-entrega-y-seguimiento.md)

## Práctica

Redacta [un ticket analítico completo](../../ejercicios/temario-13/aplicacion/ticket-analitico.md).

# De petición a ticket analítico

## Objetivos y prerrequisitos

Convertirás una petición vaga en un acuerdo de trabajo verificable.

Jira, Linear y herramientas similares registran trabajo y decisiones; no son solo listas. Un ticket analítico debe contener contexto, decisión, pregunta, definición de métrica, alcance, fuentes, criterios de aceptación, responsable y fecha de revisión.

```mermaid
flowchart LR
 A[Petición] --> B[Pregunta y criterios]
 B --> C[Datos y análisis]
 C --> D[Revisión]
 D --> E[Entrega y decisión]
 E --> F[Seguimiento]
```

Si alguien pide “analiza el onboarding”, pregunta qué decisión se tomará y qué resultado cambiaría esa decisión. Así evitas producir un dashboard interesante pero inútil.

## Práctica

Redacta el [ticket analítico](../../../ejercicios/temario-13/aplicacion/ticket-analitico.md) al finalizar el bloque.

# Proyecto reproducible y Git

## Objetivos y prerrequisitos

Organizarás un análisis para que otra persona pueda repetir y revisar sus pasos.

Un proyecto separa código, documentación, datos no versionados, resultados derivados y dependencias. Git registra cambios en archivos de texto como consultas, scripts y definiciones; un commit debe explicar una unidad de cambio comprensible.

Reproducibilidad significa poder responder: qué fuente se usó, en qué fecha, qué versión de código, qué parámetros y qué transformaciones generaron el resultado. No subas datos sensibles al repositorio para “hacerlo reproducible”: documenta un acceso seguro y datos sintéticos de ejemplo.

## Resumen

Git conserva historia; la documentación conserva significado. Necesitas ambos.

# Notebooks, scripts y revisiones

## Objetivos y prerrequisitos

Distinguirás exploración, lógica reutilizable y entrega revisable.

Un notebook mezcla explicación, código y salida: es excelente para aprender, explorar y comunicar. Para lógica repetida, mueve funciones a scripts o módulos probables, con entradas y salidas claras. Ejecuta el notebook de principio a fin antes de compartirlo: celdas ejecutadas fuera de orden producen resultados que nadie puede repetir.

Una revisión de pares busca más que estilo: definiciones, grano, filtros, nulos, uniones, límites y coherencia entre conclusión y evidencia. Deja comentarios que indiquen riesgo y una acción verificable.

## Resumen

La herramienta no impone calidad; el flujo de revisión la hace posible.

# Instrumentación, tracking plan y Amplitude

## Objetivos y prerrequisitos

Entenderás cómo se convierte una acción de producto en un evento analizable y qué debe documentarse antes de medir funnels o retención.

Un evento es un registro de una acción: `reserva_creada`, con momento, usuario y propiedades como canal o importe. Un **tracking plan** define nombre, cuándo se envía, quién lo emite, propiedades, identidad, validaciones y propietario. Amplitude puede explorar eventos, funnels, cohortes y retención, pero no corrige un evento mal definido.

Verifica cobertura y cambios de versión antes de interpretar una caída. Si una app deja de enviar una propiedad, un dashboard puede mostrar un comportamiento inexistente.

## Resumen

Medir producto es diseñar un sistema de evidencia, no pulsar “crear gráfico”.

# BI, dashboards y definición de métricas

## Objetivos y prerrequisitos

Aplicarás principios comunes a Power BI, Tableau, Looker u hojas de cálculo.

Las interfaces cambian, pero un dashboard fiable necesita modelo de datos, métrica con contrato, filtros visibles, actualización conocida, propietario y audiencia. No combines tablas con grano distinto solo para que un panel “tenga más información”.

Cada visual debe responder una pregunta y ofrecer acceso al detalle necesario para auditoría. Documenta zona horaria, exclusiones, último refresco y alertas. Un dashboard es un producto: requiere mantenimiento cuando cambian fuentes o definiciones.

## Resumen

BI comunica decisiones repetidas; no reemplaza investigación ni documentación.

# Entrega, seguimiento y comunicación

## Objetivos y prerrequisitos

Cerrarás un análisis dejando claro qué se recomienda, con qué evidencia y qué ocurrirá después.

Una entrega mínima contiene decisión, hallazgo, evidencia, recomendación, límites, enlace a fuentes y siguiente medición. Adapta forma: nota ejecutiva para dirección, ticket con criterios para ingeniería, dashboard para seguimiento. No cambies el nivel de certeza por cambiar el formato.

El seguimiento convierte análisis en aprendizaje: registra la acción acordada, dueño, fecha y métrica que evaluará resultado. Si el efecto no aparece, vuelve a hipótesis, instrumentación y supuestos en lugar de defender la conclusión inicial.

Completa el [ticket analítico](../../../ejercicios/temario-13/aplicacion/ticket-analitico.md). Después podrás abordar técnicas avanzadas sin abandonar la trazabilidad profesional.

# Bloque 14 - Nivel avanzado: causalidad, escala y criterio

## Propósito

Reconocer problemas avanzados que aparecen al analizar productos y operaciones reales: causalidad, anomalías, datos grandes y datos externos.

## Lecciones

1. [Preguntas causales y diseños posibles](lecciones/01-preguntas-causales-y-disenos.md)
2. [Bootstrap y sensibilidad](lecciones/02-bootstrap-y-sensibilidad.md)
3. [Anomalías, monitorización y alertas](lecciones/03-anomalias-monitorizacion-y-alertas.md)
4. [Escala, formatos y motores analíticos](lecciones/04-escala-formatos-y-motores.md)
5. [APIs, geoespacial y datos externos](lecciones/05-apis-geoespacial-y-datos-externos.md)

## Práctica

Evalúa [un supuesto causal](../../ejercicios/temario-14/aplicacion/supuesto-causal.md).

# Preguntas causales y diseños posibles

## Objetivos y prerrequisitos

Distinguirás “qué ocurrió” de “qué habría ocurrido si cambiamos algo” y elegirás evidencia proporcional a la decisión.

Una pregunta causal compara escenarios que no se observan a la vez: “¿reducir el formulario aumentaría reservas?”. La correlación entre formularios cortos y más reservas no basta; quizá los usuarios o campañas eran distintos. Un experimento aleatorizado aproxima una comparación justa al asignar variantes de forma controlada.

```mermaid
flowchart LR
 A[Pregunta causal] --> B{¿Experimento posible?}
 B -->|Sí| C[A/B y guardrails]
 B -->|No| D[Diseño cuasiexperimental]
 C --> E[Estimación y sensibilidad]
 D --> E
 E --> F[Decisión con límites]
```

Cuando no hay experimento, diferencias en diferencias, regresión discontinua o matching pueden aportar evidencia, pero cada uno necesita supuestos verificables y análisis de sensibilidad. No son “botones de causalidad”.

## Resumen

Declara el cambio, la población, el contrafactual y los supuestos. Continúa con [bootstrap y sensibilidad](02-bootstrap-y-sensibilidad.md).

# Bootstrap y sensibilidad

## Objetivos y prerrequisitos

Usarás remuestreo para entender estabilidad de una estimación y variarás supuestos para comprobar si una conclusión depende de una decisión frágil.

El **bootstrap** crea muchas muestras al volver a seleccionar, con reemplazo, observaciones de los datos disponibles. Al recalcular una métrica se obtiene una distribución de estimaciones. Es útil cuando la fórmula analítica es complicada, pero no corrige una muestra sesgada ni convierte datos insuficientes en evidencia sólida.

Un análisis de sensibilidad cambia decisiones razonables: ventana temporal, tratamiento de outliers, umbral o definición de métrica. Si una recomendación se invierte con cambios pequeños, comunícalo y evita una afirmación tajante.

## Resumen

Incertidumbre no es solo un intervalo: también es dependencia de datos y supuestos.

# Anomalías, monitorización y alertas

## Objetivos y prerrequisitos

Construirás una respuesta ordenada ante un valor inesperado sin confundir señal con incidente.

Una **anomalía** es una observación que se aparta de un patrón esperado. Antes de alertar a negocio, comprueba tracking, frescura de datos, calendario, despliegues y cambios de definición. Una caída de eventos puede ser un fallo de instrumentación; una subida de ventas, una campaña legítima.

Una alerta necesita métrica, referencia, umbral, ventana, responsable y runbook: qué comprobar y cuándo escalar. Umbrales demasiado sensibles producen fatiga de alertas; demasiado laxos detectan tarde. Ajusta con historial y coste de no detectar.

## Resumen

Monitorizar es diseñar una decisión operativa, no solo pintar una línea roja.

# Escala, formatos y motores analíticos

## Objetivos y prerrequisitos

Elegirás una estrategia cuando los datos superen la memoria o el tiempo de una herramienta local.

Primero reduce el problema: selecciona columnas, filtra antes de transferir, agrega cerca de la fuente y evita duplicaciones. Los formatos columnares como Parquet permiten leer solo campos necesarios. DuckDB consulta archivos y tablas localmente; Polars procesa datos de manera eficiente. Son herramientas, no excusas para ignorar grano, calidad o coste.

Cuando el equipo usa warehouse, lakehouse o procesamiento distribuido, mueve cómputo cerca de los datos y controla permisos, gasto y particiones. Una consulta rápida pero semánticamente errónea sigue siendo errónea.

## Resumen

Escalar empieza por una pregunta más precisa y un modelo de datos correcto.

# APIs, geoespacial y datos externos

## Objetivos y prerrequisitos

Integrarás datos externos sin perder trazabilidad, licencias ni contexto geográfico.

Una API permite que programas soliciten datos a otro servicio. Antes de usarla, registra proveedor, permiso, licencia, fecha, versión, límites, campos y transformaciones. Una fuente externa puede cambiar sin avisar o medir una población distinta a la tuya.

Los datos geoespaciales añaden ubicación, pero una coordenada no siempre indica residencia, tienda o zona de entrega. Agregar por áreas puede ocultar diferencias internas o crear riesgos de privacidad. Minimiza precisión cuando no sea necesaria y evita inferencias sensibles sobre personas.

## Cierre

Evalúa el [supuesto causal](../../../ejercicios/temario-14/aplicacion/supuesto-causal.md). El último bloque convertirá el recorrido en pruebas de competencia y portfolio defendible.

# Bloque 15 - Portfolio y preparación profesional

## Propósito

Convertir competencias en evidencia visible: proyectos que muestran criterio, técnica, comunicación y honestidad sobre los límites.

## Lecciones

1. [Seleccionar y delimitar casos](lecciones/01-seleccionar-y-delimitar-casos.md)
2. [Estructurar un proyecto defendible](lecciones/02-estructurar-proyecto-defendible.md)
3. [Narrativa, revisión y publicación](lecciones/03-narrativa-revision-y-publicacion.md)
4. [Entrevistas, CV y capstone](lecciones/04-entrevistas-cv-y-capstone.md)

## Capstone

El [proyecto final](../../proyectos/capstone/README.md) integra el curso: datos sin limpiar, análisis, métricas, visualización, recomendación y una entrega para público no técnico.

## Cierre

Terminar el curso no significa saberlo todo. Significa tener un método fiable para aprender una herramienta nueva, hacer preguntas mejores y justificar decisiones con evidencia.

# Seleccionar y delimitar casos

## Objetivos y prerrequisitos

Elegirás proyectos que demuestren competencias reales y limitarás su alcance para poder terminarlos con rigor.

Un portfolio no es una colección de gráficos ni una lista de tecnologías. Un caso valioso empieza por una decisión: priorizar una mejora de producto, prever demanda, entender abandono o detectar una ineficiencia. Debe permitir mostrar pregunta, datos, calidad, método, evidencia, límites y recomendación.

Elige tres casos variados en vez de diez exploraciones a medias: uno de datos tabulares y limpieza; uno de métricas/producto o SQL; y uno que incorpore incertidumbre, previsión o modelo cuando sea apropiado. Usa datos con licencia y sin información personal innecesaria.

## Límite

No inventes impacto empresarial ni presentes datos simulados como si fueran clientes reales. Un proyecto didáctico puede ser excelente si declara qué es simulado, qué decisión ilustraría y qué evidencia faltaría en producción.

## Resumen

La calidad del problema y la honestidad del alcance pesan más que la complejidad aparente. Continúa con [estructura defendible](02-estructurar-proyecto-defendible.md).

# Estructurar un proyecto defendible

## Objetivos y prerrequisitos

Organizarás los artefactos que permiten a otra persona entender, ejecutar y cuestionar un análisis.

Un proyecto debe incluir README ejecutivo, pregunta y decisión, diccionario de datos, procedencia/licencia, código o notebook reproducible, visualizaciones, límites y próximos pasos. El README no repite cada detalle técnico: permite entender en dos minutos qué se halló y dónde está la evidencia.

Este flujo responde a “¿qué debe poder seguir una persona que revisa un caso?”

```mermaid
flowchart LR
 A[Problema y decisión] --> B[Datos y calidad]
 B --> C[Métodos reproducibles]
 C --> D[Hallazgos]
 D --> E[Límites]
 E --> F[Recomendación]
 F --> G[README y presentación]
```

El diagrama no obliga a una secuencia rígida: al hallar un error de datos puedes volver a la pregunta. Sí obliga a no saltar de datos a recomendación sin mostrar el razonamiento.

## Resumen

Un caso defendible conserva tanto el resultado como el camino. Continúa con [narrativa y revisión](03-narrativa-revision-y-publicacion.md).

# Narrativa, revisión y publicación

## Objetivos y prerrequisitos

Comunicarás un hallazgo a una audiencia concreta y revisarás el proyecto antes de hacerlo público.

Una narrativa analítica ordena contexto, pregunta, evidencia, interpretación, recomendación y límite. No empieza por la herramienta: “usé Python” no es un hallazgo. Un título útil dice qué ocurrió y para quién; una visualización enseña la comparación que lo respalda.

Antes de publicar, revisa enlaces, rutas, instrucciones de ejecución, dependencias, datos sensibles, licencias, definiciones de métricas y conclusiones excesivas. Pide a otra persona que intente seguir el README: si no sabe cómo reproducir o entender una decisión, el proyecto todavía no está listo.

## Error habitual

Eliminar los pasos incómodos para que el portfolio parezca perfecto. Documentar una limitación o un dato descartado con razón aumenta credibilidad profesional.

## Resumen

Publicar es una entrega para lectores reales, no el final de una carpeta local.

# Entrevistas, CV y capstone

## Objetivos y prerrequisitos

Prepararás una explicación oral de tu método y cerrarás el curso con un proyecto integrador.

En entrevista, empieza por aclarar decisión, población, métrica y datos disponibles. Al explicar un caso, distingue hecho observado, interpretación, riesgo y siguiente comprobación. Practica responder: “¿qué grano tiene esta tabla?”, “¿cómo validarías este JOIN?”, “¿qué harías ante un dato ausente?” o “¿por qué no demuestra causalidad este gráfico?”.

El CV y GitHub deben enlazar proyectos que puedas defender línea a línea: problema, contribución, herramientas, resultado y límite. No declares competencias que no puedas aplicar o explicar.

## Capstone

El [proyecto final](../../../proyectos/capstone/README.md) integra el curso: datos sin limpiar, análisis, métricas, visualización, recomendación y una entrega para público no técnico. Empieza leyendo su [rúbrica](../../../evaluaciones/rubricas/capstone.md); úsala como lista de control, no solo como nota final.

## Cierre

El objetivo no es saberlo todo: es tener un método fiable para aprender una herramienta nueva, hacer preguntas mejores y justificar decisiones con evidencia.
