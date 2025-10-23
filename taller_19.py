def menu():
  print("Menu")
  print("1.crear")
  print("2.ver")
  print("3.salir")
  opcion = input("opcion:")
  return opcion

def crear(opcion, prismas):
  if opcion == "1":
    b = float(input("ingrese la base del triángulo:"))
    h = float(input("ingrese la altura del triángulo:"))
    l = float(input("ingrese la longitud del prisma:"))
    v = (b * h / 2) * l
    print("el volumen del prisma triangular es:", v)
    prismas.append(v)
  elif opcion == "2":
    for i in prismas:
      print(i)

def main():
  prismas = []
  while True:
    opcion = menu()
    if opcion == "3":
      print("saliendo del programa")
      break
    crear(opcion, prismas)

main()
