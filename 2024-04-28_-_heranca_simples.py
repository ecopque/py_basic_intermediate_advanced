class Pessoa: #1: 
    def __init__(self, nome, sobrenome):
        self.nome = nome
        self.sobrenome = sobrenome
    def falar_nome_classe(self):
        print(self.nome, self.sobrenome, self.__class__.__name__) #3:
class Cliente(Pessoa): #(1) #2:
    ...
class Aluno(Pessoa):
    ...
c1 = Cliente(nome='Edson', sobrenome='Copque')
c1.falar_nome_classe() #4:
a1 = Aluno(nome='Théo', sobrenome='de Mel')
a1.falar_nome_classe() #5:
