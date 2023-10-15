from datetime import datetime
from pytz import timezone #4: #5: #6:
data1 = datetime.now() #1:
print(data1) #2: #3:
data2 = datetime.now(timezone('Israel')) #7:
print(data2) #8: #9:
data4 = datetime(2020, 3, 10, 7, 37, 51, tzinfo=timezone('Israel')) #10:
print(data4) #11:
data5 = datetime.now()
print(data5.timestamp()) #12: #13:
print(datetime.fromtimestamp(1697327349.845426)) #14:

#1: Obtendo a data e hora atual.
#2: Resposta: 2023-10-14 20:17:13.578895.
#3: Essa numeração final são microsegundos.
#4: Serei obrigado instalar o pytz. Incluir types-pytz p/ não ter erro.
#5: Recomendação: se quiser, desative o ambiente virtual p/ tê-lo full-venv.
#6: pip install pytz types-pytz.
#7: Acesse o link com as timezones. Vou utilizar o formato pelo nome/str (mais fácil).
#8: Resposta: 2023-10-15 02:37:43.090206+03:00.
#9: Observe o +03:00. Significa que estão adiantados 3 horas.
#10 A data especificada mas com timezone de Israel.
#11: Resposta: 2020-03-10 07:37:51+02:21.
#12: timestamp(). Obtendo os segundos desde 1970 (por aí) até hoje. Ver link.
#13: Resposta: 1697327349.845426.
#14: Criando data com/através timestamp/segundos. Isso é muito legal (e preciso)! ;-)
#15: Resposta: 2023-10-14 20:49:09.845426.










# data1 = datetime(2025, 3, 10)
# data2 = datetime(2025, 3, 10, 7)
# data3 = datetime(2025, 3, 10, 7, 37)
# data4 = datetime(2025, 3, 10, 7, 37, 51)
# print(data1) #1: #2:
# print(data2) #3:
# print(data3) #4:
# print(data4) #5:
# data_str = '2025-05-15 15:17:26'
# formato_str = '%Y-%m-%d %H:%M:%S' #6:
# data5 = datetime.strptime(data_str, formato_str)
# print(data5) #7:


#1: Resposta: 2025-03-10 00:00:00.
#2: Perceba que as horas vieram zeradas. Com datetime podemos configurar as horas também.
#3: Resposta: 2025-03-10 07:00:00.
#4: Resposta: 2025-03-10 07:37:00.
#5: Resposta: 2025-03-10 07:37:51.
#6: Aqui no formato precisamos usar as diretivas. Ver documentação do Python.
#7: Resposta: 2025-05-15 15:17:26.