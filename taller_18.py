def menu():
  print("Menu")
  print("1.crear")
  print("2.ver")
  print("3.salir")
  opcion = input("opcion:")
  return opcion

def crear(opcion, hexagonos):
  if opcion == "1":
    l = float(input("ingrese el lado del hexágono:"))
    a = (3 * (3 ** 0.5) * (l ** 2)) / 2
    print("el área del hexágono es:", a)
    hexagonos.append(a)
  elif opcion == "2":
    for i in hexagonos:
      print(i)

def main():
  hexagonos = []
  while True:
    opcion = menu()
    if opcion == "3":
      print("saliendo del programa")
      break
    crear(opcion, hexagonos)

main()
