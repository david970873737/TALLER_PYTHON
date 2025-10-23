def menu():
  print("Menu")
  print("1.crear")
  print("2.ver")
  print("3.salir")
  opcion = input("opcion:")
  return opcion

def crear(opcion, intereses):
  if opcion == "1":
    c = float(input("ingrese cantidad de dinero:"))
    i = c * 0.05
    total = c + i
    print("el total con interés es:", total)
    intereses.append(total)
  elif opcion == "2":
    for i in intereses:
      print(i)

def main():
  intereses = []
  while True:
    opcion = menu()
    if opcion == "3":
      print("saliendo del programa")
      break
    crear(opcion, intereses)

main()
