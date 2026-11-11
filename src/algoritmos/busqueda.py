def busqueda_lineal_por_id(canciones, id_buscado):
    """Devuelve el ítem cuya clave coincide, o None."""
    #busca una canción por ID recorriendo toda la colección.
    for cancion in canciones:

        if cancion.id == id_buscado:
            return cancion
    return None
    raise NotImplementedError

def busqueda_lineal_por_titulo(canciones, titulo_buscado):

    titulo_buscado = titulo_buscado.strip().lower()

    for cancion in canciones:

        if cancion.titulo.strip().lower() == titulo_buscado.strip().lower():
            return cancion

    return None


def busqueda_binaria_por_id(canciones, id_buscado):
    #La colección tiene que estar ordenada por obtener_clave.
    izquierda = 0
    derecha = len(canciones) -1

    while izquierda <= derecha:
        medio = (izquierda + derecha) // 2

        if canciones[medio].id == id_buscado:
            return canciones[medio]

        elif canciones[medio].id < id_buscado:
            izquierda = medio + 1

        else:
            derecha = medio -1

    return None
    raise NotImplementedError
