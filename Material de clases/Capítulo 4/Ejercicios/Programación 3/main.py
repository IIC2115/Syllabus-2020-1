def get_info(app):
    return None

def best_by_genre(n, genre):
    return None

def count_by_version(date_1, date_2):
    return None

def price_of_the_best_by_genre(n, genre):
    return None

def recommend(genre, size):
    return None

def need_update_(app):
    return None

def app_with_more_income():
    return None

def add_app(app_data):
    return None

def add_comment(app_name, text, sentiment):
    return None

def download_app(app_name):
    return None

def delete_app(app_name):
    return None


if __name__ == "__main__":
    datos = get_info("Este nombre no existe")
    print(datos["error"])
    nombre = 'Superheroes Wallpapers | 4K Backgrounds'
    datos_super = get_info(nombre)
    print("{} -> {}".format(nombre, datos_super['installs']))
    download_app(nombre)
    datos_super = get_info(nombre)
    print("{} -> {}".format(nombre, datos_super['installs']))
