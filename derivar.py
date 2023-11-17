import sympy as sp
import matplotlib.pyplot as plt
import numpy as np
# Definir un símbolo
x = sp.symbols('x')

# Definir una función simbólica
f = sp.sin(x)

# Calcular la derivada simbólica
df_dx = sp.diff(f, x)

# Imprimir la derivada
print("Derivada simbólica:", df_dx)

# Convertir la expresión simbólica en una función
f_prime = sp.lambdify(x, df_dx, 'numpy')

# Crear un conjunto de datos x
x_vals = np.linspace(-np.pi, np.pi, 100)

# Calcular los valores de la derivada
y_prime = f_prime(x_vals)

# Graficar la función y su derivada
plt.plot(x_vals, np.sin(x_vals), label='Función original')
plt.plot(x_vals, y_prime, label='Derivada simbólica')
plt.legend()
plt.xlabel('x')
plt.ylabel('y')
plt.title('Función y su Derivada Simbólica')
plt.grid(True)
plt.show()
