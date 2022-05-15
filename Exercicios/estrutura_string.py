from validate_docbr import CPF

# 1. Tamanho de ‘strings’. Faça um programa que leia 2 ‘strings’ e informe o conteúdo delas seguidas do seu comprimento.
# Informe também se as duas ‘strings’ possuem o mesmo comprimento e são iguais ou diferentes no conteúdo.
import re
from collections import Counter


def compara_string():
    frase_um = input("Digite a primeira frase: ")
    frase_dois = input("Digite a segunda frase: ")

    print("Compara duas strings")
    print("String 1: {}".format(frase_um))
    print("String 2: {}".format(frase_dois))
    print("Tamanho de '{}': {} caracteres".format(frase_um, len(frase_um)))
    print("Tamanho de '{}': {} caracteres".format(frase_dois, len(frase_dois)))

    if len(frase_um) != len(frase_dois):
        print("As duas strings são de tamanhos diferentes.")
    else:
        print("As duas strings são de tamanhos iguais.")

    if frase_um != frase_dois:
        print("As duas strings possuem conteúdo diferente.")
    else:
        print("As duas strings possuem conteúdo igual.")


# 2. Nome ao contrário em maiúsculas. Faça um programa que permita ao utilizador digitar o seu nome e em seguida mostre
# o nome do utilizador de trás para frente utilizando somente letras maiúsculas. Dica: lembre−se que ao informar o nome
# o utilizador pode digitar letras maiúsculas ou minúsculas.

def nome_invertido_maisuculo():
    nome = input("Digite seu nome: ").upper()
    print("".join(reversed(nome)))


# 3. Nome na vertical. Faça um programa que solicite o nome do utilizador e imprima-o na vertical.

def nome_vertical():
    nome = input("Digite seu nome: ").upper()

    for posicao in range(len(nome)):
        print(nome[posicao])


# 4. Nome na vertical em escada. Modifique o programa anterior para mostrar o nome em formato de escada.

def nome_escada():
    lista = []
    nome_metade = ""
    nome = input("Digite seu nome: ").upper()

    for posicao in range(len(nome)):
        lista.append(nome[posicao])

    for posicao in range(len(lista)):
        nome_metade = nome_metade + nome[posicao]
        print(nome_metade)


# 5. Nome na vertical em escada invertida. Altere o programa anterior de modo que a escada seja invertida.

def nome_escada_invertida():
    lista = []
    nome_metade = ""
    nome = input("Digite seu nome: ").upper()

    for posicao in range(len(nome)):
        lista.append(nome[posicao])

    for posicao in range(len(lista)):
        nome_metade = nome_metade + nome[posicao]

    print(nome_metade)
    for posicao in range(len(nome_metade)):
        nome_metade = nome_metade[:-1]
        print(nome_metade)


# 6. Data por extenso. Faça um programa que solicite a data de nascimento (dd./mm/aaaa) do utilizador e imprima a data.
# Com o nome do mês por extenso.

def data(dia, mes, ano):
    calendario = {"Janeiro": 1,
                  "Fevereiro": 2,
                  "Março": 3,
                  "Abril": 4,
                  "Maio": 5,
                  "Junho": 6,
                  "Julho": 7,
                  "Agosto": 8,
                  "Setembro": 9,
                  "Outubro": 10,
                  "Novembro": 11,
                  "Dezembro": 12}

    for meses, valor in calendario.items():
        if mes == valor:
            mes_extenso = meses

    return print(
        "\nData de Nascimento: {}/{}/{} \nVocê Nasceu em {} de {} de {}".format(dia, mes, ano, dia, mes_extenso, ano))


def e_bissexto(ano):
    if regra_um(ano) or regra_dois(ano):
        return True


def regra_um(ano):
    if ano % 4 == 0 and ano % 100 != 0:
        return True


def regra_dois(ano):
    if ano % 4 == 0 and ano % 100 == 0 and ano % 400 == 0:
        return True


def data_extensa():
    data_escolhida = input("Digite a data no formato dd/mm/aaaa: ")

    numeros_data = [int(numero) for numero in re.findall(r'-?\d+\.?\d*', data_escolhida)]

    dia = int(numeros_data[0])
    mes = int(numeros_data[1])
    ano = int(numeros_data[2])
    tupla_meses_trinta_um_dias = (1, 3, 5, 7, 9, 10, 12)
    tupla_meses_trinta_dias = (4, 6, 8, 11)

    if mes in tupla_meses_trinta_um_dias:
        if dia <= 31:
            if 1000 <= ano <= 9999:
                data(dia, mes, ano)
            else:
                return 0
        else:
            return 0

    elif mes in tupla_meses_trinta_dias:
        if dia <= 30:
            if 1000 <= ano <= 9999:
                data(dia, mes, ano)
        else:
            return 0

    elif mes == 2:
        if e_bissexto(ano):
            if dia <= 29:
                data(dia, mes, ano)
            else:
                return 0
        else:
            if dia <= 28:
                data(dia, mes, ano)
            else:
                return 0
    else:
        return 0


# 7. Conta espaços e vogais. Dado uma ‘string’ com uma frase informada pelo utilizador (incluindo espaços em branco),
# conte: quantos espaços em branco existem na frase. Quantas vezes aparecem as vogais a, e, i, o, u.

def conta_frase():
    frase = input("Digite sua frase: ")
    aparicoes = Counter(frase.lower())

    for chave, valor in sorted(aparicoes.items()):
        if chave == "a" or chave == "e" or chave == "i" or chave == "o" or chave == "u" or chave == " ":
            print("Houve {} aparições da letra {}".format(valor, chave))


# 8. Palíndromo. Um palíndromo é uma sequência de caracteres cuja leitura é idêntica se feita da direita para
# esquerda ou vice−versa. Por exemplo: OSSO e OVO são palíndromos. Em textos mais complexos os espaços e pontuação
# são ignorados. A frase SUBI NO ONIBUS é o exemplo de uma frase palíndroma onde os espaços foram ignorados. Faça um
# programa que leia uma sequência de caracteres, mostre−a e diga se é um palíndromo ou não.

def palindromo():
    expressao = input('Escreva uma expressão: ').upper().replace(' ', '')
    expInv = expressao[::-1]
    if expressao == expInv:
        print('É palíndromo, pois, {} --> {}.'.format(expressao, expInv))
    else:
        print('Não é palíndromo.')


# 8. Verificação de CPF. Desenvolva um programa que solicite a digitação de um número de CPF no formato
# xxx.xxx.xxx-xx e indique se é um número válido ou inválido através da validação dos dígitos verificadores e dos
# caracteres de formatação.

class docCpf:
    def __init__(self, documento):
        if self.valida(documento):
            return print("CPF Válido!")
        else:
            raise ValueError("CPF Inválido!!")

    def valida(self, documento):
        validador = CPF()
        return validador.validate(documento)


def valida_cpf():
    cpf = input("Digite o CPF:")
    cpf_obj = docCpf(cpf)
    cpf_obj


if __name__ == "__main__":
    valida_cpf()
