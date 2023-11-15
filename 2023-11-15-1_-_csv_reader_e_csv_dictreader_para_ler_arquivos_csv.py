from pathlib import Path
import csv

CAMINHO_CSV = Path(__file__).parent / 'file.csv'
with open(CAMINHO_CSV, 'r') as file:
    leitor = csv.reader(file) #1:
    # next(leitor) #6:
    # print(next(leitor)) #2: #3: 
    # print(next(leitor)) #4:
    # print(next(leitor)) #5:
    for indice1 in leitor:
        print(indice1[0]) #7:
print()
with open(CAMINHO_CSV, 'r') as file2:
    leitor = csv.DictReader(file2) #8:
    for indice2 in leitor:
        print(indice2) #9:
        print(indice2['Idade']) #10:

#1: Com "x.reader()" da lib csv, vai criar um objeto de leitura CSV.
#2: Com "print(next(x))" podemos obter o próximo item de um iterador.
#3: Resposta: ['Nome', ' Idade', ' Endereço'].
#4: Resposta: ['Edson', '50', 'Rua das Lágrimas, n04, "Marte"'].
#5: Resposta: ['Théo', '15', 'Rua das Lágrimas, n02, Marte'].
#6: Este "next(x)" também pode ser usado para pular linhas.
#7: Resposta: Nome | Edson | Théo.
#8: Com "DictReader(x)" permite a leitura de um arquivo CSV como dict por linha.
#9: Resposta: {'Nome': 'Edson', ' Idade': '50', ' Endereço': 'Rua das Lágrimas, n04, "Marte"'} | {'Nome': 'Théo', ' Idade': '15', ' Endereço': 'Rua das Lágrimas, n02, Marte'}.
#10: Resposta: 50 | 15.


''' CONTEÚDO DO ARQUIVO CSV: file.csv
Nome,Idade,Endereço
Edson,50,"Rua das Lágrimas, n04, ""Marte"""
Théo,15,"Rua das Lágrimas, n02, Marte"
'''