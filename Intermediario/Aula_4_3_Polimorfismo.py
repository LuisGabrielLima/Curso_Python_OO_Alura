class Programa:

    def __init__(self, nome, ano):
        self._nome = nome.title()
        self.ano = ano
        self._likes = 0
    
    @property
    def likes(self):
        return self._likes
    
    @property
    def nome(self):
        return self._nome
    
    def dar_like(self):
        self._likes += 1
        
    @nome.setter
    def nome(self, novo_nome):
        self._nome = novo_nome.title()

class Filme(Programa):
    
    def __init__(self, nome, ano, duracao):
        super().__init__(nome, ano)
        self.duracao = duracao
        
class Serie(Programa):
    
    def __init__(self, nome, ano, temporadas):
        super().__init__(nome, ano)
        self.temporadas = temporadas

vingadores = Filme("vingadores - guerra infinita", 2018, 160)
atlanta = Serie('atlanta', 2018, 2)
vingadores.dar_like()
atlanta.dar_like()

print(f"Nome: {vingadores.nome} - Ano: {vingadores.ano} - Temporada: {vingadores.duracao} - Likes: {atlanta.likes}")
print(f"Nome: {atlanta.nome} - Ano: {atlanta.ano} - Temporadas: {atlanta.temporadas} - Likes: {atlanta.likes}")  


filmes_e_series = [vingadores, atlanta]

for programa in filmes_e_series:
    # POLIMORFISMO > CONDIÇÃO DE UMA LINHA
    detalhes = programa.duracao if hasattr(programa, 'duracao') else programa.temporadas
    print(f"Nome: {programa.nome} - Ano: {programa.ano} - Temporadas: {detalhes} - Likes: {programa.likes}") 