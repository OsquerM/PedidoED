from Producto import Producto
from Cliente import Cliente
from ProductoDigital import ProductoDigital
class Reseña(Producto, Cliente):
    def __init__(self, id_reseña: str, producto: Producto, cliente: Cliente, comentario: str, puntuacion: int):
        """_summary_

        :param id_rese: _description_
        :type id_rese: _type_
        :param producto: _description_
        :type producto: Producto
        :param cliente: _description_
        :type cliente: Cliente
        :param comentario: _description_
        :type comentario: str
        :param puntuacion: _description_
        :type puntuacion: int
        """
        self._id_reseña = id_reseña
        self._producto = producto
        self._cliente = cliente
        self._comentario = comentario
        self._puntuacion = puntuacion

    def get_id_reseña(self):
        """_summary_

        :return: _description_
        :rtype: _type_
        """
        return self._id_reseña

    def set_id_reseña(self, id_reseña: str):
        """_summary_
        """
        self._id_reseña = id_reseña

    def get_producto(self):
        """_summary_

        :return: _description_
        :rtype: _type_
        """
        return self._producto

    def set_producto(self, producto: Producto):
        """_summary_

        :param producto: _description_
        :type producto: Producto
        """
        self._producto = producto

    def get_cliente(self):
        """_summary_

        :return: _description_
        :rtype: _type_
        """
        return self._cliente

    def set_cliente(self, cliente: Cliente):
        """_summary_

        :param cliente: _description_
        :type cliente: Cliente
        """
        self._cliente = cliente

    def get_comentario(self):
        """_summary_

        :return: _description_
        :rtype: _type_
        """
        return self._comentario

    def set_comentario(self, comentario: str):
        """_summary_

        :param comentario: _description_
        :type comentario: str
        """
        self._comentario = comentario

    def get_puntuacion(self):
        """_summary_

        :return: _description_
        :rtype: _type_
        """
        return self._puntuacion

    def set_puntuacion(self, puntuacion: int):
        """_summary_

        :param puntuacion: _description_
        :type puntuacion: int
        """
        self._puntuacion = puntuacion

    def __str__(self):
        return f"Reseña(id: {self._id_reseña}, producto: {self._producto.get_nombre()}, cliente: {self._cliente.get_nombre()}, " \
               f"comentario: {self._comentario}, puntuacion: {self._puntuacion})"

# Crear una reseña
reseña1 = Reseña("R001", ProductoDigital, Cliente, "Excelente Ebook", 5)
reseñas = [reseña1]
