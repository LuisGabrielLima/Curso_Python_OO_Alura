# HERANÇA
class programa:

    def __init__(self, nome, ano):
        self._nome = nome
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

# HERDA HERANÇA
class Filme(programa):
    
    def __init__(self, nome, ano, duracao):
        self._nome = nome.title()
        self.ano = ano
        self.duracao = duracao
        self._likes = 0

# HERDA HERANÇA
class Serie(programa):
    
    def __init__(self, nome, ano, temporadas):
        self._nome = nome.title()
        self.ano = ano
        self.temporadas = temporadas
        self._likes = 0

vingadores = Filme("vingadores - guerra infinita", 2018, 160)
atlanta = Serie('atlanta', 2018, 2)
vingadores.dar_like()
atlanta.dar_like()

print(f"Nome: {vingadores.nome} - Ano: {vingadores.ano} - Temporada: {vingadores.duracao} - Likes: {atlanta.likes}")
print(f"Nome: {atlanta.nome} - Ano: {atlanta.ano} - Temporadas: {atlanta.temporadas} - Likes: {atlanta.likes}")   