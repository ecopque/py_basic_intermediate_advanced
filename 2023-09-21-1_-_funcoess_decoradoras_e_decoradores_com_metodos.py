def adiciona_repr(classe_):
    def meu_repr(self):
        class_name = self.__class__.__name__
        class_dict = self.__dict__
        class_repr = f'{class_name}({class_dict})'
        return class_repr
    classe_.__repr__ = meu_repr
    return classe_

@adiciona_repr #5:
class Time:
    def __init__(self, nome):
        self.nome = nome

@adiciona_repr
class Planeta:
    def __init__(self, nome):
        self.nome = nome
    def falar_nome(self):
        return f'O planeta é {self.nome}'

brasil = Time('Brasil')
portugal = Time('Portugal')
terra = Planeta('Terra')
marte = Planeta('Marte')

print(terra.falar_nome()) #1:
print(marte.falar_nome()) #2:

#1: Resposta: O planeta é Terra.
#2: Resposta: O planeta é Marte.