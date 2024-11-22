login = input('[E]ntrar ou [S]air: ')
senha = input('Senha: ')
senha_permitida = '123456'
if (login == 'E' or login == 'e') and senha == senha_permitida:
    print('Você está logado.')
else:
    print('Você saiu.')

# https://linktr.ee/edsoncopque
