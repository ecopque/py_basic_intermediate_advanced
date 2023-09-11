class MeuError(Exception):
    ...
class OutroError(Exception): #1:
    ...
def levantar():
    exception_ = MeuError('1-Olá', '2-Olá', '3-Olá')
    raise exception_
try:
    levantar()
except (MeuError, ZeroDivisionError) as error:
    print(error.__class__.__name__)
    print(error.args)
    exception_ = OutroError('Vou lançar novamente!') #2:
    raise exception_ from error #3: #4:

#1: Nova criação.
#2: Usando "OutroError".
#3: Vou lançar minha excessão da excessão anterior.
#4: Resposta: __main__.OutroError: Vou lançar novamente!