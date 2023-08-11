# ABRIR UM ARQUIVO
arquivo = open("palavras.txt", "w")

# MODOS DE ACESSO AO ARQUIVO
# "w" = ESCREVE > SUBSTITUI TUDO
# "r" = LER
# "a" = ACRESCENTA
# "x" = CRIAR
# "t" = TEXTO
# "n" = BINARIO

# ESCREVENDO EM UM ARQUIVO
arquivo.write("banana\n")
arquivo.write("melancia\n")

arquivo.close()