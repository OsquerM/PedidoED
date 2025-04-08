from Producto import Producto

class ProductoDigital(Producto):
    def __init__(self, id_producto: str, nombre: str, precio: float, stock: int, formato: str, tamano: float):
        super().__init__(id_producto, nombre, precio, stock)
        self._formato = formato
        self._tamano = tamano

    def get_formato(self):
        return self._formato

    def set_formato(self, formato: str):
        self._formato = formato

    def get_tamano(self):
        return self._tamano

    def set_tamano(self, tamano: float):
        self._tamano = tamano

    def __str__(self):
        return f"ProductoDigital(id: {self.get_id_producto()}, nombre: {self.get_nombre()}, precio: {self.get_precio()}, " \
               f"stock: {self.get_stock()}, formato: {self._formato}, tamaño: {self._tamano}MB)"

# Añadir productos digitales
producto_digital = ProductoDigital("P001", "Ebook Python", 10.99, 50, "PDF", 2.5)
producto.append(producto_digital)
