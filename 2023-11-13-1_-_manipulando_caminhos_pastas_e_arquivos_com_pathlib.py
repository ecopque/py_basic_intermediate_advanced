from pathlib import Path
from shutil import rmtree

caminho_projeto = Path()
print(caminho_projeto) #1: #2:
print(caminho_projeto.absolute()) #3: #4:

caminho_arquivo = Path(__file__) #5:
print(caminho_arquivo) #6:

print(caminho_arquivo.parent) #7: #8:
print(caminho_arquivo.parent.parent) #9: #10:

teste = caminho_arquivo.parent / 'Teste' #11:
print(teste / 'arquivo.txt') #12: #13:

print(Path.home()) #14: #15:
print(Path.home() / 'Teste2' / 'Teste3') #16:

criando_arquivo = (Path.home() / 'voyager2' / 'Projetos_Python' /
                   'python392'/ 'arquivo2.txt') #18:
criando_arquivo.touch() #17:
print(criando_arquivo)

criando_pasta_arquivo = (Path.home() / 'voyager2' / 'Projetos_Python' /
                   'python392'/ 'nova' / 'arquivo3.txt')
criando_pasta_arquivo.parent.mkdir(parents=True, exist_ok=True) #19: #21: #28:
criando_pasta_arquivo.touch()
print(criando_pasta_arquivo) #20:
# criando_pasta_arquivo.unlink() #22:
criando_pasta_arquivo.write_text('Olá, pequeno mundo!\n') #23: #25:
print(criando_pasta_arquivo.read_text()) #24:

# criando_pasta_arquivo.write_text('') #27:

with criando_pasta_arquivo.open('a+') as file: #26:
    file.write('Linha 2\n')
    file.write('Linha 3\n')
    file.write('Linha 4\n')
print(criando_pasta_arquivo.read_text())

nova_pasta = criando_pasta_arquivo.parent / 'nova_subpasta' #29: #30:
nova_pasta.mkdir(parents=True, exist_ok=True)
novo_arquivo = nova_pasta / 'arquivo4.txt' #31:
novo_arquivo.touch()
novo_arquivo.write_text('Olá, brave new world! ;-)\n')
print(novo_arquivo.read_text())

# nova_pasta.rmdir() #32:
# rmtree(nova_pasta) #33:

#Obs: para este exemplo, minha pasta de execução atual é: /home/aaa/bbb/Projetos_Python/python392.
#1: Resposta: "." (sem aspas).
#2: Print do caminho relativo (não absoluto) deste módulo (main1.py).
#3: Agora teremos o caminho absoluto deste módulo (sem o arquivo). Aparentemente é relativo ao diretório executado.
#4: Resposta: /home/aaa/bbb/Projetos_Python. (ainda falta /python392).
#5: "__file__" é o módulo atual, ou seja, vai informar o caminho absoluto com arquivo.
#6: Resposta: /home/aaa/bbb/Projetos_Python/python392/main1.py.
#7: "x.parent" vai indicar o diretório pai do caminho.
#8: Resposta: /home/aaa/bbb/Projetos_Python/python392.
#9: Resposta: /home/aaa/bbb/Projetos_Python.
#10: A cada ".parent" voltamos um nível.
#11: Voltando um nível e "simulando/criando" a pasta "Teste". Obs: no diretório não foi criado pasta.
#12: Printando "teste" e "simulando/adicionado" o doc "arquivo.txt".
#13: Resposta: /home/aaa/bbb/Projetos_Python/python392/Teste/arquivo.txt.
#14: A "home" do usuário.
#15: Resposta: /home/aaa.
#16: Resposta: /home/aaa/Teste2/Teste3.
#17: Em meus testes, não foi possível criar as pastas, apenas os arquivos. Assim funciona o método touch() para criar um arquivo vazio.
#18: Só para constar: os caminhos/diretórios devem já existir previamente.
#19: Agora vamos criar os diretórios "pai" se não existir.
#20: Resposta: /home/aaa/bbb/Projetos_Python/python392/nova/arquivo3.txt.
#21: O argumento "exist_ok=True" evita gerar um erro se o diretório já existir.
#22: Com "unlink()" vamos apagar o arquivo.
#23: Escrevendo dentro do arquivo. ;-)
#24: Lendo o texto do arquivo.
#25: Se quizesse, poderia utilizar ''' - '''.
#26: Abre o arquivo, insere os dados, fecha o arquivo.
#27: Se rodar assim, vai apagar todo texto anterior. Legal!
#28: Importante dizer: usei ".parent" pois o caminho da variável ia até o arquivo.
#29: Criando nova pasta dentro de "criando_pasta_arquivo".
#30: Obs: Não consegui continuar com "/ arquivo4.txt" pois o Python reconheceu como pasta (obviamente).
#31: Agora sim, meu arquivo foi legitimado por "touch()".
#32: "variavel.rmdir()" irá apagar as pastas se estiverem vazias.
#33: Com "rmtree" da lib "shutil" podemos apagar pastas e arquivos.