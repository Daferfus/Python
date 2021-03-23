#-----------------------------------------------------------------------------------------------------------
#                               Ejercicio 1
# ----------------------------------------------------------------------------------------------------------
# Crea una función llamada without_first_letter que dada una lista de palabras, 
# devuelva una nueva lista con la primera letra de cada palabra eliminada.
#-----------------------------------------------------------------------------------------------------------
from functools import reduce

def without_first_letter():
    lista_de_palabras = ["Ola", "k", "ase"]
    resultado = map(lambda palabra : palabra[-1], lista_de_palabras)
    return resultado
resultado = without_first_letter()
print(list(resultado))
#-----------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------


#-----------------------------------------------------------------------------------------------------------
#                               Ejercicio 2
# ----------------------------------------------------------------------------------------------------------
# Crea una función llamada get_minimum que dado una lista de números,
# devuelva el valor mínimo encontrado el dicho array.
#-----------------------------------------------------------------------------------------------------------
def get_minimum():
    lista_de_numeros = [6, 3, 7, 2]
    return min(lista_de_numeros)
valor_minimo = get_minimum()
print(valor_minimo)
#-----------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------


#-----------------------------------------------------------------------------------------------------------
#                               Ejercicio 3
# ----------------------------------------------------------------------------------------------------------
# Crea una función llamada every_element_greater_than que tome por parámetro 
# un número y una lista numérica y devuelva True si todos los elementos son mayores que el número 
# pasado por parámetro y False en caso contrario.
#-----------------------------------------------------------------------------------------------------------
def every_element_greater_than(numero, lista_numerica):
    es_mayor = False
    for numero_de_lista in lista_numerica:
        if numero > numero_de_lista:
            es_mayor = True
        else:
            es_mayor = False
    return es_mayor
numero = 6
lista_numerica = [1, 2, 3, 4]
resultado = every_element_greater_than(numero, lista_numerica)
print(resultado)
#-----------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------


#-----------------------------------------------------------------------------------------------------------
#                               Ejercicio 4
# ----------------------------------------------------------------------------------------------------------
# Crea una función llamada greater_than_average que tome un parámetro x de tipo numérico,
# y una lista llamada data_array. La función deberá devolver cierto en caso de que el valor x 
# sea mayor que la media de la lista, y falso en caso contrario.
#-----------------------------------------------------------------------------------------------------------
def greater_than_average(x, data_array):
    suma_total = reduce(lambda x, y : x + y, data_array)
    media = suma_total//len(data_array)
    if x > media:
        return True
    else:
        return False
x = 30
data_array = [20, 10, 25, 15]
resultado = greater_than_average(x, data_array)
print(resultado)
#-----------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------


#-----------------------------------------------------------------------------------------------------------
#                               Ejercicio 5
# ----------------------------------------------------------------------------------------------------------
# Crea una función llamada clean_list que tome una lista de nombres de usuarios 
# y una lista de nombres de usuarios baneados y devuelva una nueva lista con los usuarios no baneados.
#-----------------------------------------------------------------------------------------------------------
def clean_list(lista_de_nombres_de_usuarios, lista_de_nombres_de_usuarios_baneados):
    lista_de_usuarios_no_baneados = []
    for usuario in lista_de_nombres_de_usuarios:
        if usuario not in lista_de_nombres_de_usuarios_baneados:
            lista_de_usuarios_no_baneados.append(usuario)
    return lista_de_usuarios_no_baneados
lista_de_nombres_de_usuarios = ["Jaime", "Lloret", "Sandra", "Sendra"]
lista_de_nombres_de_usuarios_baneados = ["Jaime", "Lloret"]            
lista_de_usuarios_no_baneados = clean_list(lista_de_nombres_de_usuarios, lista_de_nombres_de_usuarios_baneados)
print(lista_de_usuarios_no_baneados) 
#-----------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------