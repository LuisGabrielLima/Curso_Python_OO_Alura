'''
VALIDA

bytebank.com/cambio
bytebank.com.br/cambio
www.bytebank.com/cambio
www.bytebank.com.br/cambio
http://www.bytebank.com/cambio
http://www.bytebank.com.br/cambio
https://www.bytebank.com/cambio
https://www.bytebank.com.br/cambio

INVALIDA

https://bytebank/cambio
https://bytebank.naoexiste/cambio
ht://bytebank.naoexiste/cambio
'''

'''
# https://www.bytebank.com.br/cambio

import re

url = "https://www.bytebank.com.br/cambio"

padrao_url = re.compile("(http(s)?://)?(www.)?bytebank.com(.br)?/cambio")
match = padrao_url.match(url)

if not match:
    raise ValueError("A URL não é valida")

print("A URL é valida")
'''

# APLICANDO NO CODIGO

import re

class ExtratorURL:
    def __init__(self, url):
        self.url = self.sanitiza_url(url)
        self.valida_url()
        
    def sanitiza_url(self, url):
        if  type(url) == str:
            return url.strip()
    
    def valida_url(self):
        if not self.url:
            raise ValueError("A URL está vazia")
        
        padrao_url = re.compile("(http(s)?://)?(www.)?bytebank.com(.br)?/cambio")
        match = padrao_url.match(self.url)

        if not match:
            raise ValueError("A URL não é valida")
        
    def get_url_base(self):
        indice_interrogacao = self.url.find("?")
        url_base = self.url[0:indice_interrogacao]
        return url_base
    
    def get_url_parametro(self):
        indice_interrogacao = self.url.find("?")
        url_parametro = self.url[indice_interrogacao+1:]
        return url_parametro
    
    def get_valor_parametro(self, parametro_busca):
        indice_parametro = self.get_url_parametro().find(parametro_busca)
        indice_valor = indice_parametro + len(parametro_busca) + 1
        indice_e_comercial = self.get_url_parametro().find("&", indice_valor)
        if indice_e_comercial == -1:
            valor = self.get_url_parametro()[indice_valor:]
        else:
            valor = self.get_url_parametro()[indice_valor:indice_e_comercial]
        return valor

extator_url = ExtratorURL("bytebank.com/cambio?moedaDestino=dolar&quantidade=100&moedaOrigem=real")
valor_quantidade = extator_url.get_valor_parametro("quantidade")