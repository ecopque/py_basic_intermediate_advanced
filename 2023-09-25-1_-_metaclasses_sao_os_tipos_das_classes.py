class Meta(type): #1:
    def __new__(mcs, name, bases, dct):
        print('Metaclass New')
        cls = super().__new__(mcs, name, bases, dct)
        return cls

class Pessoa(metaclass = Meta):
    def __new__(cls, *args, **kwargs):
        print('Meu New')
        instancia = super().__new__(cls)
        return instancia
    
    def __init__(self, nome):
        print('Meu Init')
        self.nome = nome

p1 = Pessoa('Edson') #2:

#1: Essa é a metaclass.
#2: Respostas: Metaclass New | Meu New | Meu Init.