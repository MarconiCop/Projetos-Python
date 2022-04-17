# 1. Faça um Programa que leia um vetor de 5 números inteiros e mostre-os.

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


if __name__ == "__main__":
    exibir_lista_soma_quadrados()
