def menu():
  print("Menu")
  print("1.crear")
  print("2.ver")
  print("3.salir")
  opcion=input("opcion:")
  return opcion

def crear(opcion,rectangulos):
  if opcion=="1":
    altura = float(input("escribe la altura del rectangulo:"))
    ancho = float(input("escribe el ancho del rectangulo"))
    area = altura * ancho
    print("el area de la esfera es:",area)
    rectangulos.append(area)

  elif opcion=="2":
    for area in rectangulos: 
      print(area)

def main():
  rectangulos = [] 
  while True:
    opcion=menu()
    if opcion=="3":
      print("saliendo del programa")
      break
    crear(opcion, rectangulos) 


llmar_menu= main()
