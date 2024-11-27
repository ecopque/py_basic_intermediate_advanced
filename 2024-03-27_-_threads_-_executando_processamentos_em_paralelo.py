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

#1: A função "sleep" é usada para pausar a execução do programa para um número específico de segundos.
#2: A classe "Thread" permite que você crie threads, que são unidades independentes de execução dentro de um programa.
#3: Herda da classe "Thread". Isso significa que objetos "MeuThread" terão funcionalidades de uma thread.
#4: Definindo o construtor "__init__" da classe "MeuThread". O construtor é chamado sempre que um novo objeto "MeuThread" é criado.
#5: O argumento "texto" representa o texto que a thread irá imprimir. O argumento  "tempo" representa o número de segundos que a thread irá dormir antes de imprimir o texto.
#6: Esta linha atribui o valor do argumento texto ao atributo texto do objeto.
#7: Esta linha atribui o valor do argumento tempo ao atributo tempo do objeto.
#8: Esta linha chama o construtor da classe pai (Thread) para inicializar o objeto da thread corretamente.
#9: O método run é o ponto de entrada principal da thread. Quando você inicia uma thread, o interpretador Python chama seu método run em uma thread separada. 
#10: Esta linha usa a função sleep para pausar a execução da thread pelo número de segundos especificado pelo atributo tempo.
#11: Esta linha imprime o valor do atributo texto no console.
#12: Resposta: ver imagem.
#13: Esta linha inicia um loop que itera 8 vezes.
#14: Dentro do loop, esta linha imprime o valor atual da variável de loop i no console, que será (0, 1, 2, 3, 4, 5, 6, 7).
#15: Esta linha pausa a execução do programa principal por 1 segundo.

# Edson Copque | https://linktr.ee/edsoncopque
