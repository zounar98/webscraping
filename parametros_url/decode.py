from urllib.parse import urlparse, parse_qs, unquote

url = input("URL: ")

# tratando a query string > quebra de url em categorias/parâmetros
url_tratada = urlparse(url)
parametros_url = parse_qs(url_tratada.query)
print(parametros_url)

# fazendo decode de texto restante
texto_code = input("Texto encoded: ")
print(unquote(texto_code))