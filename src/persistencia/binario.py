"""Registros de longitud fija con struct. (Documentar en docs/INFORME.md)"""

import struct
from pathlib import Path
from src.dominio.cancion import Cancion
from src.excepciones import ArchivoInvalidoError
from src.tads.lista_enlazada import ListaEnlazada

HEADER = struct.Struct("<4scI")  # 4 bytes magia, 1 byte tema, 4 bytes cantidad
FORMATO = struct.Struct("<I30s25s30sH")  # id, titulo, artista, album, anio

MAGIA = b"AYED"
TEMA = b"M"


def a_bytes(texto, ancho):
    return str(texto).encode("utf-8")[:ancho].ljust(ancho, b"\x00")


def a_texto(datos):
    return datos.rstrip(b"\x00").decode("utf-8")


def cancion_a_tupla(cancion):
    return (
        cancion.id,
        a_bytes(cancion.titulo, 30),
        a_bytes(cancion.artista, 25),
        a_bytes(cancion.album, 30),
        int(cancion.anio),
    )


def tupla_a_cancion(datos):
    id_cancion, titulo, artista, album, anio = datos
    return Cancion(
        id_cancion, a_texto(titulo), a_texto(artista), a_texto(album), anio
    )


def guardar_binario(ruta, canciones):
    ruta = Path(ruta)
    with ruta.open("wb") as archivo:
        archivo.write(HEADER.pack(MAGIA, TEMA, canciones.tamanio()))
        for cancion in canciones:
            archivo.write(FORMATO.pack(*cancion_a_tupla(cancion)))


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
            )  #[cite: 13]

        magia, tema, cantidad = HEADER.unpack(cabecera)
        if magia != MAGIA or tema != TEMA:
            raise ArchivoInvalidoError(
                "El archivo no tiene el formato esperado (magia/tema incorrectos)."
            )

        for _ in range(cantidad):
            datos = archivo.read(FORMATO.size)
            if len(datos) < FORMATO.size:
                raise ArchivoInvalidoError(
                    "El archivo está incompleto o corrupto."
                )
            cancion = tupla_a_cancion(FORMATO.unpack(datos))
            canciones.insertar_al_final(cancion)
    return canciones


def posicion_del_id(canciones, id_buscado):
    for posicion, cancion in enumerate(canciones):
        if cancion.id == id_buscado:
            return posicion
    raise ValueError(f"No existe el ID {id_buscado} en la lista de canciones.")


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
        