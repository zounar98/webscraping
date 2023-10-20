import requests
from bs4 import BeautifulSoup

arquivo = open("arquivo_texto.txt", "w+")
arquivo2 = open("arquivo_url.txt", "w+")

# fazendo requisição
url = "https://pt.wikipedia.org/wiki/Portal:Tecnologia"
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36"}
requisicao = requests.get(url, headers=headers)
print(requisicao) # verifica status code da requisição


# tratando html da requisição
site = BeautifulSoup(requisicao.text, "html.parser")
# print(site.prettify())


# encontrando tags e pegando valores
hoje_na_historia = site.find_all("tbody") # pegando valor texto
links = hoje_na_historia[1].find_all('a', rel="nofollow") # pegando valor URLs


texto_um = hoje_na_historia[1].text # tag com posicionamento na página
print(texto_um, file=arquivo) # salvando texto

for links_compartilhamento in links:
    links_compartilhamento =  links_compartilhamento["href"]
    print(links_compartilhamento, file=arquivo2) # salvando URLs de compartilhamento