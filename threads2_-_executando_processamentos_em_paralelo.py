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

from time import sleep #1:
from threading import Thread #2:

def delay(text, time):
    sleep(time) #3:
    print(text) #4:

t1 = Thread(target=delay, args=('T1 in action', 4))
t1.start()
t2 = Thread(target=delay, args=('T2 in action', 6))
t2.start()
t3 = Thread(target=delay, args=('T3 in action', 2))
t3.start()


for i in range(10):
    print(i)
    sleep(0.5) #5:


#1: Esta função é utilizada para pausar a execução do programa por um determinado tempo, especificado em segundos.
#2: Esta classe permite a criação e manipulação de threads, que são tarefas independentes que podem ser executadas simultaneamente.
#3: Um texto a ser impresso na tela.
#4: O tempo, em segundos, que a função deve esperar antes de imprimir o texto.
#5: Pausa a execução do loop principal por 0.5 segundos a cada iteração.