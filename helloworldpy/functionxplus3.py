import matplotlib.pyplot as plt
import numpy as np

# Definimos la función
def f(x):
    return x + 3

# Creamos un rango de valores para x
x = np.linspace(-10, 10, 1000)

# Evaluamos la función en cada valor de x
y = f(x)

# Creamos la gráfica
plt.plot(x, y)

# Configuramos los ejes y el título
plt.xlabel('x')
plt.ylabel('y')
plt.title('Gráfica de la función f(x) = x + 3')

# Mostramos la gráfica
plt.show()
