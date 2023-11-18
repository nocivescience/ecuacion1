import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

# Definir la ecuación diferencial
def model(y, x):
    dydx = -y
    return dydx

# Crear valores de x desde 0 hasta 5
x = np.linspace(0, 5, 100)

# Graficar la solución general
C_values = [1, 2, 3]  # Diferentes valores de la constante C

plt.figure(figsize=(8, 6))

for C in C_values:
    y_general = C * np.exp(-x)
    plt.plot(x, y_general, label=f'C = {C}')

# Graficar soluciones particulares con diferentes condiciones iniciales
y0_values = [1, 2, 3]  # Diferentes valores iniciales de y

for y0 in y0_values:
    y_particular = odeint(model, y0, x)
    plt.plot(x, y_particular, linestyle='--', label=f'y(0) = {y0}')

plt.title('Soluciones de la Ecuación Diferencial')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.grid(True)
plt.show()
