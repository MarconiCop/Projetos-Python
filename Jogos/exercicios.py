#Exercício_1
def multiplos():

    soma = 0

    for numero in range(1, 1000):

        if(numero % 3 == 0 or numero % 5 == 0):

            soma = soma + numero

    print("A soma dos múltiplos de 3 e 5 menores que 1000 são {}".format(soma))

if(__name__ == "__main__"):
    multiplos()