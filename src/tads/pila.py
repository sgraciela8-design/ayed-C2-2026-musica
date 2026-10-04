
from src.excepciones import PilaVaciaError
from src.tads.lista_enlazada import ListaEnlazada


class Pila:
    """TAD pila implementado sobre ListaEnlazada."""

    def __init__(self):
        self._datos = ListaEnlazada()

    def apilar(self, dato):
        # Agrega al inicio de la pila.
        self._datos.insertar_al_inicio(dato)

    def desapilar(self):
        # Quita y devuelve el elemento del tope.
        if self.esta_vacia():
            raise PilaVaciaError("No hay elementos en el historial")

        return self._datos.eliminar_primero()

    def ver_tope(self):
        # Consulta el elemento del tope sin quitarlo.
        if self.esta_vacia():
            raise PilaVaciaError("La pila está vacía")

        return self._datos.obtener_primero()

    def esta_vacia(self):
        return self._datos.esta_vacia()
