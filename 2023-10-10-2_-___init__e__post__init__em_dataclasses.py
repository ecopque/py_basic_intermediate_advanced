from dataclasses import dataclass

@dataclass(init=False) #1:
class Pessoa:
    nome: str
    sobrenome: str
    # def __post_init__(self, nome, sobrenome): #2:
    def __init__(self, nome, sobrenome): #3:
        self.nome = nome
        self.sobrenome = sobrenome
        self.nome_completo = f'{self.nome} {self.sobrenome}'
    def __post_init__(self):
        print('Ainda estou vivo?') #7:

if __name__ == '__main__':
    p1 = Pessoa('Edson', 'Copque')
    print(p1) #4:
    print(p1.nome, p1.sobrenome) #5:
    print(p1.nome_completo) #6:

#1: Aqui estamos eliminando o __init__. Sendo assim, como podemos usar __post_init__()? Impossível.
#2: Inseri alguns argumentos e mantive __post__init(). Resultado? Erro no código!
#3: Eis a solução: criamos nosso __init__(), agora nosso dataclass funcionará perfeitamente bem!
#4: Resposta: Pessoa(nome='Edson', sobrenome='Copque').
#5: Resposta: Edson Copque.
#6: Resposta: Edson Copque.
#7: Não, você não está vivo. Não vai rodar __post_init__(), game over!
#Obs: Perdemos nosso __post_init__() para sempre. RIP. :-/