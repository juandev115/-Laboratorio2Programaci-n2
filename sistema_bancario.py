# sistema_bancario_corregido.py
# Simulación simple de un banco: cola de clientes, depósitos, retiros y consulta de saldo.

class CuentaBancaria:
    def __init__(self, nombre_cliente, saldo_inicial=0.0):
        self.nombre_cliente = nombre_cliente
        self.saldo = float(saldo_inicial)

    def depositar(self, cantidad):
        try:
            cantidad = float(cantidad)
        except (TypeError, ValueError):
            return False, "Cantidad inválida."
        if cantidad <= 0:
            return False, "La cantidad a depositar debe ser positiva."
        self.saldo += cantidad
        return True, f"Depósito de {cantidad:.2f} realizado. Nuevo saldo: {self.saldo:.2f}"

    def retirar(self, cantidad):
        try:
            cantidad = float(cantidad)
        except (TypeError, ValueError):
            return False, "Cantidad inválida."
        if cantidad <= 0:
            return False, "La cantidad a retirar debe ser positiva."
        if cantidad > self.saldo:
            return False, "Fondos insuficientes."
        self.saldo -= cantidad
        return True, f"Retiro de {cantidad:.2f} realizado. Nuevo saldo: {self.saldo:.2f}"

    def consultar_saldo(self):
        return self.saldo


def mostrar_estado_cola(cola):
    if cola:
        print("\nClientes restantes en la cola:")
        for c in cola:
            print(f" - {c.nombre_cliente} (saldo: {c.saldo:.2f})")
    else:
        print("\nNo hay más clientes en la cola. ¡Todos atendidos!")


def proceso_clientes_automatico(cola):
    """Simula operaciones automáticas (depósito 100, retiro 50) para cada cliente."""
    while cola:
        cliente = cola.pop(0)
        print(f"\nAtendiendo a {cliente.nombre_cliente} (saldo inicial: {cliente.saldo:.2f})")
        ok, msg = cliente.depositar(100)
        print(msg)
        ok, msg = cliente.retirar(50)
        print(msg)
        print(f"Saldo final de {cliente.nombre_cliente}: {cliente.consultar_saldo():.2f}")
        mostrar_estado_cola(cola)


def proceso_clientes_interactivo(cola):
    """Permite al usuario elegir operaciones para cada cliente mientras se atiende."""
    while cola:
        cliente = cola.pop(0)
        print(f"\nAtendiendo a {cliente.nombre_cliente} (saldo actual: {cliente.saldo:.2f})")
        while True:
            print("\nOperaciones disponibles:")
            print(" 1) Depositar")
            print(" 2) Retirar")
            print(" 3) Consultar saldo")
            print(" 4) Finalizar atención y pasar al siguiente cliente")
            elec = input("Elige opción (1-4): ").strip()
            if elec == "1":
                cantidad = input("Cantidad a depositar: ").strip()
                ok, msg = cliente.depositar(cantidad)
                print(msg)
            elif elec == "2":
                cantidad = input("Cantidad a retirar: ").strip()
                ok, msg = cliente.retirar(cantidad)
                print(msg)
            elif elec == "3":
                print(f"Saldo actual: {cliente.consultar_saldo():.2f}")
            elif elec == "4":
                print(f"Finalizando atención de {cliente.nombre_cliente}. Saldo final: {cliente.consultar_saldo():.2f}")
                break
            else:
                print("Opción inválida. Intenta nuevamente.")
        mostrar_estado_cola(cola)


def simular_banco(modo="auto"):
    # Crear algunos clientes
    cliente1 = CuentaBancaria("Juan Perez", 500)
    cliente2 = CuentaBancaria("Maria Gonzalez", 300)
    cliente3 = CuentaBancaria("Carla Diaz", 700)

    cola = [cliente1, cliente2, cliente3]

    if modo == "auto":
        proceso_clientes_automatico(cola)
    else:
        proceso_clientes_interactivo(cola)


if __name__ == "__main__":
    print("Simulación de Banco")
    modo = input("Modo automático? (s = sí, n = no) [s]: ").strip().lower()
    if modo == "n":
        simular_banco(modo="interactivo")
    else:
        simular_banco(modo="auto")
