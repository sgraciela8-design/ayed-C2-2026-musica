from pathlib import Path


def cargar_binario(ruta):
    ruta = Path(ruta)
    if not ruta.exists():
        raise ArchivoInvalidoError(f"No existe el archivo binario: {ruta}")

    canciones = ListaEnlazada()
    with ruta.open("rb") as archivo:
        cabecera = archivo.read(HEADER.size)
        if len(cabecera) < HEADER.size:
            raise ArchivoInvalidoError(
                "Binario truncado: header incompleto."
            )  #[cite: 34]

        magia, tema, cantidad = HEADER.unpack(cabecera)
        if magia != MAGIA or tema != TEMA:
            raise ArchivoInvalidoError(
                "El archivo no tiene el formato esperado (magia/tema incorrectos)."
            )

        for _ in range(cantidad):
            datos = archivo.read(FORMATO.size)
            if len(datos) < FORMATO.size:
                raise ArchivoInvalidoError("El archivo está incompleto o corrupto.")
            cancion = tupla_a_cancion(FORMATO.unpack(datos))
            canciones.insertar_al_final(cancion)
    return canciones


def actualizar_registro(ruta, posicion, cancion):
    """Pisa un registro por posición (acceso directo). posicion es 0-based."""
    ruta = Path(ruta)
    if not ruta.exists():
        raise ArchivoInvalidoError(
            "Primero debés guardar el catálogo en binario antes de actualizar por posición."
        )

    with ruta.open("r+b") as archivo:
        desplazamiento = HEADER.size + posicion * FORMATO.size
        archivo.seek(desplazamiento)
        archivo.write(FORMATO.pack(*cancion_a_tupla(cancion)))
