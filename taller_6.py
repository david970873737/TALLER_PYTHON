def menu():
  print("Menu")
  print("1.crear")
  print("2.ver")
  print("3.salir")
  opcion=input("opcion:")
  return opcion

def crear(opcion,conos):
  if opcion=="1":
    radio=float(input("ingrese el radio:"))
    altura=float(input("ingrese la altura:"))
    volumen=(1/3)*3.1416*radio**2*altura
    print("el volumen del cono es:",volumen)
    conos.append(volumen)
  elif opcion=="2":
    for c in conos:
      print(c)

def main():
  conos=[]
  while True:
    opcion=menu()
    if opcion=="3":
      print("saliendo del programa")
      break
    crear(opcion,conos)

main()
