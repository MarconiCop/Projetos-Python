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

def casas_numero():
    numero = int(input("Digite o número(1 a 1000): "))

    if(numero < 10):
        print("{} = {} unidade(s).".format(numero, numero))

    if(numero >= 10 and numero < 100):
        dezena = int(numero / 10)
        unidade = int(numero - 10 * dezena)
        print("{} = {} dezena(s) e {} unidade(s).".format(numero, dezena, unidade))

    if(numero >= 100 and numero < 1000):
        centena = int(numero/100)
        dezena = int((numero % 100) / 10)
        unidade = numero % 10

        print("{} = {} centena(s), {} dezena(s) e {} unidade(s).".format(numero, centena, dezena, unidade))

if(__name__ == "__main__"):
    casas_numero()