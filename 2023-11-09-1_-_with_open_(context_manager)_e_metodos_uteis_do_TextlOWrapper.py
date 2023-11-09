with open('novo_arquivo4.txt', 'w+') as arquivo:
    arquivo.writelines(('Linha1\n', 'Linha2\n', 'Linha3\n'))
    arquivo.seek(0, 0)
    for linha in arquivo.readlines(): #1.
        print(linha.strip())

#1. Em Python, o método readlines() é usado para ler todas as linhas de um arquivo e retorná-las como uma lista de strings. Cada string na lista representa uma linha do arquivo, incluindo o caractere de nova linha (\n) no final de cada linha. A chamada ao método readlines() percorre o arquivo a partir da posição atual do ponteiro de leitura até o final do arquivo, lendo todas as linhas encontradas. Ele retorna a lista contendo todas as linhas.
