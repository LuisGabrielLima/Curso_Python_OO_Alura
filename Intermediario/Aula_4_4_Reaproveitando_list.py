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
        
    def __str__(self):
        return f"Nome: {self._nome} - Ano: {self.ano} - Temporada: {self.duracao} Temp - Likes: {self._likes}"
        
class Serie(Programa):
    
    def __init__(self, nome, ano, temporadas):
        super().__init__(nome, ano)
        self.temporadas = temporadas

    def __str__(self):
        return f"Nome: {self._nome} - Ano: {self.ano} - Temporada: {self.temporadas} Temp - Likes: {self._likes}"

# HERANÇA EM LISTA   
class Playlist(list):
    def __init__(self, nome, programas):
        self.nome = nome
        super().__init__(programas)

        
vingadores = Filme("vingadores - guerra infinita", 2018, 160)
atlanta = Serie('atlanta', 2018, 2)
tmep = Filme("Todo mundo em panico", 1999, 100)
demolidor = Serie("demolidor", 2016, 2)

vingadores.dar_like()
atlanta.dar_like()
atlanta.dar_like()
tmep.dar_like()
demolidor.dar_like()
demolidor.dar_like()


filmes_e_series = [vingadores, atlanta, demolidor, tmep]
playlist_fim_de_semana = Playlist("fim de semana", filmes_e_series)

for programa in playlist_fim_de_semana:
    print(programa)