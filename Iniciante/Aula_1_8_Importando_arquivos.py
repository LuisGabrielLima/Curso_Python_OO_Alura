# IMPORTAÇÃO DE OUTRO ARQUIVO
import a_1_adivinhacao
import a_2_forca

def escolha_jogo():
    print("##################################")
    print("Escolha o seu jogo!")
    print("##################################")

    print("(1) Forca (2) Adivinhacao")

    jogo = int(input("Qual jogo?"))
    if jogo == 1:
        print("Jogando Forca")
        a_2_forca.jogar()
    elif jogo == 2:
        print("Jogando Adivinhação")
        a_1_adivinhacao.jogar()
        
if(__name__ == "__main__"):
    escolha_jogo()