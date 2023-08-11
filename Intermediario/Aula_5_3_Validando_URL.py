# https://twitter.com/search?q=alura&src=typed_query
# twitter.com     > DOMINIO
# search          > PAGINA DE BUSCA
# q=alura         > CONSULTA
# &               > SEPARADOR DOS PARAMETROS
# src=typed_query > ORIGEM DA CONSULTA

# url = "bytebank.com/cambio?moedaDestino=dolar&quantidade=100&moedaOrigem=real"
url = " "

# SANITIZAÇÃO DA URL
url = url.replace(" ","")
url = url.strip()

# VALIDAÇÃO DA URL
if url == "":
    raise ValueError("A URL está vazia")

# SEPARA BASE E OS PARAMETROS
indice_interrogacao = url.find("?")
url_base = url[0:indice_interrogacao]
url_parametro = url[indice_interrogacao+1:]
print(url_parametro)

# BUSCA VALOR DE UM PARAMETRO
parametro_busca = "quantidade"
indice_parametro = url_parametro.find(parametro_busca)
indice_valor = indice_parametro + len(parametro_busca) + 1
indice_e_comercial = url_parametro.find("&", indice_valor)
if indice_e_comercial == -1:
    valor = url_parametro[indice_valor:]
else:
    valor = url_parametro[indice_valor:indice_e_comercial]
print(valor)