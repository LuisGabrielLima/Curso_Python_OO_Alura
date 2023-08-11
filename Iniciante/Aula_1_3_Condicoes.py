print("##################################")
print("Bem vindo ao jogo de adivinhação")
print("##################################")

numero_secreto = 42

chute_str= input("Digite o seu número: ")
print("Você digitou ", chute_str)

chute = int(chute_str)

acertou = chute == numero_secreto
maior   = chute > numero_secreto
menor   = chute < numero_secreto

# CONDIÇÕES
if acertou:
    print("Você Acertou!")
else:
    if maior:
        print("Você errou! O seu chute foi maior do que o numero secreto.")
    elif menor:
        print("Você errou! O seu chute foi menor do que o numero secreto.") 

print("Fim do jogo")
