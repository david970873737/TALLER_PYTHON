def menu():
  print("Menu")
  print("1.crear")
  print("2.ver")
  print("3.salir")
  opcion=input("opcion:")
  return opcion

def crear(opcion, trapecios):
  if opcion=="1":
    b1=float(input("ingrese base mayor:"))
    b2=float(input("ingrese base menor:"))
    h=float(input("ingrese altura:"))
    a=((b1+b2)*h)/2
    print("el área del trapecio es:",a)
    trapecios.append(a)
  elif opcion=="2":
    for i in trapecios:
      print(t)

def main():
  trapecios=[]
  while True:
    opcion=menu()
    if opcion=="3":
      print("saliendo del programa")
      break
    crear(opcion,trapecios)

main()
