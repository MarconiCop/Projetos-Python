# 1. Faça um programa para imprimir:
#     1
#     2   2
#     3   3   3
#     .....
#     n   n   n   n   n   n ... N
# para um n informado pelo utilizador. Use uma função que receba um valor n inteiro e imprima até a n-ésima linha.

def funcao(numero):
    for number in range(numero):
        number += 1
        print("  ".join((str(number) * number)))


def principal():
    n = int(input("Digite o número: "))
    funcao(n)


# 2. Faça um programa para imprimir:
#     1
#     1   2
#     1   2   3
#     .....
#     1   2   3   ...  n
# para um n informado pelo utilizador. Use uma função que receba um valor n inteiro imprima até a n-ésima linha.

def funcao_dois(n):
    for linha in range(1, n + 1):
        for coluna in range(1, linha + 1):
            print(coluna, end="  ")
        print('')


def principal_dois():
    n = int(input("Digite o número: "))
    funcao_dois(n)


# 3. Faça um programa, com uma função que necessite de três argumentos, e que forneça a soma desses três argumentos.

def funcao_tres(a, b, c):
    return a + b + c

def principal_tres():
    a = int(input("Digite o número: "))
    b = int(input("Digite o número: "))
    c = int(input("Digite o número: "))
    resultado = funcao_tres(a, b, c)
    print(resultado)


if __name__ == "__main__":
    principal_tres()
