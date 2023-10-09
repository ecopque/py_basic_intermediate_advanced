from dataclasses import dataclass
@dataclass #1:
class Pessoa:
    nome: str
    idade: int

if __name__ == '__main__':
    p1 = Pessoa('Edson', 75)
    p2 = Pessoa('Edson', 75)
    print(p1) #2:
    print(p1 == p2) #3:

#1: Com esta declaração, você obtém automaticamente um construtor "__init__()"", um método "__repr__()" para representação em string e métodos de comparação "__eq__()" e "__ne__()".
#2: Resposta: Pessoa(nome='Edson', idade=75).
#3: Resposta: True.