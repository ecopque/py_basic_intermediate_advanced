class Carro:
    def __init__(self, nome):
        self.nome = nome
        self._motor = None
        self._fabricante = None
    @property
    def motor(self):
        return self._motor
    @motor.setter
    def motor(self, valor):
        self._motor = valor
    @property
    def fabricante(self):
        return self._fabricante
    @fabricante.setter
    def fabricante(self, valor):
        self._fabricante = valor
class Motor:
    def __init__(self, nome):
        self.nome = nome
class Fabricante:
    def __init__(self, nome):
        self.nome = nome
fusca = Carro(nome='Fusca')
motor10 = Motor(nome='1.0')
volks = Fabricante(nome='Volks')
fusca.motorizacao = motor10
fusca.montadora = volks
print(fusca.nome, fusca.motorizacao.nome, fusca.montadora.nome) #1: