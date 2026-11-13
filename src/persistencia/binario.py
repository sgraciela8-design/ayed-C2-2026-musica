""" Registros de longitud fija con struct. (Documentar en docs/INFORME.md)
"""

import struct
from src.dominio import cancion
from src.dominio.cancion import Cancion
from src.tads.lista_enlazada import ListaEnlazada
from src.excepciones import ArchivoInvalidoError

HEADER = struct.Struct("<4scI")  # 4 bytes de firma, 1 byte de version, 4 bytes de cantidad de registros
FORMATO = struct.Struct("<I30s25s30sH")  # id, titulo, artista, album

MAGIA = b"AYED"
TEMA = b"M"
"""Conversión de un objeto Cancion a bytes para persistencia en binario."""
#conversión de texto a bytes
def a_bytes(texto, ancho):
    return str(texto).encode("utf-8")[:ancho].ljust(ancho, b"\x00")

"""Conversión de un objeto Cancion a bytes para persistencia en binario."""
#conversión de bytes a texto
def a_texto(datos):
    return (datos.rstrip(b"\x00")).decode("utf-8")

"""cancion a Tupla y Tupla a canción para persistencia en binario."""
#cancion a Tupla
def cancion_a_tupla(cancion):
    return(cancion.id, 
           a_bytes(cancion.titulo, 30), a_bytes(cancion.artista, 25), a_bytes(cancion.album, 30),int(cancion.anio))

#Tupla a canción
def tupla_a_cancion(datos):
    id_cancion, titulo, artista, album, anio = datos
    return Cancion(id_cancion, a_texto(titulo), a_texto(artista), a_texto(album), anio)


def guardar_binario(ruta, canciones):
    with open(ruta, "wb") as archivo:
        # Escribir el encabezado
        archivo.write(HEADER.pack(MAGIA, TEMA, canciones.tamanio()))


        # Escribir los registros
        for cancion in canciones:
            archivo.write(FORMATO.pack(*cancion_a_tupla(cancion)))

   # raise NotImplementedError

"""Carga un archivo binario y devuelve una lista enlazada de canciones."""
def cargar_binario(ruta):
    canciones = ListaEnlazada()
    with open(ruta, "rb") as archivo:
        #Leer encabezado
        cabecera = archivo.read(HEADER.size)
        magia,tema,cantidad = HEADER.unpack(cabecera)

        if magia != MAGIA or tema != TEMA:
            raise ArchivoInvalidoError("El archivo no tiene el formato esperado.")

        # Leer los registros
        for _ in range(cantidad):
            datos = archivo.read(FORMATO.size)
            if len(datos) < FORMATO.size:
                raise ArchivoInvalidoError("El archivo está incompleto o corrupto.")
            cancion = tupla_a_cancion(FORMATO.unpack(datos))
            canciones.insertar_al_final(cancion)
    return canciones

"""Posición de un registro por id (acceso directo). Devuelve -1 si no se encuentra."""
#Posicion po ID
def posicion_del_id(canciones, id_buscado):
    for posicion,cancion in enumerate(canciones):
        if cancion.id == id_buscado:
            return posicion
    raise ValueError(f"No existe el ID {id_buscado} en la lista de canciones.")
    

"""Acualización directa con seek y write. Se pisa el registro en la posición indicada (0-based)."""

#actualización directa con seek y write función estrella de la defensa

def actualizar_registro(ruta, posicion, cancion):
    """Pisa un registro por posición (acceso directo). posicion es 0-based."""
    
    with open(ruta, "r+b") as archivo:
        # Calcular el desplazamiento del registro
        desplazamiento = HEADER.size + posicion * FORMATO.size
        archivo.seek(desplazamiento)
        archivo.write(FORMATO.pack(*cancion_a_tupla(cancion)))
        

   # raise NotImplementedError
