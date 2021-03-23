#-----------------------------------------------------------------------------------------------------------
#                               Ejercicio 1
# ----------------------------------------------------------------------------------------------------------
# Dada una lista de enteros, muestra por pantalla si un número introducido por teclado 
# está en la primera o en la última posición. La longitud mínima de la lista será de 1, 
# en caso contrario, el programa terminará.
#-----------------------------------------------------------------------------------------------------------
lista_de_enteros = [1, 2, 3, 4, 5]
numero_introducido = int(input("Introduce un número: "))

if len(lista_de_enteros)>=1:
    if lista_de_enteros[0] == numero_introducido:
        print("El número introducido está en la primera posición")
    elif lista_de_enteros[-1] == numero_introducido:
        print("El número introducido está en la última posición")
    else:
        print("El número introducido no está en ningún sitio")
else:
    print("La lista está vacía")
#-----------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------


#-----------------------------------------------------------------------------------------------------------
#                               Ejercicio 2
# ----------------------------------------------------------------------------------------------------------
# Pide 4 números y añádelos a una lista. Después, rota los elementos y guárdalos en una nueva lista 
# (el último es el primero, etc.), mostrando por pantalla esta nueva lista.
#-----------------------------------------------------------------------------------------------------------
lista_de_numeros = []

while len(lista_de_numeros) < 4:
    lista_de_numeros.append(int(input("Introduce número: ")))
print(lista_de_numeros)
lista_de_numeros.reverse()
print(lista_de_numeros)
#-----------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------


#-----------------------------------------------------------------------------------------------------------
#                               Ejercicio 3
# ----------------------------------------------------------------------------------------------------------
# Dadas dos listas de longitudes diferentes, averiguar si el primero o el último elemento de ambas 
# listas es el mismo. En este caso, eliminar dicho elemento y mostrar las listas resultantes.
#-----------------------------------------------------------------------------------------------------------
lista_1 = [1, 2, 3, 4]
lista_2 = [1, 1.5, 2, 2.5, 3, 3.5, 4, 4.5]

if lista_1.index(lista_1[0]) == lista_2.index(lista_2[0]):
    del(lista_1[0])
    del(lista_2[0])
    print(lista_1)
    print(lista_2)
elif lista_1.index(lista_1[-1] == lista_2.index(lista_2[-1])):
    del(lista_1[-1])
    del(lista_2[-1])
    print(lista_1)
    print(lista_2)
else:
    print("No hay elementos repetidos en la primera y última posición")
#-----------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------


#-----------------------------------------------------------------------------------------------------------
#                               Ejercicio 4
# ----------------------------------------------------------------------------------------------------------
# Dada una lista de enteros, averiguar si el primer o el último elemento es el mayor y sustituir el
# resto de elementos por éste (sin contar el primero el último). Por ejemplo, la lista [11, 5, 9, 7] 
# debería quedar como [11, 11, 11, 7].
#-----------------------------------------------------------------------------------------------------------
lista_de_enteros = [50, 20, 10 ,30]
número_máximo = max(lista_de_enteros)
print("Número máximo es: " + str(número_máximo))
itinerador = 0

while itinerador < len(lista_de_enteros)-1:
    if lista_de_enteros[itinerador] == número_máximo:
        if itinerador == 0 or itinerador == len(lista_de_enteros):
            posicion = 0
            while posicion < len(lista_de_enteros)-1:
                if posicion!=0 and posicion!=len(lista_de_enteros):
                    print(posicion)
                    lista_de_enteros[posicion] = número_máximo
                posicion+=1
    itinerador+=1
print(lista_de_enteros)    
#-----------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------


#-----------------------------------------------------------------------------------------------------------
#                               Ejercicio 5
# ----------------------------------------------------------------------------------------------------------
# Calcular la cantidad de números impares que hay en una lista de enteros.
#-----------------------------------------------------------------------------------------------------------
lista_de_enteros = [1, 2, 3, 4, 5]
número = 0
cantidad_de_números_impares = 0

for número in lista_de_enteros:
    if número%2 != 0:
        cantidad_de_números_impares+=1
print("Hay unos " + str(cantidad_de_números_impares) + " números impares")
#-----------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------


#-----------------------------------------------------------------------------------------------------------
#                               Ejercicio 6
# ----------------------------------------------------------------------------------------------------------
# Dada una lista de enteros, mostrar por pantalla la diferencia entre el mayor y el menor valor 
# de la lista.
#-----------------------------------------------------------------------------------------------------------
lista_de_enteros = [1, 2, 3, 4, 5]
número_entero = 0
número_mayor = 0
número_menor = lista_de_enteros[0]

for número_entero in lista_de_enteros:
    if número_entero > número_mayor:
        número_mayor = número_entero
    elif número_entero < número_menor:
        número_menor = número_entero
print(número_mayor-número_menor)
#-----------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------


#-----------------------------------------------------------------------------------------------------------
#                               Ejercicio 7
# ----------------------------------------------------------------------------------------------------------
# Dada una lista de enteros, devolver la media de todos los valores.
#-----------------------------------------------------------------------------------------------------------
lista_de_enteros = [1, 2, 3, 4, 5]
suma_de_enteros = 0
número_entero = 0

for número_entero in lista_de_enteros:
    suma_de_enteros += número_entero
media = suma_de_enteros//len(lista_de_enteros)
print(media)
#-----------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------


#-----------------------------------------------------------------------------------------------------------
#                               Ejercicio 8
# ----------------------------------------------------------------------------------------------------------
# Dada una lista de enteros, mostrar por pantalla si hay algún número que esté repetido 
# en dos posiciones consecutivas
#-----------------------------------------------------------------------------------------------------------
lista_de_enteros = [1, 2, 2, 3, 4]
itinerador = 0

while itinerador < len(lista_de_enteros)-1:
    if lista_de_enteros[itinerador] == lista_de_enteros[itinerador+1]:
        print("Hay dos números seguidos iguales")
    itinerador+=1
#-----------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------