
def tomar_altura():
  altura = int(input("toma la altura del triangulo: "))
  return altura

def tomar_base():
  base = int(input("toma la base del triangulo : "))
  return base

def calcular_area(altura,base):
  area = (altura*base)/2
  return area

altura = tomar_altura()
base = tomar_base()
area = calcular_area(altura, base)
print(area)
