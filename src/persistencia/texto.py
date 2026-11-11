from pathlib import Path
from src.excepciones import ArchivoInvalidoError

def cargar_csv(ruta):
    """Carga secuencial. Devuelve una lista de dicts."""

    ruta = Path(ruta)

    if not ruta.exists():
        raise ArchivoInvalidoError(f"No existe el archivo: {ruta}"
        )
    filas = []
    with ruta.open("r", encoding="utf-8") as archivo:
        encabezados = archivo.readline().strip().split(",")
        for linea in archivo:
            linea = linea.strip()

            if not linea:
                continue 

            valores = linea.split(",")
            if len(valores) != len(encabezados):
                raise ArchivoInvalidoError(
                    f"Línea inválida: {linea}. "
                )

            fila = dict(zip(encabezados, valores))
            filas.append(fila)

    return filas


def guardar_csv(ruta, filas, encabezados):
    """
    Guarda una colección de diccionarios en un archivo CSV
    """
    ruta = Path(ruta)

    with ruta.open("w", encoding="utf-8", newline="") as archivo:
        archivo.write(",".join(encabezados) + "\n")
        for fila in filas:

            campos = [
                str(fila[campo]) 
                for campo in encabezados
            ]
            archivo.write(",".join(campos) + "\n")