def mostrar_elemento(lista, pos):
  try:
    print(lista[pos])
  except IndexError:
    print("La posición está fuera de rango")

#------------main-------------
lista = [4, 5, 1, 3]

print("inicio")

mostrar_elemento(lista,4)

print("fin")




def mostrar_elemento(lista, pos):
  if (pos >= 0 and pos < len(lista)) or (pos < 0 and abs(pos) <= len(lista)):
    print(lista[pos])
  else:
    raise IndexError("La posición está fuera de rango")

#------------main-------------
lista = [4, 5, 1, 3]

print("inicio")

try:
  mostrar_elemento(lista,-5)
except IndexError:
  print("La posición está fuera de rango")

print("fin")