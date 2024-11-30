class Pessoa:
    def __init__(self):
        self.pessoas = ['Edson', 'Neto', 'Théo', 'Mel']
    def __reversed__(self):
        return [self.pessoas[i] for i in range(len(self.pessoas) -1, -1, -1)]
x = Pessoa()
print(reversed(x)) #1:

#1: Resposta: ['Mel', 'Théo', 'Neto', 'Edson'].

# Edson Copque | https://linktr.ee/edsoncopque
