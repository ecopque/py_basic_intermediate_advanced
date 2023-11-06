import json
from pprint import pprint #5:
from typing import TypedDict #7:

class MovieClass(TypedDict): #8:
    title: str
    original_title: str
    is_movie: bool
    imdb_rating: float
    year: int
    characters: list[str]
    budget: None or float

string_json = '''
{
  "title": "DEVS Série",
  "original_title": "DEVS",
  "is_movie": true,
  "imdb_rating": 7.7,
  "year": 2020,
  "characters": ["Sonoya Mizuno", "Nick Offerman", "Jin Ha", "Alex Garland"],
  "budget": null
}
'''

movie: MovieClass = json.loads(string_json) #1: #2: #9:
print(movie) #3: #4:
pprint(movie) #6:
print(movie['original_title']) #10:
print(movie['characters'][1]) #13:
print()
movie2 = json.loads(string_json)
print(movie2['title']) #11: #12:
print()
print(json.dumps(movie, ensure_ascii=False, indent=2)) #14: #15:


#1: Convertendo essa string em json.
#2: Fique atento pois o que no Python é dict, deve ser bem escrito nos padrões json p/ que conversão ocorra com sucesso.
#3: Resposta: {'title': 'DEVS Série', 'original_title': 'DEVS', 'is_movie': True, 'imdb_rating': 7.7, 'year': 2020, 'characters': ['Sonoya Mizuno', 'Nick Offerman', 'Jin Ha', 'Alex Garland'], 'budget': None}.
#4: Perceba que "budget" é None, ou seja, isto ainda é um dicionário.
#5: Print bonito? Será?
#6: Ficou elegante, mas fora de ordem. Eu passo!
#7: Vamos tipar esse dicionário.
#8: Vamos tipar com Class para facilitar o print.
#9: Adicionamos "MovieClass". Neste passo, vou informar que minha "string_json" é "MovieClass". Antes era: movie = json.loads(string_json).
#10: Resposta: DEVS.
#11: Resposta: DEVS Série.
#12: Este é um dict normal.
#13: Resposta: Nick Offerman.
#14: Aqui estamos "jogando" para json. Precisei usar ensure_ascii como False por conta dos acêntuos. indent=2 para melhorar a visulização (2 espaços).
#15: Resposta: {"title": "DEVS Série", "original_title": "DEVS", "is_movie": true, "imdb_rating": 7.7, "year": 2020, "characters": ["Sonoya Mizuno", "Nick Offerman", "Jin Ha", "Alex Garland"], "budget": null}.
