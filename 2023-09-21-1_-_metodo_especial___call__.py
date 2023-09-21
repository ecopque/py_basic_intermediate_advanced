class CallMe:
    def __init__(self, phone):
        self.phone = phone
    
    def __call__(self, *args, **kwargs):
        print('Chamando', self.phone)

call1 = CallMe('123456789')
call1() #1: #2:
call1(123) #3: #4:

#1: Agora podemos fazer desta forma pois criamos o "def __call__". Caso contrário, teríamos que usar o "print(call1)".
#2: Resposta: Chamando 123456789.
#3: Fiz como teste e não gerou nenhum erro. Rodou como se não houvesse números.
#4: Resposta: Chamando 123456789.
