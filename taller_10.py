def menu():
  print("Menu")
  print("1.crear")
  print("2.ver")
  print("3.salir")
  opcion=input("opcion:")
  return opcion

def crear(opcion, prismas):
  if opcion=="1":
    l=float(input("ingrese longitud:"))
    a=float(input("ingrese ancho:"))
    h=float(input("ingrese altura:"))
    v=l*a*h
    print("el volumen del prisma es:",v)
    prismas.append(v)
  elif opcion=="2":
    for p in prismas:
      print(p)

def main():
  prismas=[]
  while True:
    opcion=menu()
    if opcion=="3":
      print("saliendo del programa")
      break
    crear(opcion,prismas)

main()
