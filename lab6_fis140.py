"""Fit and compare two logarithmic models for laboratory I–V measurements."""

import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit


# Measurements transcribed from the university lab exercise.
CURRENT_MA = np.array(
    [0.13, 1.87, 3.42, 4.21, 8.20, 10.11, 11.73, 13.29, 18.88, 21.15]
)
VOLTAGE_V = np.array(
    [2.190, 2.385, 2.480, 2.523, 2.664, 2.750, 2.794, 2.835, 2.977, 3.020]
)


def shifted_logarithm(current: np.ndarray, slope: float, offset: float, shift: float):
    """Log model with a vertical offset and a horizontal current shift."""
    return slope * np.log(current + shift) + offset


def logarithm(current: np.ndarray, slope: float, offset: float):
    """Log model without a horizontal shift."""
    return slope * np.log(current) + offset


def rmse(observed: np.ndarray, predicted: np.ndarray) -> float:
    return float(np.sqrt(np.mean(np.square(observed - predicted))))


def main() -> None:
    parameters_shifted, _ = curve_fit(
        shifted_logarithm,
        CURRENT_MA,
        VOLTAGE_V,
        p0=(0.2, 2.3, 0.5),
        bounds=([-np.inf, -np.inf, -CURRENT_MA.min() + 1e-8], [np.inf, np.inf, np.inf]),
        maxfev=20_000,
    )
    parameters_log, _ = curve_fit(logarithm, CURRENT_MA, VOLTAGE_V, p0=(0.2, 2.3))

    predictions_shifted = shifted_logarithm(CURRENT_MA, *parameters_shifted)
    predictions_log = logarithm(CURRENT_MA, *parameters_log)
    print("Ajuste sobre las 10 observaciones disponibles (error dentro de muestra)")
    print(
        "Logarítmico desplazado: "
        f"V = {parameters_shifted[0]:.4f} ln(I + {parameters_shifted[2]:.4f}) "
        f"+ {parameters_shifted[1]:.4f}; RMSE={rmse(VOLTAGE_V, predictions_shifted):.4f} V"
    )
    print(
        "Logarítmico simple: "
        f"V = {parameters_log[0]:.4f} ln(I) + {parameters_log[1]:.4f}; "
        f"RMSE={rmse(VOLTAGE_V, predictions_log):.4f} V"
    )
    print(
        "El RMSE es descriptivo para estos datos y no demuestra por sí solo que un "
        "modelo sea físicamente correcto ni que generalice a otras mediciones."
    )

    current_line = np.linspace(CURRENT_MA.min(), CURRENT_MA.max(), 300)
    figure, axis = plt.subplots(figsize=(9, 6))
    axis.scatter(CURRENT_MA, VOLTAGE_V, color="black", label="Mediciones", zorder=3)
    axis.plot(
        current_line,
        shifted_logarithm(current_line, *parameters_shifted),
        label="Logarítmico desplazado",
        color="steelblue",
    )
    axis.plot(
        current_line,
        logarithm(current_line, *parameters_log),
        label="Logarítmico simple",
        color="darkorange",
    )
    axis.set_title("Ajustes logarítmicos de la curva corriente–voltaje")
    axis.set_xlabel("Corriente (mA)")
    axis.set_ylabel("Voltaje (V)")
    axis.grid(alpha=0.3)
    axis.legend()
    figure.tight_layout()
    plt.show()


if __name__ == "__main__":
    main()
