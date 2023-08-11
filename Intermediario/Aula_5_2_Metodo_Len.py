# https://twitter.com/search?q=alura&src=typed_query
# twitter.com     > DOMINIO
# search          > PAGINA DE BUSCA
# q=alura         > CONSULTA
# &               > SEPARADOR DOS PARAMETROS
# src=typed_query > ORIGEM DA CONSULTA

url = "bytebank.com/cambio?moedaDestino=dolar&moedaOrigem=real"

indice_interrogacao = url.find("?")

url_base = url[0:indice_interrogacao]

url_parametro = url[indice_interrogacao+1:]
print(url_parametro)

parametro_busca = "moedaOrigem"
indice_parametro = url_parametro.find(parametro_busca)
print(indice_parametro)

# DEFINI TAMANHO DO PARAMETRO
indice_valor = indice_parametro + len(parametro_busca) + 1
valor = url_parametro[indice_valor:]
print(valor)