def ordenar_seleccion_por_id(canciones):
    """Selection Sort por ID"""
    """Ordenamiento por selección. Devuelve una nueva secuencia, no usa sorted."""

    n = len(canciones)

    for i in range(n):
        indice_minimo = i

        for j in range(i + 1,n):

            if canciones[j].id < canciones[indice_minimo].id:
                indice_minimo = j

        canciones[i], canciones[indice_minimo] = (
            canciones[indice_minimo], canciones[i]
        )
    return canciones
    raise NotImplementedError


def ordenar_insercion_por_titulo(canciones):
    """Insertion Sort por título"""
    """Ordenamiento por inserción. Devuelve una nueva secuencia, no usa sorted."""

    for i in range(1, len(canciones)):

        actual = canciones[i]

        j = i-1

        while(
            j >= 0
            and canciones[j].titulo.lower() > actual.titulo.lower()
        ):
            canciones[j + 1] = canciones[j] j-=1
        canciones[j + 1] = actual

    return canciones
    raise NotImplementedError
