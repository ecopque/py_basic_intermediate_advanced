class Pessoa:
    def __init__(self):
        self.pessoas = ['Edson', 'Neto', 'Théo', 'Mel']
    def __add__(self, p2):
        return self.pessoas + p2

x = Pessoa()
print(x + ['Lili', 'Bolinha']) #1:

#1: Resposta: ['Edson', 'Neto', 'Théo', 'Mel', 'Lili', 'Bolinha'].