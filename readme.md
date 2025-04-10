# Sistema de Gestión de Inventario y Pedidos (Python)

Sistema básico de gestión para productos, clientes, pedidos y reseñas. Está diseñado para ejecutarse por consola e interactuar mediante un menú.

## Funcionalidades principales

- **Productos**: Añadir, listar y actualizar stock.
- **Clientes**: Registrar nuevos clientes y ver su información.
- **Pedidos**: Crear pedidos con múltiples productos y calcular su total.
- **Reseñas**: Añadir comentarios y puntuaciones sobre productos.

## Estructura del sistema

- `Producto`: Clase base para productos físicos.
- `ProductoDigital`: Subclase para productos digitales (con formato y tamaño).
- `Cliente`: Representa un usuario con nombre, email y dirección.
- `Pedido`: Vincula productos con un cliente y una fecha.
- `Reseña`: Opiniones de clientes sobre productos con una puntuación.
- `main.py`: Interfaz por consola para gestionar todos los módulos.
