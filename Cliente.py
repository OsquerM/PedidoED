class Cliente:
    def __init__(self, id_cliente: str, nombre: str, email: str, direccion: str):
        self._id_cliente = id_cliente
        self._nombre = nombre
        self._email = email
        self._direccion = direccion

    def get_id_cliente(self):
        return self._id_cliente

    def set_id_cliente(self, id_cliente: str):
        self._id_cliente = id_cliente

    def get_nombre(self):
        return self._nombre

    def set_nombre(self, nombre: str):
        self._nombre = nombre

    def get_email(self):
        return self._email

    def set_email(self, email: str):
        self._email = email

    def get_direccion(self):
        return self._direccion

    def set_direccion(self, direccion: str):
        self._direccion = direccion

    def __str__(self):
        return f"Cliente(id: {self._id_cliente}, nombre: {self._nombre}, email: {self._email}, direccion: {self._direccion})"


# Listas y Diccionarios
productos = []
clientes = {}
