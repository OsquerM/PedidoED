from Producto import Producto
from project.Cliente import Cliente
from ProductoDigital import ProductoDigital

class Reseña(Producto, Cliente):
    """
    Clase que representa una reseña de un producto hecha por un cliente.

    Hereda de las clases `Producto` y `Cliente`.

    Atributos:
        id_reseña (str): Identificador único de la reseña.
        producto (Producto): El producto sobre el que se realiza la reseña.
        cliente (Cliente): El cliente que escribe la reseña.
        comentario (str): El comentario que el cliente deja sobre el producto.
        puntuacion (int): La puntuación dada al producto (de 1 a 5).
    """

    def __init__(self, id_reseña: str, producto: Producto, cliente: Cliente, comentario: str, puntuacion: int):
        """
        Inicializa una nueva reseña con los parámetros proporcionados.

        :param id_reseña: El identificador único de la reseña.
        :type id_reseña: str
        :param producto: El producto sobre el que se realiza la reseña.
        :type producto: Producto
        :param cliente: El cliente que escribe la reseña.
        :type cliente: Cliente
        :param comentario: El comentario que el cliente deja sobre el producto.
        :type comentario: str
        :param puntuacion: La puntuación dada al producto (de 1 a 5).
        :type puntuacion: int
        """
        self._id_reseña = id_reseña
        self._producto = producto
        self._cliente = cliente
        self._comentario = comentario
        self._puntuacion = puntuacion

    def get_id_reseña(self):
        """
        Devuelve el identificador de la reseña.

        :return: El identificador de la reseña.
        :rtype: str
        """
        return self._id_reseña

    def set_id_reseña(self, id_reseña: str):
        """
        Establece un nuevo identificador para la reseña.

        :param id_reseña: El nuevo identificador para la reseña.
        :type id_reseña: str
        """
        self._id_reseña = id_reseña

    def get_producto(self):
        """
        Devuelve el producto asociado a la reseña.

        :return: El producto de la reseña.
        :rtype: Producto
        """
        return self._producto

    def set_producto(self, producto: Producto):
        """
        Establece el producto para la reseña.

        :param producto: El nuevo producto asociado a la reseña.
        :type producto: Producto
        """
        self._producto = producto

    def get_cliente(self):
        """
        Devuelve el cliente que ha realizado la reseña.

        :return: El cliente que realizó la reseña.
        :rtype: Cliente
        """
        return self._cliente

    def set_cliente(self, cliente: Cliente):
        """
        Establece el cliente que ha realizado la reseña.

        :param cliente: El nuevo cliente asociado a la reseña.
        :type cliente: Cliente
        """
        self._cliente = cliente

    def get_comentario(self):
        """
        Devuelve el comentario dejado por el cliente en la reseña.

        :return: El comentario de la reseña.
        :rtype: str
        """
        return self._comentario

    def set_comentario(self, comentario: str):
        """
        Establece el comentario para la reseña.

        :param comentario: El nuevo comentario de la reseña.
        :type comentario: str
        """
        self._comentario = comentario

    def get_puntuacion(self):
        """
        Devuelve la puntuación dada al producto.

        :return: La puntuación de la reseña.
        :rtype: int
        """
        return self._puntuacion

    def set_puntuacion(self, puntuacion: int):
        """
        Establece la puntuación para la reseña.

        :param puntuacion: La nueva puntuación de la reseña.
        :type puntuacion: int
        """
        self._puntuacion = puntuacion

    def __str__(self):
        """
        Devuelve una representación en formato cadena de la reseña.

        :return: Cadena representando la reseña con sus atributos.
        :rtype: str
        """
        return f"Reseña(id: {self._id_reseña}, producto: {self._producto.get_nombre()}, cliente: {self._cliente.get_nombre()}, " \
               f"comentario: {self._comentario}, puntuacion: {self._puntuacion})"


# Crear una reseña
producto_digital = ProductoDigital("PD001", "Ebook de Python", 10.99, 50, "PDF", 2.5)
cliente1 = Cliente("C001", "Juan Pérez", "juanperez@email.com", "Calle Ficticia 123")

reseña1 = Reseña("R001", producto_digital, cliente1, "Excelente Ebook", 5)

reseñas = [reseña1]

# Mostrar la reseña
for reseña in reseñas:
    print(reseña)
