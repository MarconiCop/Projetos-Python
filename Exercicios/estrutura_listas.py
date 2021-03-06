import itertools
import random

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


# 16. Utilize uma lista para resolver o problema a seguir. Uma empresa paga os seus vendedores com base em comissões. O
# vendedor recebe $200 por semana mais 9 por cento das suas vendas brutas daquela semana. Por exemplo, um vendedor que
# teve vendas brutas de $3000 numa semana recebe $200 mais 9 por cento de $3000, ou seja, um total de $470. Escreva
# um programa (usando um array de contadores) que determine quantos vendedores receberam salários nos seguintes 
# intervalos de valores: $200 - $299 $300 - $399 $400 - $499 $500 - $599 $600 - $699 $700 - $799 $800 - $899 $900 - 
# $999 $1000 em diante Desafio: Crie uma fórmula para chegar na posição da lista a partir do salário, 
# sem fazer vários ifs aninhados. 

def exibir_lista_contador_salario():
    contadores = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    salario = 0
    salarios = []

    while salario != -1:

        salario = float(input("Digite o salário: "))

        if salario != -1:
            salario = salario + 200 + 0.09 * salario
            salarios.append(salario)

    for salario in salarios:
        indice = int((salario / 100) - 2)
        contadores[indice] += 1

    print(salarios)
    print(contadores)


# 17. Numa competição de salto em distância cada atleta tem direito a cinco saltos. O resultado do atleta será
# determinado pela média dos cinco valores restantes. Deve fazer um programa que receba o nome e as cinco
# distâncias alcançadas pelo atleta nos seus saltos e depois informe o nome, os saltos e a média dos saltos. O
# programa deve ser encerrado quando não for informado o nome do atleta. A saída do programa deve ser conforme o
# exemplo abaixo: Atleta: Rodrigo Curvêllo
#
# Primeiro Salto: 6,5 m
# Segundo Salto: 6,1 m
# Terceiro Salto: 6,2 m
# Quarto Salto: 5,4 m
# Quinto Salto: 5,3 m
#
# Resultado:
# Atleta: Rodrigo Curvêllo
# Saltos: 6.5 - 6.1 - 6.2 - 5.4 - 5.3
# Média dos saltos: 5,9 m

def exibir_lista_salto():
    nome = input("Digite o nome do atleta: ").capitalize()
    saltos = []
    if nome != "":

        for posicao in range(1, 6):
            salto = float(input("Digite a distância do salto {}: ".format(posicao)))
            saltos.append(salto)

        print("--------------------------------")
        print("Atleta: {}".format(nome))
        print("")
        print("Primeiro Salto: {} m".format(saltos[0]))
        print("Segundo Salto: {} m".format(saltos[1]))
        print("Terceiro Salto: {} m".format(saltos[2]))
        print("Quarto Salto: {} m".format(saltos[3]))
        print("Quinto Salto: {} m".format(saltos[4]))
        print("")
        print("Resultado final:")
        print("Atleta: {}".format(nome))
        print("{} - {} - {} - {} - {}".format(saltos[0], saltos[1], saltos[2], saltos[3], saltos[4]))
        print("Média dos saltos: {} m".format(sum(saltos) / len(saltos)))
        print("--------------------------------")

    else:
        return 1


# 23. Uma grande emissora de televisão quer fazer uma enquete entre os seus telespectadores para delinear o melhor
# jogador após cada jogo. Para isto, faz-se necessário o desenvolvimento de um programa, que será utilizado pelas
# telefonistas, para a computação dos votos. A sua equipa foi contratada para desenvolver este programa, utilizando a
# linguagem de programação C++. Para computar cada voto, a telefonista digitará um número, entre 1 e 23,
# correspondente ao número da camisa do jogador. Um número de jogador igual zero, indica que a votação foi encerrada.
# Se um número inválido for digitado, o programa deve ignorá-lo, mostrando uma breve mensagem de aviso, e voltando a
# pedir outro número. Após o final da votação, o programa deverá exibir: O total de votos computados; os númeos e
# respetivos votos de todos os jogadores que receberam votos; O percentual de votos de cada um destes jogadores; O
# número do jogador escolhido como o melhor jogador da partida, com o número de votos e o percentual de
# votos dados a ele. Observe que os votos inválidos e o zero finais não devem ser computados como votos. O resultado
# aparece ordenado pelo número do jogador. O programa deve usar arrays. O programa deverá executar o cálculo
# do percentual de cada jogador através de uma função. Esta função receberá dois parâmetros: o número de votos de um
# jogador e o total de votos. A função calculará o percentual e retornará o valor calculado. Abaixo segue uma tela de
# exemplo. A disposição das informações deve ser o mais próxima possível ao exemplo. Os dados são fictícios e podem
# mudar a cada execução do programa. Ao final, o programa deve ainda gravar os dados referentes ao resultado da
# votação num arquivo texto no disco, obedecendo a mesma disposição apresentada na tela.


def exibir_lista_votacao():
    contadores = [0] * 23
    jogadores = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23)
    percentuais = []

    print("-----------------------------------")
    print("Enquete: Quem foi o melhor jogador?")
    print("-----------------------------------")

    votar = int(input("Número do jogador (0=fim):"))

    if votar == 0:
        print("Programa encerrado pelo usuário!")
        return 1

    elif votar in jogadores:
        contadores[votar - 1] += 1

        while votar != 0:
            votar = int(input("Número do jogador (0=fim):"))
            if votar not in jogadores:
                while votar not in jogadores:
                    if votar == 0:
                        break
                    print("Informe um valor entre 1 e 23 ou 0 para sair!")
                    votar = int(input("Número do jogador (0=fim):"))
                    if votar == 0:
                        break
            contadores[votar - 1] += 1

        contadores[22] -= 1

    elif votar not in jogadores:
        print("Informe um valor entre 1 e 23 ou 0 para sair!")
        while votar != 0:
            votar = int(input("Número do jogador (0=fim):"))
            if votar not in jogadores:
                while votar not in jogadores:
                    if votar == 0:
                        break
                    print("Informe um valor entre 1 e 23 ou 0 para sair!")
                    votar = int(input("Número do jogador (0=fim):"))
                    if votar == 0:
                        break
            contadores[votar - 1] += 1

        contadores[22] -= 1

    print("")
    print("Resultado da votação:")
    print("")
    print("Foram computados {} votos.".format(sum(contadores)))
    print("")
    print("Jogador       Votos           %")

    for voto in contadores:
        percentual = calcula_percentual(voto, sum(contadores))
        percentuais.append(percentual)

    for posicao in range(0, 23):
        if contadores[posicao] != 0:
            print("   {}            {}           {:.1f}%".format(jogadores[posicao], contadores[posicao],
                                                                 percentuais[posicao]))

    for posicao in range(0, 23):
        if contadores[posicao] == max(contadores):
            melhor_jogador = posicao + 1
            votos_do_jogador = contadores[posicao]
            percentual_do_jogador = percentuais[posicao]

    print(
        "O melhor jogador foi o número {}, com {} votos, correspondendo a {:.2f}% do total de votos.".format(
            melhor_jogador,
            votos_do_jogador,
            percentual_do_jogador))


def calcula_percentual(numero_votos, total_votos):
    percentual = (numero_votos * 100) / total_votos
    return percentual


# 19. Uma empresa de pesquisas precisa tabular os resultados da seguinte enquete feita a um abundante de
# organizações: "Qual o melhor Sistema operativo para uso em servidores?"
#
# As possíveis respostas são:
#
# 1- Windows Servidor 2- Unix 3- Linux 4- Netware 5- Mac OS 6- Outro Foi contratado para desenvolver um programa
# que leia o resultado da enquete e informe ao final o resultado da mesma. O programa deverá ler os valores até ser
# informado o valor 0, que encerra a entrada dos dados. Não deverão ser aceites valores além dos válidos para o
# programa (0 a 6). Os valores referentes a cada uma das opções devem ser armazenados num vetor. Após os dados terem
# sido completamente informados, o programa deverá calcular a percentual de cada um dos concorrentes e informar o
# vencedor da enquete.

def exibir_lista_votacao_sistema():
    contadores = [0] * 6
    sistemas = (1, 2, 3, 4, 5, 6)
    percentuais = []

    print("---------------------------------------------------------")
    print("Qual o melhor Sistema Operacional para uso em servidores?")
    print("---------------------------------------------------------")
    print("")
    print("1- Windows Server")
    print("2- Unix")
    print("3- Linux")
    print("4- Netware")
    print("5- Mac OS")
    print("6- Outro")
    print("")

    votar = int(input("Número do Sistema (0=fim):"))

    if votar == 0:
        print("Programa encerrado pelo usuário!")
        return 1

    elif votar in sistemas:
        contadores[votar - 1] += 1

        while votar != 0:
            votar = int(input("Número do Sistema (0=fim):"))
            if votar not in sistemas:
                while votar not in sistemas:
                    if votar == 0:
                        break
                    print("Informe um valor entre 1 e 6 ou 0 para sair!")
                    votar = int(input("Número do Sistema (0=fim):"))
                    if votar == 0:
                        break
            contadores[votar - 1] += 1

        contadores[5] -= 1

    elif votar not in sistemas:
        print("Informe um valor entre 1 e 6 ou 0 para sair!")
        while votar != 0:
            votar = int(input("Número do Sistema (0=fim):"))
            if votar not in sistemas:
                while votar not in sistemas:
                    if votar == 0:
                        break
                    print("Informe um valor entre 1 e 6 ou 0 para sair!")
                    votar = int(input("Número do Sistema (0=fim):"))
                    if votar == 0:
                        break
            contadores[votar - 1] += 1

        contadores[5] -= 1

    for voto in contadores:
        percentual = calcula_percentual(voto, sum(contadores))
        percentuais.append(percentual)

    print("")
    print("Sistema Operacional     Votos   %")
    print("-------------------     -----   ---")
    print("Windows Server            {}     {:.2f}%".format(contadores[0], percentuais[0]))
    print("Unix                      {}     {:.2f}%".format(contadores[1], percentuais[1]))
    print("Linux                     {}     {:.2f}%".format(contadores[2], percentuais[2]))
    print("Netware                   {}     {:.2f}%".format(contadores[3], percentuais[3]))
    print("Mac OS                    {}     {:.2f}%".format(contadores[4], percentuais[4]))
    print("Outro                     {}     {:.2f}%".format(contadores[5], percentuais[5]))
    print("-------------------     -----")
    print("Total                    {}".format(sum(contadores)))

    for posicao in range(0, 6):
        if contadores[posicao] == max(contadores):
            melhor_sistema = posicao + 1
            votos_do_sistema = contadores[posicao]
            percentual_do_sistema = percentuais[posicao]

    if melhor_sistema == 1:
        nome_sistema = "Windows Server"
    if melhor_sistema == 2:
        nome_sistema = "Unix"
    if melhor_sistema == 3:
        nome_sistema = "Linux"
    if melhor_sistema == 4:
        nome_sistema = "Netware"
    if melhor_sistema == 5:
        nome_sistema = "Mac OS"
    if melhor_sistema == 6:
        nome_sistema = "Outro"

    print("")
    print(
        "O Sistema Operacional mais votado foi o {}, com {} votos, correspondendo a {:.2f}% dos votos.".format(
            nome_sistema,
            votos_do_sistema,
            percentual_do_sistema))


def calcula_percentual(numero_votos, total_votos):
    percentual = (numero_votos * 100) / total_votos
    return percentual


# 20. As Organizações Tabajara resolveram dar um abono aos seus colaboradores em reconhecimento ao bom resultado
# alcançado durante o ano que passou. Para isto contratou você para desenvolver a aplicação que servirá como uma
# projeção de quanto será gasto com o pagamento deste abono. Após reuniões envolvendo a diretoria executiva,
# a diretoria financeira e os representantes do sindicato laboral, chegou-se a seguinte forma de cálculo: a.Cada
# funcionário receberá o equivalente a 20% do seu salário bruto de dezembro; a.O piso do abono será de 100 reais,
# isto é, aqueles funcionários cujo salário for muito baixo, recebem este valor mínimo; Neste momento, não se deve
# ter nenhuma preocupação com colaboradores com tempo menor de casa, descontos, impostos ou outras particularidades.
# O seu programa deverá permitir a digitação do salário de um número indefinido (desconhecido) de salários. Um valor de
# salário igual a 0 (zero) encerra a digitação. Após a entrada de todos os dados o programa deverá calcular o valor
# do abono concedido a cada colaborador, conforme a regra definida acima. Ao final, o programa deverá
# apresentar: O salário de cada funcionário, com o valor do abono; O número total de funcionário
# processado; O valor total a ser gasto com o pagamento do abono; O número de funcionário que receberá o valor
# mínimo de 100 reais; O maior valor pago como abono; A tela abaixo é um exemplo de execução do programa, apenas para
# fins ilustrativos. Os valores podem mudar a cada execução do programa.

def exibir_lista_salario():
    salarios = []
    abonos = []
    contador = 0

    salario = int(input("Digite qualquer coisa (Exceto 0) para iniciar o programa:"))

    if salario == 0:
        return 1

    print("Projeção de Gastos com Abono")
    print("============================")
    print("")

    while salario != 0:
        salario = int(input("Digite o salário: "))
        salarios.append(salario)

    for posicao in range(0, len(salarios)):
        if salarios[posicao] < 1000:
            abonos.append(100)
            contador += 1
        else:
            abonos.append(0.20 * salarios[posicao])

    contador -= 1
    salarios.pop()
    abonos.pop()

    print("Salário    - Abono ")
    for posicao in range(0, len(salarios)):
        print("R$ {:.2f} - R$ {:.2f}".format(salarios[posicao], abonos[posicao]))

    print("")
    print("Foram processados {} colaboradores".format(len(salarios)))
    print("Total gasto com abonos: R${:.2f}".format(sum(abonos)))
    print("Valor mínimo pago a {} colaboradores".format(contador))
    print("Maior valor de abono pago: R${:.2f}".format(max(abonos)))


# 21. Faça um programa que carregue uma lista com os modelos de cinco carros (exemplo de modelos: FUSCA, GOL,
# VECTRA etc). Carregue outra lista com o consumo desses carros, isto é, quantos quilômetros cada um desses
# carros faz com um litro de combustível. Calcule e mostre: O modelo do carro mais econômico; Quantos litros de
# combustível cada um dos carros cadastrados consome para percorrer uma distância de 1000 quilômetros e quanto isto
# custará, considerando um que a gasolina custe R$ 2,25 o litro. Abaixo segue uma tela de exemplo. O disposição das
# informações deve ser o mais próxima possível ao exemplo. Os dados são fictícios e podem mudar a cada execução do
# programa.

def exibir_lista_carros():
    carros = ("Fusca", "Gol", "Uno", "Vectra", "Peugeout")
    consumo = []
    litros = []
    precos = []

    print("")
    print("Comparativo de Consumo de Combustível")
    print("")

    for contador in range(len(carros)):
        print("Veículo {}".format(contador + 1))
        print("Nome: {}".format(carros[contador]))
        kilometro = float(input("Km por litro: "))

        consumo.append(kilometro)

    for consumos in consumo:
        litros.append(calcula_mil(consumos))

    for litro in litros:
        precos.append((calcula_precos(litro)))

    for posicao in range(len(carros)):
        if max(consumo) == consumo[posicao]:
            carro_economico = carros[posicao]

    print("Relatório Final")
    for posicao in range(len(carros)):
        print("{} - {}  -    {} -  {:.2f} litros - R$ {:.2f}".format(posicao + 1, carros[posicao],
                                                                     consumo[posicao],
                                                                     litros[posicao],
                                                                     precos[posicao]))

    print("O menor consumo é do {}.".format(carro_economico))


def calcula_mil(consumos):
    return 1000 / consumos


def calcula_precos(litro):
    return litro * 2.25


# 22. A sua organização acaba de contratar um estagiário para trabalhar no Suporte de Informática, com a intenção de
# fazer um levantamento nas sucatas encontradas nesta área. A primeira tarefa dele é testar todos os cerca de 200
# ratos que se encontram lá, testando e anotando o estado de cada um deles, para verificar o que se pode aproveitar
# deles. Foi requisitado que desenvolva um programa para registrar este levantamento. O programa deverá receber
# um número indeterminado de entradas, cada uma contendo: um número de identificação do rato o APAGAR defeito:
# necessita da esfera; necessita de limpeza; a.necessita troca do cabo ou conector; a.quebrado ou inutilizado Uma
# identificação igual a zero encerra o programa.

def exibir_lista_mouse():
    lista = []
    quantidade_mouses = []
    problemas = []
    percentual = []
    contadores = []
    contador_um = 0
    contador_dois = 0
    contador_tres = 0
    contador_quatro = 0

    class Mouse:

        def __init__(self, codigo, numero_problema):
            self.__codigo = codigo
            self.__numero_problema = numero_problema

        @property
        def codigo(self):
            return self.__codigo

        @property
        def numero_problema(self):
            return self.__numero_problema

    for mouse in range(1, 200 + 1):
        codigo = int(input("Digite o código do mouse: "))
        if codigo == 0:
            break
        problema = int(input("Digite o número do problema: "))
        if problema != 1 and problema != 2 and problema != 3 and problema != 4:
            break

        mouses = Mouse(codigo, problema)
        lista.extend([[mouses.codigo, mouses.numero_problema]])

    for mouse in range(len(lista)):
        quantidade_mouses.append(lista[mouse][0])

    for problema in range(len(lista)):
        problemas.append(lista[problema][1])

    for problema in problemas:
        if problema == 1:
            contador_um += 1
        elif problema == 2:
            contador_dois += 1
        elif problema == 3:
            contador_tres += 1
        elif problema == 4:
            contador_quatro += 1

    contadores.extend([contador_um, contador_dois, contador_tres, contador_quatro])

    percentual_um = contador_um * 100 / sum(contadores)
    percentual_dois = contador_dois * 100 / sum(contadores)
    percentual_tres = contador_tres * 100 / sum(contadores)
    percentual_quatro = contador_quatro * 100 / sum(contadores)

    print("")
    print("Quantidade de mouses: {}".format(len(quantidade_mouses)))
    print("Situação                        Quantidade              Percentual")
    print("1- necessita da esfera                  {}                     {:.2f}%".format(contador_um, percentual_um))
    print(
        "2- necessita de limpeza                 {}                     {:.2f}%".format(contador_dois, percentual_dois))
    print(
        "3- necessita troca do cabo ou conector  {}                     {:.2f}%".format(contador_tres, percentual_tres))
    print("4- quebrado ou inutilizado              {}                     {:.2f}%".format(contador_quatro,
                                                                                          percentual_quatro))


# 24. Faça um programa que simule um lançamento de dados. Lance o dado 100 vezes e armazene os resultados num vetor.
# Depois, mostre quantas vezes cada valor foi conseguido. Dica: use um vetor de contadores(1 – 6) e uma função para
# gerar numeros aleatórios, simulando os lançamentos dos dados.

def exibir_lista_contadores():
    contadores = []
    numeros = []
    contador_um = 0
    contador_dois = 0
    contador_tres = 0
    contador_quatro = 0
    contador_cinco = 0
    contador_seis = 0

    for jogada in range(1, 100 + 1):
        numero = random.randint(1, 6)
        numeros.append(numero)

    for numero in numeros:
        if numero == 1:
            contador_um += 1
        elif numero == 2:
            contador_dois += 1
        elif numero == 3:
            contador_tres += 1
        elif numero == 4:
            contador_quatro += 1
        elif numero == 5:
            contador_cinco += 1
        elif numero == 6:
            contador_seis += 1

    contadores.extend([contador_um, contador_dois, contador_tres, contador_quatro, contador_cinco, contador_seis])

    for posicao in range(len(contadores)):
        print("Houve {} jogadas com o número {}".format(contadores[posicao], posicao + 1))

if __name__ == "__main__":
    exibir_lista_contadores()
