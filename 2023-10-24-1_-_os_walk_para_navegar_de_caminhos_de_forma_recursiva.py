import os
from itertools import count

caminho1 = os.path.join('/home', 'voyager2', 'voyager2/Projetos_Python/python392', 'diretorio_temp')
counter = count() #2:

for root, dirs, files in os.walk(caminho1): #1:
    the_counter = next(counter) #3:
    print(the_counter, 'Pasta atual:', root) #4:
    
    for indice2 in dirs:
        print(' ', the_counter, 'Dirs:', indice2)

    for indice3 in files:
        print(' ', the_counter, 'File:', indice3)
    

#1: Onde: root = diretório atual, dirs = lista de subdiretórios, files = lista dos arquivos do diretório atual.
#2: Instância da classe count().
#3: Pegando o próximo elemento, será nosso contador.
#4: A resposta será dessa forma: 0 Pasta atual: /home/Edson/...