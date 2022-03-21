#####################################################################Exercício_1

def multiplos():

    soma = 0

    for numero in range(1, 1000):

        if(numero % 3 == 0 or numero % 5 == 0):

            soma = soma + numero

    print("A soma dos múltiplos de 3 e 5 menores que 1000 são {}".format(soma))


######################################################################Exercício_3

def fator():

    lista_multiplos = []
    for numero_multiplo in range(2, 600851475143):

        if(600851475143 % numero_multiplo == 0):

            lista_multiplos.append(numero_multiplo)

            for numero_primo in range(2, numero_multiplo):

                if(numero_multiplo % numero_primo == 0):

                    if(numero_multiplo in lista_multiplos):

                        lista_multiplos.remove(numero_multiplo)


    print(lista_multiplos[len(lista_multiplos)-1])

######################################################################Exercício_6

def diferenca(quadrado_das_somas, soma_numero_quadrado):

    diferenca = quadrado_das_somas - soma_numero_quadrado
    print(diferenca)

def soma_numero_quadrado():

    soma_numero_quadrado = 0

    for numero in range(1, 101):
        numero_quadradro = numero * numero
        soma_numero_quadrado += numero_quadradro

    return soma_numero_quadrado

def quadrado_das_somas():

    soma_dos_numeros = 0

    for numero in range(1, 101):
        soma_dos_numeros += numero
        quadrado_das_somas = soma_dos_numeros * soma_dos_numeros

    return quadrado_das_somas



if(__name__ == "__main__"):
    diferenca(quadrado_das_somas(),soma_numero_quadrado())

######################################################################Exercício_

