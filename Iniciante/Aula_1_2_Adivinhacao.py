print("##################################")
print("Bem vindo ao jogo de adivinhação")
print("##################################")

numero_secreto = 42

chute = input("Digite o seu número: ")

print("Você digitou ", chute)

if numero_secreto == int(chute):
    print("Você Acertou!")
else:
    print("Você errou!")

print("Fim do jogo")