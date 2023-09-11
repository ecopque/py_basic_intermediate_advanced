class MeuError(Exception):
    ...
def levantar():
    exception_ = MeuError('1-Olá', '2-Olá', '3-Olá') #1:
    raise exception_
try:
    levantar()
except MeuError as error:
    print(error.args) #2:
    
#1: Exemplo de como colocar várias coisas.
#2: Outra forma, mesmo resultado: print(error).