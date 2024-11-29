class A(): #1:
    def __new__(cls):
        return super().__new__(cls) #2:
    
    def __init__(self):
        print('Olá, __init__')

    def __repr__(self):
        return 'Vsf!'
    
a = A()

#1: Poderia fazer "class A(object):", que daria no mesmo.
#2: Em outro momento foi feito: "return object.__new__(A)" e obtivemos o mesmo resultado.

# Edson Copque| https://linktr.ee/edsoncopque
