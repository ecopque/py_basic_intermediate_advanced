import os
# from dotenv import load_dotenv #type: ignore #10:
from dotenv import main

# bash: export SENHA='Valor que eu quero' #1: #2: #3:
# bash: echo $SENHA #4: #15:
print(os.getenv('SENHA')) #5: #6: #9:
senha = os.getenv('SENHA')
print(senha) #7: #8:

# load_dotenv() #13:
main.load_dotenv() #11: #12:
# print(os.environ) #14:

print(os.getenv('BASEDADOS_PASSWORD')) #16:


#Obs: Ao encontrar um arquivo tipo ".env-example" eu devo saber que preciso criar o meu ".env" (dotenv).
#Obs2: Nunca envie seu ".env" para o repositório, apenas o ".env-example" como exemplo (sem os dados).
#1: Foi digitado no terminal.
#2: Isto é uma variável de ambiente. São variáveis cujos valores podem ser configurados fora do código do programa e são acessíveis por esse programa durante sua execução. Elas são usadas para fornecer informações externas ou configurações que podem ser necessárias para o funcionamento do programa.
#3: Se eu fechar o terminal, essa variável de ambiente vai sumir.
#4: Aqui estamos acessando esta variável pelo terminal.
#5: Como não fechei o terminal, posso visualizar pela IDE.
#6: Resposta: Valor que eu quero.
#7: Resposta: Valor que eu quero.
#8: Em meus testes, até aqui, ao abrir outro terminal o resultado é: None.
#9: "os.getenv('x')" é uma maneira de obter/recuperar o valor de uma variável de ambiente externo.
#10: "Por algum motivo, estava apontando erro. Ignorei.
#11: Usaria o #13, mas não funcionou (importação). Pertence à biblioteca python-dotenv e é usada para carregar variáveis de ambiente a partir de um arquivo chamado .env no seu projeto Python. Este é um método comum para armazenar configurações sensíveis, como chaves de API ou informações de banco de dados, fora do código-fonte para evitar expor informações confidenciais em repositórios de controle de versão.
#12: Para trabalhar com esta função, criei o arquivo ".env" (dot env). Dentro dele coloquei alguns dados, são eles: BASEDADOS_USER="eneascarneiro", BASEDADOS_PASSWORD="Ordem1000Progresso", BASEDADOS_PORT=56, BASEDADOS_HOST="localhost".
#13: A documentação recomenda importar: "from dotenv import load_dotenv" e então usar "load_dotenv()". Por algum motivo deu erro, então, fiz um import recomendado no "stackoverflow", link no final.
#14: Resposta: environ({'SHELL': '/bin/bash', 'SESSION_MANAGER': 'local/...
#15: Resposta: Valor que eu quero.
#16: Resposta: Ordem1000Progresso.


# pip install python-dotenv (faça no ambiente virtual/vs-code)
# Link StackOverflow: https://stackoverflow.com/questions/59622868/why-can-i-not-import-load-dotenv
# Link Documentação: https://pypi.org/project/python-dotenv/