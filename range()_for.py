for i in range(0, 10, 2): # Criar uma sequência de números de 0 a 9, com um passo de 2 (ou seja, pulando de dois em dois números). A cada iteração do loop for, o valor atual da sequência é armazenado na variável "i".
    print(i) # Resposta 0, 2, 4, 6, 8.
print(list(range(10))) # Cria um objeto range em forma de lista. Resposta [0, 1, 2, 3, 4, 5, 6, 7, 8, 9].
print(i ** 2) # Em cada iteração, o número é elevado ao quadrado. Resposta 0, 1, 4, 9, 16, 25, 36, 49, 64, 81.
##########################################################
quadrado = []
for i in range(10):
   quadrado.append(i ** 2)
print(quadrado)
