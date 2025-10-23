def menu():
  print("Menu")
  print("1.crear")
  print("2.ver")
  print("3.salir")
  opcion=input("opcion:")
  return opcion

def crear(opcion, distancias):
  if opcion=="1":
    km=float(input("ingrese kilómetros:"))
    mi=km*0.621371
    print("equivalen a",mi,"millas")
    distancias.append(mi)
  elif opcion=="2":
    for i in distancias:
      print(i)

def main():
  distancias=[]
  while True:
    opcion=menu()
    if opcion=="3":
      print("saliendo del programa")
      break
    crear(opcion,distancias)

main()
