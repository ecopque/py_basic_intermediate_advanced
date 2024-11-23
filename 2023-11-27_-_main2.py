import sys #7:
import os

# Teoria / Teste simples:
print(sys.argv) #1: #2:
print(len(sys.argv)) #3: #4:

if len(sys.argv) <= 1:
    print('Você não passou argumentos!')
else:
    print(f'Você passou os argumentos {sys.argv[1:]}') #5: #6:

# 1/4. Processar diretório:
def proc_dir(caminho): #8:
    for indice1 in os.listdir(caminho):
        print(indice1)

# 2/4. Verifica argumento:
if __name__ == "__main__": #9:
    if len(sys.argv) != 2:
        print('Uso: python3 meu_script.py <caminho_do_diretorio>')
        sys.exit(1)

# 3/4. Obter caminho do diretório:
caminho_diretorio = sys.argv[1] #10:

# 4/4. Chama função:
proc_dir(caminho_diretorio) #11:


#1: "sys.argv" é uma lista em Python que contém os argumentos passados para um script quando ele é executado a partir da linha de comando.
#2: Resposta: ['main.py'].
#3: Executei no terminal: 'python3 main.py "listar"'. Obs: sem aspas simples.
#4: Resposta: 2.
#5: Resposta: Você passou os argumentos ['listar'].
#6: Lembre-se: considere 2 argumentos, pois o primeiro sempre será o "main.py" (nosso módulo, neste caso).
#7: Posso usar essa lista para fazer com que meu script responda a diferentes argumentos da linha de comando. Isso é útil para scripts que precisam de entrada variável ou que podem ser configurados de maneira diferente com base nos argumentos fornecidos.
#8: Processando diretório.
#9: Verifica se um argumento (caminho do diretório) foi fornecido.
#10: Obtém o caminho do diretório a partir do argumento.
#11: Chama a função para processar o diretório.

# Edson Copque | https://linktr.ee/edsoncopque
