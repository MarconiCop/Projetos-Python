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


# 4. Faça um programa, com uma função que necessite de um argumento. A função retorna o valor de caractere ‘P’,
# se o seu argumento for positivo, e ‘N’, se o seu argumento for zero ou negativo.


def funcao_quatro(valor):
    if valor > 0:
        return "P"
    return "N"


def principal_quatro():
    numero = int(input("Digite um número: "))
    print(funcao_quatro(numero))


# 5. Faça um programa com uma função chamada somaImposto. A função possui dois parâmetros formais: taxaImposto,
# sendo a quantia de imposto sobre venda expressa em porcentagem e custo, o custo de um ‘item’ antes do imposto.
# A função “altera” o valor de custo para incluir o imposto sobre vendas.

def soma_imposto(taxa_imposto, custo):
    return print(custo + ((custo * taxa_imposto) / 100))


def principal_cinco():
    valor_produto = float(input("Digite o valor do produto sem imposto: "))
    imposto = int(input("Digite o valor do imposto(%): "))
    soma_imposto(imposto, valor_produto)


# 6. Faça um programa que converta da notação de 24 horas para a notação de 12 horas. Por exemplo, o programa deve
# converter 14:25 em 2:25 P.M.A. entrada é dada em dois inteiros. Deve haver pelo menos duas funções: uma para fazer
# a conversão e uma para a saída. Registre a informação A.M./P.M. como um valor ‘A’ para A.M. e ‘P’ para P.M. Assim,
# a função para efetuar as conversões terão um parâmetro formal para registrar se é A.M. ou P.M. Inclua um ‘loop’ que
# permita que o utilizador repita esse cálculo para novos valores de entrada todas as vezes que desejar.

def conversao(hora, minuto):
    if hora > 12:
        letra = "P"
    else:
        letra = "A"

    if hora == 13:
        hora = 1
    elif hora == 14:
        hora = 2
    elif hora == 15:
        hora = 3
    elif hora == 16:
        hora = 4
    elif hora == 17:
        hora = 5
    elif hora == 18:
        hora = 6
    elif hora == 19:
        hora = 7
    elif hora == 20:
        hora = 8
    elif hora == 21:
        hora = 9
    elif hora == 22:
        hora = 10
    elif hora == 23:
        hora = 11

    if letra == "P":
        return print(hora, ":", minuto, "P.M")
    elif letra == "A":
        return print(hora, ":", minuto, "A.M")


def principal_seis():

    desejo = 1

    while desejo > 0:
        hora = int(input("Digite a hora: "))
        minuto = int(input("Digite o minuto: "))
        if hora <= 24 and minuto <= 59:
            conversao(hora, minuto)
        else:
            return 1
        desejo = int(input("Digite 0 para terminar ou 1 para continuar: "))


if __name__ == "__main__":
    principal_seis()
