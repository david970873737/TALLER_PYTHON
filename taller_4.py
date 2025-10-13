import math

def capturar_datos():
    radio = float(input("Ingrese el radio: "))
    return radio

def calcular_area(radio):
    return math.pi * (radio ** 2)

def mostrar_resultado(area):
    print("El área del círculo es:", area)

radio = capturar_datos()
area = calcular_area(radio)
mostrar_resultado(area)