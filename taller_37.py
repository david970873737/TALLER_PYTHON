def menu():
  print("Menu")
  print("1.crear")
  print("2.ver")
  print("3.salir")
  opcion = input("opcion:")
  return opcion

def crear(opcion, mayores):
  if opcion == "1":
    n1 = float(input("ingrese primer número:"))
    n2 = float(input("ingrese segundo número:"))
    m = max(n1, n2)
    print("el número mayor es:", m)
    mayores.append(m)
  elif opcion == "2":
    for i in mayores:
      print(i)

def main():
  mayores = []
  while True:
    opcion = menu()
    if opcion == "3":
      print("saliendo del programa")
      break
    crear(opcion, mayores)

main()
