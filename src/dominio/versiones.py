class GestorVersiones:
    def __init__(self):
        # Diccionario o lista que guarda relaciones: id_original -> [ids_derivadas]
        self.relaciones = {}

    def cargar_relaciones(self, relaciones_dict):
        """Carga las relaciones de versiones."""
        self.relaciones = relaciones_dict

    def versiones_directas(self, id_cancion):
        """Devuelve la lista de IDs de canciones que son versión directa de id_cancion."""
        return self.relaciones.get(id_cancion, [])

    def versiones_de(self, id_cancion):
        """
        Función RECURSIVA del dominio.
        Obtiene todas las versiones directas e indirectas de una canción.
        """
        directas = self.versiones_directas(id_cancion)
        
        # CASO BASE: Si la canción no tiene versiones o derivados
        if not directas:
            return []
        
        # CASO RECURSIVO: Hay versiones directas, las acumulamos y buscamos
        # las versiones de cada una de ellas.
        resultado = list(directas)
        for v in directas:
            resultado += self.versiones_de(v)  # Llamada recursiva
            
        return resultado