from dataclasses import dataclass

@dataclass(frozen=True) #1:
class Pessoa:
    nome: str
    sobrenome: str
    
if __name__ == '__main__':
    p1 = Pessoa('Edson', 'Copque')
    # p1.nome = 'Carl' #2:
    print(p1)


#1: Com "frozen" podemos congelar nossa dataclasse.
#2: Observe que não podemos alterar.