class Pessoa:
    def __init__(self):
        self.pessoas = ['Edson', 'Théo', 'Mel']
    def __str__(self):
        return f'Pessoa(pessoas = {self.pessoas})'
x = Pessoa()
print(x) #1: #2:
#1: Resposta: Pessoa(pessoas = ['Edson', 'Théo', 'Mel']).
#2: Agora sim, teremos o print pois usamos o "__str__" para tal.