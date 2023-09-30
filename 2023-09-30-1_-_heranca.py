class Pessoa:
    def __init__(self, nome, cpf, altura):
        self.nome = nome
        self.cpf = cpf
        self.altura = altura
class Secretaria(Pessoa): #1:
    pass
class Vendedor(Pessoa): #2:
    pass
s1 = Secretaria('Mel', 123456, 171)
v1 = Vendedor('Théo', 987654, 173)
print(s1.cpf) #3:
print(v1.cpf) #4: