def menu():
  print("Menu")
  print("1.crear")
  print("2.ver")
  print("3.salir")
  opcion = input("opcion:")
  return opcion

def crear(opcion, cubos):
  if opcion == "1":
    l = float(input("ingrese la longitud del lado:"))
    v = l ** 3
    print("el volumen del cubo es:", v)
    cubos.append(v)
  elif opcion == "2":
    for i in cubos:
      print(i)

def main():
  cubos = []
  while True:
    opcion = menu()
    if opcion == "3":
      print("saliendo del programa")
      break
    crear(opcion, cubos)

main()
