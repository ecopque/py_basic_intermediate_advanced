class Pessoa:
    def exibe_cpf(self):
        return '123456789'
class Secretaria(Pessoa): #1:
    pass
class Vendedor(Pessoa): #2:
    pass
s1 = Secretaria()
v1 = Vendedor()
print(s1.exibe_cpf()) #3:
print(v1.exibe_cpf()) #4:

# Edson Copque | https://linktr.ee/edsoncopque
