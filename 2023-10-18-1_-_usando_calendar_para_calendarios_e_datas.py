import calendar
print(calendar.calendar(2000)) #1:
print(calendar.month(2000, 11)) #2:
print(calendar.monthrange(2000, 12)) #3: #4: #5:
print(list(calendar.day_name)) #6:
print(list(enumerate(calendar.day_name))) #7:
primeiro_dia, ultimo_dia = calendar.monthrange(2000, 12) #8:
print(calendar.day_name[primeiro_dia]) #9:
print(calendar.weekday(2000, 12, primeiro_dia)) #10: #11: #12:
print(calendar.monthcalendar(2023, 12)) #13: #14:
for indice in calendar.monthcalendar(2023, 12):
    print(list(enumerate(indice))) #15: #16:

#1: Imprimindo calendário do ano 2000.
#2: Printando calendário do ano 2000, mês 11.
#3: Printando o último dia do mês.
#4: Resposta: (4, 31).
#5: Entendendo: este número 4 é o dia da semana em que o mês começa, ou seja, sexta-feira. 0 -> segunda-feira, 6 -> domingo. Já 31, o dia.
#6: Resposta: ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'].
#7: Resposta: [(0, 'Monday'), (1, 'Tuesday'), (2, 'Wednesday'), (3, 'Thursday'), (4, 'Friday'), (5, 'Saturday'), (6, 'Sunday')].
#8: Considere 4 e 31 (as respostas).
#9: Resposta: Friday.
#10: Perceba: ano, mês, dia.
#11: Usado para obter o dia da semana correspondente a uma data específica.
#12: Resposta: 0.
#13: Ano 2023, mês dezembro. Cada "[ ]" representa uma semana, e onde está 0 não são deste mês.
#14: Resposta: [[0, 0, 0, 0, 1, 2, 3], [4, 5, 6, 7, 8, 9, 10], [11, 12, 13, 14, 15, 16, 17], [18, 19, 20, 21, 22, 23, 24], [25, 26, 27, 28, 29, 30, 31]].
#15: [(0, 0), (1, 0), (2, 0), (3, 0), (4, 1) (...).
#16: Entenda: segunda-fora, terça-fora, quarta-fora, quinta-fora, sexta-dentro (este é nosso mês).