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
    def __iter__(self):
        i = 0
        while i < len(self.pessoas):
            yield self.pessoas[i]
            i += 1
minha_pessoa = Pessoa()
for i in minha_pessoa:
    print(i) #1:

#1: Resposta: Edson, Neto, Théo, Mel.

# Edson Copque | https://linktr.ee/edsoncopque
