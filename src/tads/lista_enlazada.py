from src.tads.nodo import Nodo

class ListaEnlazada:
    """TAD lista enlazada simple. No usar list de Python por debajo."""
    

def __init__(self): 
     self._cabeza = None #no hay nodos aun
     self._tamanio = 0 


def esta_vacia(self): 
    return self._cabeza is None
   

def tamanio(self): 
    return self._tamanio
 
def insertar_al_inicio(self, dato): #crea un nuevo nodo
    nuevo = Nodo(dato, self._cabeza)
    self._cabeza = nuevo
    self._tamanio += 1
 

def insertar_al_final(self, dato):
    nuevo = Nodo(dato)
    
    if self.esta_vacia():
       self._cabeza = nuevo
    else:
        actual = self._cabeza

        while actual.siguiente is not None:
           actual = actual.siguiente
           
        actual.siguiente = nuevo

    self._tamanio += 1

def buscar(self, dato):
    actual = self._cabeza
    
    while actual is not None:
        if actual.dato == dato:
              return actual.dato
        actual = actual.siguiente
        
    return None
        
def insertar_ordenado(self, dato, clave): 
    # si está vacía o se incerta al inicio
    if self.esta_vacia() or clave(self._cabeza.dato) >= clave(dato):
        self.insertar_al_inicio(dato)
        return
        
    nuevo = Nodo(dato)
    actual = self._cabeza
        
    while actual is not None and clave(actual.siguiente.dato) < clave(dato):
        actual = actual.siguiente

    nuevo.siguiente = actual.siguiente
    actual.siguiente = nuevo
    self._tamanio += 1
        
def eliminar(self, dato):
    if self.esta_vacia(): #caso 1 lista vacia 
        return False
        
    if self._cabeza.dato == dato:#caso 2: el elemento esta en la cabeza
        self._cabeza = self._cabeza.siguiente
        self._tamanio -= 1
        return True
        
    #if self._cabeza is not None and self._cabeza.dato == dato:
    # self._cabeza = self._cabeza.siguiente
    #self._tamanio -=1
    #return True
        actual = self._cabeza
        
        while actual.siguiente is not None:
            if actual.siguiente.dato == dato:
               actual.siguiente = actual.siguiente.siguiente
               self._tamanio -= 1 
               return True
            actual = actual.siguiente

        return False
    
def eliminar_primero(self):
        """Quita y retorna el primer elemento (para desapilar o desencolar)."""
    if self.esta_vacia():
        return None
        
    dato = self._cabeza.dato
    self._cabeza = self._cabeza.siguiente
    self._tamanio -= 1
    return dato

def obtener_primero(self):
        """Retorna el primer elemento sin quitarlo (para ver_tope)."""
    if self.esta_vacia():
        return None
        
    return self._cabeza.dato

def __iter__(self):
        actual = self._cabeza
        while actual is not None:
            yield actual.dato
            actual = actual.siguiente


