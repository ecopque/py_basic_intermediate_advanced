from dataclasses import dataclass
@dataclass
class Pessoa:
    nome: str
    sobrenome: str
    
    @property
    def nome_completo(self):
        return f'{self.nome} {self.sobrenome}'
    
    @nome_completo.setter
    def nome_completo(self, valor):
        nome, sobrenome = valor.split()
        self.nome = nome
        self.sobrenome = sobrenome

if __name__ == '__main__':
    p1 = Pessoa('Edson', 'Copque')
    print(p1) #2:
    print(p1.nome, p1.sobrenome) #3:
    print(p1.nome_completo) #1: #4:
    p2 = Pessoa('', '')
    p2.nome_completo = 'Sofia Amundsen'
    print(p2) #5:
    print(p2.nome_completo) #6:
    

#1: Se não usar @property, só vai rodar se for: "print(p1.nome_completo())", chamando como funçao.
#2: Resposta: Pessoa(nome='Edson', sobrenome='Copque').
#3: Resposta: Edson Copque.
#4: Resposta: Edson Copque.
#5: Resposta: Pessoa(nome='Sofia', sobrenome='Amundsen').
#6: Resposta: Sofia Amundsen.





