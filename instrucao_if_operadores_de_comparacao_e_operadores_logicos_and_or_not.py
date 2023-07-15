dados = [
    ['Jetta Variant', 2003, False],
    ['Passat', 1991, False],
    ['Crossfox', 1990, False],
    ['DS5', 2019, True],
    ['Aston Martin DB4', 2006, False],
    ['Palio Weekend', 2012, False],
    ['A5', 2019, True],
    ['Série 3 Cabrio', 2009, False],
    ['Dodge Jorney', 2019, False],
    ['Carens', 2011, False]
]
for lista in dados: # Começa um loop for que percorre cada item da lista 'dados'.
   if(lista[2] == True): # Verifica se o valor na terceira posição (índice 2) da lista é igual a True.
    print(lista) # Se a condição for verdadeira, imprime a lista. Caso contrário, passa para o próximo item da lista. Resposta: ['DS5', 2019, True], ['A5', 2019, True].
#########################################
zero_km_y = [] # Cria uma lista vazia.
for lista in dados: # Itera sobre a lista "dados" usando um loop for, onde em cada iteração uma sublista é armazenada na variável "lista".
   if(lista[2] == True): # Verifica se o valor do terceiro elemento da sublista é igual a True usando uma condicional if.
      zero_km_y.append(lista) # Se a condição for verdadeira, a sublista é adicionada à lista "zero_km_y" usando o método "append".
print(zero_km_y) # Resposta: [['DS5', 2019, True], ['A5', 2019, True]].
###############################################
zero_km_n = []
for lista in dados:
   if(lista[2] == False): # Verifica se o terceiro elemento de lista é "False".
      zero_km_n.append(lista) # Adiciona a sublista atual (lista) à lista "zero_km_n" se o terceiro elemento for False.
print(zero_km_n) # Resposta: [['Jetta Variant', 2003, False], ['Passat', 1991, False], ['Crossfox', 1990, False], ['Aston Martin DB4', 2006, False], ['Palio Weekend', 2012, False], ['Série 3 Cabrio', 2009, False], ['Dodge Jorney', 2019, False], ['Carens', 2011, False]].
