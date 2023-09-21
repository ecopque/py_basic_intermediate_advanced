class CallMe:
    def __init__(self, phone):
        self.phone = phone
    def __call__(self, nome):
        print(nome, 'está chamando', self.phone)
call1 = CallMe('123456789')
call1('Edson') #1:

#1: Resposta: Edson está chamando 123456789.