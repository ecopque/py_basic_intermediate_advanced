import calendar
import locale

# locale.setlocale(locale.LC_ALL, '') #1: #2:
# print(calendar.calendar(2023))    
# print(locale.getlocale()) #3: #4:

locale.setlocale(locale.LC_ALL, 'POSIX') #5:
print(calendar.calendar(2023))



#1: Parece interessante deixar em ALL (LC_ALL).
#2: Usando '', vamos utilizar a localização padrão do nosso sistema operacional.
#3: Apresentará o idioma e encoding.
#4: Resposta: ('pt_BR', 'UTF-8').
#5: Depois de listar no terminal: "locale -a", selecionei POSIX. A saída será diferente de "pt_BR.utf8".
#Link1: https://docs.python.org/3/library/locale.html
