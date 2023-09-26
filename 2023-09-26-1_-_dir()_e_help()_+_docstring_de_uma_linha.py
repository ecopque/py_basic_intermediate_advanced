import temp #1:

print(dir(temp)) #2:
print(temp.__doc__) #3:

#1: Dentro da mesma pasta, estou importando "temp" que é um arquivo temp.py.
#2: Com este comando, estou verificando o que há dentro daquele arquivo.
#3: Resposta: 5.0 ['__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', 'math', 'operacoes'].
#Obs: Na resposta encontramos 5.0 (que é uma conta realizada no arquivo temp.py).
#Obs2: Também há 'operacoes', que é uma variável com uma operação (que resultou em 5).
#3: Aqui estamos pegando algo baseado no dir(), porém, este .__doc__ é uma built-in function (algo interno, pelo visto) e por isto retornou None.