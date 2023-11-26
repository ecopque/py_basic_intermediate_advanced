import os
import shutil #1:
import pathlib #2: #from pathlib import Path
import zipfile #3: #from zipfile import ZipFile

#Definindo caminhos:
CAMINHO_RAIZ = pathlib.Path(__file__).parent
CAMINHO_PASTA01 = CAMINHO_RAIZ / 'Pasta01'
CAMINHO_ARQUIVO_ZIP = CAMINHO_RAIZ / 'Arquivo01.zip'
CAMINHO_PASTA02_DESCOMPACTADO = CAMINHO_RAIZ / 'Pasta02'

#Limpando caminhos (por segurança):
shutil.rmtree(CAMINHO_PASTA01, ignore_errors=True) #4:
pathlib.Path.unlink(CAMINHO_ARQUIVO_ZIP, missing_ok=True) #5:
shutil.rmtree(str(CAMINHO_ARQUIVO_ZIP).replace('.zip', ''), ignore_errors=True) #6:
shutil.rmtree(CAMINHO_PASTA02_DESCOMPACTADO, ignore_errors=True)

#Criando diretório:
CAMINHO_PASTA01.mkdir(exist_ok=True) #7:

#Criando arquivos:
def criar_arquivos(quantidade: int, zip_diretorio: pathlib.Path):
    for indice1 in range(quantidade): #8:
        nome = 'arquivo_%s' % indice1 #9: #10: #11:
        with open(zip_diretorio / f'{nome}.txt', 'w') as arquivo: #12:
            arquivo.write(nome) #13:
criar_arquivos(10, CAMINHO_PASTA01)

#Compactando arquivos:
with zipfile.ZipFile(CAMINHO_ARQUIVO_ZIP, 'w') as zip_arquivo: #14:
    for root, dirs, files in os.walk(CAMINHO_PASTA01): #15: #16:
        for indice2 in files:
            # print(indice2)
            zip_arquivo.write(os.path.join(root, indice2), indice2) #17:

#Lendo arquivos zip:
with zipfile.ZipFile(CAMINHO_ARQUIVO_ZIP, 'r') as zip_arquivo:
    for indice3 in zip_arquivo.namelist(): #18:
        print(indice3)

#Descompactando/extraindo arquivos zip:
with zipfile.ZipFile(CAMINHO_ARQUIVO_ZIP, 'r') as zip_arquivo:
    zip_arquivo.extractall(CAMINHO_PASTA02_DESCOMPACTADO) #19:


#1: Excelente lib para manipulação de arquivos e diretórios.
#2: "pathlib.Path" para manipulação de caminhos de arquivos e diretórios.
#3: "zipfile.ZipFile" permite criar, ler e extrair arquivos ZIP.
#4: Remover recursivamente (incluindo subdiretórios). "ignore_errors=True" ignora qualquer erro (incluindo diretórios já limpos).
#5: Excluir arquivo específico. "missing_ok=True" não gera erro se o arquivo não existir.
#6: Converte o caminho "Path" em uma string e substitui a extensão ".zip" por uma string vazia (essencialmente removendo a extensão do arquivo). Isso é feito para obter o caminho do diretório pai do arquivo ZIP.
#7: Cria um diretório.
#8: Loop que itera de 0 até "quantidade".
#9: Gerar nomes de arquivos únicos para cada iteração do loop.
#10: "%s" é um marcador de formato que indica que o valor de "indice" deve ser inserido na string naquele ponto.
#11: "%" (na sequência) é o operador de formatação de string, ou seja, "%" é usado para substituir "%s" por "indice" na string.
#12: Abrindo arquivo no modo de escrita ('w') para inserir seu próprio nome.
#13: Escrevendo dados dentro do arquivo.
#14: Abre um arquivo ZIP no modo de escrita ('w') usando o gerenciador de contexto ('with') onde o arquivo ZIP será referenciado como "zip_file".
#15: Uso a função "os.walk()" para percorrer todos os arquivos e diretórios de "CAMINHO_ZIP_DIR" onde "root" é o diretório atual, "dirs" são os subdiretórios e "files" são os arquivos no diretório.
#16: Lembrando que "os.walk()" é uma maneira eficiente de percorrer recursivamente uma árvore de diretórios. Ela gera os nomes de diretórios, subdiretórios e arquivos em um caminho específico.
#17: "os.path.join(root, indice2)": Isso cria o caminho completo para o arquivo atual. "root" contém o caminho para o diretório atual sendo percorrido por "os.walk", e "indice2" é o nome do arquivo. "indice2" (este é o modo): Este é o segundo argumento para o método "write". É o nome que será usado para o arquivo dentro do arquivo zip.
#18: "namelist()" é usado para obter uma lista dos nomes dos arquivos contidos em um arquivo zip.
#19: Extrai todos os arquivos contidos no arquivo zip para o diretório especificado.
