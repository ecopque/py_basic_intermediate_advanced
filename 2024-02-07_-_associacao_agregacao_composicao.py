class Escritor:
    def __init__(self, nome) -> None:
        self.nomeacao = nome
        self._ferramenta = None #1:
    @property
    def ferramenta(self):
        return self._ferramenta
    @ferramenta.setter
    def ferramenta(self, ferramenta):
        self._ferramenta = ferramenta
class FerramentaDeEscrever:
    def __init__(self, nome):
        self.nomeacao2 = nome
    def escrever(self):
        return f'{self.nomeacao2} está escrevendo...'
escritor = Escritor(nome='Edson')
caneta = FerramentaDeEscrever(nome='Caneta Bic')
print(caneta.escrever()) #2:
print(escritor.ferramenta) #3:
escritor.ferramenta = caneta #4: 
print(escritor.ferramenta) #(4) #5:
print(escritor.ferramenta.escrever()) #(4) #6:
