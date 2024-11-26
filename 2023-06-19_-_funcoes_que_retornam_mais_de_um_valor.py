dados = {
   'Crossfox': {'km': 35000, 'ano': 2005},
   'DS5': {'km': 15000, 'ano': 2017},
   'Corolla': {'km': 180000, 'ano': 2007}
}
def km_media(dataset, ano_atual):
   resultado = {}
   for itens in dataset.items():
      operacao = itens[1]['km'] / (ano_atual - itens[1]['ano'])
      resultado.update({itens[0] : operacao})
   return resultado
print(km_media(dados, 2019)) # Resposta: {'Crossfox': 2500.0, 'DS5': 7500.0, 'Corolla': 15000.0}.

# Edson Copque | https://linktr.ee/edsoncopque
