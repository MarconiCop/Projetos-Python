
def jogar():

    print("*********************************")
    print("***Bem vindo ao jogo de Forca!***")
    print("*********************************")

    palavra_secreta = "banana"
    letras_acertadas = ["_", "_", "_", "_", "_", "_"]

    enforcou = False
    acertou = False

    print((letras_acertadas))

    #Enquanto não enforcou E não acertou
    while(not enforcou and not acertou):

        chute = input("Digite sua letra: ")
        chute = chute.strip()

        index = 0

        for letra in palavra_secreta:

            if(chute.upper() == letra.upper()):
                letras_acertadas[index] = chute
            index = index + 1

        print(letras_acertadas)

    print("Fim do jogo!")

if(__name__ == "__main__"):
    jogar()






