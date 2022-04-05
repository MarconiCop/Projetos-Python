import math


# 1. Faça um programa que peça uma nota, entre zero e dez. Mostre uma mensagem caso o valor seja inválido e continue
# a pedir até que o utilizador informe um valor válido.

def nota_valida():
    nota = float(input("Digite uma nota entre 0 e 10: "))

    while nota < 0 or nota > 10:
        print("Valor Inválido!")
        nota = float(input("Digite uma nota entre 0 e 10: "))

    print("A nota é {}".format(nota))


# 2. Faça um programa que leia um nome de utilizador e a sua senha e não aceite a senha igual ao nome do utilizador,
# mostrando uma mensagem de erro e voltando a pedir as informações.

def login():
    nome = input("Digite o nome de usuário: ").strip()
    senha = input("Digite sua senha: ").strip()

    while nome == senha:
        print("A senha é igual ao nome de usuário!")
        nome = input("Digite o nome de usuário: ")
        senha = input("Digite sua senha: ")

    print("Logado com sucesso!")


# 3. Faça um programa que leia e valide as seguintes informações:
# Nome: maior que 3 caracteres;
# Idade: entre 0 e 150;
# Salário: maior que zero;
# Sexo: 'f' ou 'm';
# Estado Civil: 's', 'c', 'v', 'd';

def informacoes():
    nome = input("Digite seu nome: ")

    while len(nome) <= 3:
        print("Seu nome deve conter acima de 4 caracteres!")
        nome = input("Digite seu nome: ")

    idade = int(input("Digite sua idade: "))

    while idade < 0 or idade > 150:
        print("Sua idade deve estar entre 0 e 150!")
        idade = int(input("Digite sua idade: "))

    salario = float(input("Digite seu salário: "))

    while salario <= 0:
        print("Seu salário deve ser maior que zero!")
        salario = float(input("Digite seu salário: "))
    sexo = input("Digite seu sexo(f ou m): ")

    while sexo != "f" and sexo != "m":
        print("Seu sexo deve ser f ou m!")
        sexo = input("Digite seu sexo(f ou m): ")

    estado_civil = input("Digite seu estado civil(s, c, v ,d): ")

    while estado_civil != "s" and estado_civil != "c" and estado_civil != "v" and estado_civil and "d":
        print("Seu estado cívil deve ser s, c, v ou d!")
        estado_civil = input("Digite seu estado civil(s, c, v ,d): ")

    print("Todas as informações estão válidas!")


# 4. Supondo que a população de um país A seja da ordem de 80.000 habitantes com uma taxa anual de crescimento de 3% e
# que a população de B, seja 200.000 habitantes com uma taxa de crescimento de 1.5%. Faça um programa que calcule e
# escreva o número de anos necessários para que a população do país A ultrapasse ou iguale a população do país B,
# mantidas as taxas de crescimento.

def populacao():
    populacao_pais_a = 80000
    populacao_pais_b = 200000
    anos_necessarios = 0

    while populacao_pais_a < populacao_pais_b:
        populacao_pais_a = int(populacao_pais_a + (populacao_pais_a * 0.03))
        populacao_pais_b = int(populacao_pais_b + (populacao_pais_b * 0.015))
        anos_necessarios += 1

    print("Os anos necessários para que a população de A passe B é {} ano(s)".format(anos_necessarios))
    print("População A: {} habitantes".format(populacao_pais_a))
    print("População B: {} habitantes".format(populacao_pais_b))


# 5. Altere o programa anterior permitindo ao utilizador informar as populações e as taxas de crescimento iniciais.
# Valide a entrada e permita repetir a operação.

def propria_populacao():
    permitir_operacao = True
    while permitir_operacao:
        populacao_pais_a = int(input("Digite a população do país A: "))

        while populacao_pais_a < 10000:
            print("População de A é muito pequena!")
            populacao_pais_a = int(input("Digite a população do país A: "))

        populacao_pais_b = int(input("Digite a população do país B: "))
        while populacao_pais_b < 10000:
            print("População de B é muito pequena!")
            populacao_pais_a = int(input("Digite a população do país A: "))

        taxa_de_crescimento_de_a = float(input("Digite a taxa de crescimento de A (%): "))
        while taxa_de_crescimento_de_a < 1.5:
            print("Taxa de crescimento fora do intervalo!")
            taxa_de_crescimento_de_a = float(input("Digite a taxa de crescimento de A (%): "))

        taxa_de_crescimento_de_b = float(input("Digite a taxa de crescimento de B (%): "))
        while taxa_de_crescimento_de_b < 1.5:
            print("Taxa de crescimento fora do intervalo!")
            taxa_de_crescimento_de_b = float(input("Digite a taxa de crescimento de B (%): "))
        anos_necessarios = 0

        while populacao_pais_a < populacao_pais_b:
            populacao_pais_a = (populacao_pais_a + (populacao_pais_a * (taxa_de_crescimento_de_a / 100)))
            populacao_pais_b = (populacao_pais_b + (populacao_pais_b * (taxa_de_crescimento_de_b / 100)))
            anos_necessarios += 1

        print("Os anos necessários para que a população de A passe B é {} ano(s)".format(anos_necessarios))


# 6. Faça um programa que imprima na tela os números de 1 a 20, um abaixo do outro. Depois modifique o programa para
# ele mostrar os números um ao lado do outro.

def ler_numeros():
    lista = []

    for numero in range(1, 21):
        print(numero)

    lista = []
    for numero in range(1, 21):
        lista.append(numero)
    print(lista)


# 7. Faça um programa que leia 5 números e informe o maior número.

def maior_numero():
    lista = []
    for numero in range(1, 6):
        numero = int(input("Digite o número: "))
        lista.append(numero)

    print("O maior número da lista é", max(lista), end="!")


# 8. Faça um programa que leia 5 números e informe a soma e a média dos números.

def soma_e_media():
    lista = []
    for numero in range(1, 6):
        numero = int(input("Digite o número: "))
        lista.append(numero)

    print("A soma da lista é ", sum(lista))
    print("A média da lista é", (sum(lista) / 5))


# 9. Faça um programa que imprima na tela apenas os números ímpares entre 1 e 50.

def impares():
    lista = []
    for numero in range(1, 51):
        if numero % 2 != 0:
            lista.append(numero)

    print(lista)


# 10. Faça um programa que receba dois números inteiros e gere os números inteiros que estão no intervalo compreendido
# por eles.

def intervalo():
    lista = []
    numero_um = int(input("Digite o primeiro número inteiro: "))
    numero_dois = int(input("Digite o segundo número inteiro: "))

    for numero in range(numero_um, numero_dois + 1):
        lista.append(numero)

    lista.remove(numero_um)
    lista.remove(numero_dois)
    print(lista)


# 11. Altere o programa anterior para mostrar no final a soma dos números.

def soma_intervalo():
    lista = []
    numero_um = int(input("Digite o primeiro número inteiro: "))
    numero_dois = int(input("Digite o segundo número inteiro: "))

    for numero in range(numero_um, numero_dois + 1):
        lista.append(numero)

    lista.remove(numero_um)
    lista.remove(numero_dois)
    print(sum(lista))


# 12. Desenvolva um gerador de tabuada, capaz de gerar a tabuada de qualquer número inteiro entre 1 a 10. O utilizador
# deve informar de qual numero ele deseja ver a tabuada. A saída deve ser conforme o exemplo abaixo: Tabuada de 5: 5
# X 1 = 5 5 X 2 = 10
...


# 5 X 10 = 50

def tabuada():
    numero_tabuada = int(input("Digite o número entre 1 a 10: "))
    print("Tabuada de {}".format(numero_tabuada))

    for numero in range(1, 11):
        print("{} X {} = {}".format(numero_tabuada, numero, numero_tabuada * numero))


# 13. Faça um programa que peça dois números, base e expoente, calcule e mostre o primeiro número elevado ao segundo
# número. Não utilize a função de potência da linguagem.

def exponenciacao():
    base = int(input("Digite a base: "))
    expoente = int(input("Digite o expoente: "))

    calculo = 1

    for numero in range(0, expoente):
        calculo = calculo * base

    print(calculo)


# 14. Faça um programa que peça 10 números inteiros, calcule e mostre a quantidade de números pares e a quantidade de
# números impares.

def pares_impares():
    par = 0
    impar = 0

    for numero in range(1, 11):
        numeros = int(input("Digite o número {}: ".format(numero)))
        if numeros % 2 == 0:
            par += 1
        else:
            impar += 1

    print("Há {} número(s) par(es) e {} número(s) ímpar(es)!".format(par, impar))


# 15. A série de Fibonacci é formada pela sequencing 1,1,2,3,5,8,13,21,34,55,... Faça um programa capaz de gerar a
# série até o n−ésimo termo.

def fibonacci():
    lista = [1, 1]

    n = int(input("Digite o enésimo termo: "))
    for contador in range(0, n):
        if contador > 1:
            lista.append(lista[contador - 1] + lista[contador - 2])

    print(lista)


# 16. A série de Fibonacci é formada pela sequencing 0,1,1,2,3,5,8,13,21,34,55,... Faça um programa que gere a série
# até que o valor seja maior que 500.

def fibonacci_limite():
    lista = [1, 1]

    for contador in range(100):
        if contador > 1:
            lista.append(lista[contador - 1] + lista[contador - 2])
            if lista[contador] > 500:
                break

    lista.pop()
    print(lista)


# 17. Faça um programa que calcule o fatorial de um número inteiro fornecido pelo usuário. Ex.: 5!=5.4.3.2.1=120

def fatorial():
    numero = int(input("Digite o número: "))
    print(calcula_fatorial(numero))


def calcula_fatorial(numero):
    if numero != 1:
        numero_menos_um = numero - 1
        return numero * calcula_fatorial(numero_menos_um)
    else:
        return 1


# 18. Faça um programa que, dado um conjunto de N números, determine o menor valor, o maior valor e a soma dos valores.

def conjunto():
    lista = []
    tamanho = int(input("Digite o tamanho da sua lista: "))
    for numero in range(0, tamanho):
        numero_digitado = int(input("Digite o número: "))
        lista.append(numero_digitado)

    print(lista)
    print("O menor número do conjunto é {}.".format(min(lista)))
    print("O maior número do conjunto é {}.".format(max(lista)))
    print("A soma  do conjunto é {}.".format(sum(lista)))


# 19.Altere o programa anterior para que ele aceite apenas números entre 0 e 1000.

def conjunto_limitado():
    lista = []
    tamanho = int(input("Digite o tamanho da sua lista: "))

    for numero in range(tamanho):

        numero_digitado = int(input("Digite o número: "))
        if 0 < numero_digitado < 1000:
            lista.append(numero_digitado)
        else:
            numero_invalido = True
            while numero_invalido:
                print("Número Inválido!")
                numero_digitado = int(input("Digite o número: "))
                if 0 < numero_digitado < 1000:
                    lista.append(numero_digitado)
                    numero_invalido = False

    print(lista)
    print("O menor número do conjunto é {}.".format(min(lista)))
    print("O maior número do conjunto é {}.".format(max(lista)))
    print("A soma  do conjunto é {}.".format(sum(lista)))


# 20. Altere o programa de cálculo do fatorial, permitindo ao usuário calcular o fatorial várias vezes e limitando o
# fatorial a números inteiros positivos e menores que 16.

def fatorial_regra():
    fat = True
    while fat:
        numero = int(input("Digite o número: "))
        if 0 <= calcula_fatorial(numero) < 16:
            print(calcula_fatorial(numero))
        else:
            print("O fatorial não é maior que 0 ou menor que 16!")


def calcula_fatorial(numero):
    if numero != 1 and numero != 0:
        numero_menos_um = numero - 1
        return numero * calcula_fatorial(numero_menos_um)
    else:
        return 1


# 21. Faça um programa que peça um número inteiro e determine se ele é ou não um número primo. Um número primo é
# aquele sendo divisível somente por ele mesmo e por 1.

def numero_primo():
    numero = int(input("Digite o número: "))
    verifica = 0
    for contador in range(1, numero):

        if numero % contador == 0:
            verifica = contador + 1

    if verifica > 2 or numero == 0 or numero == 1:
        print("O número {} não é primo!".format(numero))
    else:
        print("O número {} é primo!".format(numero))


# 22. Altere o programa de cálculo dos números primos, informando, caso o número não seja primo, por quais número ele
# é divisível.

def numero_primo_multiplo():
    numero = int(input("Digite o número: "))
    verifica = 0
    lista = []
    for contador in range(1, numero):

        if numero % contador == 0:
            verifica = contador + 1

    if verifica > 2 or numero == 0 or numero == 1:
        print("O número {} não é primo!".format(numero))

        for percorre in range(1, numero + 1):
            if numero % percorre == 0:
                lista.append(percorre)
        if numero == 1:
            print("O número 1 é apenas divísivel por ele mesmo.")
        elif numero == 0:
            print("Não existe divisão por 0, portanto não há números em que ele possa ser divisível.")
        else:
            print("O número é dívisivel por: {}".format(lista))
    else:
        print("O número {} é primo!".format(numero))


if __name__ == "__main__":
    numero_primo_multiplo()
