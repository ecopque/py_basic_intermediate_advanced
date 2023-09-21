from contextlib import contextmanager

@contextmanager
def my_open(caminho_arquivo, modo):
    print('Abrindo arquivo...')
    arquivo = open(caminho_arquivo, modo, encoding='UTF8')
    yield arquivo
    print('Fechando arquivo...')
    arquivo.close()

with my_open('arquivo.txt', 'w') as arquivo:
    arquivo.write('Linha1\n')
    arquivo.write('Linha2\n')
    arquivo.write('Linha3\n')
    print('With', arquivo) #1: #2: #3:

#1: Resposta: Abrindo arquivo...
#2: Resposta: With <_io.TextIOWrapper name='arquivo.txt' mode='w' encoding='UTF8'>.
#3: Resposta: Fechando arquivo...
