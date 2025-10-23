def menu():
  print("Menu")
  print("1.crear")
  print("2.ver")
  print("3.salir")
  opcion = input("opcion:")
  return opcion

def crear(opcion, promedios):
  if opcion == "1":
    n1 = float(input("ingrese primer número:"))
    n2 = float(input("ingrese segundo número:"))
    p = (n1 + n2) / 2
    print("el promedio es:", p)
    promedios.append(p)
  elif opcion == "2":
    for i in promedios:
      print(i)

def main():
  promedios = []
  while True:
    opcion = menu()
    if opcion == "3":
      print("saliendo del programa")
      break
    crear(opcion, promedios)

main()
