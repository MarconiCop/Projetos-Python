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


# 23. Faça um programa que mostre todos os primos entre 1 e N sendo N um número inteiro fornecido pelo utilizador. O
# programa deverá mostrar também o número de divisões que ele executou para encontrar os números primos. Serão
# avaliados o funcionamento, o estilo e o número de testes (divisões) executados.

def numero_primo_divisoes():
    n_max = int(input("Digite o limite para os números primos: "))
    lista = []
    contador_divisoes = 0

    while n_max < 2:
        n_max = int(input("Digite o limite para os números primos: "))

    for i in range(0, n_max + 1):

        total_divisores = 0

        for j in range(1, i + 1):

            if i % j == 0:
                total_divisores += 1
                contador_divisoes += 1
            else:
                contador_divisoes += 1

        if total_divisores == 2:
            lista.append(i)

    print(lista)
    print("O número de divisões feitas foram: {}".format(contador_divisoes))


# 24. Faça um programa que calcule o mostre a média aritmética de N notas.

def media_aritmetica():
    numero_notas = int(input("Digite o número de notas: "))
    soma = 0

    for contador in range(1, numero_notas + 1):
        nota = float(input("Digite a nota {}: ".format(contador)))
        soma = soma + nota

    media = soma / numero_notas

    print("A média é {}".format(media))


# 25. Faça um programa que peça para n, pessoas a sua idade, ao final o programa devera verificar se a média de idade
# da turma varia entre 0 e 25,26 e 60 e maior que 60; e então, dizer se a turma é jovem, adulta ou idosa, conforme a
# média calculada.

def idade():
    numero_pessoas = int(input("Digite o número de pessoas: "))
    soma = 0

    for contador in range(1, numero_pessoas + 1):
        age = float(input("Digite a idade da pessoa {}: ".format(contador)))
        soma = soma + age

    media = soma / numero_pessoas

    if 0 <= media <= 25:
        print("A média das idades é {}, portanto a turma é JOVEM!".format(media))

    elif 26 <= media <= 60:
        print("A média das idades é {}, portanto a turma é ADULTA!".format(media))

    else:
        print("A média das idades é {}, portanto a turma é IDOSA!".format(media))


# 26. Numa eleição existem três candidatos. Faça um programa que peça o número total de eleitores. Peça para cada
# eleitor votar e ao final mostrar o número de votos de cada candidato.

def eleicao():
    numero_eleitores = int(input("Digite o número de eleitores: "))
    candidato_um = 0
    candidato_dois = 0
    candidato_tres = 0

    for eleitor in range(1, numero_eleitores + 1):
        voto = int(input("Olá eleitor {}! Digite 1 para votar no candidato 1, 2 para votar no candidato 2, "
                         "3 para votar no candidato 3: ".format(eleitor)))

        if voto == 1:
            candidato_um += 1
        elif voto == 2:
            candidato_dois += 1
        elif voto == 3:
            candidato_tres += 1
        else:
            print("Voto anulado!")

    print("Houve {} eleitores!".format(numero_eleitores))
    print("Houve {} votos para o Candidato 1".format(candidato_um))
    print("Houve {} votos para o Candidato 2".format(candidato_dois))
    print("Houve {} votos para o Candidato 3".format(candidato_tres))


# 27. Faça um programa que calcule o número médio de alunos por turma. Para isto, peça a quantidade de turmas e a
# quantidade de alunos para cada turma. As turmas não podem ter mais de 40 alunos.

def numero_medio():
    numero_turmas = int(input("Digite o número de turmas: "))
    armazena_quantidade_alunos_total = 0

    for turma in range(1, numero_turmas + 1):
        quantidade_alunos = int(input("Digite a quantidade de alunos da turma {}: ".format(turma)))
        if quantidade_alunos <= 40:
            armazena_quantidade_alunos_total = armazena_quantidade_alunos_total + quantidade_alunos
        else:
            while quantidade_alunos > 40:
                print("A turma {} tem mais de 40 alunos!".format(turma))
                quantidade_alunos = int(input("Digite a quantidade de alunos da turma {}: ".format(turma)))

            armazena_quantidade_alunos_total = armazena_quantidade_alunos_total + quantidade_alunos

    numero_medio_aluno = armazena_quantidade_alunos_total / numero_turmas

    print("O número médio de alunos por turma é {}".format(numero_medio_aluno))


# 28. Faça um programa que calcule o valor total investido por um colecionador na sua coleção de CDs e o valor médio
# gasto em cada um deles. O utilizador deverá informar a quantidade de CDs e o valor para em cada um.

def colecionador_cds():
    quantidade_cds = int(input("Digite a quantidade de CDs: "))
    valor_investido = 0
    for cd in range(1, quantidade_cds + 1):
        valor_cd = float(input("Digite o valor do CD {}: ".format(cd)))
        valor_investido = valor_investido + valor_cd

    valor_medio = valor_investido / quantidade_cds
    print("O colecionador possui {} CDs, com um valor investido de {:.2f} reais, com uma média de {:.2f} reais por CD."
          .format(quantidade_cds, valor_investido, valor_medio))


# 29. O Sr. Manoel Joaquim possui uma grande loja de artigos de R$ 1,99, com cerca de 10 caixas. Para agilizar o
# cálculo de quanto cada cliente deve pagar ele desenvolveu um tabela que contém o número de itens que o cliente
# comprou e ao lado o valor da conta. Desta forma a atendente do caixa precisa apenas contar quantos itens o cliente
# está levando e olhar na tabela de preços. Foi contratado para desenvolver o programa que monta esta tabela de
# preços, que conterá os preços de 1 até 50 produtos, conforme o exemplo abaixo: Lojas Quase Dois - Tabela de preços
# 1 - R$ 1.99 2 - R$ 3.98 ... 50 - R$ 99.50

def tabela_precos():
    preco_item = 1.99
    print("Lojas Quase Dois - Tabela de preços")
    for quantidade_item in range(1, 51):
        print("{} - R$ {:.2F}".format(quantidade_item, quantidade_item * preco_item))


# 30. O Sr. Manoel Joaquim acaba de adquirir uma panificadora e pretende implantar a metodologia da tabelinha,
# que já é um sucesso na sua loja de 1,99. Foi contratado para desenvolver o programa que monta a tabela de
# preços de pães, de 1 até 50 pães, a partir do preço do pão informado pelo utilizador, conforme o exemplo abaixo: preço
# do pão: R$ 0.18 Panificadora Pão de Ontem — Tabela de preços 1 - R$ 0.18 2 - R$ 0.36 ... 50 - R$ 9.00

def tabela_precos_padaria():
    preco_item = 0.18
    print("Preço do pão: R$ 0.18")
    print("Panificadora Pão de Ontem - Tabela de preços")
    for quantidade_item in range(1, 51):
        print("{} - R$ {:.2F}".format(quantidade_item, quantidade_item * preco_item))


if __name__ == "__main__":
    numero_primo_divisoes()
