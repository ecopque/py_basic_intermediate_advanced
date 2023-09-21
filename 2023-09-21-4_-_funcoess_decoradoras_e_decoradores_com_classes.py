def adiciona_repr(classe_):
    def meu_repr(self):
        class_name = self.__class__.__name__
        class_dict = self.__dict__
        class_repr = f'{class_name}({class_dict})'
        return class_repr
    classe_.__repr__ = meu_repr
    return classe_

@adiciona_repr #5: Eis o decorador com classe.
class Time:
    def __init__(self, nome):
        self.nome = nome

@adiciona_repr
class Planeta:
    def __init__(self, nome):
        self.nome = nome

brasil = Time('Brasil')
portugal = Time('Portugal')

terra = Planeta('Terra')
marte = Planeta('Marte')

print(brasil) #1:
print(portugal) #2:
print(terra) #3:
print(marte) #4:

#1: Resposta: Time({'nome': 'Brasil'}).
#2: Resposta: Time({'nome': 'Portugal'}).
#3: Resposta: Planeta({'nome': 'Terra'}).
#4: Resposta: Planeta({'nome': 'Marte'})

#5: Agora sim!
