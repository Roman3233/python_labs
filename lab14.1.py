import numpy as np
import matplotlib.pyplot as plt

# Визначення функції
def Y(x):
    with np.errstate(divide='ignore', invalid='ignore'):  # Ігнорування ділення на нуль
        result = np.sin(x) * (1 / x) * np.cos(x**2 + 1 / x)
        result[np.isnan(result)] = 0
        return result

x = np.linspace(-2, 2, 500)  # Значення x у діапазоні [-2, 2]
y = Y(x)

# Побудова графіка
plt.figure(figsize=(10, 6))
plt.plot(x, y, linestyle='-', color='blue', linewidth=2, label=r"$Y(x) = \sin(x) \cdot \frac{1}{x} \cdot \cos(x^2 + \frac{1}{x})$")
plt.title("Графік функції $Y(x)$", fontsize=16)
plt.xlabel("x", fontsize=14)
plt.ylabel("Y(x)", fontsize=14)
plt.axhline(0, color='black', linewidth=0.8, linestyle='--')  # Лінія осі X
plt.axvline(0, color='black', linewidth=0.8, linestyle='--')  # Лінія осі Y
plt.legend(fontsize=12)
plt.grid(color='gray', linestyle='--', linewidth=0.5, alpha=0.7)

plt.show()
