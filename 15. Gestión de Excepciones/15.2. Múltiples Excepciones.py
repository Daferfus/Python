lista = [4, 5, 1, 3]

print("inicio")

try:
    print(lista[4])
except (RuntimeError, IndexError) as err:
    print("se ha producido una excepción: "+str(err))
    print("esta excepción es de tipo "+type(err).__name__)

print("fin")



lista = [4, 5, 1, 3]

print("inicio")

try:
    print(lista[4])
except RuntimeError:
    print("Hacemos una cosa para RuntimeError")
except IndexError:
    print("Hacemos otra cosa para IndexError")

print("fin")





lista = [4, 5, 1, 3]

print("inicio")

try:
    print(lista[4])
except BaseException as err:
    print("se ha producido una excepción: "+str(err))
    print("esta excepción es de tipo "+type(err).__name__)

print("fin")



lista = [4, 5, 1, 3]

print("inicio")

try:
    print(lista[4])
except IndexError:
    print("Entramos por el primer except")
except BaseException:
    print("Entramos por el segundo except") # este bloque de código es inalcanzable

print("fin")