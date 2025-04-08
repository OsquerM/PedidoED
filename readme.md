**Cosas a saber del código**

- La clase Cliente se utiliza para representar a un cliente en un sistema. Cada cliente tiene los siguientes atributos:

    id_cliente: Un identificador único para el cliente (tipo de dato str).

    nombre: El nombre del cliente (tipo de dato str).

    email: La dirección de correo electrónico del cliente (tipo de dato str).

    direccion: La dirección física del cliente (tipo de dato str).

    Métodos

    __init__(id_cliente: str, nombre: str, email: str, direccion: str):

        Constructor de la clase que inicializa un nuevo cliente con los valores proporcionados para id_cliente, nombre, email y direccion.

    get_id_cliente():

        Retorna el id_cliente del cliente.

    set_id_cliente(id_cliente: str):

        Permite modificar el valor del id_cliente.

    get_nombre():

        Retorna el nombre del cliente.

    set_nombre(nombre: str):

        Permite modificar el nombre del cliente.

    get_email():

        Retorna el email del cliente.

    set_email(email: str):

        Permite modificar el email del cliente.

    get_direccion():

        Retorna la direccion del cliente.

    set_direccion(direccion: str):

        Permite modificar la direccion del cliente.

    __str__():

        Método especial que devuelve una representación en formato string de un cliente, mostrando su id_cliente, nombre, email y direccion.