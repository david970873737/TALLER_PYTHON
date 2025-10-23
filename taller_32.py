def menu():
  print("Menu")
  print("1.crear")
  print("2.ver")
  print("3.salir")
  opcion = input("opcion:")
  return opcion

def crear(opcion, triangulos):
  if opcion == "1":
    b = float(input("ingrese base:"))
    h = float(input("ingrese altura:"))
    a = (b * h) / 2
    print("el área del triángulo es:", a)
    triangulos.append(a)
  elif opcion == "2":
    for i in triangulos:
      print(i)

def main():
  triangulos = []
  while True:
    opcion = menu()
    if opcion == "3":
      print("saliendo del programa")
      break
    crear(opcion, triangulos)

main()
