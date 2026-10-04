class ArchivoInvalidoError(Exception):
     """Se lanza cuando un archivo no cumple el formato esperado."""
     pass


class ColeccionLlenaError(Exception):
    """Se lanza cuando se intenta agregar un elemento a una colección llena."""
    pass


class ColeccionVaciaError(Exception):
    """Se lanza cuando se intenta acceder a un elemento de una colección vacía."""
    pass


class PilaVaciaError(Exception):
    pass


class ColaVaciaError(Exception):
    pass

