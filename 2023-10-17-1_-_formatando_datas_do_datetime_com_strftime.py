from datetime import datetime

data1 = datetime (2020, 12, 13, 7, 20, 15) #1:
print(data1) #2:

data2 = datetime.strptime('2022-12-13 07:20:15', '%Y-%m-%d %H:%M:%S') #3:
print(data2) #4:

formato_data = '%d/%m/%Y' #5:
print(data2.strftime(formato_data)) #6:

formato_data2 = '%d/%m/%Y %H:%M' #7:
print(data2.strftime(formato_data2)) #8:

print(data2.strftime('%Y'), data2.year) #9: #10:

#1: Formato utilizado até aqui (pelo datetime).
#2: Resposta: 2020-12-13 07:20:15.
#3: Sem utilizar variável, direto. Observe o "-".
#4: Resposta: 2022-12-13 07:20:15.
#5: Definindo formato com "/" e dia/mês/ano.
#6: Resposta: 13/12/2022.
#7: Adicionei hora e minuto.
#8: Resposta: 13/12/2022 07:20.
#9: Observe que primeiro temos uma string e depois pegamos a data direto da variável.
#10: Respostas: 2022 /// 2022.