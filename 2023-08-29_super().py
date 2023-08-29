class Pessoa:
    def __init__(self, nome, cpf):
        self.nome = nome
        self.cpf = cpf
    def exibir_extrato(self):
        print('Exibindo extrato!')
class Cliente(Pessoa):
    def __init__(self, nome, cpf, total_compras):
        self.total_compras = total_compras
    def exibir_extrato(self): #3:
        print('Exibindo extrato2!')
        super().exibir_extrato() #2:
x = Cliente('Edson', '789456', 5)
x.exibir_extrato() #1: