#-----------------------------------------------------------------------------------------------------------
# Map
#-----------------------------------------------------------------------------------------------------------
''' La función map se encarga de aplicar una función a cada uno de los items de una lista, 
sin modificar la lista original.'''
def minusculas(s):
  """
  Args: s (string)
  Returns: string
  """
  return s.lower()

#------------main-------------
nombres = ["Pepe", "ana", "juan", "Toni"]
resultado = map(minusculas, nombres)
print(list(resultado)) #convertimos el resultado a una lista
#-----------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------


#-----------------------------------------------------------------------------------------------------------
# Filter
#-----------------------------------------------------------------------------------------------------------
''' La función filter se encarga de crear una nueva lista con los elementos de una lista original 
que cumplen una cierta condición'''
def longitud_mayor_que_3(s):
  """
  Args: s (string)
  Returns: bool
  """
  if len(s) > 3:
    return True
  return False

#------------main-------------
nombres = ["Pepe", "ana", "juan", "Toni"]
resultado = filter(longitud_mayor_que_3, nombres)
print(list(resultado)) 

#Es código sería equivalente:
#def longitud_mayor_que_3(s):
#  return len(s) > 3
#-----------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------


#-----------------------------------------------------------------------------------------------------------
# Reduce
#-----------------------------------------------------------------------------------------------------------
'''La función reduce llama a una función con los dos primeros items de una lista.
Esta función devuelve un valor, que se utiliza para llamar de nuevo a la función 
junto con el tercer item, y así, hasta terminar la secuencia de elementos.'''
from functools import reduce

def suma(x, y):
  """
  Args: x (int), y (int)
  Returns: int
  """
  return x + y

#------------main-------------
lista = [2, 5, 7, 3]
print(reduce(suma, lista))

lista = [2, 5, 7, 3]
print(reduce(suma, lista, 0)) #en este caso, pasamos un primer valor inicial
#-----------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------