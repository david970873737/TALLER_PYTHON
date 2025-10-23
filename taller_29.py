def menu():
  print("Menu")
  print("1.crear")
  print("2.ver")
  print("3.salir")
  opcion = input("opcion:")
  return opcion

def crear(opcion, numeros):
  if opcion == "1":
    n = int(input("ingrese un número:"))
    if n % 2 == 0:
      print("el número es par")
      numeros.append("par")
    else:
      print("el número es impar")
      numeros.append("impar")
  elif opcion == "2":
    for i in numeros:
      print(i)

def main():
  numeros = []
  while True:
    opcion = menu()
    if opcion == "3":
      print("saliendo del programa")
      break
    crear(opcion, numeros)

main()
