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

    print(lista)
    print(lista_par)
    print(lista_impar)


if __name__ == "__main__":
    exibir_lista_vetores()
