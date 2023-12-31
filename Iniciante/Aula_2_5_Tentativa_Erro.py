def jogar():
    print("##################################")
    print("Bem vindo ao jogo de Forca")
    print("##################################")
    
    palavra_secreta = "banana".upper()
    letras_acertadas = ["_","_","_","_","_","_",]
    
    enforcou = False
    acertou = False
    erros = 0
    
    while not enforcou and not acertou:
        
        chute = input("Qual letra ?")
        chute = chute.strip().upper()
        
        if chute in palavra_secreta: 
            index = 0  
            for letra in palavra_secreta:
                if chute == letra:
                    letras_acertadas[index] = letra
                index += 1
        else:
            erros += 1
            
        # QUANTIDADE DE ERROS POSSIVEIS
        enforcou = erros == 6
        # FINALIZAÇÃO APOS O ACERTO
        acertou = "_" not in letras_acertadas
        print(letras_acertadas)
    if acertou:
        print("Você ganhou!")
    else:
        print("Você perdeu!")
    print("Fim do jogo!")
    
if(__name__ == "__main__"):
    jogar()