dados = [ 
    ['Rodas de liga', 'Travas elétricas', 'Piloto automático', 'Bancos de couro', 'Ar condicionado', 'Sensor de estacionamento', 'Sensor crepuscular', 'Sensor de chuva'],
    ['Central multimídia', 'Teto panorâmico', 'Freios ABS', '4 X 4', 'Painel digital', 'Piloto automático', 'Bancos de couro', 'Câmera de estacionamento'],
    ['Piloto automático', 'Controle de estabilidade', 'Sensor crepuscular', 'Freios ABS', 'Câmbio automático', 'Bancos de couro', 'Central multimídia', 'Vidros elétricos']
]
for lista in dados:
   print(lista)

acessorios = [] # Inicia uma lista vazia chamada "acessorios".
for lista in dados: # Para cada sub-lista "lista" em "dados", faz o seguinte:
   for item in lista: # Aninhado que percorre cada item dentro de cada lista.
      acessorios.append(item) # Para cada item em "lista", adiciona o item à lista "acessorios" usando o método append().
print(acessorios)
#####################################
acessorios = ['Rodas de liga', 'Travas elétricas', 'Piloto automático', 'Bancos de couro', 'Sensor crepuscular', 'Ar condicionado', 'Sensor de estacionamento', 'Sensor crepuscular', 'Sensor de chuva'] # Lista.
print(set(acessorios)) # "set" para criar um conjunto a partir da lista "acessorios". A função "set" remove elementos duplicados da lista, criando um conjunto com os elementos únicos.
print()
print(list(acessorios))
# Estou evitando list comprehension ao máximo. Não há elegância neste tipo de trabalho.

# Edson Copque | https://linktr.ee/edsoncopque
