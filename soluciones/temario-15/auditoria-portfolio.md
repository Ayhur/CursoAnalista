# Solucion razonada - Audita un portfolio antes de publicarlo

## 1. Puntuacion orientativa

| Area | Nota | Justificacion |
| --- | ---: | --- |
| Decision y pregunta | 1/4 | hay una afirmacion, pero no destinatario, decision ni pregunta acotada |
| Datos y calidad | 0/4 | no hay grano, fechas, diccionario, calidad ni procedencia |
| Metodo y reproducibilidad | 0/4 | notebook con filtros opacos e instrucciones ausentes |
| Razonamiento e incertidumbre | 0/4 | presenta asociacion como mejora causada por una pantalla |
| Comunicacion | 1/4 | existe una captura, pero no permite interpretar ejes, denominador o poblacion |
| Etica, privacidad y licencia | 0/4 | comparte correo y no documenta permiso de datos |

Puntos ponderados: `15*1 + 20*0 + 20*0 + 20*0 + 15*1 + 10*0 = 30`; al dividir entre 4, **7,5/100**. Una puntuacion cercana que justifique cada nota tambien es valida. Esta entrega no esta lista: incumple minimos y tiene fallos criticos.

## 2. Fallos criticos

- El CSV contiene `email`, un identificador personal innecesario para el objetivo. Debe eliminarse o anonimizarse antes de compartir, aplicando minimizacion.
- No se declara licencia o permiso de redistribucion.
- La frase "la nueva pantalla mejoro" afirma causalidad sin experimento, grupo de comparacion ni control de cambios simultaneos.

## 3. Orden de correccion

1. Retirar el CSV publico y comprobar que no hay PII, secretos o copias en historial. Es seguridad y cumplimiento, no una mejora estetica.
2. Detener la afirmacion causal y publicar como borrador privado hasta conocer diseno y fechas.
3. Crear contrato, diccionario y procedencia: definir fila, retencion, poblacion, ventana, fuente y licencia.
4. Documentar filtros, validaciones y ejecucion reproducible; verificar que no se eliminan selectivamente usuarios.
5. Regenerar un grafico con titulo, ejes, unidad, numerador, denominador, ventana y limite; despues escribir README y registro de decisiones.

## 4. Redaccion responsable

**Titular:** "En los usuarios observados entre [fecha inicio] y [fecha fin], la retencion definida como [formula] fue un 20 % mayor tras el cambio de pantalla; el analisis no identifica por si solo la causa".

**Recomendacion:** "Antes de extender la pantalla, validar definicion y cobertura de eventos, comparar segmentos y disenar una prueba controlada que mida retencion y metricas de seguridad".

## 5. Contrato minimo posible

- **Decision:** la responsable de producto decide si prueba la pantalla en una parte de usuarios.
- **Pregunta:** cual es la diferencia observada en retencion a siete dias entre usuarios expuestos y no expuestos durante una ventana definida?
- **Metrica:** usuarios con al menos un evento activo entre dias 1 y 7 / usuarios elegibles; definir fecha de cohorte y zona horaria.
- **Poblacion y ventana:** usuarios nuevos de [pais/canal] entre fechas concretas; excluir pruebas internas con regla documentada.
- **Evidencia:** tabla de eventos con fuente, grano, diccionario y licencia; no publicar emails.
- **Limite:** cambios de canal, estacionalidad o seleccion pueden explicar diferencia; no hay inferencia causal.
- **Siguiente comprobacion:** auditoria de tracking y experimento aleatorizado con metrica principal y guardrails predefinidos.
