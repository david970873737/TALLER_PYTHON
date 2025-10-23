def menu():
  print("Menu")
  print("1.crear")
  print("2.ver")
  print("3.salir")
  opcion = input("opcion:")
  return opcion

def crear(opcion, sumas):
  if opcion == "1":
    n1 = float(input("ingrese primer número:"))
    n2 = float(input("ingrese segundo número:"))
    s = n1 + n2
    print("la suma es:", s)
    sumas.append(s)
  elif opcion == "2":
    for i in sumas:
      print(i)

def main():
  sumas = []
  while True:
    opcion = menu()
    if opcion == "3":
      print("saliendo del programa")
      break
    crear(opcion, sumas)

main()
