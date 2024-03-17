#[terminal]$: pip install requests types-requests bs4 #1:
#[terminal]$: python3 -m http.server -d site/ 3333 #2:

import requests #6:
from bs4 import BeautifulSoup #7:

url = 'http://127.0.0.1:3333/' #8:
response = requests.get(url) #9:
raw_html = response.text #10:
parsed_html = BeautifulSoup(raw_html, 'html.parser') #3: #11:
print(parsed_html.title) #4: #12:
print(parsed_html.title.text) #5: #13:

#[graphic]: (click/direito/browser) inspecionar > <h2>tag TOP 3 jobs</h2> == $0 > (click/direito) copy > copy selector #14:
top_jobs_heading = parsed_html.select_one('#intro > div:nth-child(1) > div:nth-child(1) > article:nth-child(1) > h2:nth-child(1)') #15:
print(top_jobs_heading) #16:
print(top_jobs_heading.text) #17:

article = top_jobs_heading.parent #18:
print(article) #19:

for i in article.select('p'): #20:
    print(i.text) #21:

#Definição: Web scraping é uma técnica usada para extrair dados de sites da web. Envolve a análise e a extração de informações de páginas da web de forma automatizada, geralmente por meio de um script ou programa. Esses dados extraídos podem ser salvos em um banco de dados, arquivo CSV, ou qualquer outro formato útil para análise posterior. Existem várias bibliotecas em Python que facilitam o web scraping, como Beautiful Soup, Scrapy e Selenium. Essas bibliotecas permitem que os desenvolvedores naveguem pelas páginas da web, localizem os elementos desejados (como texto, imagens, links, etc.) e extraiam essas informações para uso posterior. O web scraping é frequentemente usado para coletar dados para análise, pesquisa, monitoramento de preços, geração de leads, entre outras aplicações.
#Obs1: Ainda utilizamos index.html, style.css e nosso servidor localhost das aulas anteriores.
#1: A biblioteca Python chamada bs4, ou Beautiful Soup 4, é uma poderosa ferramenta para análise e extração de dados de documentos HTML e XML. É frequentemente usada em conjunto com outras bibliotecas, como requests, para realizar web scraping de forma eficiente e fácil. Aqui estão algumas características principais da Beautiful Soup: Análise de HTML/XML: Beautiful Soup permite analisar documentos HTML/XML e navegar pela estrutura do documento de forma simples e intuitiva. Seletores CSS e XPath: Ele fornece métodos para localizar elementos dentro do documento usando seletores CSS ou XPath, tornando mais fácil encontrar e extrair os dados desejados. Manipulação de dados: Beautiful Soup facilita a extração de texto, atributos, links e outros elementos específicos de uma página da web. Tratamento de documentos malformados: Pode lidar com documentos HTML/XML malformados e fornecer uma estrutura de árvore coerente para trabalhar. Integração com parsers: Beautiful Soup suporta vários parsers, incluindo o parser padrão Python, html.parser, bem como parsers externos mais rápidos, como lxml e html5lib.
#2: Quando você executa este comando no terminal, um servidor HTTP local será iniciado no diretório especificado, e os arquivos dentro desse diretório estarão disponíveis através do endereço http://localhost:3333/ em seu navegador da web, onde localhost se refere ao seu próprio computador.
#3: Pode parecer igual ao "raw_html" mas é que agora temos objetos python.
#4: Resposta: <title>Site localhost</title>.
#Obs2: Se no brwoser clicar com botão direito na página e escolher "Inspecionar Site", vamos ter o código fonte. E passando o mouse, vamos observar ao que se refere no site. 
#5: Resposta: Site localhost.
#6: Importa a biblioteca requests, que permite enviar solicitações HTTP em Python.
#7: BeautifulSoup é uma biblioteca usada para analisar documentos HTML e XML.
#8: Este é o endereço para o qual uma solicitação HTTP será feita para obter o conteúdo HTML da página.
#9: Faz uma solicitação GET para o URL especificado na variável url usando o método get() da biblioteca.
#10: Extrai o texto bruto da resposta HTTP e o armazena na variável raw_html.
#11: Cria um objeto BeautifulSoup chamado parsed_html, passando o texto bruto da resposta HTTP e o parser HTML para ele. Isso analisa o HTML e cria uma árvore de objetos que representam a estrutura do documento HTML.
#12: Imprime a tag title do documento HTML analisado. Isso imprime a tag HTML <title> e seu conteúdo.
#13: Imprime o texto contido na tag title do documento HTML. Isso imprime apenas o texto dentro da tag HTML <title>.
#14: Este é um comentário que fornece instruções sobre como obter um seletor CSS para um elemento específico no navegador.
#15: Usa o método select_one() do BeautifulSoup para selecionar o elemento HTML que corresponde ao seletor CSS fornecido. Neste caso, ele seleciona o cabeçalho <h2> que representa os "TOP 3 jobs". Ver #14.
#16: Resposta: <h2>TOP 3 jobs</h2>.
#17: Resposta: TOP 3 jobs.
#18: Obtém o elemento pai do cabeçalho <h2> selecionado.
#19: Obtemos o conteúdo textual do trecho desta página. Imprime o elemento pai do cabeçalho <h2>.
#20: Para cada parágrafo <p> dentro do elemento pai, faz o seguinte:
#21: Imprime o texto contido em cada parágrafo <p>.
#Documentação Beaultiful Soup: https://www.crummy.com/software/BeautifulSoup/bs4/doc.ptbr/.