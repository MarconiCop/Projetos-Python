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

if(__name__ == "__main__"):
    temperatura_f()
