import os
import shutil

HOME = os.path.expanduser('~') #1:
DESKTOP = os.path.join(HOME, 'Área de trabalho') #3:
PASTA_ORIGINAL = os.path.join(DESKTOP, 'Projeto') #5: #13:
NOVA_PASTA = os.path.join(DESKTOP, 'Nova_Pasta') #7:

os.makedirs(NOVA_PASTA, exist_ok=True) #14: #15:

for root, dirs, files in os.walk(PASTA_ORIGINAL): #9:
    for indice2 in dirs:
        caminho_novo_diretorio = os.path.join(root.replace(PASTA_ORIGINAL, NOVA_PASTA), indice2)
        os.makedirs(caminho_novo_diretorio, exist_ok=True) #19:
    
    for indice1 in files:
        caminho_arquivo = os.path.join(root, indice1)
        caminho_novo_arquivo = os.path.join(root.replace(PASTA_ORIGINAL, NOVA_PASTA), indice1) #17:
        shutil.copy(caminho_arquivo, caminho_novo_arquivo) #20:
        # print(caminho_novo_arquivo) #18:
        # print(caminho_arquivo) #16:
        # print(indice1) #10:
    # for indice2 in dirs:
    #     print(indice2) #11:
    # for indice3 in root:
    #     print(indice3) #12:

print(HOME) #2:
print(DESKTOP) #4:
print(PASTA_ORIGINAL) #6:
print(NOVA_PASTA) #8: