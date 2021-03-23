#-----------------------------------------------------------------------------------------------------------
#                               Ejercicio 1
# ----------------------------------------------------------------------------------------------------------
# Escribe una función generadora de la secuencia de Fibonacci y comprueba su correcto funcionamiento. 
# Los valores de esta secuencia se calculan siguiendo la siguiente fórmula:
# F0=0 
# F1=0 
# Fn=Fn−1+Fn−1∀n>1
#-----------------------------------------------------------------------------------------------------------
def f(n):
    a, b = 0, 1
    for i in range(0, n):
        a, b = b, a + b
        yield a
    return a

generador = f(10)
print(next(generador))
print(next(generador))
print(next(generador))
print(next(generador))
print(next(generador))
#----------------------------------------------------------------------------------------------------------- 
#-----------------------------------------------------------------------------------------------------------



#-----------------------------------------------------------------------------------------------------------
#                               Ejercicio 2
# ----------------------------------------------------------------------------------------------------------
# Implementa la siguiente función generadora:
# def suma_tiempos(inicio, fin, incremento):
#    """Función que devuelve tuplas de tiempo (hh,mm,ss) desde una hora inicial hasta una hora final 
#    Args: inicio (hh,mm,ss), fin (hh,mm,ss), incremento (segundos)
#    Returns: hora (hh,mm,ss)
#    """
#-----------------------------------------------------------------------------------------------------------
def suma_tiempos(inicio, fin, incremento):
    """Función que devuelve tuplas de tiempo (hh,mm,ss) desde una hora inicial hasta una hora final 
    Args: inicio (hh,mm,ss), fin (hh,mm,ss), incremento (segundos)
    Returns: hora (hh,mm,ss)
    """
    segundos_iniciales = inicio[2]
    minutos_iniciales = inicio[1]
    horas_iniciales = inicio[0]

    diferencia_horas = fin[0]-inicio[0]
    diferencia_minutos = fin[1]-inicio[1]
    diferencia_segundos = fin[2]-inicio[2]

    while horas_iniciales!=fin[0] and minutos_iniciales!=fin[1] and segundos_iniciales!=fin[0]:
        if segundos_iniciales>=60:
            minutos_iniciales+=1
            segundos_iniciales=segundos_iniciales - 60
        elif minutos_iniciales>=60:
            horas_iniciales+=1
            minutos_iniciales=minutos_iniciales - 60
        elif segundos_iniciales>fin[0] and (minutos_iniciales>fin[1] or horas_iniciales>fin[2]):
            segundos_iniciales
        segundos_iniciales+=incremento
        yield incremento
    
inicio = (00,00,00)
fin = (00,10,00)
incremento = 2
generador = suma_tiempos(inicio, fin, incremento)
print(next(generador))
print(next(generador))
print(next(generador))
print(next(generador))
print(next(generador))
#----------------------------------------------------------------------------------------------------------- 
#-----------------------------------------------------------------------------------------------------------