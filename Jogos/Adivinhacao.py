print("*********************************")
print("Bem vindo ao jogo de Adivinhação!")
print("*********************************")

numero_secreto = 42

chute_str = input("Digite o seu número: ")

chute_int = int(chute_str)

acertou = chute_int == numero_secreto
maior   = chute_int > numero_secreto
menor   = chute_int < numero_secreto

print("Você digitou", chute_int)

if(acertou):
    print("Você acertou!")
else:
    if(maior):
        print("Você errou! Seu chute foi maior que o número secreto.")
    elif(menor):
        print("Você errou! Seu chute foi menor que o número secreto.")

print("Fim do jogo!")






