# Solución razonada - Priorizar churn en Lumen

1. **Contrato.** Una fila representa una cuenta de pago activa el lunes a las 09:00. El target es cancelar dentro de los 30 días posteriores al corte; las features pueden ser sesiones de los últimos 7 días, días desde última sesión y factura impagada conocida. La acción es ordenar una cola de hasta 20 casos para revisión humana. No es una decisión automática de descuento ni una explicación causal.

2. `sesiones_7d` y `factura_impagada` son permitidas si se actualizan antes del corte. `fecha_cancelacion`, `motivo_de_cancelacion` y `tickets_cerrados_en_los_30_dias_siguientes` son fuga: aparecen al cancelar o después del horizonte. «Necesita aclaración» sería una columna sin sello temporal claro; por ejemplo, `estado_factura` si el sistema se actualiza con retraso.

3. Si churn es raro, predecir continuidad para todas las cuentas puede acertar casi todas por frecuencia. Pero genera cero verdaderos positivos y no ayuda a decidir las 20 revisiones. El baseline es útil para demostrar que accuracy no es la meta de Lumen.

4. Ordenaría por score y elegiría el score de la quinta cuenta como umbral operacional; después evaluaría **precision@5** y cobertura/recall. El umbral depende de capacidad, coste de revisión y beneficio esperado, por lo que 0,5 no tiene privilegio especial.

5. Precision = `4 / (4 + 1) = 0,80`. Recall = `4 / (4 + 2) = 0,67`. F1 = `2 × 0,80 × 0,67 / (0,80 + 0,67) ≈ 0,73`. Para valorar rentabilidad faltan coste de cada revisión, valor de una retención, tasa con la que la intervención evita una cancelación y posibles daños de contactar innecesariamente.

6. Monitorizaría semanalmente valores ausentes/distribución de scores (deriva de datos), y cuando madure el horizonte precision@20 y recall por segmento. Revisaría que variables como región u horario no funcionen como proxies injustificados y que la cola no reciba una acción automática sin revisión. La importancia de una variable no demuestra que modificarla reduzca churn.

La solución muestra una política plausible, no una única respuesta. Cambiar el tamaño de la cola, la definición de churn o el coste de intervención requiere cambiar el contrato y volver a validar.
