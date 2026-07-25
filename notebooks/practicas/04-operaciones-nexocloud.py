"""Laboratorio reproducible del bloque 04: NumPy aplicado a NexoCloud."""

import numpy as np


def main() -> None:
    canales = np.array(["web", "chat", "correo"])
    dias = np.array(["lun", "mar", "mié", "jue", "vie", "sáb", "dom"])
    objetivos = np.array([40.0, 45.0, 120.0])
    generador = np.random.default_rng(2026)

    # Datos simulados para aprender; no representan observaciones reales.
    base = np.array([39.0, 48.0, 118.0])
    tiempos = np.round(base + generador.normal(0, 4, size=(7, 3)), 1)
    tiempos[1, 1] = np.nan  # fallo conocido de tracking de chat el martes

    desviacion = tiempos - objetivos
    incumple = tiempos > objetivos
    cobertura = np.sum(~np.isnan(tiempos), axis=0)
    media = np.nanmean(tiempos, axis=0)

    print("Contrato: filas=días, columnas=canales, unidad=minutos")
    print("shape de tiempos:", tiempos.shape)
    print("shape de objetivos:", objetivos.shape)
    print("\nMedia y cobertura por canal:")
    for canal, valor, n in zip(canales, media, cobertura):
        print(f"- {canal}: {valor:.1f} minutos sobre {n}/{len(dias)} días observados")

    print("\nIncumplimientos (un NaN no es cumplimiento):")
    filas, columnas = np.where(incumple)
    for fila, columna in zip(filas, columnas):
        print(f"- {dias[fila]} / {canales[columna]}: {tiempos[fila, columna]:.1f} min "
              f"({desviacion[fila, columna]:+.1f} frente al objetivo)")

    copia = tiempos.copy()
    copia[0, 0] = 999.0
    assert tiempos[0, 0] != 999.0, "La copia no debe modificar el array original"


if __name__ == "__main__":
    main()
