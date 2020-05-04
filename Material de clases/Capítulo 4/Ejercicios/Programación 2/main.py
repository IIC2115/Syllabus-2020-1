import sqlite3  # importamos el módulo de sqlite

def crear_base_de_datos():
    """
    Esta función se encarga de crear las bases de datos en un archivo
    Retorna None
    """


    return None


def poblar_base_de_datos():
    """
    Esta función se encarga de poblar las tablas con la información del enunciado.
    Retorna None
    """


    return None


def puntaje_libro(libro):
    """
    libro: string con el título del libro
    Retorna el puntaje promedio de recomendación (integer)
    """


    return -1


def conteo_libros():
    """
    Retorna un diccionario con el conteo de libros por género y ciudad de la forma 
    {
        ciudad_1 :{
            genero_1: 4,
            genero_2: 1,
        },
            ciudad_2:{
            genero_1: 4,
            genero_2: 1,
        }
    }
    """


    return {}


def ciudad_con_mas_dinero(genero):
    """
    genero: string con el nombre del genero
    Retorna el nombre de la ciudad según lo indicado en el enunciado (string)
    """


    return "NO EXISTE"


def autor_libro_mas_caro(ciudad):
    """
    ciudad: string con el nombre de la ciudad
    Retorna el mail del autor con el libro más caro de dicha ciudad (string)
    """


    return "NO EXISTE"


# Vamos a problar las funciones
crear_base_de_datos()
poblar_base_de_datos()

titulo = "20 llamadas perdidas de mamá"
puntaje = puntaje_libro(titulo)
print("El libro '{}' tiene puntaje recomendación {}".format(titulo, puntaje))


titulo = "Un Verano sin Vicky"
puntaje = puntaje_libro(titulo)
print("El libro '{}' tiene puntaje recomendación {}".format(titulo, puntaje))

print("Probando el conteo de libros por género y ciudad")
print(conteo_libros())

genero = "terror"
ciudad = ciudad_con_mas_dinero(genero)
print("La ciudad con más dinero repartido por persona para el género '{}' es {}".format(genero, ciudad))


genero = "comedia"
ciudad = ciudad_con_mas_dinero(genero)
print("La ciudad con más dinero repartido por persona para el género '{}' es {}".format(genero, ciudad))


ciudad = "Apalachicola"
mail = autor_libro_mas_caro(ciudad)
print("El mail del autor con el libro más caro de {} es {}".format(ciudad, mail))