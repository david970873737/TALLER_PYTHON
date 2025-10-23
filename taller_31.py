def menu():
  print("Menu")
  print("1.crear")
  print("2.ver")
  print("3.salir")
  opcion = input("opcion:")
  return opcion

def crear(opcion, rectangulos):
  if opcion == "1":
    l = float(input("ingrese longitud:"))
    a = float(input("ingrese ancho:"))
    ar = l * a
    print("el área del rectángulo es:", ar)
    rectangulos.append(ar)
  elif opcion == "2":
    for i in rectangulos:
      print(i)

def main():
  rectangulos = []
  while True:
    opcion = menu()
    if opcion == "3":
      print("saliendo del programa")
      break
    crear(opcion, rectangulos)

main()
