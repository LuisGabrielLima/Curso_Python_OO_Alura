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
        
    def imprime(self):
        print(f"Nome: {self._nome} - Ano: {self.ano} - Temporada: {self.duracao} Min - Likes: {self._likes}")

class Filme(Programa):
    
    def __init__(self, nome, ano, duracao):
        super().__init__(nome, ano)
        self.duracao = duracao
        
    # POLIMORFISMO
    def imprime(self):
        print(f"Nome: {self._nome} - Ano: {self.ano} - Temporada: {self.duracao} Min - Likes: {self._likes}")
        
class Serie(Programa):
    
    def __init__(self, nome, ano, temporadas):
        super().__init__(nome, ano)
        self.temporadas = temporadas
    
    # POLIMORFISMO
    def imprime(self):
        print(f"Nome: {self._nome} - Ano: {self.ano} - Temporada: {self.temporadas} Temp - Likes: {self._likes}")

vingadores = Filme("vingadores - guerra infinita", 2018, 160)
atlanta = Serie('atlanta', 2018, 2)
vingadores.dar_like()
atlanta.dar_like()

filmes_e_series = [vingadores, atlanta]

# POLIMORFISMO
for programa in filmes_e_series:
    programa.imprime()