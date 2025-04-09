class Cliente:
    """
    Representa un cliente en el sistema.

    Esta clase almacena información sobre el cliente, como su ID, nombre,
    dirección y correo electrónico. Proporciona métodos para obtener y
    establecer estos valores.

    Atributos:
        _id_cliente (str): El identificador único del cliente.
        _nombre (str): El nombre completo del cliente.
        _email (str): La dirección de correo electrónico del cliente.
        _direccion (str): La dirección física del cliente.
    """

    def __init__(self, id_cliente: str, nombre: str, email: str, direccion: str):
        """
        Inicializa una nueva instancia de la clase Cliente.

        :param id_cliente: El identificador único del cliente.
        :type id_cliente: str
        :param nombre: El nombre completo del cliente.
        :type nombre: str
        :param email: La dirección de correo electrónico del cliente.
        :type email: str
        :param direccion: La dirección física del cliente.
        :type direccion: str
        """
        self._id_cliente = id_cliente
        self._nombre = nombre
        self._email = email
        self._direccion = direccion

    def get_id_cliente(self):
        """
        Obtiene el identificador único del cliente.

        :return: El identificador único del cliente.
        :rtype: str
        """
        return self._id_cliente

    def set_id_cliente(self, id_cliente: str):
        """
        Establece el identificador único del cliente.

        :param id_cliente: El identificador único del cliente.
        :type id_cliente: str
        """
        self._id_cliente = id_cliente

    def get_nombre(self):
        """
        Obtiene el nombre completo del cliente.

        :return: El nombre completo del cliente.
        :rtype: str
        """
        return self._nombre

    def set_nombre(self, nombre: str):
        """
        Establece el nombre completo del cliente.

        :param nombre: El nombre completo del cliente.
        :type nombre: str
        """
        self._nombre = nombre

    def get_email(self):
        """
        Obtiene la dirección de correo electrónico del cliente.

        :return: La dirección de correo electrónico del cliente.
        :rtype: str
        """
        return self._email

    def set_email(self, email: str):
        """
        Establece la dirección de correo electrónico del cliente.

        :param email: La dirección de correo electrónico del cliente.
        :type email: str
        """
        self._email = email

    def get_direccion(self):
        """
        Obtiene la dirección física del cliente.

        :return: La dirección física del cliente.
        :rtype: str
        """
        return self._direccion

    def set_direccion(self, direccion: str):
        """
        Establece la dirección física del cliente.

        :param direccion: La dirección física del cliente.
        :type direccion: str
        """
        self._direccion = direccion

    def __str__(self):
        """
        Devuelve una representación en cadena del cliente.

        :return: Una cadena con los detalles del cliente.
        :rtype: str
        """
        return f"Cliente(id: {self._id_cliente}, nombre: {self._nombre}, email: {self._email}, direccion: {self._direccion})"
