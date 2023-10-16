from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta

formato_dh = '%d/%m/%Y %H:%M:%S' #1:
data_inicio = datetime.strptime('10/10/2010 07:10:10', formato_dh)
data_fim = datetime.strptime('05/05/2023 08:00:00', formato_dh)

print(data_fim > data_inicio) #2:
print(data_fim < data_inicio) #3:
print(data_fim == data_inicio) #4:
print(data_fim - data_inicio) #5: #6:

delta = data_fim - data_inicio
print(delta.days, delta.seconds, delta.microseconds) #7:
print(delta.total_seconds()) #8: #9:

delta_2 = timedelta(days=10, hours=2)
print(data_fim + delta_2) #10: #11:
print(data_fim + relativedelta(seconds=10))

delta_3 = relativedelta(data_fim, data_inicio)
print(delta_3) #14:

#1: Modelo de formato, onde: dia/mês/ano hora:minuto:segundo.
#2: Resposta: True.
#3: Resposta: False.
#4: Resposta: False.
#5: Obtendo a diferença, chamado "timedelta".
#6: Resposta: 4590 days, 0:49:50.
#7: Resposta: 4590 2990 0.
#8: Obtendo todos os segundos de "delta".
#9: Resposta: 396578990.0.
#10: Somando mais 10 dias e 2 horas à minha data_fim.
#11: Resposta: 2023-05-15 10:00:00.
#12: Instalando dateutil: pip install python-dateutil types-python-dateutil.
#13: Resposta: 2023-05-05 08:00:10.
#14: Resposta: relativedelta(years=+12, months=+6, days=+25, minutes=+49, seconds=+50).