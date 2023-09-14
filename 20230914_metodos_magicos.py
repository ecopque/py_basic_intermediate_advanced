class Pessoa:
    def __init__(self):
        self.pessoas = ['Edson', 'Théo', 'Mel']
x = Pessoa()
print(x) #1: #2:


#Explicação: tudo na linguagem Python são instâncias de alguma classe. Ex: Quando criamos uma variável e colocarmos um número inteiro (x = 1) temos um "class int", ou seja, a variável x é uma instância da classe inteiro. Todos os métodos mágicos na linguagem Python começam e terminam com "dunder" (__init__).
#1: Resposta: <__main__.Pessoa object at 0x7fb494d1efd0>.
#2: Porque temos a resposta de #1? Quando usamos "list", por ex, não vemos este endereço de memória, vejo o valor (conteúdo), mas porque? Porque todas essas classes nativas do Python implementaram o método mágico __str__.
