# Valentine's Graph

Este proyecto genera y anima la figura de un corazón utilizando Python con las bibliotecas Matplotlib y NumPy. La animación se basa en ecuaciones paramétricas que representan la forma de un corazón y se dibuja progresivamente para crear un efecto visual atractivo.

## Requisitos

Para ejecutar este proyecto, necesitas tener instaladas las siguientes bibliotecas de Python:

- **NumPy**: Para realizar cálculos matemáticos y definir las ecuaciones paramétricas.
- **Matplotlib**: Para graficar y animar la figura.

Puedes instalarlas con el siguiente comando:

```bash
pip install numpy matplotlib
```

## Contenido del Repositorio

- **Código principal**: Archivo en Python que genera la animación del corazón.
- **Imagen generada**: Se guarda automáticamente como `corazon.png` después de ejecutar el script.

## Instrucciones de Uso

1. **Ejecutar el código**  
   Ejecuta el script en un entorno de Python compatible (como un IDE o la terminal) para visualizar la animación en tiempo real:

    ```bash
    python3 main.py
    ```

2. **Guardado de la imagen**  
   Después de la ejecución, se genera automáticamente la imagen `corazon.png` con la figura del corazón en un fondo negro.

## Explicación del Proyecto

### Ecuaciones Paramétricas del Corazón

El corazón se genera a partir de ecuaciones matemáticas en función de un parámetro `t`. Estas ecuaciones definen las coordenadas `(x, y)` del contorno del corazón y permiten trazarlo de manera precisa.

### Animación

Se utiliza `FuncAnimation` de Matplotlib para dibujar progresivamente la curva, creando una animación donde la figura se forma de manera fluida.

### Personalización

Puedes modificar el color, la resolución y otros aspectos visuales ajustando los parámetros en el código.

## Créditos

Este proyecto fue desarrollado para demostrar el uso de ecuaciones paramétricas y animaciones en Python de una manera visualmente atractiva.

¡Disfruta programando y explorando la creatividad con código! 💖
