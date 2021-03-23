# seek() - Nos permite mover el puntero a una determinada posición que pasamos por parámetro.
# tell() - La posición actual del puntero.

f = open("fichero.txt", mode="rt", encoding="utf-8")

# Leemos 10 caracteres
texto = f.read(10)
print("Leemos 10 caracteres: "+texto)

pos = f.tell()
print("La posición actual del puntero es ", pos)

# Movemos el puntero al inicio y volvemos a leer
f.seek(0)
texto = f.read(10)
print("Volvemos a leer: "+texto)

f.close()