from datetime import datetime

data1 = datetime(2025, 3, 10)
data2 = datetime(2025, 3, 10, 7)
data3 = datetime(2025, 3, 10, 7, 37)
data4 = datetime(2025, 3, 10, 7, 37, 51)
print(data1) #1: #2:
print(data2) #3:
print(data3) #4:
print(data4) #5:

data_str = '2025-05-15 15:17:26'
formato_str = '%Y-%m-%d %H:%M:%S' #6:
data5 = datetime.strptime(data_str, formato_str)
print(data5)


#1: Resposta: 2025-03-10 00:00:00.
#2: Perceba que as horas vieram zeradas. Com datetime podemos configurar as horas também.
#3: Resposta: 2025-03-10 07:00:00.
#4: Resposta: 2025-03-10 07:37:00.
#5: Resposta: 2025-03-10 07:37:51.
#6: Aqui no formato precisamos usar as diretivas. Ver documentação do Python.