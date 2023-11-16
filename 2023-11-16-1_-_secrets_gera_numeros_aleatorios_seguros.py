import secrets #1: #2:

import string
from secrets import SystemRandom

print(secrets.randbelow(100)) #3:
print(secrets.choice([10, 15, 20])) #4:

random_seguro = secrets.SystemRandom() #5:
rrange = random_seguro.randrange(10, 20, 2) #6:
rint = random_seguro.randint(10, 20) #7:
runiform = random_seguro.uniform(10, 20) #8:
nomes = ['A', 'B', 'C']
novos_nomes1 = random_seguro.sample(nomes, k=2)
novos_nomes2 = random_seguro.choices(nomes, k=3)
random_seguro.shuffle(nomes)
print(rrange, rint, runiform, nomes, novos_nomes1, novos_nomes2)
print(random_seguro.choice(nomes))

print(string.ascii_letters) #9:
print(string.digits) #10:
print(string.punctuation) #11:

print(''.join(SystemRandom().choices(string.ascii_letters + string.digits +
                              string.punctuation, k=64))) #12:

#1: "secrets" é usado para gerar números aleatórios seguros (cryptographically secure) p/ fins sensíveis à segurança (senhas, tokens de autenticação).
#2: Utiliza fontes específicas de entropia do sistema operacional para garantir uma maior imprevisibilidade, enquanto o módulo random usa um gerador de números pseudoaleatórios (PRNG) que pode ser previsível em algumas circunstâncias.
#3: Gera um número aleatório entre 0 e n-1.
#4: Retorna um elemento aleatório da sequência seq.
#5: O objetivo principal de usar "SystemRandom" é ter um gerador de números aleatórios que utiliza a implementação específica do sistema operacional para gerar números aleatórios criptograficamente seguros.
#6: O mesmo quando utilizamos "random", mas aqui estamos utilizando "secrets.SystemRandom", ou seja, números aleatórios/seguros.
#7: Idem a "random".
#8: Idem a "random".
#9: Resposta: abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ.
#10: Resposta: 0123456789.
#11: Resposta: !"#$%&'()*+,-./:;<=>?@[\]^_`{|}~.
#12: Aqui estou gerando uma senha de 12 caracteres, aleatória e segura.
#13: Resposta: HtY'.~%E0ZI4EbkO&R)KY4t=5'bjKJl9mH#X;LE9C\$C4Iv4cpKxBC~?is1Q}2uf.