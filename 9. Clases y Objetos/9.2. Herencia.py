#-----------------------------------------------------------------------------------------------------------
# Herencia
#-----------------------------------------------------------------------------------------------------------
class Figura:
  def __init__(self, tipo):
    self.tipo = tipo
    self.area = 0
    self.perimetro = 0

  def __str__(self):
    return "Figura: "+self.tipo+". Area: "+str(self.area)+" y perímetro: "+str(self.perimetro)+" \n"

class Circulo(Figura): # definimos subclase de Figura
  PI = 3.14 

  def __init__(self, radio):
    super().__init__("circulo") # llamamos al inicializador de la clase principal
    self.radio = radio # atributo específico de la subclase
    self.area = self.PI * self.radio**2 
    self.perimetro = 2 * self.PI * self.radio

c = Circulo(3)
print(c) #__str__ se hereda de figura
#-----------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------


#-----------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------
class Figura:
  def __init__(self):# este método no recibe nada
    self.tipo = "default"
    self.area = 0
    self.perimetro = 0

  def __str__(self):
    return "Figura: "+self.tipo+". Area: "+str(self.area)+" y perímetro: "+str(self.perimetro)+" \n"

class Circulo(Figura): 
  PI = 3.14 

  def __init__(self, radio):    
    self.radio = radio 
    self.area = self.PI * self.radio**2 
    self.perimetro = 2 * self.PI * self.radio

  def __str__(self): # Sobreescribimos el método en la subclase
    return "Este círculo de radio "+ str(self.radio)+" tiene area: "+str(self.area)+" y perímetro: "+str(self.perimetro)+" \n"

c = Circulo(3)
print(c) #__str__ se ha sobreescrito en la subclase
#-----------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------


#-----------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------
class Figura:
  def __init__(self, tipo):
    self.tipo = tipo
    self.area = 0
    self.perimetro = 0

  def __str__(self):
    return "Figura: "+self.tipo+". Area: "+str(self.area)+" y perímetro: "+str(self.perimetro)+" \n"

class Circulo(Figura): # definimos subclase de Figura pero sin nada adicional
  pass

c = Circulo("circulo")
print(c)
#-----------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------