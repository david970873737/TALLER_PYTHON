def menu():
  print("Menu")
  print("1.crear")
  print("2.ver")
  print("3.salir")
  opcion=input("opcion:")
  return opcion

def crear(opcion,esferas):
  if opcion=="1":
    radio = float(input("escribe el area de la esfera:"))
    area =(4/3) * 3.14 * radio**3
    print("el area de la esfera es:",area)
    esferas.append(area)

  elif opcion=="2":
    for area in esferas: 
      print(area)

def main():
  esferas = [] 
  while True:
    opcion=menu()
    if opcion=="3":
      print("saliendo del programa")
      break
    crear(opcion, esferas) 


llmar_menu= main()
