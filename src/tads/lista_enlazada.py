class ListaEnlazada:
    """TAD lista enlazada simple. No usar list de Python por debajo."""
    from src.tads.nodo import Nodo

def __init__(self): 
       self.primero = None
       self._tamanio = 0 
raise NotImplementedError

def esta_vacia(self):
    return self.primero is None
    raise NotImplementedError

    def tamanio(self): 
        return self._tamanio
        raise NotImplementedError

    def insertar_al_inicio(self, dato):
        nuevo = Nodo(dato,self.primero)
        self.primero =nuevo
        self._tamanio += 1
        raise NotImplementedError

    def insertar_al_final(self, dato):
        nuevo = nodo(dato)
        if self.esta_vacia():
            sel.primero = nuevo
        else:
            actual = self.primero

            while actual.siguiente:
                actual = actual.siguiente
            actual.siguiente = nuevo

        self._tamanio += 1
        raise NotImplementedError

    def insertar_ordenado(self, dato, clave):
        raise NotImplementedError

    def eliminar(self, dato):
        raise NotImplementedError

    def buscar(self, dato):
        raise NotImplementedError

    def __iter__(self):
        raise NotImplementedError
