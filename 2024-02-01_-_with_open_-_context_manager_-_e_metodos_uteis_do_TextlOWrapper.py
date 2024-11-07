caminho_arquivo = '/home/voyager3/voyager3/Projetos_Python/'
caminho_arquivo += 'novo_arquivo4.txt'
with open(caminho_arquivo, 'w') as arquivo: #1:
    arquivo.write('Linha 1, amigo.\n') #2:
    arquivo.write('Linha 2, friend.')
with open(caminho_arquivo, 'r') as arquivo: #3:
    print(arquivo.read()) #4:
