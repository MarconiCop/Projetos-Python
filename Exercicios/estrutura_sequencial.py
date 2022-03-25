#1.Faça um Programa que mostre a mensagem "Alo mundo" na tela.
def imprime():
    print("Alô mundo")

#2.Faça um Programa que peça um número e então mostre a mensagem O número informado foi [número].

def numero():
    numero = int(input("Digite um número: "))
    print("O número informado foi {}!".format(numero))

#3.Faça um Programa que peça dois números e imprima a soma.

def soma():
    numero_um = int(input("Digite o primeiro número: "))
    numero_dois = int(input("Digite o segundo número: "))
    soma = numero_um + numero_dois
    print("A soma dos números é {}!".format(soma))

#4.Faça um Programa que peça as 4 notas bimestrais e mostre a média.

def media():
    nota_um = float(input("Digite a primeira nota: "))
    nota_dois = float(input("Digite a segunda nota: "))
    nota_tres = float(input("Digite a terceira nota: "))
    nota_quatro = float(input("Digite a quarta nota: "))
    media = (nota_um + nota_dois + nota_tres + nota_quatro)/4
    print("A média das notas é {}!".format(media))

#5.Faça um Programa que converta metros para centímetros.

def conversao():
    metro = float(input("Digite a medida em metros: "))
    centimetro = metro * 100
    print("A medida {} metro(s) equivale  a {} centímetro(s)".format(metro, centimetro))

#6.Faça um Programa que peça o raio de um círculo, calcule e mostre sua área.

def area_circulo():
    raio = float(input("Digite o raio do círculo: "))
    area = 3.14 * raio * raio
    print("A área do círculo é {}".format(area))

#7.Faça um Programa que calcule a área de um quadrado, em seguida mostre o dobro desta área para o usuário.

def area_quadrado_dobro():
    lado_quadrado = float(input("Digite o lado do quadrado: "))
    area_quadrado = lado_quadrado * lado_quadrado
    dobro = area_quadrado * 2
    print("O dobro da área do quadrado é {}".format(dobro))

#8.Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês.

def salario():

    dinheiro_hora = float(input("Quanto você ganha por hora? "))
    numero_horas = float(input("Quantas horas você trabalha no mês? "))
    salario = dinheiro_hora * numero_horas
    print("Seu salário no mês é {}".format(salario))

#9.Faça um Programa que peça a temperatura em graus Fahrenheit, transforme e mostre a temperatura em graus Celsius. C = 5 * ((F-32) / 9).

def temperatura_c():
    temperatura_f = float(input("Digite a temperatura em Fahrenheit: "))
    temperatura_c = 5 * ((temperatura_f-32) / 9)
    print("A temperatura {}ªF equivale a {}ªC".format(temperatura_f, temperatura_c))

#10.Faça um Programa que peça a temperatura em graus Celsius, transforme e mostre em graus Fahrenheit.

def temperatura_f():
    temperatura_c = float(input("Digite a temperatura em Celcius: "))
    temperatura_f =  ((temperatura_c * 9) / 5) + 32
    print("A temperatura {}ªC equivale a {}ªF".format(temperatura_c, temperatura_f))

#11. Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:
#o produto do dobro do primeiro com metade do segundo .
#a soma do triplo do primeiro com o terceiro.
#o terceiro elevado ao cubo.

def numero_onze():
    numero_int_um = int(input("Digite seu primeiro número inteiro: "))
    numero_int_dois = int(input("Digite seu segundo número inteiro: "))
    numero_real = float(input("Digite seu número real: "))

    produto = (2 * numero_int_um) * (numero_int_dois / 2)
    soma =(3 * numero_int_um) + numero_real
    elevado = numero_real * numero_real * numero_real

    print(produto, soma, elevado)

#12. Tendo como dados de entrada a altura de uma pessoa, construa um algoritmo que calcule seu peso ideal, usando a seguinte fórmula: (72.7*altura) - 58

def peso():
    altura = float(input("Digite sua altura: "))
    peso = round((72.7 * altura) - 58, 2)
    print("Seu peso é {}!".format(peso))

#13.  como dado de entrada a altura (h) de uma pessoa, construa um algoritmo que calcule seu peso ideal, utilizando as seguintes fórmulas:
#Para homens: (72.7*h) - 58
#Para mulheres: (62.1*h) - 44.7

def peso_ideal():
    sexo = int(input("Digite 1 se você for homem ou digite 2 se você for mulher: "))
    altura = float(input("Digite sua altura: "))
    if(sexo == 1):
        peso_homem = round((72.7 * altura) - 58, 2)
        print("Seu peso ideal(homem) é {}!".format(peso_homem))
    elif(sexo == 2):
        peso_mulher = round((62.1 * altura) - 44.7, 2)
        print("Seu peso ideal(mulher) é {}!".format(peso_mulher))

#14. João Papo-de-Pescador, homem de bem, comprou um microcomputador para controlar o rendimento diário de seu trabalho.
# Toda vez que ele traz um peso de peixes maior que o estabelecido pelo regulamento de pesca do estado de São Paulo (50 quilos) deve pagar uma multa de R$ 4,00 por quilo excedente.
# João precisa que você faça um programa que leia a variável peso (peso de peixes) e calcule o excesso.
# Gravar na variável excesso a quantidade de quilos além do limite e na variável multa o valor da multa que João deverá pagar.
# Imprima os dados do programa com as mensagens adequadas.

def peixe():
    peso = float(input("Digite o peso da quantidade pescada: "))

    if(peso > 50):
        excesso = round(peso - 50, 2)
        multa = round(4 * excesso, 2)
        print("João coletou {} kilos de peixe ultrapassando {} kilos e deve pagar {} reais de multa!".format(peso, excesso, multa))

    else:
        print("João coletou {} kilos de peixes e não deve multa".format(peso))

#15. Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês,
#sabendo-se que são descontados 11% para o Imposto de Renda, 8% para o INSS e 5% para o sindicato, faça um programa que nos dê:
#salário bruto.
#quanto pagou ao INSS.
#quanto pagou ao sindicato.
#o salário líquido.
#calcule os descontos e o salário líquido, conforme a tabela abaixo:
#+ Salário Bruto : R$
#- IR (11%) : R$
#- INSS (8%) : R$
#- Sindicato ( 5%) : R$
#= Salário Liquido : R$

def salario_tipo():

    dinheiro_hora = float(input("Quanto você ganha por hora? "))
    numero_horas = float(input("Quantas horas você trabalha no mês? "))

    salario_bruto = dinheiro_hora * numero_horas
    salario_ir = (11 / 100) * salario_bruto
    salario_inss = (8 / 100) * salario_bruto
    salario_sindicato = (5 / 100) * salario_bruto
    salario_liquido = salario_bruto - salario_ir - salario_inss - salario_sindicato

    print("+ Salário Bruto : R$ {:.2f}".format(salario_bruto))
    print("- IR (11%) : R$ {:.2f}".format(salario_ir))
    print("- INSS (8%) : R$ {:.2f}".format(salario_inss))
    print("- Sindicato ( 5%) : R$ {:.2f}".format(salario_sindicato))
    print("= Salário Liquido : R$ {:.2f}".format(salario_liquido))

#16. Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada.
# Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00.
# Informe ao usuário a quantidades de latas de tinta a serem compradas e o preço total.

def tinta():
    area = float(input("Digite o tamanho da área(m²) a ser pintada: "))
    quantidade_tinta = round(area / 3, 2)
    print("Será necessário {} litros de tinta.".format(quantidade_tinta))
    quantidade_latas = round(quantidade_tinta / 18)
    print("Será necessário {} lata(s) de tinta.".format(quantidade_latas))
    preco = quantidade_latas * 80
    print("O preço total é {} reais em latas de tinta.".format(preco))


if(__name__ == "__main__"):
    tinta()
