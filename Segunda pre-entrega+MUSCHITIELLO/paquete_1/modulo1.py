class Cliente:
    def __init__(self, nombre, apellido, email, direccion):
        self.nombre = nombre
        self.apellido = apellido
        self.email = email
        self.direccion = direccion

    def realizar_compra(self, producto):
        print(f"{self.nombre} ha comprado {producto}")

    def actualizar_direccion(self, nueva_direccion):
        self.direccion = nueva_direccion

    def __str__(self):
        return f"{self.nombre} {self.apellido}, Email: {self.email}, Dirección: {self.direccion}"


class ClientePremium(Cliente):
    def __init__(self, nombre, apellido, email, direccion, tarjeta_credito):
        super().__init__(nombre, apellido, email, direccion)
        self.tarjeta_credito = tarjeta_credito

    def comprar_con_descuento(self, producto):
        print(f"{self.nombre} ha comprado {producto} con descuento del 10%")

    def __str__(self):
        return super().__str__() + f", Tarjeta de Crédito: {self.tarjeta_credito}"

cliente1 = Cliente("Juan", "Pérez", "juan.perez@ejemplo.com", "Av. Siempre Viva 123")
cliente2 = ClientePremium("María", "García", "maria.garcia@ejemplo.com", "Calle Falsa 123", "1234-5678-9012-3456")

print(cliente1)

print(cliente2)

cliente1.realizar_compra("Libro")

cliente2.realizar_compra("Camisa")

cliente2.comprar_con_descuento("Zapatos")

