class Marca:

    # -- Constructor -- 

    def __init__(self, nombre):
        self._Nombre = nombre
    
    # -- Getter and Setter --
    
    def getNombre(self):
        return self._Nombre
    
    def setNombre(self, nombre):
        self._Nombre = nombre