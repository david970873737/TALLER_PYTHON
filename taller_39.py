def menu():
  print("Menu")
  print("1.crear")
  print("2.ver")
  print("3.salir")
  opcion = input("opcion:")
  return opcion

def crear(opcion, descuentos):
  if opcion == "1":
    p = float(input("ingrese precio del artículo:"))
    d = p * 0.10
    total = p - d
    print("precio con descuento:", total)
    descuentos.append(total)
  elif opcion == "2":
    for i in descuentos:
      print(i)

def main():
  descuentos = []
  while True:
    opcion = menu()
    if opcion == "3":
      print("saliendo del programa")
      break
    crear(opcion, descuentos)

main()
