from Cliente import Cliente
from Producto import Producto
import productoDigital
class Pedido:
    def __init__(self, id_pedido: str, cliente: Cliente, fecha: str):
        self._id_pedido = id_pedido
        self._cliente = cliente
        self._productos = []
        self._fecha = fecha

    def get_id_pedido(self):
        return self._id_pedido

    def set_id_pedido(self, id_pedido: str):
        self._id_pedido = id_pedido

    def get_cliente(self):
        return self._cliente

    def set_cliente(self, cliente: Cliente):
        self._cliente = cliente

    def get_productos(self):
        return self._productos

    def set_productos(self, productos: list):
        self._productos = productos

    def get_fecha(self):
        return self._fecha

    def set_fecha(self, fecha: str):
        self._fecha = fecha

    def agregar_producto(self, producto: Producto):
        self._productos.append(producto)

    def calcular_total(self):
        total = sum([producto.get_precio() for producto in self._productos])
        return total

    def __str__(self):
        return f"Pedido(id: {self._id_pedido}, cliente: {self._cliente.get_nombre()}, fecha: {self._fecha}, " \
               f"total: {self.calcular_total()})"

# Crear un pedido
cliente1 = Cliente("C001", "Juan Pérez", "juan@correo.com", "Calle Falsa 123")
pedido1 = Pedido("P001", cliente1, "2025-04-08")
pedido1.agregar_producto(productoDigital)

# Añadir pedidos a la lista
pedidos = [pedido1]
