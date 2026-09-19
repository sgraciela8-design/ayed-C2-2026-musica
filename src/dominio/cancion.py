class Cancion:
    def __init__(self, titulo, artista, album, anio, id_cancion):
        self.id= int(id_cancion)
        self.titulo = titulo
        self.artista = artista
        self.album = album
        self.anio = anio
    def obtener_resumen(self):
        return f"[{self.id}] {self.titulo} - {self.artista}-{self.album}-{self.anio}"
    
    #ACA ESTAN DEFINIDAS LA CLASE CANCION#