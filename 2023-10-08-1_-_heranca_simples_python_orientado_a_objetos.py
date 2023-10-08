class Pessoa:
    def __init__(self, nome, sobrenome):
        self.nome = nome
        self.sobrenome = sobrenome
    def falar_nome_classe(self):
        print('Classe Pessoa:')
        print(self.nome, self.sobrenome, self.__class__.__name__)
class Cliente(Pessoa):
    def falar_nome_classe(self): #1:
        print('Classe Cliente:')
        print(self.nome, self.sobrenome, self.__class__.__name__)
class Aluno(Pessoa):
    ...
c1 = Cliente(nome='Edson', sobrenome='Copque')
c1.falar_nome_classe() #2: