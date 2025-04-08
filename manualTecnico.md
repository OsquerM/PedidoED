# Manual Técnico

## Introducción

Este manual proporciona una descripción técnica detallada de la arquitectura y las funcionalidades del sistema. Está destinado a desarrolladores y personas con conocimientos técnicos que necesiten entender cómo se ha construido la aplicación y cómo modificarla.

## Estructura del Proyecto

El proyecto está estructurado de la siguiente manera:


### Descripción de las Clases Principales

1. **Clase Producto**
   - Atributos:
     - `id_producto`: Identificador único del producto.
     - `nombre`: Nombre del producto.
     - `precio`: Precio del producto.
     - `stock`: Cantidad disponible en inventario.
   - Métodos:
     - `actualizar_stock(cantidad: int)`: Actualiza la cantidad de stock disponible.

2. **Clase ProductoDigital**
   - Hereda de la clase `Producto`.
   - Atributos adicionales:
     - `formato`: Formato del producto digital (e.g., PDF, EPUB).
     - `tamano`: Tamaño del archivo en MB.
   - Métodos:
     - Redefinición del método `__str__` para incluir atributos digitales.

3. **Clase Cliente**
   - Atributos:
     - `id_cliente`: Identificador único del cliente.
     - `nombre`: Nombre del cliente.
     - `email`: Dirección de correo electrónico.
     - `direccion`: Dirección de envío.
   - Métodos:
     - Métodos de acceso (`get_*`, `set_*`) para cada atributo.

4. **Clase Reseña**
   - Atributos:
     - `id_reseña`: Identificador único de la reseña.
     - `producto`: Instancia de la clase `Producto`.
     - `cliente`: Instancia de la clase `Cliente`.
     - `comentario`: Texto de la reseña.
     - `puntuacion`: Valor de la puntuación otorgada (1-5).
   - Métodos:
     - Métodos de acceso para cada atributo.
     - `__str__`: Proporciona una representación textual de la reseña.

## Flujo de Datos

1. **Productos**: Los productos se crean y gestionan en la clase `Producto`. Se pueden añadir o actualizar en una lista de productos. Los productos digitales son una subclase que agrega atributos específicos.
2. **Clientes**: Los clientes se gestionan en un diccionario con el ID como clave.
3. **Pedidos y Reseñas**: Los pedidos y las reseñas son objetos que se relacionan con productos y clientes mediante las clases correspondientes.

