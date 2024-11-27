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

# Edson Copque | https://linktr.ee/edsoncopque
