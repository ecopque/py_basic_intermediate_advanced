class Mamifero: #1:
    def emitir_som(self):
        pass
class Cachorro(Mamifero):
    def emitir_som(self):
        print('Au au...')
class Gato(Mamifero):
    def emitir_som(self):
        print('Miau...')
class Mico(Mamifero):
    def emitir_som(self):
        print('Wiii wiii...')
cachorro = Cachorro() #2:
gato = Gato()
mico = Mico()
mamiferos = [cachorro, gato, mico]
for indice in mamiferos:
    indice.emitir_som() #3: #4:

#1: Classe abstrata (Mamífero). Ela está definindo o comportamento que todos os mamíferos tem (emitir_som). E em cada tipo de mamífero (class) eu coloco um comportamento específico.
#2: Definindo uma instância.
#3: Isso é polimorfismo, ou seja, cada animal vai emitir um som (emitir_som()).
#4: Respostas: Au au... | Miau... | Wiii wiii...