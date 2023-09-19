class MyContextManager():
    def __init__(self, caminho_arquivo, modo):
        print('Init')
        self.caminho_arquivo = caminho_arquivo
        self.modo = modo
    
    def __enter__(self):
        print('Enter: abrindo arquivo')
        return open(self.caminho_arquivo, self.modo, encoding='utf8') #1:
    
    def __exit__(self, class_exception, exception_, traceback_):
        print('Exit: fechando arquivo')

instancia = MyContextManager('app.py', 'w')
with instancia as arquivo:
    print('With', arquivo)

#1: Quando for abrir um arquivo sem "with", devemos fechá-lo.
# Concluído.
