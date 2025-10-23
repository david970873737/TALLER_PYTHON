def menu():
  print("Menu")
  print("1.crear")
  print("2.ver")
  print("3.salir")
  opcion = input("opcion:")
  return opcion

def crear(opcion, volumenes):
  if opcion == "1":
    l = float(input("ingrese litros:"))
    g = l * 0.264172
    print("equivalen a", g, "galones")
    volumenes.append(g)
  elif opcion == "2":
    for i in volumenes:
      print(i)

def main():
  volumenes = []
  while True:
    opcion = menu()
    if opcion == "3":
      print("saliendo del programa")
      break
    crear(opcion, volumenes)

main()
