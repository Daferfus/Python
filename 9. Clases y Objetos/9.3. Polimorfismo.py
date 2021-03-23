#-----------------------------------------------------------------------------------------------------------
# Polimorfismo
#-----------------------------------------------------------------------------------------------------------
class Figura:
  def __init__(self, tipo):
    self.tipo = tipo
    self.area = 0
    self.perimetro = 0

  def __str__(self):
    return "Figura: "+self.tipo+". Area: "+str(self.area)+" y perímetro: "+str(self.perimetro)+" \n"

class Circulo(Figura): 
  PI = 3.14 

  def __init__(self, radio):  
    super().__init__("Circulo")  
    self.radio = radio 
    self.area = self.PI * self.radio**2 
    self.perimetro = 2 * self.PI * self.radio

class Cuadrado(Figura): 

  def __init__(self, lado):  
    super().__init__("Cuadrado")   
    self.lado = lado
    self.area = self.lado * self.lado
    self.perimetro = self.lado *4

#-------------------- main --------------------

def mostrar_tipo(figura):# esta función se ejecuta igual para distintos tipos de objetos pasados (p.e. Circulo y Cuadrado)
  print("El tipo es "+figura.tipo)

c1 = Circulo(2)
mostrar_tipo(c1)
c2 = Cuadrado(2)
mostrar_tipo(c2)
#-----------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------


#-----------------------------------------------------------------------------------------------------------
# Polimorfismo en Funciones
#-----------------------------------------------------------------------------------------------------------
def mostrar_longitud(valor):
  print("La longitud es "+str(len(valor)))

palabra = "duck_typing"
mostrar_longitud(palabra)
lista = [5, 4, 7, 1]
mostrar_longitud(lista)
diccionario = {1: "Pepe", 2: "Paco", 3: "Marta"}
mostrar_longitud(diccionario)
#-----------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------