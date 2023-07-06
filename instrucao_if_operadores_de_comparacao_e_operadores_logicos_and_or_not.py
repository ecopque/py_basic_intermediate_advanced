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