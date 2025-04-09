from Producto import Producto

class ProductoDigital(Producto):
    """_summary_

    :param Producto: _description_
    :type Producto: _type_
    """
    def __init__(self, id_producto: str, nombre: str, precio: float, stock: int, formato: str, tamano: float):
        """_summary_

        :param id_producto: _description_
        :type id_producto: str
        :param nombre: _description_
        :type nombre: str
        :param precio: _description_
        :type precio: float
        :param stock: _description_
        :type stock: int
        :param formato: _description_
        :type formato: str
        :param tamano: _description_
        :type tamano: float
        """
        super().__init__(id_producto, nombre, precio, stock)
        self._formato = formato
        self._tamano = tamano

    def get_formato(self):
        """_summary_

        :return: _description_
        :rtype: _type_
        """
        return self._formato

    def set_formato(self, formato: str):
        """_summary_

        :param formato: _description_
        :type formato: str
        """
        self._formato = formato

    def get_tamano(self):
        """_summary_

        :return: _description_
        :rtype: _type_
        """
        return self._tamano

    def set_tamano(self, tamano: float):
        """_summary_

        :param tamano: _description_
        :type tamano: float
        """
        self._tamano = tamano

    def __str__(self):
        """_summary_

        :return: _description_
        :rtype: _type_
        """
        return f"ProductoDigital(id: {self.get_id_producto()}, nombre: {self.get_nombre()}, precio: {self.get_precio()}, " \
               f"stock: {self.get_stock()}, formato: {self._formato}, tamaño: {self._tamano}MB)"

# Añadir productos digitales

producto_digital = ProductoDigital("P001", "Ebook Python", 10.99, 50, "PDF", 2.5)
producto_digital.append(producto_digital)
