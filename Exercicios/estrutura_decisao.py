import re
import math

#1.Faça um Programa que peça dois números e imprima o maior deles.

def maior_numero():
    numero_um = int(input("Digite o primeiro número: "))
    numero_dois = int(input("Digite o segundo número: "))

    if(numero_um > numero_dois):
        print("O maior número é {}".format(numero_um))
    else:
        print("O maior número é {}!".format(numero_dois))

#2.Faça um Programa que peça um valor e mostre na tela se o valor é positivo ou negativo

def positivo_negativo():
    valor = float(input("Digite o valor: "))

    if(valor > 0):
        print("O valor é {} é positivo!".format(valor))
    else:
        print("O valor é {} negativo!".format(valor))

#3.Faça um Programa que verifique se uma letra digitada é "F" ou "M". Conforme a letra escrever: F - Feminino, M - Masculino, Sexo Inválido.

def sexo_letra():

    letra = input("Digite F se for feminino ou M se for masculino:").upper().strip()
    if(letra == "F"):
        print("F - Feminino")
    elif(letra == "M"):
        print("M - Masculino")
    else:
        print("Sexo Inválido")

#4.Faça um Programa que verifique se uma letra digitada é vogal ou consoante.

def vogal_consoante():

    letra = input("Digite uma letra:").upper().strip()
    if(letra == "A" or letra == "E" or letra == "I" or letra == "O" or letra == "U"):
        print("A letra digitada é uma vogal!")
    else:
        print("A letra digitada é uma consoante!")

#5.Faça um programa para a leitura de duas notas parciais de um aluno. O programa deve calcular a média alcançada por aluno e apresentar:
#A mensagem "Aprovado", se a média alcançada for maior ou igual a sete;
#A mensagem "Reprovado", se a média for menor do que sete;
#A mensagem "Aprovado com Distinção", se a média for igual a dez.

def media():
    nota_um = float(input("Digite a primeira nota(1 a 10): "))
    nota_dois = float(input("Digite a segunda nota(1 a 10): "))

    media = (nota_um + nota_dois) / 2

    if(media >= 7 and media < 10):
        print("Aprovado!")
    elif(media < 7):
        print("Reprovado!")
    elif(media == 10):
        print("Aprovado com Distinção!")
    else:
        print("Média fora do intervalo!")

#6.Faça um Programa que leia três números e mostre o maior deles.

def maior_numero():
    numero_um = int(input("Digite o primeiro número: "))
    numero_dois = int(input("Digite o segundo número: "))
    numero_tres = int(input("Digite o terceiro número: "))

    if (numero_um > numero_dois and numero_um > numero_tres):
        print("O maior número é {}!".format(numero_um))
    elif(numero_dois > numero_um and numero_dois > numero_tres):
        print("O maior número é {}!".format(numero_dois))
    else:
        print("O maior número é {}!".format(numero_tres))

#7.Faça um Programa que leia três números e mostre o maior e o menor deles.

def maior_menor_numero():
    numero_um = int(input("Digite o primeiro número: "))
    numero_dois = int(input("Digite o segundo número: "))
    numero_tres = int(input("Digite o terceiro número: "))

    if (numero_um > numero_dois and numero_um > numero_tres):
        print("O maior número é {}!".format(numero_um))
        if(numero_dois > numero_tres):
            print("O menor número é {}!".format(numero_tres))
        else:
            print("O menor número é {}!".format(numero_dois))

    elif(numero_dois > numero_um and numero_dois > numero_tres):
        print("O maior número é {}!".format(numero_dois))
        if (numero_um > numero_tres):
            print("O menor número é {}!".format(numero_tres))
        else:
            print("O menor número é {}!".format(numero_um))
    else:
        print("O maior número é {}!".format(numero_tres))
        if (numero_um > numero_dois):
            print("O menor número é {}!".format(numero_dois))
        else:
            print("O menor número é {}!".format(numero_um))

#8.Faça um programa que pergunte o preço de três produtos e informe qual produto você deve comprar, sabendo que a decisão é sempre pelo mais barato.

def produto_mais_barato():

    preco_um = float(input("Digite o preço do primeiro produto: "))
    preco_dois = float(input("Digite o preço do segundo produto: "))
    preco_tres = float(input("Digite o preço do terceiro produto: "))

    if(preco_um < preco_dois and preco_um < preco_tres):
        print("O produto de preço R${:.2f} é o mais barato!".format(preco_um))
    elif(preco_dois < preco_um and preco_dois < preco_tres):
        print("O produto de preço R${:.2f} é o mais barato!".format(preco_dois))
    else:
        print("O produto de preço R${:.2f} é o mais barato!".format(preco_tres))

#9.Faça um Programa que leia três números e mostre-os em ordem decrescente.

def ordem_decrescente():
    numero_um = int(input("Digite o primeiro número: "))
    numero_dois = int(input("Digite o segundo número: "))
    numero_tres = int(input("Digite o terceiro número: "))

    if (numero_um > numero_dois and numero_um > numero_tres):
        if(numero_dois > numero_tres):
            print("Ordem decrescente: {}, {}, {}".format(numero_um, numero_dois, numero_tres))
        else:
            print("Ordem decrescente: {}, {}, {}".format(numero_um, numero_tres, numero_dois))

    elif(numero_dois > numero_um and numero_dois > numero_tres):
        if (numero_um > numero_tres):
            print("Ordem decrescente: {}, {}, {}".format(numero_dois, numero_um, numero_tres))
        else:
            print("Ordem decrescente: {}, {}, {}".format(numero_dois, numero_tres, numero_um))
    else:
        if (numero_um > numero_dois):
            print("Ordem decrescente: {}, {}, {}".format(numero_tres, numero_um, numero_dois))
        else:
            print("Ordem decrescente: {}, {}, {}".format(numero_tres, numero_dois, numero_um))

#10.Faça um Programa que pergunte em que turno você estuda.
#Peça para digitar M-matutino ou V-Vespertino ou N- Noturno. Imprima a mensagem "Bom Dia!", "Boa Tarde!" ou "Boa Noite!" ou "Valor Inválido!", conforme o caso.

def turno():
    letra = input("Digite M se você estuda de manhã, V se estuda de tarde ou N se estuda de noite: ").upper().strip()
    if (letra == "M"):
        print("Bom dia!")
    elif (letra == "V"):
        print("Boa tarde!")
    elif(letra == "N"):
        print("Boa noite!")
    else:
        print("Valor Inválido!")

#11.As Organizações Tabajara resolveram dar um aumento de salário aos seus colaboradores e lhe contraram para desenvolver o programa que calculará os reajustes.
#Faça um programa que recebe o salário de um colaborador e o reajuste segundo o seguinte critério, baseado no salário atual:
#salários até R$ 280,00 (incluindo) : aumento de 20%
#salários entre R$ 280,00 e R$ 700,00 : aumento de 15%
#salários entre R$ 700,00 e R$ 1500,00 : aumento de 10%
#salários de R$ 1500,00 em diante : aumento de 5% Após o aumento ser realizado, informe na tela:
#o salário antes do reajuste;
#o percentual de aumento aplicado;
#o valor do aumento;
#o novo salário, após o aumento.

def reajuste():
    salario_sem_reajuste = float(input("Digite seu salário atual(sem reajuste): "))
    if(salario_sem_reajuste <= 280):
        salario_com_reajuste = ((20 / 100) * salario_sem_reajuste) + salario_sem_reajuste
        percentual = 20
        valor_do_aumento = (20 / 100) * salario_sem_reajuste
    elif(salario_sem_reajuste > 280 and salario_sem_reajuste < 700):
        salario_com_reajuste = ((15 / 100) * salario_sem_reajuste) + salario_sem_reajuste
        percentual = 15
        valor_do_aumento = (15 / 100) * salario_sem_reajuste
    elif(salario_sem_reajuste >= 700 and salario_sem_reajuste < 1500):
        salario_com_reajuste = ((10 / 100) * salario_sem_reajuste) + salario_sem_reajuste
        percentual = 10
        valor_do_aumento = (10 / 100) * salario_sem_reajuste
    elif(salario_sem_reajuste >= 1500):
        salario_com_reajuste = ((5 / 100) * salario_sem_reajuste) + salario_sem_reajuste
        percentual = 5
        valor_do_aumento = (5 / 100) * salario_sem_reajuste

    print("Salário antes do reajuste: R${:.2f}".format(salario_sem_reajuste))
    print("Foi aplicado um percentual de: {}%".format(percentual))
    print("O reajuste foi de: R${:.2f}".format(valor_do_aumento))
    print("Salário após reajuste: R${:.2f}".format(salario_com_reajuste))

#19.Faça um Programa que leia um número inteiro menor que 1000 e imprima a quantidade de centenas, dezenas e unidades do mesmo.
#Observando os termos no plural a colocação do "e", da vírgula entre outros. Exemplo:
#326 = 3 centenas, 2 dezenas e 6 unidades
#12 = 1 dezena e 2 unidades Testar com: 326, 300, 100, 320, 310,305, 301, 101, 311, 111, 25, 20, 10, 21, 11, 1, 7 e 16

#12.Faça um programa para o cálculo de uma folha de pagamento, sabendo que os descontos são do Imposto de Renda, que depende do salário bruto (conforme tabela abaixo) e 3% para o Sindicato e que o FGTS corresponde a 11% do Salário Bruto, mas não é descontado (é a empresa que deposita). O Salário Líquido corresponde ao Salário Bruto menos os descontos. O programa deverá pedir ao usuário o valor da sua hora e a quantidade de horas trabalhadas no mês.
#Desconto do IR:
#Salário Bruto até 900 (inclusive) - isento
#Salário Bruto até 1500 (inclusive) - desconto de 5%
#Salário Bruto até 2500 (inclusive) - desconto de 10%
#Salário Bruto acima de 2500 - desconto de 20% Imprima na tela as informações, dispostas conforme o exemplo abaixo. No exemplo o valor da hora é 5 e a quantidade de hora é 220.
#Salário Bruto: (5 * 220)        : R$ 1100,00
#(-) IR (5%)                     : R$   55,00
#(-) INSS ( 10%)                 : R$  110,00
#FGTS (11%)                      : R$  121,00
#Total de descontos              : R$  165,00
#Salário Liquido                 : R$  935,00

def folha_pagamento():
    dinheiro_hora = float(input("Quanto você ganha por hora? "))
    numero_horas = float(input("Quantas horas você trabalha no mês? "))

    salario_bruto = dinheiro_hora * numero_horas

    if(salario_bruto <= 900):
        percentual = 0
        valor_ir = 0
    elif(salario_bruto > 900 and salario_bruto <= 1500):
        percentual = 5
        valor_ir = (5 / 100) * salario_bruto
    elif(salario_bruto > 1500 and salario_bruto <= 2500):
        percentual = 10
        valor_ir = (10 / 100) * salario_bruto
    elif(salario_bruto > 2500):
        percentual = 20
        valor_ir = (20 / 100) * salario_bruto

    valor_inss = (10 / 100) * salario_bruto
    valor_fgts = (11 / 100) * salario_bruto
    descontos = valor_ir + valor_inss
    salario_liquido = salario_bruto - valor_ir - valor_inss

    print("Salário Bruto: ({} * {})    : R$ {:.2f}".format(dinheiro_hora, numero_horas, salario_bruto))
    print("(-) IR ({}%)                    : R$  {:.2f}".format(percentual, valor_ir))
    print("(-) INSS ( 10%)                 : R$  {:.2f}".format(valor_inss))
    print("FGTS (11%)                      : R$  {:.2f}".format(valor_fgts))
    print("Total de descontos              : R$  {:.2f}".format(descontos))
    print("Salário Liquido                 : R$  {:.2f}".format(salario_liquido))


#13. Faça um Programa que leia um número e exiba o dia correspondente da semana. (1-Domingo, 2- Segunda, etc.), se digitar outro valor deve aparecer valor inválido.

def dia_semana():

    dia = int(input("Digite o número da semana(1 a 7): "))

    if(dia == 1):
        print("{} - Domingo".format(dia))
    elif (dia == 2):
        print("{} - Segunda".format(dia))
    elif (dia == 3):
        print("{} - Terça".format(dia))
    elif (dia == 4):
        print("{} - Quarta".format(dia))
    elif (dia == 5):
        print("{} - Quinta".format(dia))
    elif (dia == 6):
        print("{} - Sexta".format(dia))
    elif (dia == 7):
        print("{} - Sábado".format(dia))
    else:
        print("Valor Inválido!")

#14. Faça um programa que lê as duas notas parciais obtidas por um aluno numa disciplina ao longo de um semestre, e calcule a sua média. A atribuição de conceitos obedece à tabela abaixo:
#Média de Aproveitamento  Conceito
# Entre 9.0 e 10.0        A
# Entre 7.5 e 9.0         B
# Entre 6.0 e 7.5         C
# Entre 4.0 e 6.0         D
# Entre 4.0 e zero        E

def media():
    nota_um = float(input("Digite a primeira nota: "))
    nota_dois = float(input("Digite a segunda nota: "))
    media = (nota_um + nota_dois)/2

    if(media >= 9.0 and media <=10.0):
        conceito = "A"
    elif (media >= 7.5 and media < 9.0):
        conceito = "B"
    elif (media >= 6.5 and media < 7.0):
        conceito = "C"
    elif (media >= 4.0 and media < 6.0):
        conceito = "D"
    elif (media >= 0.0 and media < 4.0):
        conceito = "E"

    print("A média das notas é {:.2f}! - Conceito {}".format(media, conceito))


#15Faça um Programa que peça os 3 lados de um triângulo. O programa deverá informar se os valores podem ser um triângulo. Indique, caso os lados formem um triângulo, se o mesmo é: equilátero, isósceles ou escaleno.
#Dicas:
#Três lados formam um triângulo quando a soma de quaisquer dois lados for maior que o terceiro;
#Triângulo Equilátero: três lados iguais;
#Triângulo Isósceles: quaisquer dois lados iguais;
#Triângulo Escaleno: três lados diferentes;

def triangulo():

    lado_um = int(input("Digite o primeiro lado do triângulo: "))
    lado_dois = int(input("Digite o segundo lado do triângulo: "))
    lado_tres = int(input("Digite o terceiro lado do triângulo: "))

    if(verifica_triangulo(lado_um, lado_dois, lado_tres)):

        if(verifica_equilatero(lado_um, lado_dois, lado_tres)):
            return 0
        verifica_isoceles(lado_um, lado_dois, lado_tres)
        verifica_escaleno(lado_um, lado_dois, lado_tres)
    else:
        print("Não é um triângulo válido!")

def verifica_triangulo(lado_um, lado_dois, lado_tres):
    if((lado_um + lado_dois > lado_tres) and (lado_dois + lado_tres > lado_um) and (lado_tres + lado_um > lado_dois)):
        print("É um triângulo válido!")
        return True

def verifica_equilatero(lado_um, lado_dois, lado_tres):
    if(lado_um == lado_dois and lado_um == lado_tres and lado_dois == lado_tres):
        print("É um triângulo equilátero!")
        return True

def verifica_isoceles(lado_um, lado_dois, lado_tres):
    if(lado_um == lado_dois or lado_um == lado_tres or lado_dois == lado_tres):
        print("É um triângulo isóceles!")

def verifica_escaleno(lado_um, lado_dois, lado_tres):
    if(lado_um != lado_dois and lado_dois != lado_tres and lado_tres != lado_um):
        print("É um triângulo Escaleno!")

#16.Faça um programa que calcule as raízes de uma equação do segundo grau, na forma ax2 + bx + c. O programa deverá pedir os valores de a, b e c e fazer as consistências, informando ao usuário nas seguintes situações:
#Se o usuário informar o valor de A igual a zero, a equação não é do segundo grau e o programa não deve fazer pedir os demais valores, sendo encerrado;
#Se o delta calculado for negativo, a equação não possui raizes reais. Informe ao usuário e encerre o programa;
#Se o delta calculado for igual a zero a equação possui apenas uma raiz real; informe-a ao usuário;
#Se o delta for positivo, a equação possui duas raiz reais; informe-as ao usuário;

def raiz():

    a = int(input("Digite o valor de 'a': "))
    if(a == 0):
        return 0
    else:
        b = int(input("Digite o valor de 'b': "))
        c = int(input("Digite o valor de 'c': "))

        delta = ((b * b) - (4 * a * c))

        if(delta < 0):
            return 0

        elif(delta == 0):

            raiz_unica = float((-1 * b) / (2 * a))
            print(raiz_unica)

        elif(delta > 0):
            raiz_um = float(((-1 * b + math.sqrt(delta)) / (2 * a)))
            raiz_dois = float(((-1 * b - math.sqrt(delta)) / (2 * a)))

            print(raiz_um, raiz_dois)

#17.Faça um Programa que peça um número correspondente a um determinado ano e em seguida informe se este ano é ou não bissexto.

def resulta_bissexto():
    ano = int(input("Digite o ano no formato 'aaaa': "))
    if(e_bissexto(ano)):
        print("O ano é bissexto!")
    else:
        print("O ano não é bissexto!")

def e_bissexto(ano):

    if(regra_um(ano) or regra_dois(ano)):
        return True

def regra_um(ano):

    if(ano % 4 == 0 and ano % 100 != 0):
        return True

def regra_dois(ano):
    if(ano % 4 == 0 and ano % 100 == 0 and ano % 400 == 0):
        return True

#18.Faça um Programa que peça uma data no formato dd/mm/aaaa e determine se a mesma é uma data válida.

def verifica_data():

    data = input("Digite a data no formato dd/mm/aaaa: ")

    numeros_data = [int(numero) for numero in re.findall(r'-?\d+\.?\d*', data)]

    dia = numeros_data[0]
    mes = numeros_data[1]
    ano = numeros_data[2]

    tupla_meses_trinta_um_dias = (1, 3, 5, 7, 9, 10, 12)
    tupla_meses_trinta_dias = (4, 6, 8, 11)

    if(mes in tupla_meses_trinta_um_dias):
        if(dia <= 31):
            if(ano >= 1000 and ano <= 9999):
                print("Data Válida!")
            else:
                print("Data inválida!")
        else:
            print("Data Inválida")

    elif(mes in tupla_meses_trinta_dias):
        if(dia <= 30):
            if(ano >= 1000 and ano <= 9999):
                print("Data Válida!")
        else:
            print("Data inválida!")

    elif(mes == 2):
        if(e_bissexto(ano)):
            if(dia <= 29):
                print("Data válida!")
            else:
                print("Data Inválida!")
        else:
            if(dia <=28):
                print("Data válida!")
            else:
                print("Data Inválida!")
    else:
        print("Data Inválida!")

#19.Faça um Programa que leia um número inteiro menor que 1000 e imprima a quantidade de centenas, dezenas e unidades do mesmo.
#Observando os termos no plural a colocação do "e", da vírgula entre outros. Exemplo:
#326 = 3 centenas, 2 dezenas e 6 unidades
#12 = 1 dezena e 2 unidades Testar com: 326, 300, 100, 320, 310,305, 301, 101, 311, 111, 25, 20, 10, 21, 11, 1, 7 e 16

def casas_numero():
    numero = int(input("Digite o número(1 a 1000): "))

    unidade = numero % 10
    dezena = (numero % 100) // 10
    centena = numero // 100
    separador1 = ""
    separador2 = ""

    if(centena > 0 and dezena > 0 and unidade > 0):
        separador1 = " , "
        separador2 = " e "
    elif (centena > 0 and dezena > 0):
        separador1 = " e "
        separador2 = ""
    elif(centena > 0 and unidade > 0) or (dezena > 0 and unidade > 0):
        separador1 = ""
        separador2 = " e "

    if(centena > 0):
        if(centena == 1):
            centena = "1 centena"
        else:
            centena = "{} centenas".format(centena)
    else:
        centena = ""

    if(dezena > 0):
        if(dezena == 1):
            dezena = "1 dezena"
        else:
            dezena = "{} dezenas".format(dezena)
    else:
        dezena = ""

    if(unidade > 0):
        if(unidade == 1):
            unidade = "1 unidade"
        else:
            unidade = "{} unidades".format(unidade)
    else:
        unidade = ""

    print("{} = {}{}{}{}{}.".format(numero, centena, separador1, dezena, separador2, unidade))

#20.Faça um Programa para leitura de três notas parciais de um aluno. O programa deve calcular a média alcançada por aluno e presentar:
#A mensagem "Aprovado", se a média for maior ou igual a 7, com a respectiva média alcançada;
#A mensagem "Reprovado", se a média for menor do que 7, com a respectiva média alcançada;
#A mensagem "Aprovado com Distinção", se a média for igual a 10.

def notas():
    nota_um = float(input("Digite a primeira nota: "))
    nota_dois = float(input("Digite a segunda nota: "))
    nota_tres = float(input("Digite a terceira nota: "))
    media = (nota_um + nota_dois + nota_tres) / 3

    if (media >= 7 and media < 10):
        print("Aprovado!")
    elif(media < 7):
        print("Reprovado!")
    elif (media == 10):
        print("Aprovado com distinção!")
    else:
        print("Média fora do intervalo!")

#21.Faça um Programa para um caixa eletrônico. O programa deverá perguntar ao usuário a valor do saque e depois informar quantas notas de cada valor serão fornecidas.
#As notas disponíveis serão as de 1, 5, 10, 50 e 100 reais. O valor mínimo é de 10 reais e o máximo de 600 reais. O programa não deve se preocupar com a quantidade de notas existentes na máquina.
#Exemplo 1: Para sacar a quantia de 256 reais, o programa fornece duas notas de 100, uma nota de 50, uma nota de 5 e uma nota de 1;
#Exemplo 2: Para sacar a quantia de 399 reais, o programa fornece três notas de 100, uma nota de 50, quatro notas de 10, uma nota de 5 e quatro notas de 1.


def caixa_eletronico():

    saque = int(input("Digite o valor do saque(10 a 600): "))
    if(saque >= 10 and saque <= 600):
        notas_de_cem = int(saque / 100)
        notas_de_cinquenta = int((saque % 100) / 50)
        notas_de_dez = int(((saque % 100) % 50) / 10)
        notas_de_cinco = int((((saque % 100) % 50) % 10) / 5)
        notas_de_um = int((((saque % 100) % 50) % 10) % 5)

        if(notas_de_cem != 0):
            print("Serão fornecidas {} nota(s) de cem".format(notas_de_cem))
        if (notas_de_cinquenta != 0):
            print("Serão fornecidas {} nota(s) de cinquenta".format(notas_de_cinquenta))
        if (notas_de_dez != 0):
            print("Serão fornecidas {} nota(s) de dez".format(notas_de_dez))
        if (notas_de_cinco != 0):
            print("Serão fornecidas {} nota(s) de cinco".format(notas_de_cinco))
        if (notas_de_um != 0):
            print("Serão fornecidas {} nota(s) de um".format(notas_de_um))

#22.Faça um Programa que peça um número inteiro e determine se ele é par ou impar. Dica: utilize o operador módulo (resto da divisão).

def par_ou_impar():
    numero = int(input("Digite um número: "))
    if(numero % 2 == 0):
        print("O número é par!")
    else:
        print("O número é impar!")

#23.Faça um Programa que peça um número e informe se o número é inteiro ou decimal. Dica: utilize uma função de arredondamento.

def arredonda(numero):

    numero_arredondado = (round(numero))

    if(numero_arredondado != numero):
        return True

def inteiro_ou_decimal():
    numero = float(input("Digite um número: "))

    if(arredonda(numero)):
        print("O número é decimal!")
    else:
        print("O número é inteiro!")

#24.Faça um Programa que leia 2 números e em seguida pergunte ao usuário qual operação ele deseja realizar. O resultado da operação deve ser acompanhado de uma frase que diga se o número é:
#par ou ímpar;
#positivo ou negativo;
#inteiro ou decimal.

def operacoes():
    numero_um = float(input("Digite o primeiro número: "))
    numero_dois = float(input("Digite o segundo número: "))



    print("---------------------------------------")
    print("1.*****************SOMA****************")
    print("2.**************SUBTRAÇÃO**************")
    print("3.************MULTIPLICAÇÃO************")
    print("4.***************DIVISÃO***************")
    print("---------------------------------------")

    operacao = int(input("Escolha a operação que deseja realizar:"))

    if(operacao == 1):
        soma = numero_um + numero_dois
        if (soma % 2 == 0):
            print("O número é par!")
        else:
            print("O número é impar!")

        if (soma > 0):
            print("O número é positivo!")
        else:
            print("O número é negativo!")

        if (arredonda(soma)):
            print("O número é decimal!")
        else:
            print("O número é inteiro!")

    elif(operacao == 2):
        subtracao = numero_um - numero_dois
        if (subtracao % 2 == 0):
            print("O número é par!")
        else:
            print("O número é impar!")

        if (subtracao > 0):
            print("O número é positivo!")
        else:
            print("O número é negativo!")

        if (arredonda(subtracao)):
            print("O número é decimal!")
        else:
            print("O número é inteiro!")
    elif (operacao == 3):
        multiplicacao = numero_um * numero_dois
        if (multiplicacao % 2 == 0):
            print("O número é par!")
        else:
            print("O número é impar!")

        if (multiplicacao > 0):
            print("O número é positivo!")
        else:
            print("O número é negativo!")

        if (arredonda(multiplicacao)):
            print("O número é decimal!")
        else:
            print("O número é inteiro!")
    elif (operacao == 4):
        divisao = numero_um / numero_dois
        if (divisao % 2 == 0):
            print("O número é par!")
        else:
            print("O número é impar!")

        if (divisao > 0):
            print("O número é positivo!")
        else:
            print("O número é negativo!")

        if (arredonda(divisao)):
            print("O número é decimal!")
        else:
            print("O número é inteiro!")

#25.Faça um programa que faça 5 perguntas para uma pessoa sobre um crime. As perguntas são:
#"Telefonou para a vítima?"
#"Esteve no local do crime?"
#"Mora perto da vítima?"
#"Devia para a vítima?"
#"Já trabalhou com a vítima?"
#O programa deve no final emitir uma classificação sobre a participação da pessoa no crime.
#Se a pessoa responder positivamente a 2 questões ela deve ser classificada como "Suspeita", entre 3 e 4 como "Cúmplice" e 5 como "Assassino". Caso contrário, ele será classificado como "Inocente".

def crime():
    contador = 0
    pergunta_um = input("Telefonou para a vítima? Responda com SIM ou NÃO: ").strip().upper()
    pergunta_dois = input("Esteve no local do crime? Responda com SIM ou NÃO: ").strip().upper()
    pergunta_tres = input("Mora perto da vítima? Responda com SIM ou NÃO: ").strip().upper()
    pergunta_quatro = input("Devia para a vítima? Responda com SIM ou NÃO: ").strip().upper()
    pergunta_cinco = input("Já trabalhou com a vítima? Responda com SIM ou NÃO: ").strip().upper()

    if(pergunta_um == "SIM"):
        contador += 1
    if (pergunta_dois == "SIM"):
        contador += 1
    if (pergunta_tres == "SIM"):
        contador += 1
    if (pergunta_quatro == "SIM"):
        contador += 1
    if (pergunta_cinco == "SIM"):
        contador += 1

    if(contador == 1):
        print("Você é inocente!")
    elif(contador == 2):
        print("Você é suspeito(a)!")
    elif(contador == 3 or contador == 4):
        print("Você é cúmplice!")
    elif(contador == 5):
        print("Você é assassino(a)!")

#26.Um posto está vendendo combustíveis com a seguinte tabela de descontos:
# Álcool:
# até 20 litros, desconto de 3% por litro
# acima de 20 litros, desconto de 5% por litro
# Gasolina:
# até 20 litros, desconto de 4% por litro
# acima de 20 litros, desconto de 6% por litro Escreva um algoritmo que leia o número de litros vendidos, o tipo de combustível (codificado da seguinte forma: A-álcool, G-gasolina),
# calcule e imprima o valor a ser pago pelo cliente sabendo-se que o preço do litro da gasolina é R$ 2,50 o preço do litro do álcool é R$ 1,90.

def posto_de_combustivel():

    litros_vendidos = float(input("Digite a quantidade de litros que você deseja: "))
    tipo_de_combustivel = input("Digite o tipo de combustível que você deseja. A-álcool, G-gasolina: ").strip().upper()

    if(tipo_de_combustivel == "A"):
        preco_total = litros_vendidos * 1.90
        if(litros_vendidos <= 20):
            desconto_por_litro = (3 / 100) * 1.90
            desconto_total = desconto_por_litro * litros_vendidos
            preco_com_desconto = preco_total - desconto_total
            print("O preço com desconto é {:.2f}".format(preco_com_desconto))
        elif(litros_vendidos > 20):
            desconto_por_litro = (5 / 100) * 1.90
            desconto_total = desconto_por_litro * litros_vendidos
            preco_com_desconto = preco_total - desconto_total
            print("O preço com desconto é {:.2f}".format(preco_com_desconto))

    elif(tipo_de_combustivel == "G"):
        preco_total = litros_vendidos * 2.50
        if (litros_vendidos <= 20):
            desconto_por_litro = (4 / 100) * 2.50
            desconto_total = desconto_por_litro * litros_vendidos
            preco_com_desconto = preco_total - desconto_total
            print("O preço com desconto é {:.2f}".format(preco_com_desconto))
        elif (litros_vendidos > 20):
            desconto_por_litro = (6 / 100) * 2.50
            desconto_total = desconto_por_litro * litros_vendidos
            preco_com_desconto = preco_total - desconto_total
            print("O preço com desconto é {:.2f}".format(preco_com_desconto))

#27.Uma fruteira está vendendo frutas com a seguinte tabela de preços:
#                       Até 5 Kg           Acima de 5 Kg
# Morango         R$ 2,50 por Kg          R$ 2,20 por Kg
# Maçã            R$ 1,80 por Kg          R$ 1,50 por Kg
# Se o cliente comprar mais de 8 Kg em frutas ou o valor total da compra ultrapassar R$ 25,00, receberá ainda um desconto de 10% sobre este total.
# Escreva um algoritmo para ler a quantidade (em Kg) de morangos e a quantidade (em Kg) de maças adquiridas e escreva o valor a ser pago pelo cliente.

def fruteira():
    quantidade_de_morangos = int(input("Digite a quantidade de morangos a ser comprada(Kg) : "))
    quantidade_de_macas = int(input("Digite a quantidade de maçãs a ser comprada(Kg): "))

    if(quantidade_de_morangos <= 5):
        valor_a_pagar_de_morangos = quantidade_de_morangos * 2.50
    else:
        valor_a_pagar_de_morangos = quantidade_de_morangos * 2.20

    if(quantidade_de_macas <= 5):
        valor_a_pagar_de_macas = quantidade_de_macas * 1.80
    else:
        valor_a_pagar_de_macas = quantidade_de_macas * 1.50

    valor_a_pagar_total = valor_a_pagar_de_morangos + valor_a_pagar_de_macas

    if(quantidade_de_morangos + quantidade_de_macas > 8 or valor_a_pagar_de_morangos + valor_a_pagar_de_macas > 25):
        desconto_valor_a_pagar_total = valor_a_pagar_total * (10 / 100)
        valor_a_pagar_total = valor_a_pagar_total - desconto_valor_a_pagar_total
        print("O valor a pagar total é {:.2f}".format(valor_a_pagar_total))
    else:
        print("O valor a pagar total é {:.2f}".format(valor_a_pagar_total))

#28. O Hipermercado Tabajara está com uma promoção de carnes que é imperdível. Confira:
#                       Até 5 Kg           Acima de 5 Kg
# File Duplo      R$ 4,90 por Kg          R$ 5,80 por Kg
# Alcatra         R$ 5,90 por Kg          R$ 6,80 por Kg
# Picanha         R$ 6,90 por Kg          R$ 7,80 por Kg
# Para atender a todos os clientes, cada cliente poderá levar apenas um dos tipos de carne da promoção, porém não há limites para a quantidade de carne por cliente.
# Se compra for feita no cartão Tabajara o cliente receberá ainda um desconto de 5% sobre o total da compra.
# Escreva um programa que peça o tipo e a quantidade de carne comprada pelo usuário e gere um cupom fiscal,
# contendo as informações da compra: tipo e quantidade de carne, preço total, tipo de pagamento, valor do desconto e valor a pagar.

def acougue():
    tipo_de_carne = input("Digite o tipo de carne comprada(F - Filé Duplo, A - Alcatra, P - Picanha): ").strip().upper()
    quantidade_de_carne_comprada = int(input("Digite a quantidade de carne comprada(Kg): "))
    cartao = input("Usará o cartão Tabajara? (Sim ou Não): ").strip().upper()

    if(tipo_de_carne == "F"):
        if(quantidade_de_carne_comprada <= 5):
            if(cartao == "SIM"):
                preco = quantidade_de_carne_comprada * 4.90
                desconto = (5 / 100 * preco)
                preco_com_desconto = preco - desconto
                print("Tipo: Filé Duplo, Quantidade de carne: {} Kg, Preço Total: {:.2f}, Tipo de Pagamento: Cartão Tabajara, Valor do Desconto: {:.2f}, Valor a Pagar: {:.2f}".format(quantidade_de_carne_comprada, preco,desconto, preco_com_desconto))
            else:
                preco = quantidade_de_carne_comprada * 4.90
                desconto = 0
                preco_com_desconto = preco
                print("Tipo: Filé Duplo, Quantidade de carne: {} Kg, Preço Total: {:.2f}, Tipo de Pagamento: Dinheiro, Valor do Desconto: {:.2f}, Valor a Pagar: {:.2f}".format(quantidade_de_carne_comprada, preco, desconto, preco_com_desconto))
        elif(quantidade_de_carne_comprada > 5):
            if (cartao == "SIM"):
                preco = quantidade_de_carne_comprada * 5.80
                desconto = (5 / 100 * preco)
                preco_com_desconto = preco - desconto
                print(
                    "Tipo: Filé Duplo, Quantidade de carne: {} Kg, Preço Total: {:.2f}, Tipo de Pagamento: Cartão Tabajara, Valor do Desconto: {:.2f}, Valor a Pagar: {:.2f}".format(quantidade_de_carne_comprada, preco, desconto, preco_com_desconto))
            else:
                preco = quantidade_de_carne_comprada * 5.80
                desconto = 0
                preco_com_desconto = preco
                print("Tipo: Filé Duplo, Quantidade de carne: {} Kg, Preço Total: {:.2f}, Tipo de Pagamento: Dinheiro, Valor do Desconto: {:.2f}, Valor a Pagar: {:.2f}".format(quantidade_de_carne_comprada, preco, desconto, preco_com_desconto))

    if (tipo_de_carne == "A"):
        if (quantidade_de_carne_comprada <= 5):
            if (cartao == "SIM"):
                preco = quantidade_de_carne_comprada * 5.90
                desconto = (5 / 100 * preco)
                preco_com_desconto = preco - desconto
                print("Tipo: Alcatra, Quantidade de carne: {} Kg, Preço Total: {:.2f}, Tipo de Pagamento: Cartão Tabajara, Valor do Desconto: {:.2f}, Valor a Pagar: {:.2f}".format(quantidade_de_carne_comprada, preco, desconto, preco_com_desconto))
            else:
                preco = quantidade_de_carne_comprada * 5.90
                desconto = 0
                preco_com_desconto = preco
                print( "Tipo: Alcatra, Quantidade de carne: {} Kg, Preço Total: {:.2f}, Tipo de Pagamento: Dinheiro, Valor do Desconto: {:.2f}, Valor a Pagar: {:.2f}".format(quantidade_de_carne_comprada, preco, desconto, preco_com_desconto))
        elif (quantidade_de_carne_comprada > 5):
            if (cartao == "SIM"):
                preco = quantidade_de_carne_comprada * 6.80
                desconto = (5 / 100 * preco)
                preco_com_desconto = preco - desconto
                print("Tipo: Alcatra, Quantidade de carne: {} Kg, Preço Total: {:.2f}, Tipo de Pagamento: Cartão Tabajara, Valor do Desconto: {:.2f}, Valor a Pagar: {:.2f}".format(quantidade_de_carne_comprada, preco, desconto, preco_com_desconto))
            else:
                preco = quantidade_de_carne_comprada * 6.80
                desconto = 0
                preco_com_desconto = preco
                print("Tipo: Alcatra, Quantidade de carne: {} Kg, Preço Total: {:.2f}, Tipo de Pagamento: Dinheiro, Valor do Desconto: {:.2f}, Valor a Pagar: {:.2f}".format(quantidade_de_carne_comprada, preco, desconto, preco_com_desconto))

    if (tipo_de_carne == "P"):
        if (quantidade_de_carne_comprada <= 5):
            if (cartao == "SIM"):
                preco = quantidade_de_carne_comprada * 6.90
                desconto = (5 / 100 * preco)
                preco_com_desconto = preco - desconto
                print("Tipo: Picanha, Quantidade de carne: {} Kg, Preço Total: {:.2f}, Tipo de Pagamento: Cartão Tabajara, Valor do Desconto: {:.2f}, Valor a Pagar: {:.2f}".format(quantidade_de_carne_comprada, preco, desconto, preco_com_desconto))
            else:
                preco = quantidade_de_carne_comprada * 6.90
                desconto = 0
                preco_com_desconto = preco
                print( "Tipo: Picanha, Quantidade de carne: {} Kg, Preço Total: {:.2f}, Tipo de Pagamento: Dinheiro, Valor do Desconto: {:.2f}, Valor a Pagar: {:.2f}".format(quantidade_de_carne_comprada, preco, desconto, preco_com_desconto))
        elif (quantidade_de_carne_comprada > 5):
            if (cartao == "SIM"):
                preco = quantidade_de_carne_comprada * 7.80
                desconto = (5 / 100 * preco)
                preco_com_desconto = preco - desconto
                print("Tipo: Picanha, Quantidade de carne: {} Kg, Preço Total: {:.2f}, Tipo de Pagamento: Cartão Tabajara, Valor do Desconto: {:.2f}, Valor a Pagar: {:.2f}".format(quantidade_de_carne_comprada, preco, desconto, preco_com_desconto))
            else:
                preco = quantidade_de_carne_comprada * 7.80
                desconto = 0
                preco_com_desconto = preco
                print("Tipo: Picanha, Quantidade de carne: {} Kg, Preço Total: {:.2f}, Tipo de Pagamento: Dinheiro, Valor do Desconto: {:.2f}, Valor a Pagar: {:.2f}".format(quantidade_de_carne_comprada, preco, desconto, preco_com_desconto))
if (__name__ == "__main__"):
     acougue()






