#-----------------------------------------------------------------------------------------------------------
#                               Ejercicio 1
# ----------------------------------------------------------------------------------------------------------
# Crea una función llamada squares_greater que dada una lista de números, 
# devuelva una nueva lista con los cuadrados de aquellos números mayores que 10.
#-----------------------------------------------------------------------------------------------------------
def squares_greater(lista_de_numeros):
    lista_cuadratica = [i * i for i in lista_de_numeros]
    return lista_cuadratica
lista_de_numeros = [1, 2, 3, 4, 5]
lista_cuadratica = squares_greater(lista_de_numeros)
print(lista_cuadratica)
#-----------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------



#-----------------------------------------------------------------------------------------------------------
#                               Ejercicio 2
# ----------------------------------------------------------------------------------------------------------
# Crea una función llamada word_length que dada una lista de palabras, 
# devuelva una nueva lista con la longitud de cada una siempre y cuando la palabra no sea "el".
#-----------------------------------------------------------------------------------------------------------
def word_length(lista_de_palabras):
    lista_de_longitudes = [len(i) for i in lista_de_palabras if i!="el"]
    return lista_de_longitudes
lista_de_palabras = ["Ola", "k", "ase", "el", "mamon"]
lista_de_palabras = word_length(lista_de_palabras)
print(lista_de_palabras)
#-----------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------



#-----------------------------------------------------------------------------------------------------------
#                               Ejercicio 3
# ----------------------------------------------------------------------------------------------------------
# Crea una función llamada clean_list que tome una lista de nombres de usuarios 
# y una lista de nombres de usuarios baneados y devuelva una nueva lista con los usuarios no baneados.
#-----------------------------------------------------------------------------------------------------------
def clean_list(lista_de_nombres_de_usuarios, lista_de_nombres_de_usuarios_baneados):
    lista_de_usuarios_no_baneados = [usuario for usuario in lista_de_nombres_de_usuarios if usuario not in lista_de_nombres_de_usuarios_baneados]
    return lista_de_usuarios_no_baneados
lista_de_nombres_de_usuarios = ["Jaime", "Lloret", "Sandra", "Sendra"]
lista_de_nombres_de_usuarios_baneados = ["Jaime", "Lloret"]   
lista_de_usuarios_no_baneados = clean_list(lista_de_nombres_de_usuarios, lista_de_nombres_de_usuarios_baneados)
print(lista_de_usuarios_no_baneados)
#-----------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------