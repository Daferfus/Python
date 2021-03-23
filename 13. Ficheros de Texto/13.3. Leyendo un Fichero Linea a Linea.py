#-----------------------------------------------------------------------------------------------------------
# readlin()
#-----------------------------------------------------------------------------------------------------------
# readline() - Lee, como su nombre indica, una línea del fichero.
f = open("fichero.txt", mode="rt", encoding="utf-8")

texto = f.readline()
print("Leemos una línea: "+texto)

texto = f.readline()
print("Leemos otra línea: "+texto)

f.close()


f = open("fichero.txt", mode="rt", encoding="utf-8")

linea = f.readline()
while linea != "" :
  print("he leído: " + linea)
  linea = f.readline()

f.close()
#-----------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------

#-----------------------------------------------------------------------------------------------------------
# Otra Forma de Leer Líneas
#-----------------------------------------------------------------------------------------------------------
f = open("fichero.txt", mode="rt", encoding="utf-8")

for linea in f:
  print("he leído: " + linea)

f.close()

#stdout.write() no mete una línea en blanco como un print
# readlines() - Devuelve una lista donde cada elemento es una línea leída.
f = open("fichero.txt", mode="rt", encoding="utf-8")

lista_lineas = f.readlines()
print("Lista de líneas leídas: ", lista_lineas)

f.close()
#-----------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------


#-----------------------------------------------------------------------------------------------------------
# writelines()
#-----------------------------------------------------------------------------------------------------------
# writelines() - Escribe en el fichero multiples líneas.
f = open("fichero.txt", mode="at", encoding="utf-8")

f.writelines(["Línea añadida de un listado \n", "otra línea añadida \n"])

f.close()


# r+ - Opción de lectura-escritura. En el caso de escribir añade líneas al fichero.
f = open("fichero.txt", mode="r+t", encoding="utf-8")

texto = f.read(10)
print("Leemos 10 caracteres: "+texto)

f.write("Esto es un mensaje añadido. \n")

f.close()
#-----------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------


#-----------------------------------------------------------------------------------------------------------
# Abrir y Cerrar Ficheros Automáticamente
#-----------------------------------------------------------------------------------------------------------
# Bloque with - Asegura que las operaciones de abrir y cerrar ficheros se haga automáticamente.
with open("fichero.txt", mode="rt", encoding="utf-8") as f:
  for linea in f:
    print("he leído: " + linea)
#-----------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------