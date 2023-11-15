from pathlib import Path
import csv

CAMINHO_CSV = Path(__file__).parent / 'file.csv'
listas_clientes = [ #1:
    {'Nome': 'Edson Copque', 'Endereço': 'Rua das Lágrimas, 100'},
    {'Nome': 'Mel Saints', 'Endereço': 'Rua das Lágrimas, 110'},
    {'Nome': 'Théo Saints', 'Endereço': 'Rua das Lágrimas, 110'},
    {'AAA': 'Valor de A', 'BBB': 'Valor de B'},
]
print(listas_clientes[1]) #2:
print(listas_clientes[0].keys()) #3: #4:
print(listas_clientes[3].keys()) #5:
print(listas_clientes[2].values()) #6:

with open(CAMINHO_CSV, 'w') as file: #10:
    nome_colunas = listas_clientes[0].keys() #9:
    escritor = csv.writer(file) #7:
    escritor.writerow(nome_colunas) #8:
    for indice in listas_clientes: 
        escritor.writerow(indice.values()) #11:

#1: Lembre-se: aqui temos uma lista de dicionários.
#2: Resposta: {'Nome': 'Mel Saints', 'Endereço': 'Rua das Lágrimas, 110'}.
#3: Com ".keys()" é um método usado para obter uma visão dos objetos-chave em um dict.
#4: Resposta: dict_keys(['Nome', 'Endereço']).
#5: Resposta: dict_keys(['AAA', 'BBB']).
#6: Resposta: dict_values(['Valor de A', 'Valor de B']).
#7: "csv.writer(x)" fornece métodos para escrever em arquivos CSV.
#8: ",writenow(y)" é usado para escrever uma linha no arquivo CSV.
#9: Selecionando as "keys" de "Edson Copque".
#10: Agora (aqui é o início do processo) temos nosso arquivo alterado (após rodar código).
#11: Agora podemos iterar adicionando os valores ao nosso arquivo CSV.

''' CONTEÚDO DE file.csv
Nome,Endereço
Edson Copque,"Rua das Lágrimas, 100"
Mel Saints,"Rua das Lágrimas, 110"
Théo Saints,"Rua das Lágrimas, 110"
Valor de A,Valor de B
'''