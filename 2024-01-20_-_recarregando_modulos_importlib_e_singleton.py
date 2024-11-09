import importlib #1:
import repeticao #2: #3: #4:
print(repeticao.variavel_sobrenome) #5: #6:
for indice in range(10): #7:
    importlib.reload(repeticao) #8:
    print(indice) #9:
print(str('Fim'), __name__) #10:
