def menu():
  print("Menu")
  print("1.crear")
  print("2.ver")
  print("3.salir")
  opcion=input("opcion:")
  return opcion

def crear(opcion, conversiones):
  if opcion=="1":
    d=float(input("ingrese cantidad en dólares:"))
    t=float(input("ingrese tasa de cambio a euros:"))
    e=d*t
    print("equivalen a",e,"euros")
    conversiones.append(e)
  elif opcion=="2":
    for i in conversiones:
      print(x)

def main():
  conversiones=[]
  while True:
    opcion=menu()
    if opcion=="3":
      print("saliendo del programa")
      break
    crear(opcion,conversiones)

main()
