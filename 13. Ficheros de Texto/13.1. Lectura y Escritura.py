# open() - Abrir fichero.
''' file: la ruta del fichero (obligatorio).
    mode: lectura (r), escritura (w) , añadir (a), lectura-escritura (r+), fichero binario(b) 
          y fichero de texto (t).
    encoding: codificación a utiliar en modo texto. 
              Si no especificamos esto, Python utilizará la codificación por defecto, 
              que podemos averiguar con la llamada a sys.getdefaultencoding().
'''
# write() - Escribir en fichero.
# close() - Cerrar fichero para que los cambios surtan efecto.

f = open("fichero.txt", mode="wt", encoding="utf-8")

f.write("Esto es un mensaje. ")

f.write("Esto es otro mensaje en la misma línea. \n")

f.write("Esto es un mensaje en una nueva línea.")

f.close()

# read() - Leer fichero.

f = open("fichero.txt", mode="rt", encoding="utf-8")

#leemos 10 caracteres
texto = f.read(10)
print("Leemos 10 caracteres: "+texto)
print(type(texto))

#leemos los restantes
texto = f.read()
print("\n\nLeemos hasta el final del fichero: "+texto)

f.close()