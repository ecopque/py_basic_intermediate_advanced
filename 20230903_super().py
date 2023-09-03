class Pessoa:
    def __init__(self, nome, cpf):
        self.nome = nome
        self.cpf = cpf
        print('Classe Pessoa')
    def exibir_extrato(self):
        print('Exibindo extrato!')
class Cliente(Pessoa):
    def __init__(self, nome, cpf, total_compras): #1:
        self.total_compras = total_compras
        super().exibir_extrato() #2:
        super().__init__(nome, cpf) #3:
        print('Classe Cliente')
x = Cliente(nome = 'Edson', cpf = '123456', total_compras = 10)
print(x.total_compras)
print(x.nome) #4: