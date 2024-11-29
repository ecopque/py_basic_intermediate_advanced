class MyContextManager():
    def __init__(self, caminho_arquivo, modo):
        print('Init')
        self.caminho_arquivo = caminho_arquivo
        self.modo = modo
        self._arquivo = None
    
    def __enter__(self):
        print('Enter: abrindo arquivo')
        self._arquivo = open(self.caminho_arquivo, self.modo, encoding='utf8') #1:
        return self._arquivo
    
    def __exit__(self, class_exception, exception_, traceback_):
        print('Exit: fechando arquivo')
        self._arquivo.close() #2:


instancia = MyContextManager('app.txt', 'w')
with instancia as arquivo:
    arquivo.write('Linha 1\n') #4:
    arquivo.write('Linha 2\n')
    arquivo.write('Linha 3\n')
    print('With', arquivo) #3:

#1: Abrindo arquivo: quando for abrir um arquivo sem "with", devemos fechá-lo.
#2: Fechando arquivo.
#3: Resposta: Init | Enter: abrindo arquivo | With <_io.TextIOWrapper name='app.txt' mode='w' encoding='utf8'> | Exit: fechando arquivo.
#4: Inserindo informações no "arquivo".
# Concluído.

# Edson Copque | https://linktr.ee/edsoncopque
