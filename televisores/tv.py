class TV:
    # -- Constructor --
    _numTV = 0

    def __init__(self, marca, estado):
        self._Marca = marca
        self._Estado = estado
        self._Precio = 500
        self._Volumen = 1
        self._Canal = 1
        TV._numTV += 1
    
    # -- Getter and Setter --
    def getNumTV():
        return TV._numTV

    def setNumTV(a):
        _numTV = a

    def getMarca(self):
        return self._Marca

    def setMarca(self, marca):
        self._Marca = marca
    
    def getControl(self):
        return self._Control

    def setControl(self, control):
        self._Control = control
    
    def getPrecio(self):
        return self._Precio
    
    def setPrecio(self, precio):
        self._Precio = precio
    
    def getVolumen(self):
        return self._Volumen
    
    def setVolumen(self, volumen):
        self._Volumen = volumen

    def getCanal(self):
        return self._Canal

    def setCanal(self, canal):
        if (self._Estado == True):
            if(canal <= 120 and canal >= 1):
                self._Canal = canal
            elif(canal > 120):
                self._Canal = 2
    
    def getEstado(self):
        return self._Estado

    # -- Methods -- 

    def turnOn(self):
        self._Estado = True
    
    def turnOff(self):
        self._Estado  = False
    
    def canalUp(self):
        if (self._Canal >= 1 and self._Canal < 120):
            self._Canal = self._Canal + 1

    def canalDown(self):
        if (self._Canal > 1 and self._Canal <= 120):
            self._Canal = self._Canal - 1
    
    def volumenUp(self):
        if (self._Volumen >= 1 and self.getVolumen < 7):
            self._Volumen = self._Volumen + 1
    
    def volumenDown(self):
        if (self._Volumen > 1 and self._Volumen <= 7):
            self._Volumen = self._Volumen - 1