print("*********************************")
print("Bem vindo ao jogo de Adivinhação!")
print("*********************************")

numero_secreto = 42
total_de_tentativas = 3
rodada = 1

while(rodada <= total_de_tentativas):

    print("Tentativa {} de {}".format(rodada,total_de_tentativas))

    chute_str = input("Digite o seu número: ")
    chute_int = int(chute_str)
    print("Você digitou", chute_int)

    acertou = chute_int == numero_secreto
    maior   = chute_int > numero_secreto
    menor   = chute_int < numero_secreto

    if(acertou):
        print("Você acertou!")
    else:
        if(maior):
            print("Você errou! Seu chute foi maior que o número secreto.")
        elif(menor):
            print("Você errou! Seu chute foi menor que o número secreto.")
    rodada = rodada + 1

print("Fim do jogo!")






