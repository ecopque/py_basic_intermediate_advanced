from datetime import date, timedelta
class Pessoa:
    def __init__(self, nome, data_nascimento):
        self.nome = nome
        self.data_nascimento = data_nascimento
    def dias_vividos(self):
        return (date.today() - self.data_nascimento).days
    @property
    def data_nascimento(self):
        return self._data_nascimento + timedelta(days=20) #1:
    @data_nascimento.setter
    def data_nascimento(self, value):
        if not isinstance(value, date):
            raise ValueError('data_nascimento deve ser um objeto do tipo date.')
        self._data_nascimento = value
p2 = Pessoa('Théo', date(2000, 8, 30))
print(p2.data_nascimento) #2:

# Edson Copque | https://linktr.ee/edsoncopque
