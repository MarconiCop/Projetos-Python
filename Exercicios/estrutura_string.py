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


# 9. Verificação de CPF. Desenvolva um programa que solicite a digitação de um número de CPF no formato
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


# 10. Número por extenso. Escreva um programa que solicite ao utilizador a digitação de um número até 99 e imprima-o na
# tela por extenso.

def converter_em_texto(numeral):
    dicionario_numerico = {
        0: 'zero', 1: 'um', 2: 'dois', 3: 'três', 4: 'quatro', 5: 'cinco',
        6: 'seis', 7: 'sete', 8: 'oito', 9: 'nove', 10: 'dez',
        11: 'onze', 12: 'doze', 13: 'treze', 14: 'quatorze', 15: 'quinze',
        16: 'dezesseis', 17: 'dezessete', 18: 'dezoito', 19: 'dezenove', 20: 'vinte',
        30: 'trinta', 40: 'quarenta', 50: 'cinquenta', 60: 'sessenta', 70: 'setenta',
        80: 'oitenta', 90: 'noventa',
    }

    if numeral > 99 or numeral < 0:
        raise ValueError('O número deve estar entre 0 e 99 (inclusive)')

    if numeral < 20 or numeral % 10 == 0:
        return dicionario_numerico.get(numeral)

    decimal = numeral // 10 * 10
    unidade = numeral % 10
    extenso = f'{dicionario_numerico.get(decimal)} e {dicionario_numerico.get(unidade)}'
    return extenso


def principal_dez():
    print('Insira um número:')
    numeral = int(input())
    numero_por_extenso = converter_em_texto(numeral)
    print(numero_por_extenso)


# 11. Jogo de Forca. Desenvolva um jogo da forca. O programa terá uma lista de palavras lidas de um arquivo texto e
# escolherá uma aleatoriamente. O jogador poderá errar 6 vezes antes de ser enforcado.

def principal_onze():
    print("Feito em outro arquivo!")


# 12. Valida e corrige número de telefone. Faça um programa que leia um número de telefone, e corrija o número no
# caso deste conter somente 7 dígitos, acrescentando o '3' na frente. O usuário pode informar o número com ou sem o
# traço separador.


def principal_doze():
    numero = int(input('Telefone: '))
    novoNumero = ''
    if len(str(numero)) < 8:
        diferenca = 8 - len(str(numero))
        novoNumero = '3' * diferenca

    numeroFormatado = novoNumero + str(numero)
    numeroFormatado = numeroFormatado[0:4] + '-' + numeroFormatado[5:]

    print('Telefone possui %d dígitos. Vou acrescentar o digito três na frente.' % len(str(numero)))
    print('Telefone corrigido sem formatação: %d' % numero)
    print('Telefone corrigido com formatação: %s' % numeroFormatado)


# 13. Jogo da palavra embaralhada. Desenvolva um jogo em que o utilizador tenha que adivinhar uma palavra que será
# mostrada com as letras embaralhadas. O programa terá uma lista de palavras lidas de um arquivo texto e escolherá
# uma aleatoriamente. O jogador terá seis tentativas para adivinhar a palavra. Ao final a palavra deve ser mostrada
# na tela, informando se o utilizador ganhou ou perdeu o jogo.

def principal_treze():
    print("Feito em outro arquivo!")


# 14. Leet spek generator. Leet é uma forma de se escrever o alfabeto latino usando outros símbolos em lugar das
# letras, como números, por exemplo. A própria palavra leet admite muitas variações, como l33t ou 1337. O uso do leet
# reflete uma subcultura relacionada ao mundo dos jogos de computador e ‘internet’, sendo muito usada para confundir os
# iniciantes e afirmar-se como parte de um grupo. Pesquise sobre as principais formas de traduzir as letras. Depois,
# faça um programa que peça um texto e transforme-o para a grafia leet speak.


from utilitybelt import change_charset


def principal_quatorze():
    origspace = "abcdefghijklmnopqrstuvwxyz"
    keyspace = "4bcd3fgh1jklmn0pqr57uvwxyz"
    palavra = input("Digite a palavra:")

    print(change_charset("{}".format(palavra), origspace, keyspace))


if __name__ == "__main__":
    principal_doze()
