'''1. Escribe un programa que genere un fichero de texto con los números del 1 al 5000 y sus 
      cuadrados.
'''
with open("fichero.txt", mode="wt", encoding="utf-8") as f:

    contador = 0
    while contador <= 5000 :
        f.writelines("Número: " + str(contador) + " Cuadrado: " + str(contador**2)+"\n")
        contador+=1
    
'''2. Escribe una función que reciba el nombre de un fichero que contiene palabras 
      (cada línea tiene una palabra) y que devuelva la palabra que tiene una longitud máxima 
      y su longitud.
'''

'''3. Escribe una función que recibe el nombre de un fichero 
      (cada línea puede tener varias palabras) y una letra, y que muestre por pantalla 
      las palabras del fichero que contienen la letra.'''

'''4. Escribe una función que reciba el nombre de un fichero y que muestre por pantalla 
      cuántas veces aparece cada palabra.
'''

'''5. Escribe una función generadora que devuelva una palabra de un fichero cada vez 
      que es llamada.
'''

'''6. Escribe un función que anonimice el fichero interview.txt. 
      Este fichero contiene una entrevista con Trump, pero su nombre no puede aparecer 
      y hay que cambiarlo a "Mr. X" para anonimizar el fichero. 
      El resultado, será escrito en un fichero anonymous.txt.
'''

'''7. Escribe un programa que lee el nombre del fichero de texto del teclado y muestra 
      por pantalla el texto codificado de forma que sólo las letras minúsculas se sustituyen 
      por las siguientes según el abecedario (una a por una b, una b por una c, etc.).
'''