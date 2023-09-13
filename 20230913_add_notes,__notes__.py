class MeuError(Exception):
    ...
class OutroError(Exception):
    ...
def levantar():
    exception_ = MeuError('1-Olá', '2-Olá', '3-Olá')
    exception_.add_note('Olha a nota1.') #1:
    raise exception_
try:
    levantar()
except (MeuError, ZeroDivisionError) as error:
    print(error.__class__.__name__)
    print(error.args)
    exception_ = OutroError('Vou lançar novamente!')
    exception_.add_note('Adicionando mais uma nota!') #2:
    exception_.__notes__ += error.__notes__.copy() #3: #4:
    raise exception_ from error

#1: Incluindo notas das exceptions.
#2: Adicionando mas uma nova nota.
#3: Estamos copiando as notas do "error".
#4: Não consegui reproduzir. No site foi citado Python 3.11 (estou usando 3.9.2).
