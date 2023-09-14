class Pessoa:
    def __init__(self):
        self.pessoas = ['Edson', 'Théo', 'Mel']
    def __getitem__ (self, posicao): #1:
        return self.pessoas[posicao]
x = Pessoa()
print(x[1]) #2:

#1: __getitem__ é um método especial (ou método dunder, que significa "double underscore" ou "método com duplo sublinhado") que permite que objetos de uma classe suportem a indexação. Isso significa que você pode usar a notação de colchetes [] para acessar elementos de um objeto da classe como se fosse uma sequência (como uma lista ou uma string).
#2: Resposta: Théo.