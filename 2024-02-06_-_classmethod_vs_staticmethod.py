class Usuario:
    cargo = 'Usuário'
    def __init__(self, nome, idade, altura):
        self.altura = altura
    @classmethod
    def altura_usuario(cls):
        cls.cargo = 'Gerente'
        print(cls.cargo)
usuario1 = Usuario('Edson', '39', '171')
usuario1.altura_usuario() #1:
Usuario.altura_usuario() #2:
