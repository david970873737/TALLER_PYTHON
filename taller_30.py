def menu():
  print("Menu")
  print("1.crear")
  print("2.ver")
  print("3.salir")
  opcion = input("opcion:")
  return opcion

def crear(opcion, circulos):
  if opcion == "1":
    r = float(input("ingrese radio:"))
    c = 2 * 3.1416 * r
    print("la circunferencia es:", c)
    circulos.append(c)
  elif opcion == "2":
    for i in circulos:
      print(i)

def main():
  circulos = []
  while True:
    opcion = menu()
    if opcion == "3":
      print("saliendo del programa")
      break
    crear(opcion, circulos)

main()
