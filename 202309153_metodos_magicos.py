class Pessoa:
    def __init__(self):
        self.pessoas = ['Edson', 'Neto', 'Théo', 'Mel']
    def __mul__(self, n):
        return self.pessoas * n

x = Pessoa()
print(x * 2) #1:

#1: Resposta: ['Edson', 'Neto', 'Théo', 'Mel', 'Edson', 'Neto', 'Théo', 'Mel']
