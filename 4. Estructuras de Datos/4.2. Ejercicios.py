#-----------------------------------------------------------------------------------------------------------
#                               Ejercicio 1
# ----------------------------------------------------------------------------------------------------------
# Escribe un programa que, dado un string y un valor "n" no negativo, muestre por pantalla el string 
# repetido "n" veces.
#-----------------------------------------------------------------------------------------------------------
cadena_de_texto = "Ola k ase"
valor_n_no_negativo = 10

while valor_n_no_negativo > 0:
    print(cadena_de_texto)
    valor_n_no_negativo-=1
#-----------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------



#-----------------------------------------------------------------------------------------------------------
#                               Ejercicio 2
# ----------------------------------------------------------------------------------------------------------
# Escribe un programa que, dado un string y un valor "n" no negativo, muestre por pantalla el string 
# repetido "n" veces.
#-----------------------------------------------------------------------------------------------------------
cadena_de_texto = "Ola k ase"
valor_n_no_negativo = 10

if len(cadena_de_texto) >= 3:
    while valor_n_no_negativo > 0:
        print(cadena_de_texto[:3])
        valor_n_no_negativo-=1
else:
    print("El mensaje es demasiado corto")
#-----------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------



#-----------------------------------------------------------------------------------------------------------
#                               Ejercicio 3
# ----------------------------------------------------------------------------------------------------------
# Dado un string, muestra por pantalla un nuevo string que sea 3 copias de los últimos dos 
# caracteres del string original. Lo longitud mínima del string será de 2, si no, el programa mostrará 
# un mensaje y terminará.
#-----------------------------------------------------------------------------------------------------------
cadena_de_texto = "Cara al Sol y con la Camisa Nueva"
if len(cadena_de_texto) >= 2:
    nueva_cadena_de_texto = cadena_de_texto[-2:] + cadena_de_texto[-2:] + cadena_de_texto[-2:]
    print(nueva_cadena_de_texto) 
else:
    print("El mensaje es demasiado corto")
#-----------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------



#-----------------------------------------------------------------------------------------------------------
#                               Ejercicio 4
# ----------------------------------------------------------------------------------------------------------
# Dado un string, muestra por pantalla un nuevo string que tenga los dos últimos caracteres movidos 
# al inicio. La longitud mínima del string será de 2.
#-----------------------------------------------------------------------------------------------------------
cadena_de_texto = "Hello... It is me you're looking for..."
print("{0}Hello... It is me you're looking for...".format(cadena_de_texto[-2:]))
#-----------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------



#-----------------------------------------------------------------------------------------------------------
#                               Ejercicio 5
# ----------------------------------------------------------------------------------------------------------
# Dado un string, muestra por pantalla un nuevo string que sea el original, repitiendo cada caracter
# dos veces.
#-----------------------------------------------------------------------------------------------------------
cadena_de_texto = "This is the Night"
for letra in cadena_de_texto:
    intentos = 2
    while intentos>0:
        print(letra)
        intentos-=1
#-----------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------



#-----------------------------------------------------------------------------------------------------------
#                               Ejercicio 6
# ----------------------------------------------------------------------------------------------------------
# Dados dos strings, muestra por pantalla la cantidad de veces que el segundo string aparece 
# en el primero.
#-----------------------------------------------------------------------------------------------------------
cadena_de_texto = "You're to Slow"
cadena_de_texto_2 = "Slow"
repeticiones = cadena_de_texto.count(cadena_de_texto_2)
print("La palabra se repite " + str(repeticiones) + " veces")
#-----------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------



#-----------------------------------------------------------------------------------------------------------
#                               Ejercicio 7
# ----------------------------------------------------------------------------------------------------------
# Dados dos strings, muestra por pantalla un mensaje indicando si uno de los dos aparece al final 
# del otro, ignorando diferencias de mayúsculas y minúsculas. Por ejemplo, el string "AbC" y "HiaBc" 
# debería mostrar que si que aparece uno al final del otro.
#-----------------------------------------------------------------------------------------------------------
cadena_de_texto = "AbC"
cadena_de_texto_2 = "HiaBc"

cadena_de_texto_minusculas = cadena_de_texto.lower()
cadena_de_texto_2_minusculas = cadena_de_texto_2.lower()

if cadena_de_texto_2_minusculas.endswith(cadena_de_texto_minusculas):
    print("La segunda cadena si que aparece al final de la primera")
#-----------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------