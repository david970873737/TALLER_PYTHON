def menu():
  print("Menu")
  print("1.crear")
  print("2.ver")
  print("3.salir")
  opcion = input("opcion:")
  return opcion

def crear(opcion, cocientes):
  if opcion == "1":
    n1 = int(input("ingrese primer número:"))
    n2 = int(input("ingrese segundo número:"))
    if n2 != 0:
      c = n1 // n2
      print("el cociente entero es:", c)
      cocientes.append(c)
    else:
      print("no se puede dividir entre cero")
  elif opcion == "2":
    for i in cocientes:
      print(i)

def main():
  cocientes = []
  while True:
    opcion = menu()
    if opcion == "3":
      print("saliendo del programa")
      break
    crear(opcion, cocientes)

main()
