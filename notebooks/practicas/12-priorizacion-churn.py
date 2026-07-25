"""Laboratorio 12: priorización de churn en Lumen.

Ejecuta desde la raíz del repositorio:
    python notebooks/practicas/12-priorizacion-churn.py

El ejemplo evita librerías externas para que pueda ejecutarse desde un entorno
online o móvil. La puntuación es una regla didáctica; no es un modelo listo
para producción ni establece causas del churn.
"""

from csv import DictReader
from pathlib import Path
from math import exp


DATASET = Path(__file__).resolve().parents[2] / "datasets" / "lumen_churn_ejemplo.csv"


def load_rows(path: Path) -> list[dict]:
    """Carga una fila por cuenta y convierte columnas numéricas."""
    with path.open(encoding="utf-8", newline="") as file:
        rows = list(DictReader(file))
    numeric = ("sesiones_7d", "dias_desde_ultima_sesion", "factura_impagada", "tickets_30d", "churn_30d")
    for row in rows:
        for column in numeric:
            row[column] = int(row[column])
    return rows


def lumen_score(row: dict) -> float:
    """Score explicable basado solo en información disponible en el corte."""
    linear_score = (
        0.65 * row["factura_impagada"]
        + 0.10 * row["tickets_30d"]
        + 0.12 * row["dias_desde_ultima_sesion"]
        - 0.18 * row["sesiones_7d"]
        - 0.80
    )
    return 1 / (1 + exp(-linear_score))


def confusion(rows: list[dict], threshold: float) -> dict[str, int]:
    result = {"vp": 0, "fp": 0, "fn": 0, "vn": 0}
    for row in rows:
        predicted = row["score"] >= threshold
        actual = row["churn_30d"] == 1
        key = "vp" if predicted and actual else "fp" if predicted else "fn" if actual else "vn"
        result[key] += 1
    return result


def metrics(matrix: dict[str, int]) -> dict[str, float]:
    vp, fp, fn = matrix["vp"], matrix["fp"], matrix["fn"]
    precision = vp / (vp + fp) if vp + fp else 0.0
    recall = vp / (vp + fn) if vp + fn else 0.0
    f1 = 2 * precision * recall / (precision + recall) if precision + recall else 0.0
    return {"precision": precision, "recall": recall, "f1": f1}


def main() -> None:
    rows = load_rows(DATASET)
    for row in rows:
        row["score"] = lumen_score(row)
    rows.sort(key=lambda row: row["score"], reverse=True)

    # Política de Lumen: puede revisar cinco cuentas del ejemplo esta semana.
    capacity = 5
    selected = rows[:capacity]
    threshold = selected[-1]["score"]
    matrix = confusion(rows, threshold)
    result = metrics(matrix)

    print("Contrato: cuentas activas, corte 2026-01-05, churn en 30 días.")
    print(f"Capacidad: {capacity}; umbral operativo: {threshold:.2f}")
    print("\nCola priorizada")
    for row in selected:
        print(f"- {row['cuenta_id']}: score={row['score']:.2f}, churn observado={row['churn_30d']}")
    print("\nMatriz de confusión", matrix)
    print("Métricas", ", ".join(f"{name}={value:.2f}" for name, value in result.items()))
    print("\nInterpretación: estos resultados usan etiquetas históricas solo para evaluar.")
    print("No concluyen que una variable cause churn ni miden el efecto de contactar.")


if __name__ == "__main__":
    main()
