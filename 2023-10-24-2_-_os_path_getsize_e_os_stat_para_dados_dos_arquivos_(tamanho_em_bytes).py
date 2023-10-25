import os
import math
from itertools import count
def formata_tamanho(tamanho_em_bytes: int, base: int = 1000) -> str: #1:
    if tamanho_em_bytes <= 0:
        return '0B'
    abreviacao_tamanhos = 'B', 'KB', 'MB', 'GB', 'TB', 'PB'
    indice_abreviacao_tamanhos = int(math.log(tamanho_em_bytes, base)) #2:
    potencia = base ** indice_abreviacao_tamanhos #3:
    tamanho_final = round(tamanho_em_bytes / potencia, 2) #4:
    abreviacao = abreviacao_tamanhos[indice_abreviacao_tamanhos]
    return f'{tamanho_final} {abreviacao}'
print(formata_tamanho(1_000)) #5:
print(formata_tamanho(1_000_000)) #6:
print(formata_tamanho(1_000_000_000)) #7:
#-> Novo bloco:
caminho1 = os.path.join('/home', 'Edson', 'Copque/Projetos_Python/python392', 'diretorio_temp')
counter = count() #2:
for root, dirs, files in os.walk(caminho1): #1:
    the_counter = next(counter) #3:
    print(the_counter, 'Pasta atual:', root) #4:
    for indice2 in dirs:
        print(' ', the_counter, 'Dirs:', indice2)
    for indice3 in files:
        caminho_completo_arquivo = os.path.join(root, indice3)
        tamanho = os.path.getsize(caminho_completo_arquivo) #8: #9:
        print(' ', the_counter, 'File:', indice3, formata_tamanho(tamanho))

#1: Vai formatar um tamanho de bytes para o tamanho apropriado.
#2: math.log vai retornar o logaritmo do "tamanho_em_bytes". A base padrão é 1024 ou 1000, isso deve bater com nosso indice de abreviação dos tamanhos: 1=B, 2=KB, 3=MB, 4=GB, 5=TB, 6=PB.
#3: Por quanto nosso tamanho deve ser dividido para gerar o tamanho correto.
#4: Este é nosso tamanho final.
#5: Resposta: 1.0 KB
#6: Resposta: 1.0 MB
#7: Resposta: 1.0 GB
#8: Assim, vamos obter o tamanho dos arquivos no terminal.
#9: Poderíamos substituir por: stats = os.stat(caminho_completo_arquivo), tamanho = stats.st_size.
#Link1: https://stackoverflow.com/questions/5194057/better-way-to-convert-file-sizes-in-python