def menu():
  print("Menu")
  print("1.crear")
  print("2.ver")
  print("3.salir")
  opcion=input("opcion:")
  return opcion

def crear(opcion, cuadrados):
  if opcion=="1":
    l=float(input("ingrese el lado del cuadrado:"))
    a=l*l
    print("el área del cuadrado es:",a)
    cuadrados.append(a)
  elif opcion=="2":
    for i in cuadrados:
      print(i)

def main():
  cuadrados=[]
  while True:
    opcion=menu()
    if opcion=="3":
      print("saliendo del programa")
      break
    crear(opcion,cuadrados)

main()
