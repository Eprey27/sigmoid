import matplotlib.pyplot as plt
import numpy as np
import inspect

# Definimos la función
def f(x):
    return x**2 - 2*x + 3

# Creamos un rango de valores para x
x = np.linspace(-10, 10, 1000)

# Evaluamos la función en cada valor de x
y = f(x)

# Creamos la gráfica
fig, ax = plt.subplots()
ax.plot(x, y)

# Creamos un arreglo de ubicaciones de subejes más delgados en el eje x
x_minor_ticks = np.arange(-120, 120, 5)

# Creamos un arreglo de ubicaciones de subejes más delgados en el eje x
y_minor_ticks = np.arange(-120, 120, 5)

# Establecemos las ubicaciones de los subejes más delgados en el eje x e y
ax.set_xticks(x_minor_ticks, minor=True)
ax.set_yticks(y_minor_ticks, minor=True)

# Colocamos los ejes de coordenadas en el punto (0, 0)
ax.spines['left'].set_position('zero')
ax.spines['bottom'].set_position('zero')
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')

# Creamos los subejes más delgados
ax.grid(which='major', linestyle='-', linewidth='0.5', color='black')
ax.grid(which='minor', linestyle='--', linewidth='0.2', color='red')

# Obtenemos la definición de la función
definicion_funcion = inspect.getsource(f)

# Configuramos los ejes y el título
plt.xlabel('x')
plt.ylabel('y')
plt.title('Gráfica de la función {0}'.format(definicion_funcion))

# Configuramos la relación de aspecto de los ejes
ax.set_aspect('equal')

# Mostramos la gráfica
plt.show()
