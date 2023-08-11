# ABRIR UM ARQUIVO
arquivo = open("palavras.txt", "r")

# MODOS DE ACESSO AO ARQUIVO
# "w" = ESCREVE > SUBSTITUI TUDO
# "r" = LER
# "a" = ACRESCENTA
# "x" = CRIAR
# "t" = TEXTO
# "n" = BINARIO

# LENDO UM ARQUIVO
# print(arquivo.read())
for linha in arquivo:
    print(linha)

arquivo.close()
