import requests

url = input("url:")
requisicao = requests.get(url)
print(requisicao)
print(requisicao.json())