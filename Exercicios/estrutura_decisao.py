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



if(__name__ == "__main__"):
    triangulo()

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

