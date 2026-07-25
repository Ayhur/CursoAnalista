# Solución razonada - Diagnóstico operativo de NexoCloud

## 1. Contrato antes de calcular

`tiempos.shape` es `(4, 3)`: cuatro filas de días y tres columnas de canales, en minutos. `np.nan` significa «tiempo no observado por el sistema», no cero minutos ni ausencia de solicitudes. El contrato permite interpretar cada reducción posterior.

## 2. Desviación por canal

```python
desviacion = tiempos - objetivos
print(desviacion)
# [[-2.,  7., -10.],
#  [ 1., nan,  10.],
#  [ 4.,  2.,  -5.],
#  [-1., 10.,   5.]]
```

`objetivos.shape` es `(3,)`, que coincide con la última dimensión de `tiempos` `(4, 3)`. NumPy aplica 40 a web, 45 a chat y 120 a correo en cada fila. Esto es correcto porque ambos arrays comparten el mismo orden de canales; si el orden fuese distinto, una forma compatible no salvaría el análisis.

## 3. Incumplimientos

```python
incumple = tiempos > objetivos
filas, columnas = np.where(incumple)
for fila, columna in zip(filas, columnas):
    print(f"día {fila}: {canales[columna]}")
```

Los incumplimientos son: lunes-chat; martes-web y correo; miércoles-web y chat; jueves-chat y correo. El martes-chat no aparece porque comparar con `NaN` devuelve `False`; esto no prueba cumplimiento. Debe quedar marcado como dato pendiente de investigación.

## 4. Media y cobertura

```python
media_por_canal = np.nanmean(tiempos, axis=0)
observados_por_canal = np.sum(~np.isnan(tiempos), axis=0)
print(media_por_canal)       # [40.5, 51.333..., 120.0]
print(observados_por_canal)  # [4, 3, 4]
```

Chat muestra una media de aproximadamente 51.3 minutos, pero se calcula sobre tres días, no cuatro. Informar media y cobertura juntos evita presentar la ausencia como si el desempeño de ese día hubiese sido normal.

## 5. Vista y copia

```python
vista = tiempos[:, :2]
vista[0, 0] = 999.0          # altera tiempos: es una vista básica

trabajo = tiempos.copy()
trabajo[0, 0] = 999.0        # no altera tiempos
```

En una práctica real primero restauraríamos el valor de prueba o volveríamos a cargar `tiempos`. La copia evita corromper el origen durante una imputación o una simulación, y facilita reproducir la auditoría.

## 6. Recomendación prudente

La evidencia justifica revisar el canal chat: supera su objetivo en los tres días observados y tiene una media por encima de 45 minutos. Antes de afirmar que el problema es de capacidad, hay que investigar el dato ausente del martes y comprobar severidad de casos, cambios de tracking y volumen por canal.
