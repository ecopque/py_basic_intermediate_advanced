from dataclasses import dataclass
@dataclass
class Pessoa:
    nome: str
    sobrenome: str

    def __post_init__(self): #1:
        self.nome_completo = f'{self.nome} {self.sobrenome}'

if __name__ == '__main__':
    p1 = Pessoa('Edson', 'Copque')
    print(p1) #2:
    print(p1.nome, p1.sobrenome) #3:
    print(p1.nome_completo) #4:

#1: É um método que é chamado logo quando termina o __init__ da dataclasse.
#2: Resposta: Pessoa(nome='Edson', sobrenome='Copque').
#3: Resposta: Edson Copque.
#4: Resposta: Edson Copque.