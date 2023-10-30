import os
import shutil
HOME = os.path.expanduser('~')
DESKTOP = os.path.join(HOME, 'Área de trabalho')
PASTA_ORIGINAL = os.path.join(DESKTOP, 'Projeto')
NOVA_PASTA = os.path.join(DESKTOP, 'Nova_Pasta')

shutil.rmtree(NOVA_PASTA, ignore_errors=True) #1: #3:
shutil.copytree(PASTA_ORIGINAL, NOVA_PASTA) #2:
shutil.move(NOVA_PASTA, NOVA_PASTA + '2') #4:

#1: Bem simples, vamos apagar "NOVA_PASTA".
#2: Vamos copiar "PASTA_ORIGINAL" como "NOVA_PASTA".
#3: Com "ignore_erros" vai ignorar qualquer erro desta linha.
#4: Estamos movendo para um "novo local"/name chamado "NOVA_PASTA2".




# os.makedirs(NOVA_PASTA, exist_ok=True) #14: #15:
# for root, dirs, files in os.walk(PASTA_ORIGINAL): #9:
#     for indice2 in dirs:
#         caminho_novo_diretorio = os.path.join(root.replace(PASTA_ORIGINAL, NOVA_PASTA), indice2)
#         os.makedirs(caminho_novo_diretorio, exist_ok=True) #19:
#     for indice1 in files:
#         caminho_arquivo = os.path.join(root, indice1) #21:
#         caminho_novo_arquivo = os.path.join(root.replace(PASTA_ORIGINAL, NOVA_PASTA), indice1) #17:
#         shutil.copy(caminho_arquivo, caminho_novo_arquivo) #20:
#         # print(caminho_novo_arquivo) #18:
#         # print(caminho_arquivo) #16:
#         # print(indice1) #10:
#     # for indice2 in dirs:
#     #     print(indice2) #11:
#     # for indice3 in root:
#     #     print(indice3) #12:
# print(HOME) #2:
# print(DESKTOP) #4:
# print(PASTA_ORIGINAL) #6:
# print(NOVA_PASTA) #8:

#Obs: Com "$echo HOME" vamos obter a home do usuário.
#1: Aponta para "home" do sistema.
#2: Resposta: /home/voyager2.
#3: "HOME" + 'Área de trabalho'.
#4: Resposta: /home/voyager2/Área de trabalho.
#5: "DESKTOP" + 'Projeto'.
#6: Resposta: /home/voyager2/Área de trabalho/Projeto
#7: "DESKTOP" + 'Nova_Pasta'.
#8: Resposta: /home/voyager2/Área de trabalho/Nova_Pasta.
#9: Acessando os arquivos de "PASTA_ORIGINAL".
#10: Irá listar todos os arquivos de: /home/voyager2/Área de trabalho/Projeto.
#11: Irá listar todas as pastas de: /home/voyager2/Área de trabalho/Projeto.
#12: Virou uma bagunça. Apresentou por letra todas as pastas.
#13: Obs: tive que criar essa pasta na mão, pois estes comandos até então não criaram pastas.
#14: Agora sim, estamos criando uma nova pasta. Sua localização será: /home/voyager2/Área de trabalho/Nova_Pasta.
#15: Se não utilizar "exist_ok=True", ao rodar o código novamente dará erro, pois já teremos a pasta.
#16: Aqui vamos imprimir o caminho com arquivo. Ex: /home/voyager2/Área de trabalho/Projeto/eee.jpg. (...)
#17: Perceba: Vai trocar o caminho "PASTA_ORIGINAL" por "NOVA_PASTA". Por isso o replace(). Obs: mas não copiou os arquivos p/ a nova pasta.
#18: Agora temos a "PASTA_ORIGINAL" com seus arquivos antigos e a "NOVA_PASTA" vazia. Ainda!
#19: Agora sim, vamos copiar as pastas para "NOVA_PASTA".
#20: Realizando cópia dos arquivos.

#21: Aqui, você está criando o caminho completo para um arquivo dentro do diretório original. root representa o caminho da pasta atual, e indice1 é o nome do arquivo. Isso cria o caminho completo para o arquivo no diretório original.
