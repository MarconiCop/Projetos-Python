import math
import sys

# 1. Faça um programa que peça uma nota, entre zero e dez. Mostre uma mensagem caso o valor seja inválido e continue
# a pedir até que o utilizador informe um valor válido.
import string


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


# 31. O Sr. Manoel Joaquim expandiu os seus negócios para além dos negócios de 1,99 e agora possui uma loja de
# conveniências. Faça um programa que implemente uma caixa registradora rudimentar. O programa deverá receber um
# número desconhecido de valores referentes aos preços das mercadorias. Um valor zero deve ser informado pelo
# operador para indicar o final da compra. O programa deve então mostrar o total da compra e perguntar o valor em
# dinheiro que o cliente forneceu, para então calcular e mostrar o valor do troco. Após esta operação, o programa
# deverá voltar ao ponto inicial, para registrar a próxima compra. A saída deve ser conforme o exemplo abaixo:
# Lojas Tabajara
# Produto 1: R$ 2.20
# Produto 2: R$ 5.80
# Produto 3: R$ 0
# Total: R$ 9.00
# Dinheiro: R$ 20.00
# Troco: R$ 11.00
# ...

def recibo():
    lista = []

    for produto in range(1, 1000):
        valor_produto = float(input("Digite o valor do produto {}: ".format(produto)))
        lista.append(valor_produto)
        if valor_produto == 0:
            break

    print("Total a pagar : R$ {:.2f}".format((sum(lista))))

    dinheiro = float(input("Digite quanto vai pagar: "))
    troco = dinheiro - sum(lista)

    print("Lojas Tabajara")
    for posicao_lista in range(len(lista)):
        print("Produto {}: R$ {:.2f}".format(posicao_lista + 1, lista[posicao_lista]))
    print("Total: R$ {:.2f}".format(sum(lista)))
    print("Dinheiro: R$ {:.2f}".format(dinheiro))
    print("Troco: R$ {:.2f}".format(troco))


# 32. Faça um programa que calcule o fatorial de um número inteiro fornecido pelo usuário. Ex.: 5!=5.4.3.2.1=120. A
# saída deve ser conforme o exemplo abaixo:

def fatorial_dois():
    numero = int(input("Digite o número: "))

    print("Fatorial de: {}".format(numero))

    print("{}! = {} = {}".format(numero, retorna_sequencia(numero), calcula_fatorial_dois(numero)))


def retorna_sequencia(numero):
    lista = []
    for numero in range(numero, 0, -1):
        lista.append(numero)

    string_lista = str(lista).replace(",", " .").replace("[", "").replace("]", "")

    return string_lista


def calcula_fatorial_dois(numero):
    if numero != 1:
        numero_menos_um = numero - 1
        return numero * calcula_fatorial(numero_menos_um)
    else:
        return 1


# 33. O Departamento Estadual de Meteorologia contratou-lhe para desenvolver um programa que leia os conjunto
# indeterminado de temperaturas, e informe ao final a menor e a maior temperaturas informadas, bem como a média das
# temperaturas.


def temperaturas():
    quantidade = int(input("Digite a quantidade de temperaturas do conjunto: "))
    lista = []

    for posicao_temperatura in range(1, quantidade + 1):
        temperatura = float(input("Digite a temperatura {} do conjunto: ".format(posicao_temperatura)))
        lista.append(temperatura)

    media = sum(lista) / quantidade

    if media < 0:
        media = media * -1

    print("A menor temperatura é: {:.2f}".format(min(lista)))
    print("A maior temperatura é: {:.2f}".format(max(lista)))
    print("A média das temperaturas é: {:.2f}".format(media))


# 34. Os números primos possuem várias aplicações na Computação, por exemplo, na Criptografia. Um número primo
# é aquele sendo divisível apenas por um e por ele mesmo. Faça um programa que peça um número inteiro e determine se
# ele é ou não um número primo.

def numero_primo_dois():
    numero = int(input("Digite o número: "))
    verifica = 0
    for contador in range(1, numero):

        if numero % contador == 0:
            verifica = contador + 1

    if verifica > 2 or numero == 0 or numero == 1:
        print("O número {} não é primo!".format(numero))
    else:
        print("O número {} é primo!".format(numero))


# 35. Encontrar números primos é uma tarefa difícil. Faça um programa que gera uma lista dos números primos
# existentes entre 1 e um número inteiro informado pelo utilizador.

def numero_primo_divisoes_dois():
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


# 36. Desenvolva um programa que faça a tabuada de um número qualquer inteiro que será digitado pelo utilizador,
# mas a tabuada não deve necessariamente iniciar em 1 e terminar em 10, o valor inicial e final devem ser informados
# também pelo utilizador, conforme exemplo abaixo:

# Montar a tabuada de: 5
# Começar por: 4
# Terminar em: 7

# Vou montar a tabuada de 5 começando em 4 e terminando em 7:
# 5 X 4 = 20
# 5 X 5 = 25
# 5 X 6 = 30
# 5 X 7 = 35

def tabuada_personalizada():
    numero_tabuada = int(input("Digite o número entre 1 a 10: "))
    numero_inicial = int(input("Digite o número inicial da tabuada: "))
    numero_final = int(input("Digite o número final da tabuada: "))

    while numero_inicial > numero_final:
        print("O número inicial deve ser menor que o número final!")
        numero_inicial = int(input("Digite o número inicial da tabuada: "))
        numero_final = int(input("Digite o número final da tabuada: "))

    print("")
    print("Montar a tabuada de: {}".format(numero_tabuada))
    print("Começar por: {}".format(numero_inicial))
    print("Terminar em: {}".format(numero_final))
    print("")
    print("Vou montar a tabuada de {} começando em {} e terminando em {}".format(numero_tabuada, numero_inicial,
                                                                                 numero_final))

    for numero in range(numero_inicial, numero_final + 1):
        print("{} X {} = {}".format(numero_tabuada, numero, numero_tabuada * numero))


# 37. Uma academia deseja fazer um senso entre os seus clientes para descobrir o mais alto, o mais baixo, a mais gordo e
# o mais magro, para isto deve fazer um programa que pergunte a cada um dos clientes da academia o seu código,
# sua altura e seu peso. O final da digitação de dados deve ser dada quando o utilizador digitar 0 (zero) no campo
# código. Ao encerrar o programa também deve ser informados os códigos e valores do cliente mais alto, do mais baixo,
# do mais gordo e do mais magro, além da média das alturas e dos pesos dos clientes.

def academia():
    lista = []

    class Cliente:

        def __init__(self, codigo, altura, peso):
            self.__codigo = codigo
            self.__altura = altura
            self.__peso = peso

        @property
        def codigo(self):
            return self.__codigo

        @property
        def altura(self):
            return self.__altura

        @property
        def peso(self):
            return self.__peso

    for cliente in range(1, 1000):
        c = int(input("Digite seu código:"))
        if c == 0:
            break
        a = float(input("Digite sua altura:"))
        p = float(input("Digite seu peso: "))

        cliente = Cliente(c, a, p)
        lista.extend([[cliente.codigo, cliente.altura, cliente.peso]])

    print(lista)

    lista_codigos = []
    for cliente in range(0, len(lista)):
        lista_codigos.append(lista[cliente][0])

    lista_alturas = []
    for cliente in range(0, len(lista)):
        lista_alturas.append(lista[cliente][1])

    lista_pesos = []
    for cliente in range(0, len(lista)):
        lista_pesos.append(lista[cliente][2])

    for posicao in range(0, len(lista_alturas)):
        if max(lista_alturas) is lista_alturas[posicao]:
            print("O cliente que tem a maior altura é o de código {} ".format(lista_codigos[posicao]))
            print("A maior altura é {:.2f}".format(max(lista_alturas)))

    for posicao in range(0, len(lista_alturas)):
        if min(lista_alturas) is lista_alturas[posicao]:
            print("O cliente que tem a menor altura é o de código {} ".format(lista_codigos[posicao]))
            print("A menor altura é {:.2f}".format(min(lista_alturas)))

    for posicao in range(0, len(lista_pesos)):
        if max(lista_pesos) is lista_pesos[posicao]:
            print("O cliente que tem o maior peso é o de código {} ".format(lista_codigos[posicao]))
            print("O maior peso é {:.2f}".format(max(lista_pesos)))

    for posicao in range(0, len(lista_pesos)):
        if min(lista_pesos) is lista_pesos[posicao]:
            print("O cliente que tem o menor peso é o de código {} ".format(lista_codigos[posicao]))
            print("O menor peso é {:.2f}".format(min(lista_pesos)))

    print("A média das alturas é {:.2f}".format(sum(lista_alturas) / len(lista_alturas)))
    print("A média dos pesos é {:.2f}".format(sum(lista_pesos) / len(lista_pesos)))


# 38. Um funcionário de uma empresa recebe aumento salarial anualmente: por que método? Que: Esse funcionário foi
# contratado em 1995, com salário inicial de R$ 1.000,00; em 1996 recebeu aumento de 1,5% sobre o seu salário
# inicial; A partir de 1997 (inclusive), os aumentos salariais sempre correspondem ao dobro do percentual do ano
# anterior. Faça um programa que determine o salário atual desse funcionário. Após concluir isto, altere o programa
# permitindo que o utilizador digite o salário inicial do funcionário.


def funcionario_empresa():
    salario = float(input("Digite o salário: "))
    porcentagem = 0.015

    for ano in range(1996, 2022):
        salario = salario + (porcentagem * salario)
        print("Salário em {}: {:.2f}, porcentagem: {}".format(ano, salario, porcentagem))
        porcentagem = porcentagem * 2


# 39. Faça um programa que leia dez conjuntos de dois valores, o primeiro representando o número do aluno e o segundo
# representando a sua altura em centímetros. Encontre o aluno mais alto e o mais baixo. Mostre o número do aluno mais
# alto e o número do aluno mais baixo, junto com suas alturas.

def listar_alunos():
    lista = []
    lista_alturas = []
    lista_numeros = []

    class Aluno:

        def __init__(self, numero, altura):
            self.__numero = numero
            self.__altura = altura

        @property
        def numero(self):
            return self.__numero

        @property
        def altura(self):
            return self.__altura

    for aluno in range(1, 11):
        n = int(input("Digite seu número:"))
        a = float(input("Digite sua altura:"))
        aluno = Aluno(n, a)
        lista.extend([[aluno.numero, aluno.altura]])

    for aluno in range(0, len(lista)):
        lista_numeros.append(lista[aluno][0])

    for aluno in range(0, len(lista)):
        lista_alturas.append(lista[aluno][1])

    for posicao in range(0, len(lista_alturas)):
        if max(lista_alturas) is lista_alturas[posicao]:
            print("O aluno que tem a maior altura é o de código {} ".format(lista_numeros[posicao]))
            print("A maior altura é {:.2f}".format(max(lista_alturas)))

    for posicao in range(0, len(lista_alturas)):
        if min(lista_alturas) is lista_alturas[posicao]:
            print("O aluno que tem a menor altura é o de código {} ".format(lista_numeros[posicao]))
            print("A menor altura é {:.2f}".format(min(lista_alturas)))


# 40. Foi feita uma estatística em cinco cidades brasileiras para coletar dados sobre acidentes de trânsito. Foram
# obtidos os seguintes dados: código da cidade; número de veículos de passeio (em 1999); número de acidentes de
# trânsito com vítimas (em 1999). Deseja-se saber: qual o maior e menor índice de acidentes de trânsito e a que
# cidade pertence; qual a média de veículos nas cinco cidades juntas; qual a média de acidentes de trânsito nas
# cidades com menos de 2.000 veículos de passeio.

def cidades():
    soma = 0
    lista = []
    lista_codigos = []
    lista_veiculos = []
    lista_acidentes = []

    class Cidade:

        def __init__(self, codigo, numero_veiculos, numero_acidentes):
            self.__codigo = codigo
            self.__numero_veiculos = numero_veiculos
            self.__numero_acidentes = numero_acidentes

        @property
        def codigo(self):
            return self.__codigo

        @property
        def numero_veiculos(self):
            return self.__numero_veiculos

        @property
        def numero_acidentes(self):
            return self.__numero_acidentes

    for cidade in range(1, 6):
        c = int(input("Digite o código da cidade: "))
        nv = int(input("Digite o número de veículos: "))
        na = int(input("Digite o número de acidentes: "))
        cidade = Cidade(c, nv, na)
        lista.extend([[cidade.codigo, cidade.numero_veiculos, cidade.numero_acidentes]])

    for cidade in range(0, len(lista)):
        lista_codigos.append(lista[cidade][0])

    for cidade in range(0, len(lista)):
        lista_veiculos.append(lista[cidade][1])

    for cidade in range(0, len(lista)):
        lista_acidentes.append(lista[cidade][2])

    for posicao in range(0, len(lista_acidentes)):
        if max(lista_acidentes) is lista_acidentes[posicao]:
            print("A cidade que tem o maior indice de acidentes é a de código {} ".format(lista_codigos[posicao]))
            print("O maior indice de acidentes é {:.2f}".format(max(lista_acidentes)))

    for posicao in range(0, len(lista_acidentes)):
        if min(lista_acidentes) is lista_acidentes[posicao]:
            print("A cidade que tem o menor indice de acidentes é a de código {} ".format(lista_codigos[posicao]))
            print("O menor indice de acidentes é {:.2f}".format(min(lista_acidentes)))

    for posicao in range(0, len(lista_veiculos)):
        if lista_veiculos[posicao] < 2000:
            soma = soma + lista_acidentes[posicao]

    print("A média de veiculos das 5 cidades é {}".format(sum(lista_veiculos) / len(lista_veiculos)))
    print("A média de acidentes nas cidades com menos de 2000 veículos é {}".format(soma / len(lista_acidentes)))


# 41. Faça um programa que receba o valor de uma dívida e mostre uma tabela com os seguintes dados: valor da dívida,
# valor dos juros, quantidade de parcelas e valor da parcela. Os juros e a quantidade de parcelas seguem a tabela
# abaixo: Quantidade de Parcelas % de Juros sobre o valor inicial da dívida 1 0 3 10 6 15 9
# 20 12 25 Exemplo de saída do programa: Valor da Dívida Valor dos Juros Quantidade de Parcelas Valor da
# Parcela R$ 1.000,00 0 1                       R$  1.000,00 R$ 1.100,00     100             3
# R$ 366,00 R$ 1.150,00 150 6 R$    191,67

def divida():
    valor_divida = float(input("Digite o valor da dívida: "))

    quantidade_parcelas = 1
    valor_juros = 0
    print("Valor da Dívida Valor dos Juros Quantidade de Parcelas  Valor da Parcela")
    print("   R$ {:.2f}           {}               {}                 {:.2f}     ".format(valor_divida, valor_juros,
                                                                                          quantidade_parcelas,
                                                                                          valor_divida /
                                                                                          quantidade_parcelas))

    quantidade_parcelas = 3
    valor_juros = (10 / 100) * valor_divida
    valor_divida = valor_divida + valor_juros
    print("   R$ {:.2f}           {}               {}                 {:.2f}     ".format(valor_divida, valor_juros,
                                                                                          quantidade_parcelas,
                                                                                          valor_divida /
                                                                                          quantidade_parcelas))

    valor_divida = valor_divida - valor_juros
    quantidade_parcelas = 6
    valor_juros = (15 / 100) * valor_divida
    valor_divida = valor_divida + valor_juros
    print("   R$ {:.2f}           {}               {}                 {:.2f}     ".format(valor_divida, valor_juros,
                                                                                          quantidade_parcelas,
                                                                                          valor_divida /
                                                                                          quantidade_parcelas))

    valor_divida = valor_divida - valor_juros
    quantidade_parcelas = 9
    valor_juros = (20 / 100) * valor_divida
    valor_divida = valor_divida + valor_juros
    print("   R$ {:.2f}           {}               {}                 {:.2f}     ".format(valor_divida, valor_juros,
                                                                                          quantidade_parcelas,
                                                                                          valor_divida /
                                                                                          quantidade_parcelas))

    valor_divida = valor_divida - valor_juros
    quantidade_parcelas = 12
    valor_juros = (25 / 100) * valor_divida
    valor_divida = valor_divida + valor_juros
    print("   R$ {:.2f}           {}               {}                 {:.2f}     ".format(valor_divida, valor_juros,
                                                                                          quantidade_parcelas,
                                                                                          valor_divida /
                                                                                          quantidade_parcelas))


# 42. Faça um programa que leia uma quantidade indeterminada de números positivos e conte quantos deles estão nos
# seguintes intervalos: [0-25], [26-50], [51-75] e [76-100]. A entrada de dados deverá terminar quando for lido um
# número negativo.


def numeros_positivos_intervalo():
    numero_positivo = 0
    contador_um = 0
    contador_dois = 0
    contador_tres = 0
    contador_quatro = 0
    lista_um = []
    lista_dois = []
    lista_tres = []
    lista_quatro = []

    while numero_positivo >= 0:

        numero_positivo = int(input("Digite um número positivo: "))

        if numero_positivo in lista_um or numero_positivo in lista_dois or numero_positivo in lista_tres \
                or numero_positivo in lista_quatro:
            print("Este número já foi adicionado!")

        if 0 <= numero_positivo <= 25:
            contador_um += 1
            lista_um.append(numero_positivo)

        elif 26 <= numero_positivo <= 50:
            contador_dois += 1
            lista_dois.append(numero_positivo)

        elif 51 <= numero_positivo <= 75:
            contador_tres += 1
            lista_tres.append(numero_positivo)

        elif 76 <= numero_positivo <= 100:
            contador_quatro += 1
            lista_quatro.append(numero_positivo)

        else:
            print("Número Inválido!")
            print("Digitação finalizada!")

    tamanho_lista_um = len(sorted(set(lista_um)))
    tamanho_lista_dois = len(sorted(set(lista_dois)))
    tamanho_lista_tres = len(sorted(set(lista_tres)))
    tamanho_lista_quatro = len(sorted(set(lista_quatro)))

    if contador_um > 0:
        print("Há {} número(s) no intervalo [0-25] -> {}".format(tamanho_lista_um, sorted(set(lista_um))))
    else:
        print("Não há números no intervalo [0-25]")

    if contador_dois > 0:
        print("Há {} número(s) no intervalo [26-50] -> {}".format(tamanho_lista_dois, sorted(set(lista_dois))))
    else:
        print("Não há números no intervalo [26-50]")

    if contador_tres > 0:
        print("Há {} número(s) no intervalo [51-75] -> {}".format(tamanho_lista_tres, sorted(set(lista_tres))))
    else:
        print("Não há números no intervalo [51-75]")

    if contador_quatro > 0:
        print("Há {} número(s) no intervalo [76-100] -> {}".format(tamanho_lista_quatro, sorted(set(lista_quatro))))
    else:
        print("Não há números no intervalo [76-100]")


# 43. O cardápio de uma café é o seguinte: (especificação) Código Preço Cachorro Quente 100 R$ 1,
# 20 Bauru Simples 101 R$ 1,30 Bauru com ovo 102 R$ 1,50 Hambúrguer 103 R$ 1,20 Cheeseburguer
# 104 R$ 1,30 efrigerante 105 R$ 1,00 Faça um programa que leia o código dos itens pedidos e as
# quantidades desejadas. Calcule e mostre o valor a ser pago por ‘item’ (preço * quantidade) e o total geral do pedido.
# Considere que o cliente deve informar quando o pedido deve ser encerrado.

def lanchonete():
    print("--------------------------------")
    print("Especificação   Código    Preço")
    print("Cachorro Quente  100     R$ 1,20")
    print("Bauru Simples    101     R$ 1,30")
    print("Bauru com ovo    102     R$ 1,50")
    print("Hambúrguer       103     R$ 1,20")
    print("Cheeseburguer    104     R$ 1,30")
    print("Refrigerante     105     R$ 1,00")
    print("--------------------------------")

    fazer_pedido = int(input("Digite 1 para fazer seu pedido ou 2 para TERMINAR: "))
    while fazer_pedido != 1 and fazer_pedido != 2:
        print("--------------")
        print("Opção Inválida")
        print("--------------")
        fazer_pedido = int(input("Digite 1 para fazer seu pedido ou 2 para TERMINAR: "))

    if fazer_pedido == 2:
        print("--------------------------------")
        print("Programa encerrado pelo usuário!")
        print("--------------------------------")
        return 1

    preco_total = 0
    quantidade_cachorro_quente = 0
    quantidade_bauru_simples = 0
    quantidade_bauru_com_ovo = 0
    quantidade_hamburguer = 0
    quantidade_cheeseburguer = 0
    quantidade_refrigerante = 0

    contador_cachorro_quente = 0
    contador_bauru_simples = 0
    contador_bauru_com_ovo = 0
    contador_hamburguer = 0
    contador_cheeseburguer = 0
    contador_refrigerante = 0

    preco_por_cachorro_quente = 0
    preco_por_bauru_simples = 0
    preco_por_bauru_com_ovo = 0
    preco_por_hamburguer = 0
    preco_por_cheeseburguer = 0
    preco_por_refrigerante = 0

    while fazer_pedido != 2:

        if fazer_pedido == 1:

            print("------------------------------")
            print("Digite o código do seu pedido!")
            print("------------------------------")
            codigo_pedido = int(input("Digite o código do pedido(100, 101, 102, 103, 104, ou 105): "))

            if codigo_pedido == 100:
                print("----------------------------------")
                print("Você selecionou 'Cachorro Quente'!")
                print("----------------------------------")

                quantidade_cachorro_quente = int(input("Digite a quantidade desejada: "))
                contador_cachorro_quente += quantidade_cachorro_quente
                preco_cachorros_quentes = 1.20 * quantidade_cachorro_quente
                preco_total += preco_cachorros_quentes

                preco_por_cachorro_quente += 1.20 * quantidade_cachorro_quente

            elif codigo_pedido == 101:
                print("--------------------------------")
                print("Você selecionou 'Bauru Simples'!")
                print("--------------------------------")

                quantidade_bauru_simples = int(input("Digite a quantidade desejada: "))
                contador_bauru_simples += quantidade_bauru_simples
                preco_bauru_simples = 1.30 * quantidade_bauru_simples
                preco_total += preco_bauru_simples

                preco_por_bauru_simples += 1.30 * quantidade_bauru_simples

            elif codigo_pedido == 102:
                print("--------------------------------")
                print("Você selecionou 'Bauru com Ovo'!")
                print("--------------------------------")

                quantidade_bauru_com_ovo = int(input("Digite a quantidade desejada: "))
                contador_bauru_com_ovo += quantidade_bauru_com_ovo
                preco_bauru_com_ovo = 1.50 * quantidade_bauru_com_ovo
                preco_total += preco_bauru_com_ovo

                preco_por_bauru_com_ovo += 1.50 * quantidade_bauru_com_ovo

            elif codigo_pedido == 103:
                print("-----------------------------")
                print("Você selecionou 'Hambúrguer'!")
                print("-----------------------------")

                quantidade_hamburguer = int(input("Digite a quantidade desejada: "))
                contador_hamburguer += quantidade_hamburguer
                preco_hamburguer = 1.20 * quantidade_hamburguer
                preco_total += preco_hamburguer

                preco_por_hamburguer += 1.20 * quantidade_hamburguer

            elif codigo_pedido == 104:
                print("-----------------------------")
                print("Você selecionou 'Cheeseburguer'!")
                print("-----------------------------")

                quantidade_cheeseburguer = int(input("Digite a quantidade desejada: "))
                contador_cheeseburguer += quantidade_cheeseburguer
                preco_cheeseburguer = 1.30 * quantidade_cheeseburguer
                preco_total += preco_cheeseburguer

                preco_por_cheeseburguer += 1.30 * quantidade_cheeseburguer

            elif codigo_pedido == 105:
                print("-----------------------------")
                print("Você selecionou 'Refrigerante'!")
                print("-----------------------------")

                quantidade_refrigerante = int(input("Digite a quantidade desejada: "))
                contador_refrigerante += quantidade_refrigerante
                preco_refrigerante = 1.00 * quantidade_refrigerante
                preco_total += preco_refrigerante

                preco_por_refrigerante += 1.00 * quantidade_refrigerante

            else:
                print("------------------------------------")
                print("Não existem pedidos com este código!")
                print("------------------------------------")

            fazer_pedido = int(input("Digite 1 para adicionar produtos ao pedido ou 2 para TERMINAR: "))
            while fazer_pedido != 1 and fazer_pedido != 2:
                print("--------------")
                print("Opção Inválida")
                print("--------------")
                fazer_pedido = int(input("Digite 1 para adicionar produtos ao pedido ou 2 para TERMINAR: "))

    print("-------------------------------")
    print("Pedido finalizado pelo usuário!")
    print("-------------------------------")
    if quantidade_cachorro_quente > 0 or quantidade_bauru_simples > 0 or quantidade_bauru_com_ovo > 0 \
            or quantidade_hamburguer > 0 or quantidade_cheeseburguer > 0 or quantidade_refrigerante > 0:
        print("PEDIDO              QUANTIDADE       PREÇO TOTAL")

        if quantidade_cachorro_quente > 0:
            print("CACHORRO QUENTE         {}              R${:.2f}".format(contador_cachorro_quente,
                                                                            preco_por_cachorro_quente))
        if quantidade_bauru_simples > 0:
            print("BAURU SIMPLES           {}              R${:.2f}".format(contador_bauru_simples,
                                                                            preco_por_bauru_simples))
        if quantidade_bauru_com_ovo > 0:
            print("BAURU COM OVO           {}              R${:.2f}".format(contador_bauru_com_ovo,
                                                                            preco_por_bauru_com_ovo))
        if quantidade_hamburguer > 0:
            print("HAMBÚRGUER              {}              R${:.2f}".format(contador_hamburguer, preco_por_hamburguer))
        if quantidade_cheeseburguer > 0:
            print("CHEESEBÚRGUER           {}              R${:.2f}".format(contador_cheeseburguer,
                                                                            preco_por_cheeseburguer))
        if quantidade_refrigerante > 0:
            print("REFRIGERANTE            {}              R${:.2f}".format(contador_refrigerante,
                                                                            preco_por_refrigerante))

        print("                                       R${:.2f}".format(preco_total))
    else:
        print("O usuário não desejou comprar nada!")


# 44. Numa eleição presidencial existem quatro candidatos. Os votos são informados por código. Os códigos
# utilizados são: 1, 2, 3, 4 — Votos para os respetivos candidatos (deve montar a tabela ex-: 1 - Jose/ 2-
# João/etc) 5 - Voto Nulo 6 — Voto em Branco Faça um programa que calcule e mostre: O total de votos para cada
# candidato; O total de votos nulos; O total de votos em branco; A percentagem de votos nulos sobre o total de votos;
# #A percentagem de votos em branco sobre o total de votos. Para finalizar o conjunto de votos tem-se o valor zero.

def eleicao_presidencial():
    print("--------------------")
    print("1 - Manuel Fonseca")
    print("2 - Silva Ramos")
    print("3 - Fernando Belarte")
    print("4 - Henrique Cardoso")
    print("5 - VOTO NULO")
    print("6 - VOTO EM BRANCO")
    print("--------------------")

    contador_um = 0
    contador_dois = 0
    contador_tres = 0
    contador_quatro = 0
    contador_nulo = 0
    contador_em_branco = 0
    contador_de_votos = 0

    votar = int(input("Digite 1 para votar ou 0 para TERMINAR: "))
    while votar != 1 and votar != 0:
        print("--------------")
        print("Opção Inválida")
        print("--------------")
        votar = int(input("Digite 1 para votar ou 0 para TERMINAR: "))

    if votar == 0:
        print("--------------------------------")
        print("Programa encerrado pelo usuário!")
        print("--------------------------------")
        return 1

    while votar != 0:

        print("---------------------")
        print("Você optou por votar!")
        print("---------------------")

        voto = int(input("Digite o número de votação(1 a 6):"))

        if voto == 1:
            print("-----------------------------")
            print("Você votou em Manuel Fonseca!")
            print("-----------------------------")
            contador_um += 1
            contador_de_votos += 1

        elif voto == 2:
            print("--------------------------")
            print("Você votou em Silva Ramos!")
            print("--------------------------")
            contador_dois += 1
            contador_de_votos += 1

        elif voto == 3:
            print("-------------------------------")
            print("Você votou em Fernando Belarte!")
            print("-------------------------------")
            contador_tres += 1
            contador_de_votos += 1

        elif voto == 4:
            print("-------------------------------")
            print("Você votou em Henrique Cardoso!")
            print("-------------------------------")
            contador_quatro += 1
            contador_de_votos += 1

        elif voto == 5:
            print("----------------")
            print("Você votou NULO!")
            print("----------------")
            contador_nulo += 1
            contador_de_votos += 1

        elif voto == 6:
            print("---------------------")
            print("Você votou EM BRANCO!")
            print("---------------------")
            contador_em_branco += 1
            contador_de_votos += 1

        else:
            print("---------------------------------")
            print("Não candidaturas com este número!")
            print("---------------------------------")

        votar = int(input("Digite 1 para votar novamente ou 0 para TERMINAR: "))

        while votar != 1 and votar != 0:
            print("--------------")
            print("Opção Inválida")
            print("--------------")
            votar = int(input("Digite 1 para votar novamente ou 0 para TERMINAR: "))

    print("-----------------------------------------------------------------")
    print("CANDIDATOS           QUANTIDADE DE VOTOS")
    print("Manuel Fonseca                {}".format(contador_um))
    print("Silva Ramos                   {}".format(contador_dois))
    print("Fernando Belarte              {}".format(contador_tres))
    print("Henrique Cardoso              {}".format(contador_quatro))
    print("VOTOS NULOS                   {} sendo {:.2f}% equivalente ao"
          " TOTAL".format(contador_nulo, (contador_nulo * 100) / contador_de_votos))
    print("VOTOS EM BRANCO               {} sendo {:.2f}% equivalente ao"
          " TOTAL".format(contador_em_branco, (contador_em_branco * 100) / contador_de_votos))
    print("                              {} VOTO(S) AO TOTAL".format(contador_de_votos))
    print("-----------------------------------------------------------------")


# 45. Desenvolver um programa para verificar a nota do aluno numa prova com 10 questões, o programa deve perguntar
# ao aluno a resposta de cada questão e ao final comparar com o gabarito da prova e assim calcular o total de acertos
# e a nota (atribuir 1 ponto por resposta certa). Após cada aluno utilizar o sistema deve ser feita uma pergunta se
# outro aluno vai utilizar o sistema. Após todos os alunos terem respondido informar: Maior e Menor Acerto; Total de
# Alunos que utilizaram o sistema; A Média das Notas da Turma. Gabarito da Prova:
# 01 - A 02 - B 03 - C 04 - D 05 - E 06 - E 07 - D 08 - C 09 - B 10 - A Após concluir isto poderia incrementar o
# programa permitindo que o professor digite o gabarito da prova antes dos alunos usarem o programa.

def prova():
    maior_acerto = 0

    class Aluno:

        def __init__(self, numero_aluno, total_acertos, nota):
            self.__numero_aluno = numero_aluno
            self.__total_acertos = total_acertos
            self.__nota = nota

        @property
        def numero_aluno(self):
            return self.__numero_aluno

        @property
        def total_acertos(self):
            return self.__total_acertos

        @property
        def nota(self):
            return self.__nota

    gabarito = []
    alunos = []
    sair = 0

    for questao in range(0, 10):
        gabarito_questao = input("PROFESSOR -> Digite o gabarito da Questão {}: ".format(questao + 1)).strip().upper()
        gabarito.append(gabarito_questao)

    print("------------------------------------------------------------------------")
    sair = int(input("Irá usar o sistema? Digite 1 para CONTINUAR ou 0 para SAIR: "))

    while sair != 0:

        for aluno in range(1, 1000):

            print("------------------")
            print("Bem vindo Aluno {}".format(aluno))
            print("------------------")
            contador_acertos = 0
            nota = 0

            for posicao in range(0, 10):
                questao_prova = input("Digite a resposta da Questão {}:".format(posicao + 1)).strip().upper()
                if gabarito[posicao] == questao_prova:
                    contador_acertos += 1
                    nota += 1

            aluno = Aluno(aluno, contador_acertos, nota)
            alunos.extend([[aluno.numero_aluno, aluno.total_acertos, aluno.nota]])

            sair = int(input("Irá usar o sistema? Digite 1 para CONTINUAR ou 0 para SAIR: "))
            if sair == 0:
                break

    lista_acertos = []
    for posicao in range(0, len(alunos)):
        lista_acertos.append(alunos[posicao][1])

    lista_notas = []
    for posicao in range(0, len(alunos)):
        lista_notas.append(alunos[posicao][2])

    media = sum(lista_notas) / len(lista_notas)

    print("-----------------------------------------------------------------")
    print("O maior acerto é {} questão(es) e o menor acerto é {} questão(es)".format(max(lista_acertos),
                                                                                     min(lista_acertos)))
    print("O  total de alunos que utilizou o sistema foi {} aluno(s)".format(len(alunos)))

    print("A média das notas é {:.2f}".format(media))
    print("-----------------------------------------------------------------")


# 46. Numa competição de salto em distância cada atleta tem direito a cinco saltos. No final da série de saltos de
# cada atleta, o melhor e o pior resultados são eliminados. O seu resultado fica a ser a média dos três valores
# restantes. Deve fazer um programa que receba o nome e as cinco distâncias alcançadas pelo atleta nos seus
# saltos e depois informe a média dos saltos conforme a descrição acima informada (retirar o melhor e o pior salto e
# depois calcular a média). Use uma lista para armazenar os saltos. Os saltos são informados na ordem da
# execução, portanto não são ordenados. O programa deve ser encerrado quando não for informado o nome do atleta. A
# saída do programa deve ser conforme o exemplo abaixo: Atleta: Rodrigo Curvêllo
# Primeiro Salto: 6,5 m
# Segundo Salto: 6,1 m
# Terceiro Salto: 6,2 m
# Quarto Salto: 5,4 m
# Quinto Salto: 5,3 m
# Melhor salto: 6,5 m
# Pior salto: 5,3 m
# Média dos demais saltos: 5,9 m
# Resultado:
# Rodrigo Curvêllo: 5.9 m

def competicao_salto():
    nome = input("Digite o nome do atleta: ").capitalize()
    saltos = []
    if nome != "":

        for posicao in range(1, 6):
            salto = float(input("Digite a distância do salto {}: ".format(posicao)))
            saltos.append(salto)

        print("--------------------------------")
        print("Atleta: {}".format(nome))
        print("")
        print("Primeiro Salto: {} m".format(saltos[0]))
        print("Segundo Salto: {} m".format(saltos[1]))
        print("Terceiro Salto: {} m".format(saltos[2]))
        print("Quarto Salto: {} m".format(saltos[3]))
        print("Quinto Salto: {} m".format(saltos[4]))
        print("")
        print("Melhor Salto: {} m".format(max(saltos)))
        print("Pior Salto: {} m".format(min(saltos)))
        media = (sum(saltos) - max(saltos) - min(saltos)) / 3
        print("Média dos demais saltos: {:.2f} m".format(media))
        print("")
        print("Resultado Final:")
        print("{}: {:.2f} m".format(nome, media))
        print("--------------------------------")

    else:
        return 1


# 47.Numa competição de ginástica, cada atleta recebe votos de sete jurados. A melhor e a pior nota são eliminadas.
# A sua nota fica a ser a média dos votos restantes. Deve fazer um programa que receba o nome do ginasta e as
# notas dos sete jurados alcançadas pelo atleta na sua apresentação e depois informe a sua média, conforme a
# descrição acima informada (retirar o melhor e o pior salto e depois calcular a média com as notas restantes). As
# notas não são informados ordenadas. Um exemplo de saída do programa deve ser conforme o exemplo abaixo: Atleta:
# Aparecido Parente Nota: 9.9 Nota: 7.5 Nota: 9.5 Nota: 8.5 Nota: 9.0 Nota: 8.5 Nota: 9.7

# Resultado:
# Atleta: Aparecido Parente
# Melhor nota: 9,9
# Pior nota: 7.5
# Média: 9,04

def competicao_ginastica():
    nome = input("Digite o nome do atleta: ").capitalize()
    notas = []
    if nome != "":

        for posicao in range(1, 8):
            nota = float(input("Digite a nota {}: ".format(posicao)))
            notas.append(nota)

        print("--------------------------------")
        print("Atleta: {}".format(nome))
        print("Nota: {}".format(notas[0]))
        print("Nota: {}".format(notas[1]))
        print("Nota: {}".format(notas[2]))
        print("Nota: {}".format(notas[3]))
        print("Nota: {}".format(notas[4]))
        print("Nota: {}".format(notas[5]))
        print("Nota: {}".format(notas[6]))
        print("")
        print("Resultado Final:")
        print("Atleta: {}".format(nome))
        print("Melhor nota: {}".format(max(notas)))
        print("Pior nota: {}".format(min(notas)))

        media = (sum(notas) - max(notas) - min(notas)) / 5
        print("Média: {}".format(media))
        print("--------------------------------")

    else:
        return 1


# 48. Faça um programa que peça um número inteiro positivo e em seguida mostre este numero invertido.
# Exemplo:
# 12376489
# => 98467321

def numero_invertido():
    numero = int(input("Informe um número inteiro: "))
    inverso = 0

    while numero != 0:
        resto = numero % 10
        inverso = inverso * 10 + resto
        numero = numero // 10

    print("O número invertido é", inverso)


# 49. Faça um programa que mostre o n termos da Série a seguir:
# S = 1/1 + 2/3 + 3/5 + 4/7 + 5/9 + ... + n/m. Imprima no final a soma da série.

def soma_fracao():
    numerador = 1
    denominador = 1
    lista_numerador = []
    lista_denominador = []
    soma = 1

    print("S = ", end="")

    while numerador <= 10:
        print(numerador, "/", denominador, "   +   ", end="")
        lista_numerador.append(numerador)
        lista_denominador.append(denominador)
        numerador += 1
        denominador += 2

    print(numerador, "/", denominador, " = ", soma)


# 50. Sendo H= 1 + 1/2 + 1/3 + 1/4 + ... + 1/N, Faça um programa que calcule o valor de H com N termos.

def soma_fracao_escolha():
    numerador = 1
    denominador = 1
    lista_numerador = []
    lista_denominador = []
    soma = 0

    print("H = ", end="")

    n = int(input("Digite o término(n): "))

    while denominador < n:
        print(numerador, "/", denominador, "   +   ", end="")
        lista_numerador.append(numerador)
        lista_denominador.append(denominador)
        denominador += 1

    for i in range(1, n + 1):
        soma = soma + 1 / i

    print(numerador, "/", denominador, " = ", soma)


if __name__ == "__main__":
    soma_fracao()
