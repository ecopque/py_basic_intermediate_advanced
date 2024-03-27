from time import sleep #1:
from threading import Thread #2:

class MeuThread(Thread): #3:
    def __init__(self, texto, tempo): #4: #5:
        self.texto = texto #6:
        self.tempo = tempo #7:
        super().__init__() #8:
    def run(self): #9:
        sleep(self.tempo) #10:
        print(self.texto) #11:

t1 = MeuThread('Thread1', 5)
t1.start() #12:
t2 = MeuThread('Thread2', 3)
t2.start() #12:
t3 = MeuThread('Thread3', 2)
t3.start() #12:

for i in range(8): #13:
    print(i) #14: #12:
    sleep(1) #15:
