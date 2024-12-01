class Pessoa:
    def __init__(self):
        self.pessoas = ['Edson', 'Neto', 'Théo', 'Mel']
    def __len__(self) -> int:
        x = 0 #1:
        while True: #2:
            try:
                y = self.pessoas[x]
                x += 1 #3:
            except:
                break
        return x
x = Pessoa()
print(len(x)) #4:

#1: Contador.
#2: Enquanto for verdade (loop infinito).
#3: A cada iteração de y, x recebe mais um.
#4: Resposta: 4.

# Edson Copque | https://linktr.ee/edsoncopque
