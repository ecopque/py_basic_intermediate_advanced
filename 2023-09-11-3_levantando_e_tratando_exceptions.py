class MeuError(Exception):
    ...
def levantar():
    exception_ = MeuError('1-Olá', '2-Olá', '3-Olá')
    raise exception_
try:
    1/0 #1:
    levantar()
except (MeuError, ZeroDivisionError) as error: #2:
    print(error.__class__.__name__) #3:
    print(error.args) #4:
    
#1: Adicionamos esta conta errada p/ obter um erro específico.
#2: Além de MeuError, adicionamos outro erro bem específico: Zero DivisinoError.
#3: Resposta: ZeroDivisionError.
#4: Resposta: ('division by zero',)

# Edson Copque | https://linktr.ee/edsoncopque
