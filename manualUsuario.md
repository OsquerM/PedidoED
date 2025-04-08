# Manual de Usuario

## Introducción

Este manual está diseñado para guiar a los usuarios a través de las funcionalidades de la aplicación. Se abordarán las operaciones básicas como la gestión de productos, clientes, pedidos y reseñas.

## Funcionalidades Principales

### Gestión de Productos

1. **Añadir Producto**
   - Selecciona "Gestionar Productos" en el menú principal.
   - Ingresa el `ID`, `nombre`, `precio` y `stock` del producto.
   - El producto será añadido a la lista.

2. **Ver Productos**
   - Desde el menú de gestión de productos, selecciona "Listar productos" para ver todos los productos disponibles.

3. **Actualizar Stock**
   - Ingresa el `ID` del producto y la cantidad a añadir al stock.
   - El stock del producto se actualizará automáticamente.

### Gestión de Clientes

1. **Añadir Cliente**
   - Ingresa el `ID`, `nombre`, `email` y `dirección` del cliente.
   - El cliente será registrado en el sistema.

2. **Ver Clientes**
   - Visualiza una lista de todos los clientes registrados.

### Gestión de Pedidos

1. **Crear Pedido**
   - Selecciona un cliente y productos para crear un pedido.
   - El sistema calculará el total del pedido.

2. **Ver Pedidos**
   - Visualiza una lista de los pedidos creados.

3. **Calcular Total**
   - Calcula el total de un pedido ingresando su `ID`.

### Gestión de Reseñas

1. **Añadir Reseña**
   - El cliente puede añadir una reseña para un producto, especificando el comentario y la puntuación.
   
2. **Ver Reseñas**
   - Visualiza una lista de reseñas de productos.

## Salir

Para salir de la aplicación, selecciona la opción "Salir" en el menú principal.

---

### **Casos de Uso**

#### **Caso de Uso 1: Añadir Producto**
1. **Actor**: Administrador
2. **Descripción**: El administrador desea añadir un nuevo producto a la base de datos del sistema.
3. **Flujo**:
   - El administrador selecciona "Gestionar Productos" en el menú.
   - Introduce los detalles del producto (ID, nombre, precio y stock).
   - El sistema confirma la creación del producto y lo añade a la lista.

#### **Caso de Uso 2: Crear Pedido**
1. **Actor**: Cliente
2. **Descripción**: Un cliente realiza un pedido de productos disponibles.
3. **Flujo**:
   - El cliente selecciona productos e ingresa su información.
   - El sistema crea un pedido y calcula el total.