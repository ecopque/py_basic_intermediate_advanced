class MeuError(Exception):
    ...
def levantar():
    raise MeuError('A mensagem do meu erro.')
try:
    levantar()
except MeuError as error:
    print(error) #1:
#1: Resposta: A mensagem do meu erro.