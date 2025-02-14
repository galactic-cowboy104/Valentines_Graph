import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Definir el rango de valores para t
t = np.linspace(0, 2 * np.pi, 1000)

# Ecuaciones paramétricas para la forma de corazón
x = 16 * np.sin(t) ** 3
y1 = - 2 * np.cos(3*t) - np.cos(4*t)  # Componentes adicionales para la forma
y2 = 13 * np.cos(t) - 5 * np.cos(2*t) + y1  # Ecuación final de y

# Crear la figura y el eje
fig, ax = plt.subplots()
fig.patch.set_facecolor('black')  # Fondo negro de la figura
ax.set_facecolor('black')  # Fondo negro del gráfico
ax.set_xlim(-20, 20)
ax.set_ylim(-20, 15)
ax.set_aspect('equal')  # Mantener proporciones correctas

# Configuración de la cuadrícula
ax.grid(color='white', linestyle='--', linewidth=0.5)

# Configurar los colores de los ejes
ax.spines['bottom'].set_color('white')
ax.spines['left'].set_color('white')
ax.spines['top'].set_color('black')
ax.spines['right'].set_color('black')

ax.tick_params(colors='white')  # Color blanco para las etiquetas de los ejes

# Inicializar la línea de la animación
line, = ax.plot([], [], color='red', lw=2)

# Función de inicialización (línea vacía al inicio)
def init():
    line.set_data([], [])
    return line,

# Función para actualizar la animación en cada frame
def update(i):
    line.set_data(x[:i], y2[:i])  # Dibuja la curva progresivamente
    return line,

# Configurar la animación
ani = animation.FuncAnimation(
    fig, update,
    frames=len(t),  # Número de frames según la cantidad de puntos
    init_func=init, 
    blit=True, 
    interval=1,  # Velocidad de la animación
    repeat=False
)

# Mostrar la animación
plt.show()

# Guardar la imagen final
fig.savefig(
    'corazon.png',
    facecolor='black',
    dpi=300
)