class Pessoa:
    def __init__(self):
        self.pessoas = ['Edson', 'Neto', 'Théo', 'Mel']
    
    def __delitem__(self, n):
        del self.pessoas[n]
        #ou
        #del self.pessoas
        #ou
        #self.pessoas = []
x = Pessoa()
del x[1]
print(x.pessoas)