"""Laboratorio reproducible: previsión de pedidos diarios de Lumen.

Ejecuta: python notebooks/practicas/11-prevision-demanda.py
No usa dependencias externas. Los datos son sintéticos y didácticos.
"""

from datetime import date, timedelta
from math import sqrt
from random import Random


def crear_pedidos(dias=90, semilla=11):
    """Genera una serie diaria con patrón semanal y ruptura de stock."""
    generador = Random(semilla)
    inicio = date(2026, 1, 1)
    patron_semanal = [0, -8, -5, 0, 7, 18, 12]
    serie = []
    for indice in range(dias):
        fecha = inicio + timedelta(days=indice)
        tendencia = indice * 0.25
        ruptura_stock = -22 if 62 <= indice <= 68 else 0
        ruido = generador.randint(-6, 6)
        pedidos = round(max(0, 100 + patron_semanal[fecha.weekday()] + tendencia + ruptura_stock + ruido))
        serie.append((fecha, pedidos))
    return serie


def naive(historial):
    return historial[-1]


def seasonal_naive(historial, periodo=7):
    return historial[-periodo]


def media_movil(historial, ventana=7):
    return sum(historial[-ventana:]) / ventana


def metricas(reales, predicciones, entrenamiento):
    errores = [real - pred for real, pred in zip(reales, predicciones)]
    mae = sum(abs(error) for error in errores) / len(errores)
    rmse = sqrt(sum(error**2 for error in errores) / len(errores))
    mape_componentes = [abs(error) / real for error, real in zip(errores, reales) if real != 0]
    mape = 100 * sum(mape_componentes) / len(mape_componentes) if mape_componentes else None
    smape = 100 * sum(2 * abs(error) / (abs(real) + abs(pred)) for error, real, pred in zip(errores, reales, predicciones) if real != 0 or pred != 0) / len(errores)
    naive_in_sample = [abs(entrenamiento[i] - entrenamiento[i - 1]) for i in range(1, len(entrenamiento))]
    mase = mae / (sum(naive_in_sample) / len(naive_in_sample))
    return {"MAE": mae, "RMSE": rmse, "MAPE": mape, "sMAPE": smape, "MASE": mase}


def evaluar_walk_forward(serie, corte=63):
    """Predice cada día futuro usando solo los pedidos previos a ese día."""
    nombres = {"naive": naive, "seasonal_naive": seasonal_naive, "media_movil_7": media_movil}
    entrenamiento = [pedidos for _, pedidos in serie[:corte]]
    reales = [pedidos for _, pedidos in serie[corte:]]
    resultados = {}
    for nombre, modelo in nombres.items():
        historial = entrenamiento.copy()
        predicciones = []
        for real in reales:
            predicciones.append(modelo(historial))
            historial.append(real)
        resultados[nombre] = metricas(reales, predicciones, entrenamiento)
    return resultados


if __name__ == "__main__":
    serie = crear_pedidos()
    print("Contrato: pedidos diarios, Madrid, horizonte diario, corte tras el día 63.")
    print("Ruptura simulada: reducción de stock entre los días 63 y 69.")
    for nombre, resultado in evaluar_walk_forward(serie).items():
        legible = ", ".join(f"{clave}={valor:.2f}" for clave, valor in resultado.items() if valor is not None)
        print(f"{nombre}: {legible}")
    print("Interpreta MAPE con cautela: no está definido cuando el valor real es cero.")
