# 1. Faça um Programa que leia um vetor de 5 números inteiros e mostre-os.
import itertools


def exibir_lista():
    lista = []
    for numero in range(1, 5 + 1):
        num = int(input("Digite o número {}: ".format(numero)))
        lista.append(num)
    print(lista)


# 2. Faça um Programa que leia um vetor de 10 números reais e mostre-os na ordem inversa.

def exibir_lista_inversa():
    lista = []
    for numero in range(1, 10 + 1):
        num = int(input("Digite o número {}: ".format(numero)))
        lista.append(num)

    lista = list(reversed(lista))
    print(lista)


# 3. Faça um Programa que leia 4 notas, mostre as notas e a média na tela

def exibir_lista_notas():
    lista = []
    for nota in range(1, 4 + 1):
        notas = float(input("Digite a nota {}: ".format(nota)))
        lista.append(notas)

    for nota in range(0, len(lista)):
        print(lista[nota])
    print(sum(lista) / len(lista))


# 4. Faça um Programa que leia um vetor de 10 caracteres, e diga quantas consoantes foram lidas. Imprima as consoantes.

def exibir_lista_consoantes():
    lista = []
    for numero in range(1, 10 + 1):
        letra = input("Digite a letra {}: ".format(numero)).strip().upper()
        if letra != "A" and letra != "E" and letra != "I" and letra != "O" and letra != "U":
            lista.append(letra)

    print("Foram lidas {} consoante(s)".format(len(lista)))
    print(lista)


# 5. Faça um Programa que leia 20 números inteiros e armazene-os num vetor. Armazene os números pares no vetor PAR e
# os números IMPARES no vetor impar. Imprima os três vetores.

def exibir_lista_vetores():
    lista = []
    lista_par = []
    lista_impar = []

    for numero in range(1, 20 + 1):

        num = int(input("Digite o número {}: ".format(numero)))

        if num not in lista:

            lista.append(num)

            if num % 2 == 0:
                lista_par.append(num)
            else:
                lista_impar.append(num)

        else:
            print("Opa! Número repetido. Que tal digitar outro número?")
            num = int(input("Digite o número {}: ".format(numero)))

            while num in lista:
                print("Opa! Número repetido novamente. Que tal digitar outro número?")
                num = int(input("Digite o número {}: ".format(numero)))

            lista.append(num)

            if num % 2 == 0:
                lista_par.append(num)
            else:
                lista_impar.append(num)

    print(lista)
    print(lista_par)
    print(lista_impar)


# 6. Faça um Programa que peça as quatro notas de 10 alunos, calcule e armazene num vetor a média de cada aluno,
# imprima o número de alunos com média maior ou igual a 7,0.

def exibir_lista_media():
    lista_media = []
    soma_das_notas = 0
    contador = 0

    for aluno in range(1, 10 + 1):

        for nota in range(1, 4 + 1):
            nota_do_aluno = float(input(("Digite a nota {} do Aluno {}: ".format(nota, aluno))))
            soma_das_notas += nota_do_aluno

        lista_media.append(soma_das_notas / 4)
        soma_das_notas = 0

    for posicao in range(0, len(lista_media)):
        if lista_media[posicao] >= 7:
            contador += 1
    print("-------------------------------------------------------------------")
    print("Médias dos alunos: {}".format(lista_media))
    print("O número de alnos com média maior ou igual a 7  é(são) {} aluno(s).".format(contador))
    print("-------------------------------------------------------------------")


# 7. Faça um Programa que leia um vetor de 5 números inteiros, mostre a soma, a multiplicação e os números.

def exibir_lista_multiplicacao():
    lista = []
    mult = 1

    for numero in range(1, 5 + 1):
        num = int(input(("Digite o número {}: ".format(numero))))
        mult *= num
        lista.append(num)

    print("A soma dos números é: {}".format(sum(lista)))
    print("A multiplicação dos números é: {}".format(mult))
    print("Os números são: {}".format(lista))


# 8. Faça um Programa que peça a idade e a altura de 5 pessoas, armazene cada informação no seu respetivo vetor.
# Imprima a idade e a altura na ordem inversa a ordem lida.

def exibir_lista_idade_altura():
    lista_idade = []
    lista_altura = []

    for posicao in range(1, 5 + 1):
        idade = int(input("Digite a idade da pessoa {}: ".format(posicao)))
        altura = float(input("Digite a altura da pessoa {}: ".format(posicao)))
        lista_idade.append(idade)
        lista_altura.append(altura)

    lista_idade_invertida = list(reversed(lista_idade))
    lista_altura_invertida = list(reversed(lista_altura))
    print(lista_idade_invertida)
    print(lista_altura_invertida)


# 9. Faça um Programa que leia um vetor A com 10 números inteiros, calcule e mostre a soma dos quadrados dos
# elementos do vetor.

def exibir_lista_soma_quadrados():
    A = []

    for posicao in range(1, 10 + 1):
        numero = int(input("Digite o número {}: ".format(posicao)))
        numero = numero * numero
        A.append(numero)

    print(A)
    print("Soma dos quadrados: {}".format(sum(A)))


# 10. Faça um Programa que leia dois vetores com 10 elementos cada. Gere um terceiro vetor de 20 elementos,
# cujos valores deverão ser compostos pelos elementos intercalados dos dois outros vetores.

def exibir_lista_intercalado():
    lista_um = []
    lista_dois = []

    for posicao in range(1, 10 + 1):
        numero = int(input("Digite o número {} da lista 1: ".format(posicao)))
        lista_um.append(numero)

    for posicao in range(1, 10 + 1):
        numero = int(input("Digite o número {} da lista 2: ".format(posicao)))
        lista_dois.append(numero)

    res = list(itertools.chain(*zip(lista_um, lista_dois)))

    print(lista_um)
    print(lista_dois)
    print(res)


# 11. Altere o programa anterior, intercalando 3 vetores de 10 elementos cada.

def exibir_lista_intercalado_tres():
    lista_um = []
    lista_dois = []
    lista_tres = []

    for posicao in range(1, 10 + 1):
        numero = int(input("Digite o número {} da lista 1: ".format(posicao)))
        lista_um.append(numero)

    for posicao in range(1, 10 + 1):
        numero = int(input("Digite o número {} da lista 2: ".format(posicao)))
        lista_dois.append(numero)

    for posicao in range(1, 10 + 1):
        numero = int(input("Digite o número {} da lista 3: ".format(posicao)))
        lista_tres.append(numero)

    res = list(itertools.chain(*zip(lista_um, lista_dois, lista_tres)))

    print(lista_um)
    print(lista_dois)
    print(lista_tres)
    print(res)


# 12. Foram anotadas as idades e alturas de 30 alunos. Faça um Programa que determine quantos alunos com mais de 13
# anos possuem altura inferior à média de altura desses alunos.

def exibir_lista_altura_inferior_media():
    lista_idade = []
    lista_altura = []
    lista_altura_media = []
    cont = 0
    cont_treze = 0

    for posicao in range(1, 30 + 1):
        idade = int(input("Digite a idade da pessoa {}: ".format(posicao)))
        altura = float(input("Digite a altura da pessoa {}: ".format(posicao)))
        lista_idade.append(idade)
        lista_altura.append(altura)

    media_alturas = sum(lista_altura) / len(lista_altura)

    for posicao in range(0, 30):
        if lista_idade[posicao] > 13 and lista_altura[posicao] < media_alturas:
            cont += 1

    for posicao in range(0, 30):
        if lista_idade[posicao] > 13:
            lista_altura_media.append(lista_altura[posicao])

    media_altura_treze = sum(lista_altura_media) / len(lista_altura_media)

    for posicao in range(0, len(lista_altura_media)):
        if lista_altura_media[posicao] < media_altura_treze:
            cont_treze += 1

    print("Há {} aluno(s) acima de 13 anos com altura inferior a média de altura dos alunos!".format(cont))
    print(
        "Há {} aluno(s) acima de 13 anos com altura inferior a média de altura dos alunos com mais de 13 anos!".format(
            cont_treze))


# 13. Faça um programa que receba a temperatura média de cada mês do ano e armazene-as numa lista. Após isto,
# calcule a média anual das temperaturas e mostre todas as temperaturas acima da média anual, e em que mês elas
# ocorreram (mostrar o mês por extenso: 1 – Janeiro, 2 – Fevereiro, . . . ).

def exibir_lista_temperatura():
    lista_temperaturas = []

    for mes in range(1, 12 + 1):
        temperatura = float(input("Digite a temperatura no mês {}: ".format(mes)))
        lista_temperaturas.append(temperatura)

    media_temperaturas = sum(lista_temperaturas) / len(lista_temperaturas)

    for posicao in range(0, 12):

        if lista_temperaturas[posicao] > media_temperaturas:
            if posicao == 0:
                print("1 - Janeiro: ", lista_temperaturas[posicao])
            if posicao == 1:
                print("2 - Fevereiro: ", lista_temperaturas[posicao])
            if posicao == 2:
                print("3 - Março: ", lista_temperaturas[posicao])
            if posicao == 3:
                print("4 - Abril: ", lista_temperaturas[posicao])
            if posicao == 4:
                print("5 - Maio: ", lista_temperaturas[posicao])
            if posicao == 5:
                print("6 - Junho: ", lista_temperaturas[posicao])
            if posicao == 6:
                print("7 - Julho: ", lista_temperaturas[posicao])
            if posicao == 7:
                print("8 - Agosto: ", lista_temperaturas[posicao])
            if posicao == 8:
                print("9 - Setembro: ", lista_temperaturas[posicao])
            if posicao == 9:
                print("10 - Outubro: ", lista_temperaturas[posicao])
            if posicao == 10:
                print("11 - Novembro: ", lista_temperaturas[posicao])
            if posicao == 11:
                print("12 - Dezembro: ", lista_temperaturas[posicao])


# 14. Utilizando listas faça um programa que faça 5 perguntas para uma pessoa sobre um crime. As perguntas são: :
# "Telefonou para a vítima?" "Esteve no local do crime?" "Mora perto da vítima?" "Devia para a vítima?" "Já trabalhou
# com a vítima?" O programa deve no final emitir uma classificação sobre a participação da pessoa no crime. Se a
# pessoa responder positivamente a 2 questões ela deve ser classificada como "Suspeita", entre 3 e 4 como "Cúmplice"
# e 5 como "Assassino". Caso contrário, ele será classificado como "Inocente".

def exibir_lista_crime():
    lista = []
    pergunta_um = input("Telefonou para a vítima? Responda com SIM ou NÃO: ").strip().upper()
    pergunta_dois = input("Esteve no local do crime? Responda com SIM ou NÃO: ").strip().upper()
    pergunta_tres = input("Mora perto da vítima? Responda com SIM ou NÃO: ").strip().upper()
    pergunta_quatro = input("Devia para a vítima? Responda com SIM ou NÃO: ").strip().upper()
    pergunta_cinco = input("Já trabalhou com a vítima? Responda com SIM ou NÃO: ").strip().upper()

    if pergunta_um == "SIM":
        lista.append(1)
    if pergunta_dois == "SIM":
        lista.append(1)
    if pergunta_tres == "SIM":
        lista.append(1)
    if pergunta_quatro == "SIM":
        lista.append(1)
    if pergunta_cinco == "SIM":
        lista.append(1)

    if sum(lista) == 1:
        print("Você é inocente!")
    elif sum(lista) == 2:
        print("Você é suspeito(a)!")
    elif sum(lista) == 3 or sum(lista) == 4:
        print("Você é cúmplice!")
    elif sum(lista) == 5:
        print("Você é assassino(a)!")


# 15. Faça um programa que leia um número indeterminado de valores, correspondentes a notas, encerrando a entrada de
# dados quando for informado um valor igual a -1 (que não deve ser armazenado). Após esta entrada de dados,
# faça: Mostre a quantidade de valores lidos; Exiba todos os valores na ordem em que foram informados,
# um ao lado do outro; Exiba todos os valores na ordem inversa à que foram informados, um abaixo do outro; Calcule e
# mostre a soma dos valores; Calcule e mostre a média dos valores; Calcule e mostre a quantidade de valores acima da
# média calculada; Calcule e mostre a quantidade de valores abaixo de sete; Encerre o programa com uma mensagem;

def exibir_lista_notas():
    nota = 0
    lista = []

    while nota != -1:
        nota = float(input("Digite uma nota: "))
        lista.append(nota)

    lista.pop()

    print("Foram lidos {} valor(es)".format(len(lista)))
    print("Valores: {}".format(lista))

    lista_invertida = list(reversed(lista))
    for posicao in range(0, len(lista_invertida)):
        print(lista_invertida[posicao])

    media = sum(lista) / len(lista)
    cont = 0

    print("A soma dos valores é: {}".format(sum(lista)))
    print("A média dos valores é: {}".format(media))

    for posicao in range(0, len(lista)):
        if lista[posicao] > media:
            cont += 1

    print("Há {} valor(es) acima da média.".format(cont))

    cont_sete = 0
    for posicao in range(0, len(lista)):
        if lista[posicao] < 7:
            cont_sete += 1

    print("Há {} valor(es) abaixo de 7.".format(cont_sete))

    print("-------------------------")
    print("O programa foi encerrado!")
    print("-------------------------")


if __name__ == "__main__":
    exibir_lista_notas()