#-----------------------------------------------------------------------------------------------------------
# Lambda Estándar
#-----------------------------------------------------------------------------------------------------------
'''Un ejemplo de uso de este tipo de funciones es cuando todo lo que queremos que haga la función 
es una simple línea.'''
res = lambda x, y : x * y
print(res(5, 2))

def multiplica(x, y):
  return x * y

print(multiplica(5, 2))
#-----------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------


#-----------------------------------------------------------------------------------------------------------
# Lambda con Map, Filter y Reduce
#-----------------------------------------------------------------------------------------------------------
# Ejemplo de map
nombres = ["Pepe", "ana", "juan", "Toni"]
resultado = map(lambda s : s.lower(), nombres)
print(list(resultado)) 

# Ejemplo de filter
nombres = ["Pepe", "ana", "juan", "Toni"]
resultado = filter(lambda s: len(s) > 3, nombres)
print(list(resultado)) 

# Ejemplo de reduce
from functools import reduce
lista = [2, 5, 7, 3]
print(reduce(lambda x, y : x + y, lista))
#-----------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------