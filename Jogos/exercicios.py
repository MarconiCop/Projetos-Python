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

        if(13195 % numero_multiplo == 0):

            lista_multiplos.append(numero_multiplo)

            for numero_primo in range(2, numero_multiplo):

                if(numero_multiplo % numero_primo == 0):

                    if(numero_multiplo in lista_multiplos):

                        lista_multiplos.remove(numero_multiplo)


    print(lista_multiplos[len(lista_multiplos)-1])

if(__name__ == "__main__"):
    fator()
#################################################################################