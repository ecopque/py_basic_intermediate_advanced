from dataclasses import dataclass, asdict, astuple
@dataclass(frozen=False)
class Pessoa:
    nome: str
    sobrenome: str
if __name__ == '__main__':
    p1 = Pessoa('Edson', 'Copque')
    print(asdict(p1)) #1: #3:
    print(astuple(p1)) #2: #4:
    print(asdict(p1).keys()) #5: 
    print(asdict(p1).values()) #6:
    print(asdict(p1).items()) #7:
    print(astuple(p1)[0]) #8:



#1: Aqui estamos transformando em dict.
#2: Já neste, transformando em tupla.
#3: Resposta: {'nome': 'Edson', 'sobrenome': 'Copque'}.
#4: Resposta: ('Edson', 'Copque').
#5: Resposta: dict_keys(['nome', 'sobrenome']).
#6: Resposta: dict_values(['Edson', 'Copque']).
#7: Resposta: dict_items([('nome', 'Edson'), ('sobrenome', 'Copque')]).
#8: Resposta: Edson.