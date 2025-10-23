def menu():
  print("Menu")
  print("1.crear")
  print("2.ver")
  print("3.salir")
  opcion=input("opcion:")
  return opcion

def crear(opcion,triangulos):
  if opcion=="1":
    base = float(input("escribe la base del triangulo:"))
    altura = float(input("escribe la altura del triangulo:"))
    area = (base*altura)/2
    print("el area del triangulo es:",area)
    triangulos.append(area)

  elif opcion=="2":
    for area in triangulos: 
      print(area)

def main():
  triangulos = [] 
  while True:
    opcion=menu()
    if opcion=="3":
      print("saliendo del programa")
      break
    crear(opcion, triangulos) )


llmar_menu= main()
