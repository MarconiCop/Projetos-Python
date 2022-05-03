import random
import re


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


# 7. Faça um programa que use a função valorPagamento para determinar o valor a ser pago por uma prestação de uma
# conta. O programa deverá solicitar ao utilizador o valor da prestação e o número de dias em atraso e passar estes
# valores para a função valorPagamento, que calculará o valor a ser pago e devolverá este valor ao programa que a
# chamou. O programa deverá então exibir o valor a ser pago na tela. Após a execução o programa deverá voltar a pedir
# outro valor de prestação e assim continuar até que seja informado um valor igual a zero para a prestação. Agora o
# programa deverá ser encerrado, exibindo o relatório do dia, que conterá a quantidade e o valor total de prestações
# pagas no dia. O cálculo do valor a ser pago é feito da seguinte forma. Para pagamentos sem atraso, cobrar o valor
# da prestação. Quando houver atraso, cobrar 3% de multa, mais 0,1% de juros por dia de atraso.

def valorPagamento(valor_prestacao, dias_em_atraso):
    if dias_em_atraso == 0:
        return valor_prestacao
    else:
        valor_prestacao += (0.03 * valor_prestacao) + (0.01 * dias_em_atraso * valor_prestacao)
        return valor_prestacao


def principal_sete():
    prestacao = 1
    lista = []
    catalogo = {}

    while prestacao != 0:
        prestacao = float(input("Digite a prestação: "))
        dias = int(input("Digite os dias em atraso: "))
        valor_a_ser_pago = valorPagamento(prestacao, dias)
        lista.append(valor_a_ser_pago)
        catalogo[valor_a_ser_pago] = dias

    del catalogo[0]
    lista.pop()

    for chave, valor in catalogo.items():
        print(chave, "reais para", valor, "dias de atraso")


# 8. Faça uma função que informe a quantidade de dígitos de um determinado número inteiro informado.

def quantidade(numero):
    numero_str = str(numero)
    return print(len(numero_str))


def principal_oito():
    numero = int(input("Digite um número: "))
    quantidade(numero)


# 9. Reverso do número. Faça uma função que retorne o reverso de um número inteiro informado. Por exemplo: 127 -> 721.

def reverso(numero):
    inverso = 0
    while numero != 0:
        resto = numero % 10
        inverso = inverso * 10 + resto
        numero = numero // 10

    return print("O número invertido é", inverso)


def principal_nove():
    numero = int(input("Digite um número: "))
    reverso(numero)


# 10. Jogo de Craps. Faça um programa de implemente um jogo de Craps. O jogador lança um par de dados, obtendo um
# valor entre 2 e 12. Se, na primeira jogada, você tirar 7 ou 11, você um "natural" e ganhou. Se você tirar 2,
# 3 ou 12 na primeira jogada, isto é chamado "craps" e perdeu. Se, na primeira jogada, fez um 4, 5, 6,
# 8, 9 ou 10,este é seu "Ponto". O seu objetivo agora é continuar a jogar os dados até tirar este número novamente.
# Perde, no entanto, se tirar um 7 antes de tirar este Ponto novamente.

def principal_dez():
    lancar = int(input("Digite 0 para lançar o dado 1 e 2: "))
    if lancar == 0:
        dado_um = random.randrange(1, 6)
        dado_dois = random.randrange(1, 6)
        soma = dado_um + dado_dois

    if soma == 7 or soma == 11:
        print("Você é um Natural e Ganhou!! A soma deu: {}".format(soma))
        return 1
    elif soma == 2 or soma == 3 or soma == 12:
        print("CRAPS! Você perdeu! A soma deu: {}".format(soma))
        return 1
    elif soma == 4 or soma == 5 or soma == 6 or soma == 8 or soma == 9 or soma == 10:
        print("Soma: {}".format(soma))
        ponto = soma

    lancar = int(input("Digite 1 para lançar o dado 1 e 2: "))
    while lancar != 0:
        dado_um = random.randrange(1, 6)
        dado_dois = random.randrange(1, 6)
        soma = dado_um + dado_dois
        print("Soma: {}".format(soma))

        if soma == 7:
            print("CRAPS! Você perdeu! A soma deu: {}".format(soma))
            return 1
        elif soma == ponto:
            print("Você Ganhou!! A soma deu: {} e o ponto {}".format(soma, ponto))
            return 1

        lancar = int(input("Digite 1 para lançar o dado 1 e 2: "))


# 11. Data com mês por extenso. Construa uma função que receba uma data no formato DD/MM/AAAA e devolva uma ‘string’ no
# formato D de mesPorExtenso de AAAA. Opcionalmente, valide a data e retorne NULL caso a data seja inválida.


def data(dia, mes, ano):
    calendario = {"Janeiro": 1,
                  "Fevereiro": 2,
                  "Março": 3,
                  "Abril": 4,
                  "Maio": 5,
                  "Junho": 6,
                  "Julho": 7,
                  "Agosto": 8,
                  "Setembro": 9,
                  "Outubro": 10,
                  "Novembro": 11,
                  "Dezembro": 12}

    for meses, valor in calendario.items():
        if mes == valor:
            mes_extenso = meses

    return print("{} de {} de {}".format(dia, mes_extenso, ano))


def e_bissexto(ano):
    if regra_um(ano) or regra_dois(ano):
        return True


def regra_um(ano):
    if ano % 4 == 0 and ano % 100 != 0:
        return True


def regra_dois(ano):
    if ano % 4 == 0 and ano % 100 == 0 and ano % 400 == 0:
        return True


def principal_onze():
    data_escolhida = input("Digite a data no formato dd/mm/aaaa: ")

    numeros_data = [int(numero) for numero in re.findall(r'-?\d+\.?\d*', data_escolhida)]

    dia = int(numeros_data[0])
    mes = int(numeros_data[1])
    ano = int(numeros_data[2])
    tupla_meses_trinta_um_dias = (1, 3, 5, 7, 9, 10, 12)
    tupla_meses_trinta_dias = (4, 6, 8, 11)

    if mes in tupla_meses_trinta_um_dias:
        if dia <= 31:
            if 1000 <= ano <= 9999:
                data(dia, mes, ano)
            else:
                return 0
        else:
            return 0

    elif mes in tupla_meses_trinta_dias:
        if dia <= 30:
            if 1000 <= ano <= 9999:
                data(dia, mes, ano)
        else:
            return 0

    elif mes == 2:
        if e_bissexto(ano):
            if dia <= 29:
                data(dia, mes, ano)
            else:
                return 0
        else:
            if dia <= 28:
                data(dia, mes, ano)
            else:
                return 0
    else:
        return 0


if __name__ == "__main__":
    principal_onze()
