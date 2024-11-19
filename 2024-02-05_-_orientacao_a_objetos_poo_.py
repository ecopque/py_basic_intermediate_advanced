class Usuario:
    cargo = 'Usuário' #14:
    def __init__(self, nome, idade, altura): #1: #3:
        print(nome)
        self.x = 1 #4: #11:
        self.altura = altura
    def retorna_altura(self):
        print(self.altura) #12:
    def exibe_cargo(cls): #21:
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
