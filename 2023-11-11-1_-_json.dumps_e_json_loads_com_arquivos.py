import json
import os

NOME_ARQUIVO = 'main2.json' #1:
CAMINHO_ABSOLUTO_ARQUIVO = os.path.abspath( #2:
    os.path.join( #3:
        os.path.dirname(__file__), #4: #5: #6: #7:
        NOME_ARQUIVO
    )
)

print(__file__) #8:
print(os.path.dirname(__file__)) #9:
print(os.path.join(os.path.dirname(__file__), NOME_ARQUIVO)) #10:

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
print(json.loads(string_json)) #11:

dict_movie = {
    'title': 'DEVS Série',
    'original_title': 'DEVS',
    'is_movie': True,
    'imdb_rating': 7.7,
    'year': 2020,
    'characters': ['Sonoya Mizuno', 'Nick Offerman', 'Jin Ha', 'Alex Garland'],
    'budget': None} #12: #13:
print(dict_movie)

with open(CAMINHO_ABSOLUTO_ARQUIVO, 'w') as arquivo: #14:
    json.dump(dict_movie, arquivo, ensure_ascii=False, indent=2) #15:

with open(CAMINHO_ABSOLUTO_ARQUIVO, 'r') as arquivo2: #16:
    json_movie = json.load(arquivo2) #17:
    print(json_movie)

#1: Vou salvar algo neste arquivo.
#2: abs = absoluto. "os.path.abspath()" é uma função do módulo os.path que retorna o caminho absoluto (caminho completo a partir da raiz do sistema de arquivos) de um determinado caminho especificado como argumento. Isso é útil para converter caminhos relativos (caminhos em relação ao diretório de trabalho atual) em caminhos absolutos.
#3: "os.path.join()" é uma função do módulo os.path que é usada para construir caminhos de arquivo de forma adequada, independentemente do sistema operacional em que o código está sendo executado. Essa função recebe um ou mais argumentos representando partes do caminho e os combina em um único caminho completo, garantindo que os separadores de diretório sejam apropriados para o sistema operacional em questão.
#4: "os.path.dirname()" é uma função do módulo os.path que é usada para obter o diretório pai de um caminho de arquivo ou diretório. Em outras palavras, ela extrai o componente de diretório de um caminho, deixando de lado o nome do arquivo.
#5: Então, estamos pedindo o diretório pai deste arquivo (__file__).
#6: "__file__" é uma variável especial em Python que se refere ao arquivo do qual o código está sendo executado. Ela contém o caminho relativo ou absoluto do arquivo Python em execução. Geralmente, esse atributo é usado em módulos e scripts Python para referenciar o próprio arquivo.
#7: Por exemplo, se você tiver um script Python chamado "meu_script.py" e o executar, "meu_script.py" será o arquivo atual. Da mesma forma, se você estiver trabalhando com um projeto contendo vários módulos e executar um deles, o módulo em execução será o arquivo atual. A variável __file__ é definida automaticamente pelo interpretador.
#8: Resposta: /home/aaa/bbb/Projetos_Python/python392/main1.py.
#9: Resposta: /home/aaa/bbb/Projetos_Python/python392.
#10: Resposta: /home/aaa/bbb/Projetos_Python/python392/main2.json.
#11: Resposta: {'title': 'DEVS Série', 'original_title': 'DEVS', 'is_movie': True, 'imdb_rating': 7.7, 'year': 2020, 'characters': ['Sonoya Mizuno', 'Nick Offerman', 'Jin Ha', 'Alex Garland'], 'budget': None}.
#12: Observe que peguei o resultado de #11 e inseri nessa nova string (manualmente), agora temos um dict.
#13: Poderia ter colocado dentro de uma variável, tipo: xxx = json.loads(string_json).
#14: Lembrando que se o arquivo não existir, será criado.
#15: Escreve o conteúdo do dicionário dict_movie no arquivo. O módulo json é usado para serializar o objeto Python em uma representação JSON e gravá-lo no arquivo.
#16: Agora vamos ler nosso arquivo.
#17: A simples leitura do arquivo json.