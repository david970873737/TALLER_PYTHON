def menu():
  print("Menu")
  print("1.crear")
  print("2.ver")
  print("3.salir")
  opcion=input("opcion:")
  return opcion

def crear(opcion,grados):
  if opcion=="1":
    c=float(input("ingrese grados Celsius:"))
    f=(c*9/5)+32
    print("equivalen a",f,"°F")
    grados.append(f)
  elif opcion=="2":
    for g in grados:
      print(g)

def main():
  grados=[]
  while True:
    opcion=menu()
    if opcion=="3":
      print("saliendo del programa")
      break
    crear(opcion,grados)

main()
