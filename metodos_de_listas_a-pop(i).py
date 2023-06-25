acessorios = [
    'Rodas de liga', 'Travas elétricas', 'Piloto automático',
    'Bancos de couro', 'Ar condicionado', 'Sensor de estacionamento', 
    'Sensor crepuscular', 'Sensor de chuva'
    ]
acessorios.append('4 x 4')
acessorios.sort()
acessorios.pop() # Retira o último.
acessorios.pop(3) # Remover um item específico da lista pelo seu índice.
print(acessorios)