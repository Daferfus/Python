#-----------------------------------------------------------------------------------------------------------
# Iteradores
#-----------------------------------------------------------------------------------------------------------
# recorremos un string
palabra = "hola"
for i in palabra:
  print(i)

# recorremos una lista
lista = [2, 5, 8, 0, 11]
for i in lista:
  print(i)

# recorremos un diccionario
dic = {123: "Juan", 456: "Maria", 789: "Pedro"}
for i in dic:
  print(i)

lista = [2, 5, 8, 0, 11]

# obtenemos un iterator sobre la lista
iterador = iter(lista)

# utilizamos next cada vez que queremos el siguiente dato del iterador
print("Ahora me hace falta un dato")
print(next(iterador))
print("Ahora me hace falta otro")
print(next(iterador))
print("Ahora otro")
print(next(iterador))
#-----------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------


#-----------------------------------------------------------------------------------------------------------
# Generador
#-----------------------------------------------------------------------------------------------------------
# Función generadora de números pares
def numeros():
  print("NUMEROS: inicio de la función")
  i = 0
  # bucle infinito  
  while True:
    print("NUMEROS: antes del yield")
    yield i
    print("NUMEROS: después del yield")
    i+=2

# La función generadora nos devuelve un generador
generador = numeros()
print("Después de llamar a la función y obtener el generador")

# utilizamos next cada vez que queremos generar un nuevo dato
print("Ahora me hace falta un dato")
print(next(generador))
print("Ahora me hace falta otro")
print(next(generador))
print("Ahora otro")
print(next(generador))


# Función generadora de números pares
def numeros():
  for n in range(10):
    if n % 2 == 0:
      yield n

# La función generadora nos devuelve un generador
generador = numeros()

print(next(generador))
print(next(generador))
print(next(generador))


# Función generadora de números pares
def numeros():
  for n in range(10):
    if n % 2 == 0:
      yield n

# La función generadora nos devuelve un generador
generador = numeros()

# Recorremos el generador
for i in generador:
  print(i)
#----------------------------------------------------------------------------------------------------------- 
#-----------------------------------------------------------------------------------------------------------