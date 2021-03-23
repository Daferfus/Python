#-----------------------------------------------------------------------------------------------------------
# Visibilidad
#-----------------------------------------------------------------------------------------------------------
# Definimos una clase Persona
class Persona:

  def __init__(self, n, e):
    self.nombre = n # público
    self.__edad = e # privado

  def mostrar(self): # público
    print("El nombre es ",self.nombre, " y la edad es ",self.__edad)

  def __mostrar(self): # privado
    print("El nombre es ",self.nombre, " y la edad es ",self.__edad)  

p = Persona("Juan", 25)
print("El nombre es "+p.nombre)
p.mostrar()

#Estos fallan
print("La edad es "+p.__edad)
p.__mostrar()
#-----------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------


#-----------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------
# Definimos una clase Persona
class Persona:

  def __init__(self, n, e):
    self.nombre = n 
    self.edad = e 

  def __str__(self): 
    return "El nombre es "+self.nombre+" y la edad es "+str(self.edad)

p = Persona("Juan", 25)
print("El nombre es "+p.nombre)
print(p)
#-----------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------