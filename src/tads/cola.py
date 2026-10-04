from src.excepciones import ColaVaciaError
from src.tads.lista_enlazada import ListaEnlazada

class Cola:
    """TAD cola implementado sobre ListaEnlazada."""
def __init__(self):
    self._datos = ListaEnlazada()

def encolar(self, dato): 
    #agrega al final de la cola
    self._datos.insertar_al_final(dato)

def desencolar(self): 
    #si la cola está vacia, da ColaVaciaError
    if self.esta_vacia():
       raise ColaVaciaError ("No hay elementos en la cola")
        
    dato = self._datos._cabeza.dato
    self._datos._cabeza = self._datos._cabeza.siguiente
    self._datos._tamanio -=1
    return dato

def ver_frente(self): 
    #mira al del frente sin sacarlo
    if self.esta_vacia():
       raise ColaVaciaError ("la cola esta vacia")
       
    return self._datos._cabeza.dato

def esta_vacia(self):
    return self._datos.esta_vacia()
