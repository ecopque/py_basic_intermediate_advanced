import os

caminho1 = os.path.join('/home', 'Edson', 'Copque/Projetos_Python/python392', 'diretorio_temp')

for indice1 in os.listdir(caminho1): #1:
    caminho_completo_pasta = os.path.join(caminho1, indice1)
    # print(caminho_completo_pasta) #3:
    if not os.path.isdir(caminho_completo_pasta):
        continue
    for indice2 in os.listdir(caminho_completo_pasta): #2:
        print(indice2)

#1: Com o primeiro "for" vamos acessar a primeira pasta.
#2: Com o segundo "for", vamos acessar a segunda camada.
#3: Se liberar, vai listar todo conteúdo da pasta "diretorio_temp".