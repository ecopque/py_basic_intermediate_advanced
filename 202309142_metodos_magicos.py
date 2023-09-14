class Pessoa:
    def __init__(self):
        self.pessoas = ['Edson', 'Théo', 'Mel']
    def __str__(self): #1: Aqui estamos pedindo para retornar o __str__.
        return 'Olá, amigos!'
x = Pessoa()
print(x) #2: Resposta: Olá, amigos!
print(x.pessoas) #3: ['Edson', 'Théo', 'Mel'].