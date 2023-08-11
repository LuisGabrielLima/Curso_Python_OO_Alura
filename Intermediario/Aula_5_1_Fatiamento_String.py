# https://twitter.com/search?q=alura&src=typed_query
# twitter.com - DOMINIO
# search - PAGINA DE BUSCA
# q=alura > CONSULTA
# & > SEPARADOR DOS PARAMETROS
# src=typed_query > ORIGEM DA CONSULTA

# url = "https://bytebank.com/cambio?moedaOrigem=real&moedaDestino=dolar&quantidade=100"
url = "bytebank.com/cambio?moedaOrigem=real"
print(url)

# FATIAMENTO DA STRING
url_base = url[0:19]
print(url_base)

url_parametro = url[20:36]
print(url_parametro)