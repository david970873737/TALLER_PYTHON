def menu():
  print("Menu")
  print("1.crear")
  print("2.ver")
  print("3.salir")
  opcion = input("opcion:")
  return opcion

def crear(opcion, medidas):
  if opcion == "1":
    p = float(input("ingrese pulgadas:"))
    c = p * 2.54
    print("equivalen a", c, "centímetros")
    medidas.append(c)
  elif opcion == "2":
    for i in medidas:
      print(i)

def main():
  medidas = []
  while True:
    opcion = menu()
    if opcion == "3":
      print("saliendo del programa")
      break
    crear(opcion, medidas)

main()
