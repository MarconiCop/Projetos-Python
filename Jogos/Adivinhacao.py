print("*********************************")
print("Bem vindo ao jogo de Adivinhação!")
print("*********************************")

numero_secreto = 42

chute_str = input("Digite o seu número: ")

chute_int = int(chute_str)

print("Você digitou", chute_int)

if(numero_secreto == chute_int):
    print("Você acertou!")
else:
    print("Você errou!")

print("Fim do jogo!")





