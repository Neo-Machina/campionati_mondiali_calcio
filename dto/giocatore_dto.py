class Giocatore:
    def __init__(self, id, nome):
        self.id = id
        self.nome = nome
    
    def __str__(self):
        return 'Id: {}, Nome: {}'.format(self.id, self.nome)
    
    @property
    def id(self):
        return self._id 
    
    @id.setter    
    def id(self, id):
        self._id = id
        
    @property
    def nome(self):
        return self._nome
    
    @nome.setter    
    def nome(self, nome):
        self._nome = nome