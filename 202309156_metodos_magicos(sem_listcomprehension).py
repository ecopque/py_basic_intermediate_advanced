class Pessoa:
    def __init__(self):
        self.pessoas = ['Edson', 'Neto', 'Théo', 'Mel']
    def __reversed__(self):
        reversed_list = []
        for i in range(len(self.pessoas) - 1, -1, -1):
            reversed_list.append(self.pessoas[i])
        return reversed_list
x = Pessoa()
print(list(reversed(x)))  #1: #2:
print(reversed(x)) #3:

#1: Converter o resultado de reversed para lista.
#2: Resposta: ['Mel', 'Théo', 'Neto', 'Edson'].
#3: Resposta: ['Mel', 'Théo', 'Neto', 'Edson'].