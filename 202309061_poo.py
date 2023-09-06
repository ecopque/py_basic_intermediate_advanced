# # Orientação à objetos (POO).
# class Usuario:
#     cargo = 'Usuário' #4:
#     def logar(self): #1: #2:
#         print('Fui chamado.')
#     def sair(self):
#         print('Saindo...')
# usuario1 = Usuario() #3:
# print(usuario1) #5:
# usuario1.logar() #6:
# usuario1.sair() #7:
# print(usuario1.cargo) #8:

# #1: Atributos: valores de determinada classe.
# #2: Método: o que aquela determinada classe faz. É uma função dentro de determinada classe.
# #3: "usuario1" é uma instância da classe Usuario().
# #4: Uma variável dentro de uma classe é chamada de "atributo".
# #5: Resposta: <__main__.Usuario object at 0x7f8b5ff7ffd0>.
# #6: Resposta: Fui chamado.
# #7: Resposta: Saindo...
# #8: Usuário.



class Usuario:
    cargo = 'Usuário' #14:
    def __init__(self, nome, idade, altura): #1: #3:
        print(nome)
        self.x = 1 #4: #11:
        self.altura = altura
    def retorna_altura(self):
        print(self.altura) #12:
    def exibe_cargo(cls):
        print(cls.cargo) #15:
usuario1 = Usuario('Edson', '39', '171') #2: #5:
usuario2 = Usuario('Mel', '10', '183') #6:
print(usuario1.x) #7:
print(usuario2.x) #8:
usuario1.x = 10
print(usuario1.x) #9:
print(usuario2.x) #10:
usuario2.retorna_altura() #13:
usuario1.exibe_cargo() #16:
usuario2.exibe_cargo() #17:
Usuario.cargo = 'Gerente' #18:
usuario1.exibe_cargo() #19:
usuario2.exibe_cargo() #20:

#1: __init__ é um método mágico. É um método especial pois sempre é chamado quando eu crio uma "instância" daquela minha classe.
#2: Aqui uma instância da minha classe, ou seja, quando chamo minha classe e abro e fecho parênteses.
#3: "self" representa o eu, ou seja, a própria instância da classe. Representa o próprio usuário1 e usuário2.
#4: Aqui é o valor de instância onde usuário1 e usuário2 tem acesso.
#5: Resposta: Edson.
#6: Resposta: Mel.
#7: Resposta: 1.
#8: Resposta: 1.
#9: Resposta: 10.
#10: Resposta: 1.
#11: Precisamos usar o "self" pois assim teremos condições de acessar, pois cada variável é seu próprio self (usuario1, usuario2).
#12: Estamos acessando "self.altura" de "def __init__".
#13: Resposta: 183.
#14: Aqui temos um atributo das classes (e não das instâncias), ou seja, será igual para todas as classes.
#15: Vai buscar o atributo de classe "cargo".
#16: Resposta: Usuário.
#17: Resposta: Usuário.
#18: Estamos alterando de toda a classe, de "Usuário" para "Gerente".
#19: Resposta: Gerente.
#20: Resposta: Gerente.