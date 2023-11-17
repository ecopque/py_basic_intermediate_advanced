import locale #1:
from datetime import datetime #5:
import json
import string
from pathlib import Path

locale.setlocale(locale.LC_ALL, '') #2: #3: #4:

valor_teste = 1234.56
valor_teste_formatado = locale.currency(valor_teste) #6:
print(valor_teste_formatado) #7:

def converte_br(numero: float or int) -> str: #10:
    br1 = 'R$ ' + locale.currency(val=numero, symbol=False, grouping=True) #8: #9:
    return br1
data = datetime(2023, 12, 5)
dados = dict(nome='Edson', valor=converte_br(1_234_56), #12:
             data=data.strftime('%d/%m/%Y'), empresa='IBM', #11:
             telefone='+55 11 999-888-777',
             email='contact@ibm.com')

print(json.dumps(dados, ensure_ascii=False, indent=2))

texto = '''
Prezado(a) ${nome},
Informamos que seu contrato foi estipulado no valor mensal de ${valor}, iniciando no dia ${data}.

Caso deseje questionar este acordo, entre em contato no telefone ${telefone} ou e-mail ${email}.

Atenciosamente,
${empresa}.
'''
template_texto = string.Template(texto) #13:
# print(template_texto.substitute(dados)) #14:
print(template_texto.safe_substitute(dados)) #15:
print('*' * 10)

CAMINHO_ARQUIVO = Path(__file__).parent / 'file100.txt' #16:
with open(CAMINHO_ARQUIVO, 'r') as file:
    leitura = file.read() #17:
    modelagem = string.Template(leitura)
    print(modelagem.substitute(dados))


#1: Este módulo lida com localização e formatação regional. Fornece funções para ajustar a formatação de números, moedas, datas e outras informações sensíveis à localização.
#2: "locale.LC_ALL" representa todas as categorias de localização, ou seja, está configurando a localização para todas as categorias para a configuração padrão do sistema.
#3: "' '" representa a localização desejada, ou seja, quando está vazia tenta usar a localização padrão do sistema.
#4: Este trecho é útil quando você deseja que o programa se adapte à configuração regional do usuário ou do sistema, garantindo que as operações de formatação sejam feitas de acordo com as convenções culturais locais.
#5: Este módulo fornece classes para manipular datas e horas. O principal objetivo é trabalhar com informações de data e hora de forma eficiente e precisa.
#6: "locale.currency()" é usada para formatar um valor como uma string de moeda de acordo com as convenções de formatação da localidade atual.
#7: Resposta: R$ 1234,56.
#8: "symbol=False" removerá o símbolo da moeda (R$) uma vez que já adicionei manualmente.
#9: "grouping=True" adiciona separadores de milhar para melhor legibilidade.
#10: Essa anotação indica que a função retorna uma string (Tipo de Retorno).
#11: "strftime" -> string format time.
#12: Estes "_" não são considerados pelo Python, apenas para eu visualizar melhor.
#13: "string.Template" é uma classe que fornece uma maneira simples e segura de realizar substituições de strings.
#14: ".substitute(x)" é um método utilizado para realizar substituições em um template de string, onde espaços reservados (marcados $) são substituídos por valores específicos.
#15: ".safe_substitute(x)" semelhante ao #14, mas com a diferença que não levanta uma exceção se existirem espaços reservados no template que não foram fornecidos no dicionário.
#16: Lembrando que dentro deste arquivo temos que ter o nosso texto.
#17: "x.read()" é um método usado em objetos de arquivo para ler o conteúdo do arquivo.
#Link: https://docs.python.org/3/library/string.html#template-strings