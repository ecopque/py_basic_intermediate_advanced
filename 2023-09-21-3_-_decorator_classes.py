class Multiplicar:
    def __init__(self, func):
        self.func = func
        self._multiplicador = 10

    def __call__(self, *args, **kwargs):
        resultado = self.func(*args, **kwargs)
        return resultado * self._multiplicador

@Multiplicar
def soma(x, y):
    return x + y
calculo1 = soma(2, 5) #1:
print(calculo1) #2:

#1: Ficará morto, sem resposta alguma.
#2: Resposta: 70.