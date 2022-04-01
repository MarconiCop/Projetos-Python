#1.Faça um programa que peça uma nota, entre zero e dez. Mostre uma mensagem caso o valor seja inválido e continue pedindo até que o usuário informe um valor válido.

def nota_valida():

    nota = float(input("Digite uma nota entre 0 e 10: "))

    while(nota < 0 or nota > 10):
        print("Valor Inválido!")
        nota = float(input("Digite uma nota entre 0 e 10: "))

    print("A nota é {}".format(nota))

if(__name__ == "__main__"):
    nota_valida()