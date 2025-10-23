def menu():
  print("Menu")
  print("1.crear")
  print("2.ver")
  print("3.salir")
  opcion = input("opcion:")
  return opcion

def crear(opcion, raices):
  if opcion == "1":
    n = float(input("ingrese un número:"))
    if n >= 0:
      r = n ** 0.5
      print("la raíz cuadrada es:", r)
      raices.append(r)
    else:
      print("no existe raíz real para número negativo")
  elif opcion == "2":
    for i in raices:
      print(i)

def main():
  raices = []
  while True:
    opcion = menu()
    if opcion == "3":
      print("saliendo del programa")
      break
    crear(opcion, raices)

main()
