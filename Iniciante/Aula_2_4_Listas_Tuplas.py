# TUPLA
tupla = (1,2)

# LISTA DE TUPLAS
t1 = (3,4)
t2 = (5,6)
t3 = (7,8)

listaT = [t1, t2, t3]
print(listaT)

p1 = ("Pedro", 28)
p2 = ("Vinicius", 23)

listaP = [p1, p2]
print(listaP)

# ACESSAR ELEMENTOS DA TUPLA
print(listaP[0][1])

# TRANSFORMAR LISTA EM TUPLA
lista = [1,2]
lista = tuple(lista)
print(lista)

# TRANSFORMAR TUPLA EM LISTA
tupla = (1,2)
tupla = list(tupla)
print(tupla)