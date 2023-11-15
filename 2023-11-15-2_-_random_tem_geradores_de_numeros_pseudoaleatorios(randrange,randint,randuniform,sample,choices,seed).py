import random
aleatorio_range = random.randrange(10, 20) #1:
aleatorio_range2 = random.randrange(10, 20, 5) #2:
aleatorio_int1 = random.randint(10, 20) #3:
aleatorio_uniform1 = random.uniform(10, 20) #4:
print(aleatorio_range, aleatorio_range2, aleatorio_int1,
      aleatorio_uniform1)

nomes = ['Carl Sagan', 'Enéas Carneiro', 'Steven Presfield', 'Baltasar Gracián',
         'Marcus Aurelius']
random.shuffle(nomes) #5:
print(nomes)
novos_nomes1 = random.sample(nomes, k=2) #6:
print(novos_nomes1)
novos_nomes2 = random.choices(nomes, k=3) #7:
print(novos_nomes2)
print(random.choice(nomes)) #8:

#1: Vai gerar um número inteiro, aleatório, dentro do intervalo de 10 (inclusive) e 20 (exclusive).
#2: O terceiro item (5) é o "passo" ou "incremento". Indica que apenas os números múltiplos de 5 serão retornados.
#3: Gera um número inteiro aleatório entre os valores dados, incluindo ambos os extremos.
#4: Gera um número de ponto flutuante aleatório no intervalo especificado, onde 10(inclusive) e 20(inclusive ou exclusive).
#5: Realiza a operação de embaralhar os elementos de uma sequência mutável, como uma lista.
#6: Realiza uma amostragem sem reposição (ou seja, cada elemento é escolhido apenas uma vez) de uma sequência, onde k=2 é o número de elementos a serem mostrados.
#7: Realiza uma amostragem com reposição de uma sequência, ou seja, mesmo elemento pode ser escolhido mais de uma vez.
#8: Escolher aleatoriamente um único elemento de uma sequência.

#Link: https://docs.python.org/pt-br/3/library/random.html

