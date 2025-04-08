from Producto import Producto
from Cliente import Cliente
from ProductoDigital import ProductoDigital
class Reseña(Producto, Cliente):
    def __init__(self, id_reseña: str, producto: Producto, cliente: Cliente, comentario: str, puntuacion: int):
        self._id_reseña = id_reseña
        self._producto = producto
        self._cliente = cliente
        self._comentario = comentario
        self._puntuacion = puntuacion

    def get_id_reseña(self):
        return self._id_reseña

    def set_id_reseña(self, id_reseña: str):
        self._id_reseña = id_reseña

    def get_producto(self):
        return self._producto

    def set_producto(self, producto: Producto):
        self._producto = producto

    def get_cliente(self):
        return self._cliente

    def set_cliente(self, cliente: Cliente):
        self._cliente = cliente

    def get_comentario(self):
        return self._comentario

    def set_comentario(self, comentario: str):
        self._comentario = comentario

    def get_puntuacion(self):
        return self._puntuacion

    def set_puntuacion(self, puntuacion: int):
        self._puntuacion = puntuacion

    def __str__(self):
        return f"Reseña(id: {self._id_reseña}, producto: {self._producto.get_nombre()}, cliente: {self._cliente.get_nombre()}, " \
               f"comentario: {self._comentario}, puntuacion: {self._puntuacion})"

# Crear una reseña
reseña1 = Reseña("R001", productoDigital, cliente1, "Excelente Ebook", 5)
reseñas = [reseña1]
