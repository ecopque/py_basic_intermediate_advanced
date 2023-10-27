class Caneta:
    def __init__(self, cor):
        self.cor_tinta = cor
    @property
    def cor(self):
        print('Iniciando property...')
        return self.cor_tinta
canetinha = Caneta(cor='Azul')
print(canetinha.cor) #1: 