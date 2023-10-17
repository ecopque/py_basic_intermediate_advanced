from datetime import datetime
from dateutil.relativedelta import relativedelta

valor_total = 1_000_000
data_emprestimo = datetime(2020, 12, 20)
delta_anos = relativedelta(years=5)
data_final = data_emprestimo + delta_anos

hd = []
data_parcela = data_emprestimo

while data_parcela < data_final: #1:
    hd.append(data_parcela)
    data_parcela += relativedelta(months=+1)

numero_parcelas = len(hd) #2:
valor_parcela = valor_total / numero_parcelas

for indice in hd:
    print(indice.strftime('%d/%m/%Y'), f'R${valor_parcela:,.2f}') #3: #4:

print(f'Você fez empréstimo de R${valor_total:,.2f} '
      f'em {numero_parcelas} parcelas '
      f'de R${valor_parcela:,.2f} '
      f'num total de {delta_anos.years} anos.') #5:
      
#1: Enquanto menor, adicionar em "hd" e soma+1.
#2: Conferindo total de parcelas.
#3: Impressão de todos os dias e valor de cada parcela.
#4: Resposta[s]: 20/12/2020 R$16,666.67 (...) [até] 20/11/2025 R$16,666.67.
#5: Resposta: Você fez empréstimo de R$1,000,000.00 em 60 parcelas de R$16,666.67 num total de 5 anos.












