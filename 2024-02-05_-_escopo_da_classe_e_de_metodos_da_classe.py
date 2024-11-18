class Animal:
    def __init__(self, parametro):
        self.nome = parametro
        variavel = 'Iniciando...'
        print(variavel)
    def acao(self, parametro2):
        return f'{self.nome} está comendo {parametro2}'
    def executar(self, *args, **kwargs):
        return self.acao(*args, **kwargs)
cachorro = Animal(parametro='Théo')
print(cachorro.nome) #1: #2:
print(cachorro.acao(parametro2='Semente de Abóbora.')) #3:
print(cachorro.executar(parametro2='ração')) #4:
