from collections import namedtuple

Carta = namedtuple('KARTA', ['Valor', 'Naipe'], defaults=['VALOR', 'NAIPE'])
as_espadas = Carta('A', 'Espadas')
print(as_espadas) #5:
print(as_espadas[0]) #1: #2:
print(as_espadas.Valor) #3:
print(as_espadas.Naipe) #4:
print(as_espadas._fields) #6: #7:
as_espadas2 = Carta() #8:
print(as_espadas2) #9:
print(as_espadas2._field_defaults) #10:
print(as_espadas2._asdict()) #11:

#1: Tradicionamente faríamos assim, buscando o índice.
#2: Resposta: A.
#3: Resposta: A.
#4: Resposta: Espadas.
#5: Resposta: KARTA(Valor='A', Naipe='Espadas').
#6: Na documentação a orientação é usar underline: "._fields".
#7: Resposta: ('Valor', 'Naipe').
#8: Como não atribui valor, "defaults=" entrará em ação!
#9: Resposta: KARTA(Valor='VALOR', Naipe='NAIPE').
#10: Resposta: {'Valor': 'VALOR', 'Naipe': 'NAIPE'}.
#11: Resposta: {'Valor': 'VALOR', 'Naipe': 'NAIPE'}.