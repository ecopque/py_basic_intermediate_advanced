class CallMe:
    def __init__(self, phone):
        self.phone = phone
    def __call__(self, nome):
        print(nome, 'está chamando', self.phone)
        return 123456 #1:
call1 = CallMe('123456789')
ligacao = call1('Edson') #2:
print(ligacao) #3:

#1: Adicionado, veja resposta do print.
#2: Resposta: Edson está chamando 123456789.
#3: Resposta: 123456.