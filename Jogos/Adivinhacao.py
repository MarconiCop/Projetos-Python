import random

print("*********************************")
print("Bem vindo ao jogo de Adivinhação!")
print("*********************************")


numero_secreto = random.randrange(1, 101)

total_de_tentativas = 3


for rodada in range(1, total_de_tentativas + 1):

    print("Tentativa {:02d} de {:02d}".format(rodada, total_de_tentativas))

    chute_str = input("Digite o seu número entre 1 e 100: ")
    chute_int = int(chute_str)
    print("Você digitou", chute_int)

    if(chute_int < 1 or chute_int > 100):
        print("Você deve digitar um número entre 1 e 100!")
        continue

    acertou = chute_int == numero_secreto
    maior   = chute_int > numero_secreto
    menor   = chute_int < numero_secreto

    if(acertou):
        print("Você acertou!")
        break
    else:
        if(maior):
            print("Você errou! Seu chute foi maior que o número secreto.")
        elif(menor):
            print("Você errou! Seu chute foi menor que o número secreto.")

print("O número era", numero_secreto)
print("Fim do jogo!")






