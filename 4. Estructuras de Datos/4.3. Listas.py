#-----------------------------------------------------------------------------------------------------------
# Crear Listas
#-----------------------------------------------------------------------------------------------------------
datos = [] # vacía
datos = list() # otra forma
datos = [4, "mensaje", -15, 3.4] # con elementos
#-----------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------


#-----------------------------------------------------------------------------------------------------------
# Acceder a Valores en Listas
#-----------------------------------------------------------------------------------------------------------
print("Elemento de la pos 2:", datos[2])
print("Penúltimo elemento:", datos[-2])
print("Desde la posición 1 hasta una anterior a la 3:", datos[1:3])
print("Los dos primeros:", datos[:2])
print("Desde la posición 1 hasta el final:", datos[1:])
#-----------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------


#-----------------------------------------------------------------------------------------------------------
# Modificar Valor de una Lista
#-----------------------------------------------------------------------------------------------------------
datos[2] = 10
print(datos)
#-----------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------


#-----------------------------------------------------------------------------------------------------------
# Repetir Elementos de una Lista
#-----------------------------------------------------------------------------------------------------------
print("Repetimos la lista dos veces:", datos * 2)
print("Creamos una lista con 5 ceros:", [0] * 5)
#-----------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------


#-----------------------------------------------------------------------------------------------------------
# Funciones de Listas
#-----------------------------------------------------------------------------------------------------------
datos = [4, "mensaje", -15, 3.4]

# Obtener la longitud de una lista
longitud = len(datos)
print(longitud)

# Añadir un elemento al final
datos.append(12)
print("Añado el 12 al final: ", datos)

# Añadir un elemento en una posición determinada (sin machacar el existente)
datos.insert(2,"nuevo_elemento")
print("Añado 'nuevo_elemento' en pos 2: ", datos)

# Buscar un elemento
print("Posición del -15:", datos.index(-15))
print("Está el -15?:", -15 in datos)

# Combinar dos listas
datos.extend([55, 22])
print("Combino dos listas: ", datos)
#-----------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------


#-----------------------------------------------------------------------------------------------------------
# Eliminar Elementos en una Lista
#-----------------------------------------------------------------------------------------------------------
datos = [4, "mensaje", -15, 3.4, -15, 25, 12]

# Eliminar un elemento (si hay varios, el primero que encuentra)
datos.remove(-15)
print("Elimino el -15: ",datos)

# Eliminar el elemento de determinada posición
del(datos[2])

# Otra forma mediante la que nos podemos guardar el valor eliminado
# res = datos.pop(2) 
print("Elimino el de la pos 2: ",datos)

# Vaciar parcialmente una lista
datos[:2] = []
print("Vacio desde la pos 0 hasta la 2: ",datos)

# Vaciarla totalmente
# datos = []
# Otra forma
# datos.clear()
# Otra forma que borra incluso la lista
# del(datos)
print("La vacío entera: ",datos)
#-----------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------


#-----------------------------------------------------------------------------------------------------------
# Funciones de Posición
#-----------------------------------------------------------------------------------------------------------
datos = [4, "mensaje", -15, 3.4, -15, 25, 12]

# Contar cuántas veces aparece un elemento en la lista
res = datos.count(-15)
print("Veces que aparece el -15: ",res)

# Encontar el índice de un elemento de la lista (su primera aparición)
res = datos.index(-15)
print("Posición del -15: ",res)

# Ordenar de varias formas. Observa como podemos ordenar por longitud:
datos = ["esto", "es", "un", "mensaje"]
datos.sort()
print("Nuevos datos ordenados:", datos)
datos.sort(key=len)
print("Nuevos datos ordenados por longitud:", datos)

# Invertir: datos.reverse()
# Copiar: copia = datos.copy()
#-----------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------


#-----------------------------------------------------------------------------------------------------------
# Recorrer una Lista
#-----------------------------------------------------------------------------------------------------------
datos = [4, "mensaje", -15, 3.4]

for i in datos:
  print(i)
#-----------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------


#-----------------------------------------------------------------------------------------------------------
# Comprobar si un Item Está en una Lista
#-----------------------------------------------------------------------------------------------------------
# Ejemplo con in
datos = [4, "mensaje", -15, 3.4]

is_34 = 3.4 in datos
print(is_34)

is_23 = 23 in datos
print(is_23)


# Ejemplo manual
lista = [5, 2, 3, 7, 4, 1, 7]
encontrado = False
i = 0

while (not encontrado) and (i < len(lista)): # Los paréntesis son para facilitar la lectura, pero no son necesarios
  if lista[i] == 7:
    print("Encontrado en posición "+str(i))
    encontrado = True
  i += 1 # No existe la instrucción i++

if not encontrado:
  print("No se ha encontrado")
#-----------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------


#-----------------------------------------------------------------------------------------------------------
# Acciones en Bucles
#-----------------------------------------------------------------------------------------------------------
# La instrucción break nos permite salir de un bucle en un momento determinado
for i in [5, 2, 3, 7, 4, 1, 7]:
  if i == 7:
    print("Encontrado!")
    break

print("Fin")


# continue para romper una iteración determinada
for i in [5, 2, 3, 7, 4, 1, 7]:
  if i == 7:
    print("Encontrado!")
    continue
  print("Este código sólo se ejecuta si no entra por el if, ya que el continue se carga la iteración")

print("Fin")
#-----------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------