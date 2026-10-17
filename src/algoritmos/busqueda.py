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


def busqueda_binaria_por_id():
    print ("Función pendiente para Entrega 4.")
    """La colección tiene que estar ordenada por obtener_clave."""
    raise NotImplementedError
