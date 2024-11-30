class Pessoa:
    def __init__(self):
        self.pessoas = ['Edson', 'Neto', 'Théo', 'Mel']
    def __len__(self) -> int:
        x = 0
        while True:
            try:
                y = self.pessoas[x]
                x += 1
            except:
                break
        return x
    def __getitem__(self, posicao):
        return self.pessoas[posicao]
    def __eq__(self, p2):
        if len(self.pessoas) == len(p2):
            resultado = []
            for i in range(len(self.pessoas)):
                resultado.append(self.pessoas[i] == p2[i])
                return all(resultado)
        else:
            return False
x = Pessoa()
y = Pessoa()
print(x == y) #1:

#1: Resposta: True.

# Edson Copque | https://linktr.ee/edsoncopque
