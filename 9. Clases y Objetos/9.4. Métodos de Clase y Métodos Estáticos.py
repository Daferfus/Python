#-----------------------------------------------------------------------------------------------------------
# Métodos de Clase y Estáticos
#-----------------------------------------------------------------------------------------------------------
from datetime import date

class ClaseEjemplo:
  def __init__(self, nombre, edad):
    self.n = nombre
    self.e = edad

  def metodo_instancia(self):
    print("El nombre es "+self.n)

  @classmethod
  def metodo_clase(cls, nombre, anyo):
    return cls(nombre, date.today().year - anyo)

  @staticmethod
  def metodo_estatico(base, altura):
    print("Este metodo es estático y sirve para alguna funcionalidad que no dependa de ningún objeto en si")
    area = base * altura
    return area

p1 = ClaseEjemplo("Pepe", 20)
p1.metodo_instancia()

p2 = ClaseEjemplo("Ana", 25)
p2.metodo_instancia()
print(type(p2))

p3 = ClaseEjemplo.metodo_clase("Manolo", 30)
p3.metodo_instancia()
print(type(p3))

res = ClaseEjemplo.metodo_estatico(5, 3)
print(res)
#-----------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------