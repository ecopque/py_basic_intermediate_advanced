class Pessoa:
    ano = 2023 #1:
    def __init__(self, nome, idade):
        self.nomeacao = nome
        self.age = idade
    @classmethod
    def criar_com_50_anos(cls, nome):
        return cls(nome, 50) #3:
p1 = Pessoa(nome='Edsuuu', idade=100)
print(Pessoa.ano) #2:
p2 = Pessoa.criar_com_50_anos('Neto')
print(p2.nomeacao, p2.age) #4:
print(p2) #5:

# Edson Copque | https://linktr.ee/edsoncopque
