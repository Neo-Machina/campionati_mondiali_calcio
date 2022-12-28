class Organizzazione:
    def __init__(self, anno, nazione):
        self.anno = anno
        self.nazione = nazione
    
    def __str__(self):
        return 'Anno: {}, Nazione: {}'.format(self.anno, self.nazione)
    
    @property
    def anno(self):
        return self._anno 
    
    @anno.setter    
    def anno(self, anno):
        self._anno = anno
        
    @property
    def nazione(self):
        return self._nazione
    
    @nazione.setter    
    def nazione(self, nazione):
        self._nazione = nazione