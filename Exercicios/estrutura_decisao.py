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
    elif(letra == "m"):
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

if(__name__ == "__main__"):
    ordem_decrescente()