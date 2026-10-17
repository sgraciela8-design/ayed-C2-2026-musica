def busqueda_lineal_por_id(canciones, id_buscado):
    """Devuelve el ítem cuya clave coincide, o None."""

    for cancion in canciones:

        if cancion.id == id_buscado:
            return cancion
    return None
    raise NotImplementedError


def busqueda_binaria(coleccion_ordenada, clave, obtener_clave):
    """La colección tiene que estar ordenada por obtener_clave."""
    raise NotImplementedError
