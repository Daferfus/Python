from libro import Libro
from autor import Autor
import sys
sys.path.insert(1, './')

def mas_antiguos(lista_de_libros, anyo):
    lista_de_titulos_de_libros = list()
    if (anyo >= 1900) and (anyo <= 2021):
        for libro in lista_de_libros:
            if libro.anyo <= anyo:
                lista_de_titulos_de_libros.append(libro.titulo)
    else:
        raise ValueError("El anyo de publicación del libro debe de ser entre 1900 y 2021.")
    return lista_de_titulos_de_libros

libro1 = Libro(autor = Autor(1, "Miguel", "Cervantes"), titulo = "Don Quijote", anyo = 1941)
libro2 = Libro(autor = Autor(2, "Julio", "Verne"), titulo = "La Vuelta al Mundo en 80 Días", anyo = 1920)
lista_de_libros = [libro1, libro2]

try:
    lista_de_titulos_de_libros = mas_antiguos(lista_de_libros, 2021)
    print(lista_de_titulos_de_libros)
except ValueError:
    print("El anyo de publicación del libro debe de ser entre 1900 y 2021.")