def menu():
  print("Menu")
  print("1.crear")
  print("2.ver")
  print("3.salir")
  opcion=input("opcion:")
  return opcion

def crear(opcion, piramides):
  if opcion=="1":
    l=float(input("ingrese longitud de la base:"))
    a=float(input("ingrese ancho de la base:"))
    h=float(input("ingrese altura:"))
    v=(l*a*h)/3
    print("el volumen de la pirámide es:",v)
    piramides.append(v)
  elif opcion=="2":
    for p in piramides:
      print(p)

def main():
  piramides=[]
  while True:
    opcion=menu()
    if opcion=="3":
      print("saliendo del programa")
      break
    crear(opcion,piramides)

main()
