# 1. Tamanho de ‘strings’. Faça um programa que leia 2 ‘strings’ e informe o conteúdo delas seguidas do seu comprimento.
# Informe também se as duas ‘strings’ possuem o mesmo comprimento e são iguais ou diferentes no conteúdo.

def compara_string():
    frase_um = input("Digite a primeira frase: ")
    frase_dois = input("Digite a segunda frase: ")

    print("Compara duas strings")
    print("String 1: {}".format(frase_um))
    print("String 2: {}".format(frase_dois))
    print("Tamanho de '{}': {} caracteres".format(frase_um, len(frase_um)))
    print("Tamanho de '{}': {} caracteres".format(frase_dois, len(frase_dois)))

    if len(frase_um) != len(frase_dois):
        print("As duas strings são de tamanhos diferentes.")
    else:
        print("As duas strings são de tamanhos iguais.")

    if frase_um != frase_dois:
        print("As duas strings possuem conteúdo diferente.")
    else:
        print("As duas strings possuem conteúdo igual.")


# 2. Nome ao contrário em maiúsculas. Faça um programa que permita ao utilizador digitar o seu nome e em seguida mostre
# o nome do utilizador de trás para frente utilizando somente letras maiúsculas. Dica: lembre−se que ao informar o nome
# o utilizador pode digitar letras maiúsculas ou minúsculas.

def nome_invertido_maisuculo():
    nome = input("Digite seu nome: ").upper()
    print("".join(reversed(nome)))


# 3. Nome na vertical. Faça um programa que solicite o nome do utilizador e imprima-o na vertical.

def nome_vertical():
    nome = input("Digite seu nome: ").upper()

    for posicao in range(len(nome)):
        print(nome[posicao])


# 4. Nome na vertical em escada. Modifique o programa anterior para mostrar o nome em formato de escada.

def nome_escada():
    lista = []
    nome_metade = ""
    nome = input("Digite seu nome: ").upper()

    for posicao in range(len(nome)):
        lista.append(nome[posicao])

    for posicao in range(len(lista)):
        nome_metade = nome_metade + nome[posicao]
        print(nome_metade)


if __name__ == "__main__":
    nome_escada()
