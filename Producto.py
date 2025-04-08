import ProductoDigital
class Producto:
    def __init__(self, id_producto: str, nombre: str, precio: float, stock: int):
        self._id_producto = id_producto
        self._nombre = nombre
        self._precio = precio
        self._stock = stock

    def get_id_producto(self):
        return self._id_producto

    def set_id_producto(self, id_producto: str):
        self._id_producto = id_producto

    def get_nombre(self):
        return self._nombre

    def set_nombre(self, nombre: str):
        self._nombre = nombre

    def get_precio(self):
        return self._precio

    def set_precio(self, precio: float):
        self._precio = precio

    def get_stock(self):
        return self._stock

    def set_stock(self, stock: int):
        self._stock = stock

    def __str__(self):
        return f"Producto(id: {self._id_producto}, nombre: {self._nombre}, precio: {self._precio}, stock: {self._stock})"

    def actualizar_stock(self, cantidad: int):
        self._stock += cantidad
        print(f"Stock de {self._nombre} actualizado a {self._stock}")

# Listas y Diccionarios
productos = []

