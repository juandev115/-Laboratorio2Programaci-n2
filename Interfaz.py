#solicita y muestra informacion
#menu
def menu():
    """
    muestra el menu de opciones
    
    """
    print("bienvenido a la calculadora de figuras geometricas")
    print("selcione una figura para calcular su area: ")
    print("1. cuadrado")
    print("2. circulo")
    print("3. triangulo")
    print("4. rectangulo")
    print("5. rombo")
    print("6. trapecio")
    print("7. pentangono")
    print("8. romboide")
    print("9.. salir")
    op=int(input("selecione una opcion: "))
    return op

#solicitar datos cuadrado
def solicitar_datos_cuadrado():
    """
    solicitar el lado de un cuadrado
    return:float
    
    """
    lado=float(input("ingrese el lado del cuadrado: "))
    return lado
#solicitar datos circulo
def solicitar_datos_circulo():
    """
    solicitar el radio de un circulo
    return:float
    
    """
    radio=float(input("ingrese el radio del circulo: "))
    return radio
#solicitar datos triangulo
def solicitar_datos_triangulo():
    """
    solicitar la base y altura de un triangulo
    return:float,float
    
    """
    base=float(input("ingrese la base del triangulo: "))
    altura=float(input("ingrese la altura del triangulo: "))
    return base,altura
#solicitar datos rectangulo
def solicitar_datos_rectamgulo():
    """
    solicitar la base y altura de un rectangulo
    return:float,float
    
    """
    basse=float(input("ingrese la base del rectangulo:"))
    altura=float(input("ingrese la altura del rectangulo:"))
    return basse,altura
#solicitar datos rombo
def solicitar_datos_rombo():
    """
    solicitar la diagonal mayor y menor de un rombo
    return:float,float
    
    """
    diagonal_mayor=float(input("ingrese la diagonal mayor del rombo: "))
    diagonal_menor=float(input("ingrese la diagonal menor del rombo: "))
    return diagonal_mayor,diagonal_menor
#solicitar datos trapecio
def solicitar_datos_trapecio():
    """
    solicitar la base mayor, menor y altura de un trapecio
    return:float,float,float
    
    """
    base_mayor=float(input("ingrese la base mayor del trapecio: "))
    base_menor=float(input("ingrese la base menor del trapecio: "))
    altura=float(input("ingrese la altura del trapecio: "))
    return base_mayor,base_menor,altura
#solicitar datos pentagono
def solicitar_datos_pentagono():
    """
    solicitar el lado y apotema de un pentagono
    return:float,float
    
    """
    lado=float(input("ingrese el lado del pentagono: "))
    apotema=float(input("ingrese el apotema del pentagono: "))
    return lado,apotema
#solicitar datos romboide
def solicitar_datos_romboide():
    """
    solicitar la base y altura de un rombaide
    return:float,float
    
    """
    base=float(input("ingrese la base del romboide: "))
    altura=float(input("ingrese la altura del romboide: "))
    return base,altura

#mostrar area del cuadrado
def mostrar_area_cuadrado(area):
    """
    muestra el area de un cuadrado
    param:float
    
    """
    print(f"el area del cuadrado es: {area}")
#mostrar area del circulo
def mostrar_area_circulo(area):
    """
    muestra el area de un circulo
    param:float
    
    """
    print(f"el area del circulo es: {area}")
#mostrar area del triamgulo
def mostrar_area_triangulo(area):
    """
    muestra el area de un triamgulo
    param:float
    
    """
    print(f"el area del triangulo es: {area}")
#mostrat area del rectamgulo
def mostrar_area_rectangulo(area):
    """
    muestra el area de un rectangulo
    param:float
    
    """
    print(f"el area del rectangulo es: {area}")
#mostrar area del rombo
def mostrar_area_rombo(area):
    """
    muestra el area de un rombo
    param:float
    
    """
    print(f"el area del rombo es: {area}")
#mostrar area del trapecio
def mostrar_area_trapecio(area):
    """
    muestra el area de un trapecio
    param:float
    
    """
    print(f"el area del trapecio es: {area}")
#mostrar area del pentagono
def mostrar_area_pentagono(area):
    """
    muestra el area de un pentagono
    param:float
    
    """
    print(f"el area del pentagono es: {area}")
#mostrar area del romboide
def mostrar_area_romboide(area):
    """
    muestra el area de un romboide
    param:float
    
    """
    print(f"el area del romboide es: {area}")

