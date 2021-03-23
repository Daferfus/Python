#-----------------------------------------------------------------------------------------------------------
# Acceso a Información Docstring
#-----------------------------------------------------------------------------------------------------------
import math

help(math.sqrt)

func = math.sqrt
print(func.__doc__)


#-----------------------------------------------------------------------------------------------------------
# Declaración de Docstring
#-----------------------------------------------------------------------------------------------------------
def funcion():
  '''Esta función devuelve True.'''
  return True

help(funcion)


#-----------------------------------------------------------------------------------------------------------
# Docstring para Funciones y Métodos
#-----------------------------------------------------------------------------------------------------------
def por3(valor):
  """ Esta función devuelve el número multiplicado por 3

  Args: 
    valor (int): El número que se recibe

  Returns:
    int: El número multiplicado por 3

  """

  return valor*3

help(por3)


#-----------------------------------------------------------------------------------------------------------
# Docstring para Clases
#-----------------------------------------------------------------------------------------------------------
class Persona:
  """
  Representación de una persona

  Attributes:
    nombre (str): El nombre de la persona
    apellido (str): El apellido de la persona
    edad (int): La edad de la persona
  
  Methods:
    mostrar_info(): Muestra los datos de la persona

  """

  def __init__(self, nombre, apellido, edad):
    """ Inicializa una persona con sus datos
    Args:
      nombre (str): El nombre de la persona
      apellido (str): El apellido de la persona
      edad (int): La edad de la persona
    """
    self.__nombre = nombre
    self.__apellido = apellido
    self.__edad = edad

  def mostrar_info(self):
    """ Muestra los datos de la persona
   
    """
    print("Hola, soy "+self.__nombre+" "+self.__apellido+" y tengo "+str(self.edad)+" años.")

help(Persona)


#-----------------------------------------------------------------------------------------------------------
# Docstring para Módulos
#-----------------------------------------------------------------------------------------------------------
"""
Este módulo incluya la definición para poder representar personas.

Classes:
  Persona

"""

class Persona:
  """
  Representación de una persona

  Attributes:
    nombre (str): El nombre de la persona
    apellido (str): El apellido de la persona
    edad (int): La edad de la persona
  
  Methods:
    mostrar_info(): Muestra los datos de la persona

  """

  def __init__(self, nombre, apellido, edad):
    """ Inicializa una persona con sus datos
    Args:
      nombre (str): El nombre de la persona
      apellido (str): El apellido de la persona
      edad (int): La edad de la persona
    """
    self.__nombre = nombre
    self.__apellido = apellido
    self.__edad = edad

  def mostrar_info(self):
    """ Muestra los datos de la persona
   
    """
    print("Hola, soy "+self.__nombre+" "+self.__apellido+" y tengo "+str(self.edad)+" años.")

import math

help(math)