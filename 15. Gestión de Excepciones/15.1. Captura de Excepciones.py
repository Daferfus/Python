lista = [4, 5, 1, 3]

print("inicio")

print(lista[4])

print("fin")



lista = [4, 5, 1, 3]

print("inicio")

try:
    print(lista[4])
except:
    print("se ha producido una excepción")

print("fin")



lista = [4, 5, 1, 3]

print("inicio")

try:
    print(lista[4])
except:
    print("se ha producido una excepción")
else:
    print("este fin se muestra si no se produce excepción")



 def mostrar_elemento():
  lista = [4, 5, 1, 3]

  print("inicio de la función")

  try:
    print(lista[4])
  except:
    print("se ha producido una excepción")
    return -1
  else:
    print("este fin se muestra si no se produce excepción")
  finally:
    print("el código del finally se ejecuta siempre")
  
  print("fin de la función")
  return 1

#------------main-------------

mostrar_elemento()