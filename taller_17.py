def menu():
  print("Menu")
  print("1.crear")
  print("2.ver")
  print("3.salir")
  opcion = input("opcion:")
  return opcion

def crear(opcion, pesos):
  if opcion == "1":
    lb = float(input("ingrese libras:"))
    kg = lb * 0.453592
    print("equivalen a", kg, "kilogramos")
    pesos.append(kg)
  elif opcion == "2":
    for i in pesos:
      print(i)

def main():
  pesos = []
  while True:
    opcion = menu()
    if opcion == "3":
      print("saliendo del programa")
      break
    crear(opcion, pesos)

main()
