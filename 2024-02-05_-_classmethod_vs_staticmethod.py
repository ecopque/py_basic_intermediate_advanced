class Usuario:
    cargo = 'Usuário' #6:
    def __init__(self, nome, idade, altura):
        self.altura = altura #5:
    @classmethod
    def altura_usuario(cls): #4:
        print(cls.cargo)
usuario1 = Usuario('Edson', '39', '171')
usuario1.altura_usuario() #1:
Usuario.altura_usuario() #2: #3:

# Edson Copque | https://linktr.ee/edsoncopque
