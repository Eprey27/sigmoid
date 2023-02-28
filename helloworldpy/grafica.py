import matplotlib.pyplot as plt
import numpy as np
import sympy as sp

# Definimos la función
x = sp.Symbol('x')
e = sp.E
f = 1 / (1 + e**(-x))

# Creamos un rango de valores para x
x_range = np.linspace(-10, 10, 200)

# Evaluamos la función en cada valor de x
y = np.array([f.subs(x, i) for i in x_range])

# Creamos la gráfica
fig, ax = plt.subplots()
ax.plot(x_range, y)

# Creamos un arreglo de ubicaciones de subejes más delgados en el eje x
x_minor_ticks = np.arange(-10, 10, 1)

# Creamos un arreglo de ubicaciones de subejes más delgados en el eje y
y_minor_ticks = np.arange(-10, 10, 1)

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

# Obtenemos la definición de la función en lenguaje matemático
definicion_funcion = r'${}$'.format(sp.latex(f))

# Configuramos los ejes y el título
plt.xlabel('x')
plt.ylabel('y')
plt.title('Gráfica de la función\n{}'.format(definicion_funcion))

# Configuramos la relación de aspecto de los ejes
ax.set_aspect('equal')

# Mostramos la gráfica
plt.show()
