class Control:

    def getTv(self):
        return self.tv
    
    def setTv(self, tv):
        self.tv = tv

    # -- Methods -- 

    def turnOn(self):
        self.tv._Estado = True
    
    def turnOff(self):
        self.tv_Estado  = False
    
    def canalUp(self):
        if (self.tv._Canal >= 1 and self.tv._Canal < 120):
            self.tv._Canal = self.tv._Canal + 1

    def canalDown(self):
        if (self.tv._Canal > 1 and self.tv._Canal <= 120):
            self.tv._Canal = self.tv._Canal - 1
    
    def volumenUp(self):
        if (self.tv._Volumen >= 1 and self.tv._Volumen < 7):
            self.tv._Volumen = self.tv._Volumen + 1
    
    def volumenDown(self):
        if (self.tv._Volumen > 1 and self.tv._Volumen <= 7):
            self.tv._Volumen = self.tv._Volumen - 1
    
    def enlazar(self, tvEnlazado):
        self.tv = tvEnlazado
        self.tv.setControl(self)
    
    def setCanal(self, canal):
        if (self.tv._Estado == True):
            if(canal <= 120 and canal >= 1):
                self.tv.canal = canal
            elif(canal > 120):
                self.tv.canal = 2