class Caneta:
    def __init__(self, cor):
        self._cor = cor #1:
    @property
    def cor(self): #2:
        print('Iniciando property...')
        return self._cor
    @cor.setter #3:
    def cor(self, valor):
        print('Estou no setter: ', valor)
        self._cor = valor
canetinha = Caneta(cor='Azul') #4:
canetinha.cor = 'Vermelha' #5:
print(canetinha.cor) #6:

# Edson Copque | https://linktr.ee/edsoncopque
