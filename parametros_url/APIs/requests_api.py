import requests


# PEGAR INFORMAÇÕES - GET

requisicao = requests.get("")
print(requisicao)
print(requisicao.json())

# CRIAR INFORMAÇÕES - POST

data = '{"dicionario python"}'
requisicao = requests.post(link, data=data)
print(requisicao)
print(requisicao.json())


# EDITAR INFORMAÇÕES - PATCH (atualiza informação)

data = '{"dicionario python"}'
requisicao = requests.patch(link, data=data)
print(requisicao)
print(requisicao.json())


# DELETAR INFORMAÇÕES - DELETE

requisicao = requests.delete(link)
print(requisicao)
print(requisicao.json())