import random

def jogar():
    print("*********************************")
    print("***Bem vindo ao jogo da Forca!***")
    print("*********************************")

    arquivo = open("palavras.txt","r")
    palavras = []

    for linha in arquivo:
        linha = linha.strip()
        palavras.append(linha)

    arquivo.close()

    numero = random.randrange(0, len(palavras))

    palavra_secreta = palavras[numero].upper()

    letras_acertadas = ["_" for letra in palavra_secreta]

    enforcou = False
    acertou = False
    erros = 0

    print(letras_acertadas)

    while(not enforcou and not acertou):

        chute = input("Qual letra? ")
        chute = chute.strip().upper()

        if(chute in palavra_secreta):
            index = 0
            for letra in palavra_secreta:
                if(chute == letra):
                    letras_acertadas[index] = letra
                index += 1
        else:
            erros += 1
            print("{} tentativas restantes.".format(6 - erros))

        enforcou = erros == 6
        acertou = "_" not in letras_acertadas
        print(letras_acertadas)


    if(acertou):
        print("Você ganhou!!")
    else:
        print("Você perdeu!!")

    print("Fim do jogo")

if(__name__ == "__main__"):
    jogar()

#Métodos = Sequências

#Funções não alteram variáveis

#Strings e Tuplas são sequências imutáveis. Listas também são sequências, mas mutáveis.

#Usa-se listas para guardar valores (salvar valores)

#Listas também são sequências

#Listas [] e Tuplas ()

#Um set é uma coleção não ordenada de elementos. Cada elemento é único, isso significa que
#não existem elementos duplicados dentro do set.

#Dictionary é tipo um set, porém em pares com dois pontos ( : )

#função open() e close()

#w,r,a (escrever,ler,adicionar)







