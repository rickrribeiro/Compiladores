class Estado:
    def __init__(self, init,final):
        self.estado = init #valor do estado
        self.isFinal = final
        self.transicoes = [] #lista de transições
    
class Transicao:
    def __init__(self, atomo):
        self.atomo = atomo #atomo da transição
        self.finais = [] #estados finais da transição