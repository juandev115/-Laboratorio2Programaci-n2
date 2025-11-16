#calcular el areas de las figuras geometricas
import math
#1.Cuadrado
def area_cuadrado(lado):
    """
    calcula el area de un cuadrado
    area= lado*lado
    param= lado:float
    return: float
    """
    area = lado**2
    return area
#2.Circulo
def area_circulo(radio):
    """
    calcula el area de un circulo
    area= pi*radio^2
    param= radio:float
    return: float
    """
    area = math.pi*(radio**2)
    return area
#3. Triangulo 
def area_triangulo(base, altura):
    """
    calcula el area de un triangulo
    area= (base*altura)/2
    param= base:float
    param= altura:float
    return: float
    """
    area= (base*altura)/2
    return area
#4.recatangulo
def area_rectangulo(base, altura):
    """
    calcula el ares de un recatangulo
    area= base * altura
    param= base: float
    patam= altura: float
    return: float
    """
    area= base*altura
    return area
#5. Rombo
def area_rombo(diagonal_mayor, diagonal_menor):
    """
    calcular el area de un rombo
    area= (diagonal_mayor*diagonal_menor)/2
    param= diagonal_mayor:float
    param= diagonal_menor:float
    return: float
    """
    area= (diagonal_mayor*diagonal_menor)/2
    return area
#6. trapecio
def area_trapecio(base_mayor, base_menor, altura):
    """
    calcuolar el area de un trapecio
    area= ((base_mayor+base_menor)*altura)/2
    param= base_mayor:float
    param= base_menor:float
    param= altura:float
    return: float
    """
    area= ((base_mayor+base_menor)*altura)/2
    return area
#7. pentagono
def area_pentagono(apotema, perimetro):
    """
    calcular el area de un pentagono
    area= (perimetro*apotema)/2
    param= apotema:float
    param= perimetro:float
    return:float
    """
    area= (perimetro*apotema)/2
    return area
#8. romboide
def area_romboide(base, altura):
    """
    calcular el area de un romboide
    area= base*altura
    param= base:float
    param= altura:float
    return: floa
    """
    area= base*altura
    return area