#sistemas de gestion de productos 
class Producto:
    def __init__(self, nombre, precio, cantidad):
        self.nombre = nombre
        self.precio = precio
        self.cantidad = cantidad
        
    def aumentar_stock(self,cantidad):
        self.cantidad += cantidad
    def disminuir_stock(self,cantidad):
        if cantidad > self.cantidad:
            print(f"No hay suficientes stock de {self.nombre}.")
        else:
            self.cantidad -= cantidad
    def mostrar_info(self):
        return f"{self.nombre}-Precio: {self.precio:.2f}-Stock: {self.cantidad}"
    
# Funciones
def crear_inventario():
    return [
        Producto("Mouse", 20.0, 15),
        Producto("Teclado", 35.0, 10),
        Producto("Monitor", 150.0, 5)
    ]
def mostrar_inventario(inventario):
    print("\nInventario Actual: ")
    for i, producto in enumerate(inventario):
        print(f"{i+1}. {producto.mostrar_info()}")
def seleccionar_producto(inventario):
    mostrar_inventario(inventario)
    try:
        eleccion = int(input("Seleccione el número del producto: "))
        if 1 <= eleccion <= len(inventario):
            return inventario[eleccion - 1]
    except ValueError:
        print("Entrada no válida. Por favor, ingrese un número.")
    return None
def menu():
    inventario = crear_inventario()
    while True:
        print("\n--- Menu De Inventario ---")
        print("1. Mostrar Inventario")
        print("2. Comprar Producto (aumentar stock)")
        print("3. Vender Producto (disminuir stock)")
        print("4. Salir")
        opcion = input("Elige una opción: ")
        if opcion == "1":
            mostrar_inventario(inventario)
        elif opcion == "2":
            Producto = seleccionar_producto(inventario)
            if Producto:
                try:
                    cantidad = int(input("Cantidad a agregar: "))
                    if cantidad > 0:
                        Producto.aumentar_stock(cantidad)
                        print("Stock aumentado.")
                    else:
                        print("Cantidad inválida.")
                except ValueError:
                    print("Entrada no validad.")
        elif opcion == "3":
            Producto = seleccionar_producto(inventario)
            if Producto:
                try:
                    cantidad = int(input("Cantidad a vender: "))
                    if cantidad >= 0:
                        Producto.disminuir_stock(cantidad)
                        print("Venta realizada.")
                    else:
                        print("Cantidad inválida.")
                except ValueError:
                    print("Entrada no válida.")
        elif opcion == "4":
            print("Cerrando el sistema de inventario.")
            break
        else:
            print("Opción no válida intenta nuevamente.")

#ejecutar menú
menu()