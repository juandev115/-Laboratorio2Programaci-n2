#importar funciones de script
from Interfaz import(
    menu,
    solicitar_datos_cuadrado,
    solicitar_datos_circulo,
    solicitar_datos_triangulo,
    solicitar_datos_rectamgulo,
    solicitar_datos_rombo,
    solicitar_datos_trapecio,
    solicitar_datos_pentagono,
    solicitar_datos_romboide,
    mostrar_area_cuadrado,
    mostrar_area_circulo,
    mostrar_area_triangulo,
    mostrar_area_rectangulo,
    mostrar_area_rombo,
    mostrar_area_trapecio,
    mostrar_area_pentagono,
    mostrar_area_romboide
)
from Figuras import(
    area_cuadrado,
    area_circulo,
    area_triangulo,
    area_rectangulo,
    area_rombo,
    area_trapecio,
    area_pentagono,
    area_romboide
)

#variables
CUADRADO = 1
CIRCULO = 2
TRIANGULO = 3
RECTANGULO = 4
ROMBO = 5
TRAPECIO = 6
PENTAGONO = 7
ROMBOIDE = 8
SALIR = 9 

#inicializar variable de opcion 
op = 0

#estructura while
while op != SALIR:
    #mostrar menu
    op = menu()
    #seleccionar figura
    if op == CUADRADO:
        #solicitar datos
        lado = solicitar_datos_cuadrado()
        #calcular area
        area= area_cuadrado(lado)
        #mostrar resultado
        mostrar_area_cuadrado(area)
    elif op == CIRCULO:
        #solicitar datos
        radio = solicitar_datos_circulo()
        #calcular area
        area= area_circulo(radio)
        #mostrar resultado
        mostrar_area_circulo(area)
    elif op == TRIANGULO:
        #solicitar datos
        base, altura = solicitar_datos_triangulo()
        #calcular area
        area= area_triangulo(base, altura)
        #mostrar resultado
        mostrar_area_triangulo(area)
    elif op == RECTANGULO:
        #solicitar datos 
        base, altura = solicitar_datos_rectamgulo()
        #calcular area
        area= area_rectangulo(base, altura)
        #mostrar resultado
        mostrar_area_rectangulo(area)
    elif op == ROMBO:
        #solicitar datos
        diagonal_mayor, diagonal_menor = solicitar_datos_rombo()
        #calcular area 
        area= area_rombo(diagonal_mayor, diagonal_menor)
        #mostrar resultado
        mostrar_area_rombo(area)
    elif op == TRAPECIO:
        #solicitar datos
        base_mayor, base_menor, altura = solicitar_datos_trapecio()
        #calcular area
        area= area_trapecio(base_mayor,base_menor, altura)
        #mostrar resultado
        mostrar_area_trapecio(area)
    elif op == PENTAGONO:
        #solicitar datos
        lado = solicitar_datos_pentagono()
        #calcular area
        area= area_pentagono(lado)
        #mostrar resultado
        mostrar_area_pentagono(area)
    elif op == ROMBOIDE:
        #solicitar datos
        base, altura = solicitar_datos_romboide()
        #calcular area
        area= area_romboide(base, altura)
        #mostrar resultado
        mostrar_area_romboide(area)
    elif op == SALIR:
        print("Gracias por utilizar la calculadora de figuras geometricas!!!")
    else:
        print("Opcion no valida!!!")