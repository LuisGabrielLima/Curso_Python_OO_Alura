class Filme:
    
    def __init__(self, nome, ano, duracao):
        self.nome = nome
        self.ano = ano
        self.duracao = duracao
        
class Serie:
    
    def __init__(self, nome, ano, temporadas):
        self.nome = nome
        self.ano = ano
        self.temporadas = temporadas

vingadores = Filme("vingadores - guerra infinita", 2018, 160)
# f > Tem a mesma funcionalidade do ".format()"
print(f"Nome: {vingadores.nome} - Ano: {vingadores.ano} - Temporada: {vingadores.duracao}")
atlanta = Serie('atlanta', 2018, 2)
print(f"Nome: {atlanta.nome} - Ano: {atlanta.ano} - Temporadas: {atlanta.temporadas}")