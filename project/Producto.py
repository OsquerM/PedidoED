class Producto:
    """
    Clase que representa un producto en un sistema de inventario.

    Atributos:
        id_producto (str): Identificador único del producto.
        nombre (str): Nombre del producto.
        precio (float): Precio del producto.
        stock (int): Cantidad disponible en inventario del producto.
    """

    def __init__(self, id_producto: str, nombre: str, precio: float, stock: int):
        """
        Inicializa un producto con los parámetros proporcionados.

        :param id_producto: El identificador único del producto.
        :type id_producto: str
        :param nombre: El nombre del producto.
        :type nombre: str
        :param precio: El precio del producto.
        :type precio: float
        :param stock: La cantidad de unidades disponibles del producto.
        :type stock: int
        """
        self._id_producto = id_producto
        self._nombre = nombre
        self._precio = precio
        self._stock = stock

    def get_id_producto(self):
        """
        Obtiene el identificador del producto.

        :return: El identificador único del producto.
        :rtype: str
        """
        return self._id_producto

    def set_id_producto(self, id_producto: str):
        """
        Establece un nuevo identificador para el producto.

        :param id_producto: El nuevo identificador del producto.
        :type id_producto: str
        """
        self._id_producto = id_producto

    def get_nombre(self):
        """
        Obtiene el nombre del producto.

        :return: El nombre del producto.
        :rtype: str
        """
        return self._nombre

    def set_nombre(self, nombre: str):
        """
        Establece un nuevo nombre para el producto.

        :param nombre: El nuevo nombre del producto.
        :type nombre: str
        """
        self._nombre = nombre

    def get_precio(self):
        """
        Obtiene el precio del producto.

        :return: El precio del producto.
        :rtype: float
        """
        return self._precio

    def set_precio(self, precio: float):
        """
        Establece un nuevo precio para el producto.

        :param precio: El nuevo precio del producto.
        :type precio: float
        """
        self._precio = precio

    def get_stock(self):
        """
        Obtiene la cantidad de unidades disponibles del producto en stock.

        :return: La cantidad de unidades del producto.
        :rtype: int
        """
        return self._stock

    def set_stock(self, stock: int):
        """
        Establece una nueva cantidad de unidades disponibles en stock.

        :param stock: La nueva cantidad de unidades en stock.
        :type stock: int
        """
        self._stock = stock

    def __str__(self):
        """
        Devuelve una representación en formato cadena del producto.

        :return: Una cadena representando al producto con su id, nombre, precio y stock.
        :rtype: str
        """
        return f"Producto(id: {self._id_producto}, nombre: {self._nombre}, precio: {self._precio}, stock: {self._stock})"

    def actualizar_stock(self, cantidad: int):
        """
        Actualiza el stock del producto incrementando su cantidad.

        :param cantidad: La cantidad a añadir al stock.
        :type cantidad: int
        """
        self._stock += cantidad
        print(f"Stock de {self._nombre} actualizado a {self._stock}")


# Lista para almacenar los productos
productos = []
