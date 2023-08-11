# https://twitter.com/search?q=alura&src=typed_query
# twitter.com     > DOMINIO
# search          > PAGINA DE BUSCA
# q=alura         > CONSULTA
# &               > SEPARADOR DOS PARAMETROS
# src=typed_query > ORIGEM DA CONSULTA

# url = "bytebank.com/cambio?moedaOrigem=real"
url = "https://bytebank.com/cambio?moedaOrigem=real"
print(url)

# BUSCA ALGO NA STRING
indice_interrogacao = url.find("?")

url_base = url[0:indice_interrogacao]
print(url_base)

url_parametro = url[indice_interrogacao+1:]
print(url_parametro)