def menu():
  print("Menu")
  print("1.crear")
  print("2.ver")
  print("3.salir")
  opcion=input("opcion:")
  return opcion

def crear(opcion,areas):
  if opcion=="1":
    radio=float(input("ingrese el radio:"))
    area=3.1416*radio**2
    print("el área del círculo es:",area)
    areas.append(area)
  elif opcion=="2":
    for a in areas:
      print(a)

def main():
  areas=[]
  while True:
    opcion=menu()
    if opcion=="3":
      print("saliendo del programa")
      break
    crear(opcion,areas)

main()
