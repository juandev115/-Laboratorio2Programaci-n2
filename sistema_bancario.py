# Simulación de un sistema bancario

# Definición de la clase CuentaBancaria
class CuentaBancaria:
    def __init__(self, nombre_cliente, saldo_inicial=0):
        self.nombre_cliente = nombre_cliente
        self.saldo = saldo_inicial

    def depositar(self, cantidad):
        if cantidad > 0:
            self.saldo += cantidad
            print(f"Depósito de {cantidad} realizado con éxito. Nuevo saldo: {self.saldo}")
        else:
            print("La cantidad a depositar debe ser positiva.")

    def retirar(self, cantidad):
        if cantidad > self.saldo:
            print("Fondos insuficientes para realizar el retiro.")
        elif cantidad > 0:
            self.saldo -= cantidad
            print(f"Retiro de {cantidad} realizado con éxito. Nuevo saldo: {self.saldo}")
        else:
            print("La cantidad a retirar debe ser positiva.")

    def consultar_saldo(self):
        return self.saldo


# Función para simular el procesamiento de clientes en la cola
def proceso_clientes(cola):
    while cola:
        cliente = cola.pop(0)  # atender al primer cliente de la cola
        print(f"\nAtendiendo a {cliente.nombre_cliente}...")

        # Simulación de operaciones
        print("Realizando operaciones:")
        cliente.depositar(100)  # depósito ficticio de 100
        cliente.retirar(50)     # retiro ficticio de 50

        print(f"Saldo final de {cliente.nombre_cliente}: {cliente.consultar_saldo()}")

        # Mostrar el estado de la cola
        mostrar_estado_cola(cola)


# Función para mostrar el estado actual de la cola
def mostrar_estado_cola(cola):
    if cola:
        print("\nClientes restantes en la cola:")
        for cliente in cola:
            print(f"- {cliente.nombre_cliente}")
    else:
        print("\nNo hay más clientes en la cola. ¡Todos atendidos!")


# Función principal para crear clientes y simular el banco
def simular_banco():
    # Crear algunos clientes con cuentas bancarias
    cliente1 = CuentaBancaria("Juan Perez", 500)
    cliente2 = CuentaBancaria("Maria Gonzalez", 300)
    cliente3 = CuentaBancaria("Carla Díaz", 700)

    # Crear la cola de clientes
    cola = [cliente1, cliente2, cliente3]

    # Procesar clientes en la cola
    proceso_clientes(cola)


# Ejecutar la simulación
simular_banco()
