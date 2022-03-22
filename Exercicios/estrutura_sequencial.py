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

if(__name__ == "__main__"):
    conversao()
