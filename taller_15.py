def menu():
  print("Menu")
  print("1.crear")
  print("2.ver")
  print("3.salir")
  opcion = input("opcion:")
  return opcion

def crear(opcion, paralelogramos):
  if opcion == "1":
    b = float(input("ingrese la base:"))
    h = float(input("ingrese la altura:"))
    a = b * h
    print("el área del paralelogramo es:", a)
    paralelogramos.append(a)
  elif opcion == "2":
    for i in paralelogramos:
      print(i)

def main():
  paralelogramos = []
  while True:
    opcion = menu()
    if opcion == "3":
      print("saliendo del programa")
      break
    crear(opcion, paralelogramos)

main()
