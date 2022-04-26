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


n = int(input("Digite o número: "))
funcao(n)
