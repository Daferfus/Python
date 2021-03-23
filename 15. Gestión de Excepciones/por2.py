# función
def por2(valor):
    if valor < 0:
        raise ValueError("El valor es negativo")
    else:
        return valor * 2