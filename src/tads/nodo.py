class Nodo: 
    #contiene un dato y la referencia al sigiente
    def __init__(self, dato, siguiente=None):
        self.dato = dato
        self.siguiente = siguiente
