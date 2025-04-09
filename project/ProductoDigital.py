from Producto import Producto

class ProductoDigital(Producto):
    """
    Clase que representa un producto digital, que es una extensión de la clase Producto.

    Atributos:
        id_producto (str): Identificador único del producto.
        nombre (str): Nombre del producto digital.
        precio (float): Precio del producto digital.
        stock (int): Cantidad de productos digitales disponibles en stock.
        formato (str): El formato del producto digital (e.g., PDF, EPUB).
        tamano (float): El tamaño del producto digital en megabytes (MB).
    """

    def __init__(self, id_producto: str, nombre: str, precio: float, stock: int, formato: str, tamano: float):
        """
        Inicializa un producto digital con los parámetros proporcionados.

        :param id_producto: El identificador único del producto.
        :type id_producto: str
        :param nombre: El nombre del producto digital.
        :type nombre: str
        :param precio: El precio del producto digital.
        :type precio: float
        :param stock: La cantidad de productos digitales disponibles en stock.
        :type stock: int
        :param formato: El formato del producto digital (e.g., PDF, EPUB).
        :type formato: str
        :param tamano: El tamaño del producto digital en MB.
        :type tamano: float
        """
        super().__init__(id_producto, nombre, precio, stock)
        self._formato = formato
        self._tamano = tamano

    def get_formato(self):
        """
        Devuelve el formato del producto digital.

        :return: El formato del producto digital.
        :rtype: str
        """
        return self._formato

    def set_formato(self, formato: str):
        """
        Establece el formato del producto digital.

        :param formato: El nuevo formato para el producto digital.
        :type formato: str
        """
        self._formato = formato

    def get_tamano(self):
        """
        Devuelve el tamaño del producto digital en MB.

        :return: El tamaño del producto digital en MB.
        :rtype: float
        """
        return self._tamano

    def set_tamano(self, tamano: float):
        """
        Establece el tamaño del producto digital en MB.

        :param tamano: El nuevo tamaño del producto digital en MB.
        :type tamano: float
        """
        self._tamano = tamano

    def __str__(self):
        """
        Devuelve una representación en formato cadena del producto digital.

        :return: Cadena representando el producto digital con sus atributos.
        :rtype: str
        """
        return f"ProductoDigital(id: {self.get_id_producto()}, nombre: {self.get_nombre()}, precio: {self.get_precio()}, " \
               f"stock: {self.get_stock()}, formato: {self._formato}, tamaño: {self._tamano}MB)"


# Crear un producto digital
producto_digital = ProductoDigital("P001", "Ebook Python", 10.99, 50, "PDF", 2.5)

# Lista de productos
productos = []
productos.append(producto_digital)

# Mostrar el producto digital añadido
for producto in productos:
    print(producto)
