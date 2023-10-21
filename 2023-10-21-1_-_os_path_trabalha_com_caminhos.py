import os

caminho1 = os.path.join('/home/users/', 'Desktop', 'Edson', 'devs_s01.torrent') #1:
print(caminho1) #2:
print(os.path.split(caminho1)) #3: #4:

diretorio1, arquivo1 = os.path.split(caminho1) #5:
print(diretorio1) #6:
print(arquivo1) #7:

nome_arquivo1, extensao_arquivo1 = os.path.splitext(arquivo1) #8:
print(nome_arquivo1)#9:
print(extensao_arquivo1) #10:

completo_caminho1_arquivo1, extensao_arquivo1 = os.path.splitext(caminho1) #11:
print(completo_caminho1_arquivo1) #12:
print(extensao_arquivo1) #13:

print(os.path.exists(caminho1)) #14: #15:
print(os.path.exists('/home/')) #16:

print(os.path.abspath('.')) #17:
print(os.path.basename(caminho1)) #18: #19:
print(os.path.dirname(caminho1)) #20: #21:


#1: Neste exemplo, perceba que "join" vai unir tudo.
#2: Resposta: /home/users/Desktop/Edson/devs_s01.torrent.
#3: Perceba que agora temos o diretório e arquivo. Ver #4:.
#4: Resposta: ('/home/users/Desktop/Edson', 'devs_s01.torrent').
#5: Diretório e arquivo em suas respectivas variáveis.
#6: Resposta: /home/users/Desktop/Edson.
#7: Resposta: devs_s01.torrent.
#8: Estamos obtendo apenas o nome e em seguida a extensão do arquivo.
#9: Resposta: devs_s01.
#10: Resposta: .torrent.
#11: Obtendo o endereço completo + nome do arquivo, para em seguida obter apenas a extensão.
#12: Resposta: /home/users/Desktop/Edson/devs_s01.
#13: Resposta: .torrent.
#14: Verificando se caminho existe.
#15: Resposta: False.
#16: Resposta: True.
#17: Semelhante à "pwd".
#18: basename() é a parte final do seu caminho.
#19: Resposta: devs_s01.torrent.
#20: dirname() é o diretório final.
#21: Resposta: /home/users/Desktop/Edson.