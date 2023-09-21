class Multiplicar:
    def __init__(self, func): #1:
        self.func = func

    def __call__(self, *args, **kwargs):
        print(*args, **kwargs)
        return self.func(*args, **kwargs)

@Multiplicar
def soma(x, y):
    return x + y

calculo1 = soma(2, 5) #2:
print(calculo1) #3:

#1: Neste exemplo, parece que "func" é "x + y".
#2: Resposta: 2 5.
#3: Resposta: 7.