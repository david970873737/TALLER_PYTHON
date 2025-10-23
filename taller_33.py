def menu():
  print("Menu")
  print("1.crear")
  print("2.ver")
  print("3.salir")
  opcion = input("opcion:")
  return opcion

def crear(opcion, tiempos):
  if opcion == "1":
    h = float(input("ingrese horas:"))
    m = h * 60
    print("equivalen a", m, "minutos")
    tiempos.append(m)
  elif opcion == "2":
    for i in tiempos:
      print(i)

def main():
  tiempos = []
  while True:
    opcion = menu()
    if opcion == "3":
      print("saliendo del programa")
      break
    crear(opcion, tiempos)

main()
