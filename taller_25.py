def menu():
  print("Menu")
  print("1.crear")
  print("2.ver")
  print("3.salir")
  opcion = input("opcion:")
  return opcion

def crear(opcion, divisiones):
  if opcion == "1":
    n1 = float(input("ingrese primer número:"))
    n2 = float(input("ingrese segundo número:"))
    if n2 != 0:
      d = n1 / n2
      print("la división es:", d)
      divisiones.append(d)
    else:
      print("no se puede dividir entre cero")
  elif opcion == "2":
    for i in divisiones:
      print(i)

def main():
  divisiones = []
  while True:
    opcion = menu()
    if opcion == "3":
      print("saliendo del programa")
      break
    crear(opcion, divisiones)

main()
