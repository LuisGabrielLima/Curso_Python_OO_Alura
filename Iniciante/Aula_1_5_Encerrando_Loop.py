print("##################################")
print("Bem vindo ao jogo de adivinhação")
print("##################################")

numero_secreto = 42
total_tentativas = 3

for rodada in range(1, total_tentativas+1):
    print("Tentativa {} de {}".format(rodada, total_tentativas))
    chute_str= input("Digite um número entre 1 e 100: ")
    print("Você digitou ", chute_str)

    chute = int(chute_str)
    
    if chute < 1 or chute > 100:
        print("Você deve digitar um número entre 1 e 100!")
        # QUEBRA A INTERAÇÃO
        continue

    acertou = chute == numero_secreto
    maior   = chute > numero_secreto
    menor   = chute < numero_secreto

    if acertou:
        print("Você Acertou!")
        # QUEBRA O LAÇO
        break
    else:
        if maior:
            print("Você errou! O seu chute foi maior do que o numero secreto.")
        elif menor:
            print("Você errou! O seu chute foi menor do que o numero secreto.")

print("Fim do jogo")
