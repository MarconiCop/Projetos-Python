# 1. Faça um programa que peça uma nota, entre zero e dez. Mostre uma mensagem caso o valor seja inválido e continue
# a pedir até que o utilizador informe um valor válido.

def nota_valida():
    nota = float(input("Digite uma nota entre 0 e 10: "))

    while nota < 0 or nota > 10:
        print("Valor Inválido!")
        nota = float(input("Digite uma nota entre 0 e 10: "))

    print("A nota é {}".format(nota))


# 2. Faça um programa que leia um nome de utilizador e a sua senha e não aceite a senha igual ao nome do utilizador,
# mostrando uma mensagem de erro e voltando a pedir as informações.

def login():
    nome = input("Digite o nome de usuário: ").strip()
    senha = input("Digite sua senha: ").strip()

    while nome == senha:
        print("A senha é igual ao nome de usuário!")
        nome = input("Digite o nome de usuário: ")
        senha = input("Digite sua senha: ")

    print("Logado com sucesso!")


# 3. Faça um programa que leia e valide as seguintes informações:
# Nome: maior que 3 caracteres;
# Idade: entre 0 e 150;
# Salário: maior que zero;
# Sexo: 'f' ou 'm';
# Estado Civil: 's', 'c', 'v', 'd';

def informacoes():
    nome = input("Digite seu nome: ")

    while len(nome) <= 3:
        print("Seu nome deve conter acima de 4 caracteres!")
        nome = input("Digite seu nome: ")

    idade = int(input("Digite sua idade: "))

    while idade < 0 or idade > 150:
        print("Sua idade deve estar entre 0 e 150!")
        idade = int(input("Digite sua idade: "))

    salario = float(input("Digite seu salário: "))

    while salario <= 0:
        print("Seu salário deve ser maior que zero!")
        salario = float(input("Digite seu salário: "))
    sexo = input("Digite seu sexo(f ou m): ")

    while sexo != "f" and sexo != "m":
        print("Seu sexo deve ser f ou m!")
        sexo = input("Digite seu sexo(f ou m): ")

    estado_civil = input("Digite seu estado civil(s, c, v ,d): ")

    while estado_civil != "s" and estado_civil != "c" and estado_civil != "v" and estado_civil and "d":
        print("Seu estado cívil deve ser s, c, v ou d!")
        estado_civil = input("Digite seu estado civil(s, c, v ,d): ")

    print("Todas as informações estão válidas!")


# 4. Supondo que a população de um país A seja da ordem de 80.000 habitantes com uma taxa anual de crescimento de 3% e
# que a população de B, seja 200.000 habitantes com uma taxa de crescimento de 1.5%. Faça um programa que calcule e
# escreva o número de anos necessários para que a população do país A ultrapasse ou iguale a população do país B,
# mantidas as taxas de crescimento.

def populacao():
    populacao_pais_a = 80000
    populacao_pais_b = 200000
    anos_necessarios = 0

    while populacao_pais_a < populacao_pais_b:
        populacao_pais_a = int(populacao_pais_a + (populacao_pais_a * 0.03))
        populacao_pais_b = int(populacao_pais_b + (populacao_pais_b * 0.015))
        anos_necessarios += 1

    print("Os anos necessários para que a população de A passe B é {} ano(s)".format(anos_necessarios))
    print("População A: {} habitantes".format(populacao_pais_a))
    print("População B: {} habitantes".format(populacao_pais_b))


# 5. Altere o programa anterior permitindo ao utilizador informar as populações e as taxas de crescimento iniciais.
# Valide a entrada e permita repetir a operação.

def propria_populacao():
    permitir_operacao = True
    while permitir_operacao:
        populacao_pais_a = int(input("Digite a população do país A: "))

        while populacao_pais_a < 10000:
            print("População de A é muito pequena!")
            populacao_pais_a = int(input("Digite a população do país A: "))

        populacao_pais_b = int(input("Digite a população do país B: "))
        while populacao_pais_b < 10000:
            print("População de B é muito pequena!")
            populacao_pais_a = int(input("Digite a população do país A: "))

        taxa_de_crescimento_de_a = float(input("Digite a taxa de crescimento de A (%): "))
        while taxa_de_crescimento_de_a < 1.5:
            print("Taxa de crescimento fora do intervalo!")
            taxa_de_crescimento_de_a = float(input("Digite a taxa de crescimento de A (%): "))

        taxa_de_crescimento_de_b = float(input("Digite a taxa de crescimento de B (%): "))
        while taxa_de_crescimento_de_b < 1.5:
            print("Taxa de crescimento fora do intervalo!")
            taxa_de_crescimento_de_b = float(input("Digite a taxa de crescimento de B (%): "))
        anos_necessarios = 0

        while populacao_pais_a < populacao_pais_b:
            populacao_pais_a = (populacao_pais_a + (populacao_pais_a * (taxa_de_crescimento_de_a / 100)))
            populacao_pais_b = (populacao_pais_b + (populacao_pais_b * (taxa_de_crescimento_de_b / 100)))
            anos_necessarios += 1

        print("Os anos necessários para que a população de A passe B é {} ano(s)".format(anos_necessarios))


if __name__ == "__main__":
    propria_populacao()
