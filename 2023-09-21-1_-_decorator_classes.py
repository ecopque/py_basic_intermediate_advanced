class Multiplicar:
    def __init__(self, func):
        self.func = func
    
    def __call__(self, *args, **kwargs):
        print(*args, **kwargs) #2:
        return 123456

@Multiplicar #1:
def soma(x, y):
    return x * y

calculo1 = soma(2, 5) #3:
print(calculo1) #4:

#1: Iniciamos com letra maíscula, indicando que é um decorador/classe.
#2: Recebe os valores 2 e 5.
#3: Resposta: 2 5.
#4: Resposta: 123456.