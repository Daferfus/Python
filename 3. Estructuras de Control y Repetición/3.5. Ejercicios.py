#-----------------------------------------------------------------------------------------------------------
#                               Ejercicio 1
# ----------------------------------------------------------------------------------------------------------
# Realiza un programa para calcular el factorial de un número entero introducido por el teclado 
# (sin utilizar la librería).
#-----------------------------------------------------------------------------------------------------------
x = int(input("Introduce un número: "))
resultado = x
while x > 0:
    if (x-1)!=0:
        resultado = resultado*(x-1)
    x-=1
print(resultado)
#-----------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------


#-----------------------------------------------------------------------------------------------------------
#                               Ejercicio 2
# ----------------------------------------------------------------------------------------------------------
# Implementa un juego que genere un número entero aleatorio entre 1 y 100. 
# Entonces, el usuario deberá introducir números por teclado para intentar adivinar el número generado. 
# Cada vez que el usuario introduzca un número por teclado, el programa deberá determinar si el número 
# es el generado inicialmente (ganando el usuario la partida), si el número introducido por el usuario 
# es múltiplo o divisor del número (informando de que el número introducido es múltiplo o divisor),
# o si no es ninguno de los otros dos casos. Al final de la partida, el número de puntos obtenido por el 
# usuario es 100 menos el número de intentos del usuario. La puntuación debe imprimirse al final del juego.
#-----------------------------------------------------------------------------------------------------------
puntuación = 100
for x in range(1,100):
    numero = int(input("Introduce un número: "))
    if numero == x:
        print("Has ganado la partida")
        break
    elif numero%x == 0:
        print("El número es múltiplo o divisor del número")
        puntuación-=1
    else:
        print("Vuelve a intentarlo")
        puntuación-=1
print("Has ganado la partida con una puntuación de " + str(puntuación))
#-----------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------