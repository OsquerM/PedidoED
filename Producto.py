import ProductoDigital
   
class Producto:
    """_summary_
    """
    def __init__(self, id_producto: str, nombre: str, precio: float, stock: int):
        """_summary_

        :param id_producto: _description_
        :type id_producto: str
        :param nombre: _description_
        :type nombre: str
        :param precio: _description_
        :type precio: float
        :param stock: _description_
        :type stock: int
        """        
        self._id_producto = id_producto
        self._nombre = nombre
        self._precio = precio
        self._stock = stock

    def get_id_producto(self):
        """_summary_

        :return: _description_
        :rtype: _type_
        """
        return self._id_producto

    def set_id_producto(self, id_producto: str):
        """_summary_

        :param id_producto: _description_
        :type id_producto: str
        """
        self._id_producto = id_producto

    def get_nombre(self):
        """_summary_

        :return: _description_
        :rtype: _type_
        """
        return self._nombre

    def set_nombre(self, nombre: str):
        """_summary_

        :param nombre: _description_
        :type nombre: str
        """
        self._nombre = nombre

    def get_precio(self):
        """_summary_

        :return: _description_
        :rtype: _type_
        """
        return self._precio

    def set_precio(self, precio: float):
        """_summary_

        :param precio: _description_
        :type precio: float
        """
        self._precio = precio

    def get_stock(self):
        """_summary_

        :return: _description_
        :rtype: _type_
        """
        return self._stock

    def set_stock(self, stock: int):
        """_summary_

        :param stock: _description_
        :type stock: int
        """
        self._stock = stock

    def __str__(self):
        """_summary_

        :return: _description_
        :rtype: _type_
        """
        return f"Producto(id: {self._id_producto}, nombre: {self._nombre}, precio: {self._precio}, stock: {self._stock})"

    def actualizar_stock(self, cantidad: int):
        """_summary_

        :param cantidad: _description_
        :type cantidad: int
        """
        self._stock += cantidad
        print(f"Stock de {self._nombre} actualizado a {self._stock}")

# Listas y Diccionarios
productos = []

