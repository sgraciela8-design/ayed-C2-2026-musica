def cargar_csv(ruta):
    """Carga secuencial. Devuelve una lista de dicts."""
    raise NotImplementedError

def guardar_csv(ruta, filas, encabezados):
    raise NotImplementedError

from pathlib import Path
from src.excepciones import ArchivoInvalidoError


RAIZ = Path(__file__).resolve().parents[2]
DATA = RAIZ / "data"
def cargar_texto(ruta):

ruta = Path(ruta)
if not ruta.exists():
raise ArchivoInvalidoError(f"No existe el archivo: {ruta}")
filas = []
with ruta.open("r", encoding="utf-8") as archivo:
encabezado = archivo.readline().strip().split(",")
for linea in archivo:
linea = linea.strip()
if not linea: # línea vacía al final del archivo
continue
valores = linea.split(",")
if len(valores) != len(encabezado):
raise ArchivoInvalidoError(
f"Línea con {len(valores)} campos "
f"(se esperaban {len(encabezado)}): {linea}"
)
fila = dict(zip(encabezado, valores)) # {'id': '1', 'nombre': ...}
filas.append(fila)
return filas
