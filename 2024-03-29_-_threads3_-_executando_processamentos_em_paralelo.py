# from time import sleep #1:
# from threading import Thread #2:
# class MeuThread(Thread): #3:
#     def __init__(self, texto, tempo): #4: #5:
#         self.texto = texto #6:
#         self.tempo = tempo #7:
#         super().__init__() #8:
#     def run(self): #9:
#         sleep(self.tempo) #10:
#         print(self.texto) #11:
# t1 = MeuThread('Thread1', 5)
# t1.start() #12:
# t2 = MeuThread('Thread2', 3)
# t2.start() #12:
# t3 = MeuThread('Thread3', 2)
# t3.start() #12:
# for i in range(8): #13:
#     print(i) #14: #12:
#     sleep(1) #15:
###
# from time import sleep #1:
# from threading import Thread #2:

# def delay(text, time):
#     sleep(time) #3:
#     print(text) #4:
# t1 = Thread(target=delay, args=('T1 in action', 4))
# t1.start()
# t2 = Thread(target=delay, args=('T2 in action', 6))
# t2.start()
# t3 = Thread(target=delay, args=('T3 in action', 2))
# t3.start()
# for i in range(10):
#     print(i)
#     sleep(0.5) #5:
###
# from time import sleep #1:
# from threading import Thread #2:
# def delay(text, time):
#     sleep(time) #3:
#     print(text) #4:
# t1 = Thread(target=delay, args=('T1 in action', 10)) #5:
# t1.start() #6:
# while t1.is_alive(): #7:
#     print('Waiting for thread...') #8:
#     sleep(2) #9:
# print('Thread is over!')

from time import sleep #1:
from threading import Thread #2:
from threading import Lock #3:

class tickets:
    def __init__(self, stock): #4:
        self.stock = stock #5:
        self.lock = Lock() #6:

    def buy(self, amount): #7:
        self.lock.acquire() #8:
        if self.stock < amount: #9:
            print('We don\'t have enough tickets.')
            self.lock.release() #10:
            return
        
        sleep(1) #11:

        self.stock -= amount #12:
        print(f'You purchased {amount} tickets. We still have {self.stock} in stock.')
    
        self.lock.release()

if __name__ == '__main__': #13:
    tickets1 = tickets(10) #14:

    for i in range(1, 20): #15:
        t = Thread(target=tickets1.buy, args=(i,)) #16:
        t.start() #17:

#1: Essa função permite pausar a execução do programa por um determinado tempo (em segundos).
#2: A classe Thread permite a execução de várias operações em paralelo.
#3: Um objeto Lock é usado para sincronizar o acesso a partes compartilhadas do código entre várias threads.
#4: Ele recebe um argumento stock que representa o estoque inicial de ingressos. 
#5: Atribui o valor do parâmetro stock ao atributo de instância stock, representando o estoque de ingressos.
#6: Este objeto será usado para sincronizar o acesso ao estoque de ingressos entre várias threads.
#7: Define um método chamado buy que representa a compra de ingressos. Recebe um parâmetro amount, representando a quantidade de ingressos a serem comprados.
#8: Adquire o bloqueio antes de acessar o estoque de ingressos, garantindo que apenas uma thread possa acessar o estoque de cada vez.
#9: Verifica se há ingressos suficientes disponíveis para compra.
#10: Libera o bloqueio após a conclusão do acesso ao estoque de ingressos.
#11: Simula um pequeno atraso de 1 segundo.
#12: Subtrai a quantidade de ingressos comprados do estoque disponível.
#13: Verifica se o script está sendo executado diretamente.
#14: Cria uma instância da classe tickets com um estoque inicial de 10 ingressos.
#15: Loop que itera de 1 a 19.
#16: Cria uma nova thread que chama o método buy da instância tickets1, passando i como argumento.
#17: Inicia a execução da thread criada. Este loop cria várias threads que tentarão comprar ingressos ao mesmo tempo. O uso do objeto Lock garante que apenas uma thread possa acessar o estoque de ingressos por vez, evitando problemas de concorrência.

# Edson Copque | https://linktr.ee/edsoncopque
