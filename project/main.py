from Producto import Producto
from project.Cliente import Cliente
from Pedido import Pedido
from Reseña import Reseña

productos = []
clientes = {}
pedidos = []
reseñas = []

def mostrar_menu():
    """
    Muestra el menú principal con las opciones disponibles para gestionar productos, clientes, pedidos, reseñas, o salir del sistema.

    :return: None
    """
    print("\n--- Menú Principal ---")
    print("1. Gestionar productos")
    print("2. Gestionar clientes")
    print("3. Gestionar pedidos")
    print("4. Gestionar reseñas")
    print("5. Salir")

def gestionar_productos():
    """
    Permite gestionar los productos en el sistema. Ofrece opciones para agregar productos, listar productos y actualizar el stock de productos existentes.

    :return: None
    """
    while True:
        print("\n--- Gestión de Productos ---")
        print("1. Añadir producto")
        print("2. Listar productos")
        print("3. Actualizar stock")
        print("4. Volver")
        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
            id_producto = input("ID Producto: ")
            nombre = input("Nombre: ")
            try:
                precio = float(input("Precio: "))
                stock = int(input("Stock: "))
                producto = Producto(id_producto, nombre, precio, stock)
                productos.append(producto)
                print(f"Producto '{nombre}' añadido.")
            except ValueError:
                print("Error: Ingrese un precio y un stock válidos.")
        elif opcion == "2":
            print("\nLista de productos:")
            for producto in productos:
                print(producto)
        elif opcion == "3":
            id_producto = input("ID Producto a actualizar: ")
            cantidad = int(input("Cantidad a añadir: "))
            for producto in productos:
                if producto.id_producto == id_producto:
                    producto.actualizar_stock(cantidad)
                    print(f"Stock de '{producto.nombre}' actualizado.")
                    break
            else:
                print("Producto no encontrado.")
        elif opcion == "4":
            break

def gestionar_clientes():
    """
    Permite gestionar los clientes en el sistema. Ofrece opciones para agregar clientes, listar clientes y volver al menú principal.

    :return: None
    """
    while True:
        print("\n--- Gestión de Clientes ---")
        print("1. Añadir cliente")
        print("2. Listar clientes")
        print("3. Volver")
        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
            id_cliente = input("ID Cliente: ")
            nombre = input("Nombre: ")
            email = input("Email: ")
            direccion = input("Dirección: ")
            cliente = Cliente(id_cliente, nombre, email, direccion)
            clientes[id_cliente] = cliente
            print(f"Cliente '{nombre}' añadido.")
        elif opcion == "2":
            print("\nLista de clientes:")
            for cliente in clientes.values():
                print(cliente)
        elif opcion == "3":
            break

def gestionar_pedidos():
    """
    Permite gestionar los pedidos de los clientes. Ofrece opciones para crear nuevos pedidos, listar pedidos existentes, calcular el total de un pedido y volver al menú principal.

    :return: None
    """
    while True:
        print("\n--- Gestión de Pedidos ---")
        print("1. Crear pedido")
        print("2. Listar pedidos")
        print("3. Calcular total de pedido")
        print("4. Volver")
        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
            id_pedido = input("ID Pedido: ")
            cliente_id = input("ID Cliente: ")
            fecha = input("Fecha: ")
            cliente = clientes.get(cliente_id)
            if cliente:
                pedido = Pedido(id_pedido, cliente, fecha)
                productos_ids = input("IDs de productos (separados por coma): ").split(",")
                for id_producto in productos_ids:
                    producto = next((p for p in productos if p.id_producto == id_producto.strip()), None)
                    if producto:
                        pedido.agregar_producto(producto)
                    else:
                        print(f"Producto con ID {id_producto.strip()} no encontrado.")
                pedidos.append(pedido)
                print(f"Pedido '{id_pedido}' creado.")
            else:
                print("Cliente no encontrado.")
        elif opcion == "2":
            print("\nLista de pedidos:")
            for pedido in pedidos:
                print(pedido)
        elif opcion == "3":
            id_pedido = input("ID Pedido: ")
            pedido = next((p for p in pedidos if p.id_pedido == id_pedido), None)
            if pedido:
                print(f"Total del pedido: {pedido.calcular_total()}")
            else:
                print("Pedido no encontrado.")
        elif opcion == "4":
            break

def gestionar_resenas():
    """
    Permite gestionar las reseñas de los productos. Ofrece opciones para agregar reseñas, listar reseñas existentes y volver al menú principal.

    :return: None
    """
    while True:
        print("\n--- Gestión de Reseñas ---")
        print("1. Añadir reseña")
        print("2. Listar reseñas")
        print("3. Volver")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            id_reseña = input("ID Reseña: ")
            id_producto = input("ID Producto: ")
            id_cliente = input("ID Cliente: ")
            comentario = input("Comentario: ")
            try:
                puntuacion = int(input("Puntuación (1-5): "))
                if 1 <= puntuacion <= 5:
                    producto = next((p for p in productos if p.id_producto == id_producto), None)
                    cliente = clientes.get(id_cliente)
                    if producto and cliente:
                        reseña = Reseña(id_reseña, producto, cliente, comentario, puntuacion)
                        reseñas.append(reseña)
                        print(f"Reseña para el producto '{producto.nombre}' añadida.")
                    else:
                        print("Producto o Cliente no encontrados.")
                else:
                    print("La puntuación debe ser un número entre 1 y 5.")
            except ValueError:
                print("Error: Puntuación no válida.")
        elif opcion == "2":
            print("\nLista de reseñas:")
            for reseña in reseñas:
                print(reseña)
        elif opcion == "3":
            break

def main():
    """
    Función principal que ejecuta el programa. Muestra el menú y permite gestionar productos, clientes, pedidos, reseñas, o salir.

    :return: None
    """
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
            gestionar_productos()
        elif opcion == "2":
            gestionar_clientes()
        elif opcion == "3":
            gestionar_pedidos()
        elif opcion == "4":
            gestionar_resenas()
        elif opcion == "5":
            print("Saliendo...")
            break

if __name__ == "__main__":
    main()
