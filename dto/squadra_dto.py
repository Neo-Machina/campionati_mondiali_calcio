class Squadra:
    def __init__(self, nazione, anno, allenatore, posizioneInClassifica):
        self.nazione = nazione
        self.anno = anno
        self.allenatore = allenatore
        self.posizioneInClassifica = posizioneInClassifica
    
    def __str__(self):
        return 'Nazione: {}, Anno: {}, Allenatore: {}, Posizione in Classifica: {}'.format(self.nazione, self.anno, self.allenatore, self.posizioneInClassifica)
    
    @property
    def nazione(self):
        return self._nazione 
    
    @nazione.setter    
    def nazione(self, nazione):
        self._nazione = nazione
        
    @property
    def anno(self):
        return self._anno
    
    @anno.setter    
    def anno(self, anno):
        self._anno = anno
    
    @property
    def allenatore(self):
        return self._allenatore 
    
    @allenatore.setter    
    def allenatore(self, allenatore):
        self._allenatore = allenatore
        
    @property
    def posizioneInClassifica(self):
        return self._posizioneInClassifica 
    
    @posizioneInClassifica.setter    
    def posizioneInClassifica(self, posizioneInClassifica):
        self._posizioneInClassifica = posizioneInClassifica
        
