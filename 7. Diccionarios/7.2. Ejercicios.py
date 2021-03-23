#-----------------------------------------------------------------------------------------------------------
#                               Ejercicio 1
# ----------------------------------------------------------------------------------------------------------
# Escribe una función que reciba dos diccionarios con claves de tipo string y valores de tipo numérico,
# y que devuelva un nuevo diccionario que contenga los dos anteriores. Muestra el resultado por pantalla.
#-----------------------------------------------------------------------------------------------------------
def nuevo_diccionario(diccionario1, diccionario2):
    diccionario3 = dict()
    diccionario3.update(diccionario1)
    diccionario3.update(diccionario2)
    return diccionario3
diccionario1 = {"A": 10, "B": 2, "C": 20, "D": 40}
diccionario2 = {"E": 30, "F": 90, "G": 40, "H": 80}
nuevo_diccionario = nuevo_diccionario(diccionario1, diccionario2)
print(nuevo_diccionario)



#-----------------------------------------------------------------------------------------------------------
#                               Ejercicio 2
# ----------------------------------------------------------------------------------------------------------
# Escribe una función que reciba un diccionario y una lista de palabras. 
# La función debe devolver un nuevo diccionario con los items cuyas claves correspondan a cada una de las 
# palabras de la lista. Muestra el resultado por pantalla.
#-----------------------------------------------------------------------------------------------------------
def crear_diccionario(diccionario, tupla):
    nuevo_diccionario = {i : diccionario[i] for i in diccionario.keys() if i in tupla}
    return nuevo_diccionario
diccionario = {"A": 10, "B": 2, "C": 20, "D": 40}
tupla = ("A", "D")
diccionario_remasterizado = crear_diccionario(diccionario, tupla)
print(diccionario_remasterizado)
#-----------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------



#-----------------------------------------------------------------------------------------------------------
#                               Ejercicio 3
# ----------------------------------------------------------------------------------------------------------
# Escribe una función que reciba un diccionario de valores numéricos y devuelva el valor mínimo 
# de este diccionario. Muestra el resultado por pantalla.
#-----------------------------------------------------------------------------------------------------------
diccionario = {"A": 10, "B": 2, "C": 20, "D": 40}
clave_valor_minimo = min(diccionario, key=diccionario.get)
print(diccionario[clave_valor_minimo])
#-----------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------



#-----------------------------------------------------------------------------------------------------------
#                               Ejercicio 4
# ----------------------------------------------------------------------------------------------------------
# Escribe un programa que lea un texto por teclado. 
# Posteriormente debe crear un diccionario donde las claves sean las palabras del texto y sus valores 
# el número de apariciones de cada una de éstas en el texto. Muestra el resultado por pantalla.
#-----------------------------------------------------------------------------------------------------------
texto_introducido = str(input("Introduce un texto: "))
texto_separado = texto_introducido.split(" ")
diccionario = dict()
print(texto_separado)
for palabra in texto_separado:
    diccionario[palabra] =  len(palabra)
print(diccionario)
#-----------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------



#-----------------------------------------------------------------------------------------------------------
#                               Ejercicio 5
# ----------------------------------------------------------------------------------------------------------
# Escribe una función que reciba el siguiente diccionario y cuente la cantidad de items 
# que tienen True el campo success. Diccionario:
#-----------------------------------------------------------------------------------------------------------
dic = {
 1 : {'id': 1, 
 'success': True, 
 'name': 'Lary'
 }, 
 2 : {'id': 2, 
 'success': False, 
 'name': 'Rabi'
 }, 
 3 : {'id': 3, 
 'success': True, 
 'name': 'Alex'
 }
}
def comprobar_exito(dic):
    i = 0
    contador = 0
    for diccionario in dic:
        if dic[diccionario]["success"]:
            contador += 1
    return contador
contador_exitos = comprobar_exito(dic)
print(contador_exitos)
#-----------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------