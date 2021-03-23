#-----------------------------------------------------------------------------------------------------------
# Importación y Uso de Módulos
#-----------------------------------------------------------------------------------------------------------
import math

x = 10
print("La raíz cuadrada de", x, "es", math.sqrt(x)

# help(math)
# help(math.factorial)
#-----------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------


#-----------------------------------------------------------------------------------------------------------
# Importación de Funciones
#-----------------------------------------------------------------------------------------------------------
from math import factorial

print(factorial(10))
#-----------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------


#-----------------------------------------------------------------------------------------------------------
# Renombrar Módulo
#-----------------------------------------------------------------------------------------------------------
from math import factorial as fac

print(fac(10))
#-----------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------


#-----------------------------------------------------------------------------------------------------------
# Importar Más de un Módulo
#-----------------------------------------------------------------------------------------------------------
from math import sin
from math import sin, cos # lo recomendable, según la guía de estilo, sería en dos líneas separadas
from math import *
#-----------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------