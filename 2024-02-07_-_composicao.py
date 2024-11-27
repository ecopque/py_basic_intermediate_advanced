class Cliente:
    def __init__(self, nome):
        self.nome = nome
        self.enderecos = []
    def inserir_enderecos(self, rua, numero):
        self.enderecos.append(Endereco(rua, numero))
    def listar_enderecos(self):
        for endereco in self.enderecos:
            print(endereco.rua, endereco.numero)
    def __del__(self):
        print('Apagando »', self.nome)
class Endereco:
    def __init__(self, rua, numero):
        self.rua = rua
        self.numero = numero
    def __del__(self):
        print('Apagando »', self.rua, self.numero)
cliente1 = Cliente('Maria')
cliente1.inserir_enderecos('Rua 01', 10)
cliente1.inserir_enderecos('Rua 02', 15)
cliente1.listar_enderecos() #1:
del cliente1 #2:
print('*** Aqui termina meu código...') #3:

# Edson Copque | https://linktr.ee/edsoncopque
