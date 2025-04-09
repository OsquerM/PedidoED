from project.Cliente import Cliente
from Producto import Producto
from ProductoDigital import ProductoDigital

class Pedido:
    """
    Clase que representa un pedido realizado por un cliente.

    Atributos:
        id_pedido (str): Identificador único del pedido.
        cliente (Cliente): El cliente que realiza el pedido.
        productos (list): Lista de productos asociados al pedido.
        fecha (str): La fecha en que se realiza el pedido.
    """

    def __init__(self, id_pedido: str, cliente: Cliente, fecha: str):
        """
        Inicializa un pedido con los parámetros proporcionados.

        :param id_pedido: El identificador único del pedido.
        :type id_pedido: str
        :param cliente: El cliente que realiza el pedido.
        :type cliente: Cliente
        :param fecha: La fecha en que se realiza el pedido.
        :type fecha: str
        """
        self._id_pedido = id_pedido
        self._cliente = cliente
        self._productos = []
        self._fecha = fecha

    def get_id_pedido(self):
        """
        Devuelve el identificador del pedido.

        :return: El identificador del pedido.
        :rtype: str
        """
        return self._id_pedido

    def set_id_pedido(self, id_pedido: str):
        """
        Establece un nuevo identificador para el pedido.

        :param id_pedido: El nuevo identificador para el pedido.
        :type id_pedido: str
        """
        self._id_pedido = id_pedido

    def get_cliente(self):
        """
        Devuelve el cliente que realizó el pedido.

        :return: El cliente del pedido.
        :rtype: Cliente
        """
        return self._cliente

    def set_cliente(self, cliente: Cliente):
        """
        Establece el cliente para el pedido.

        :param cliente: El nuevo cliente para el pedido.
        :type cliente: Cliente
        """
        self._cliente = cliente

    def get_productos(self):
        """
        Devuelve la lista de productos asociados al pedido.

        :return: Lista de productos en el pedido.
        :rtype: list
        """
        return self._productos

    def set_productos(self, productos: list):
        """
        Establece los productos asociados al pedido.

        :param productos: Lista de productos que forman el pedido.
        :type productos: list
        """
        self._productos = productos

    def get_fecha(self):
        """
        Devuelve la fecha en que se realizó el pedido.

        :return: La fecha del pedido.
        :rtype: str
        """
        return self._fecha

    def set_fecha(self, fecha: str):
        """
        Establece una nueva fecha para el pedido.

        :param fecha: La nueva fecha para el pedido.
        :type fecha: str
        """
        self._fecha = fecha

    def agregar_producto(self, producto: Producto):
        """
        Agrega un producto al pedido.

        :param producto: El producto que se desea agregar al pedido.
        :type producto: Producto
        """
        self._productos.append(producto)

    def calcular_total(self):
        """
        Calcula el total del pedido sumando los precios de los productos.

        :return: El total del pedido.
        :rtype: float
        """
        total = sum([producto.get_precio() for producto in self._productos])
        return total

    def __str__(self):
        """
        Devuelve una representación en formato cadena del pedido.

        :return: Cadena representando el pedido con sus atributos.
        :rtype: str
        """
        return f"Pedido(id: {self._id_pedido}, cliente: {self._cliente.get_nombre()}, fecha: {self._fecha}, " \
               f"total: {self.calcular_total()})"


# Crear una instancia de Cliente y ProductoDigital
cliente1 = Cliente("C001", "Juan Pérez", "juan@correo.com", "Calle Falsa 123")
producto_digital = ProductoDigital("PD001", "Ebook de Python", 10.99, 50, "PDF", 2.5)

# Crear un pedido y agregar el producto
pedido1 = Pedido("P001", cliente1, "2025-04-08")
pedido1.agregar_producto(producto_digital)

# Añadir pedidos a la lista
pedidos = [pedido1]

# Mostrar los pedidos
for pedido in pedidos:
    print(pedido)
