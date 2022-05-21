import re  # Expressões Regulares

padrao = re.compile("[0-9]?[0-9]")
lista = []

try:
    with open('dados/contatos.csv', mode='r', encoding='latin_1') as arquivo_contatos:

        for linha in arquivo_contatos:
            busca = padrao.search(linha)
            lista.append(busca.group())

    print(lista)
    int_list = list(map(int, lista))
    print(int_list)



except FileNotFoundError:
    print("Arquivo não encontrado!")

except PermissionError:
    print("Sem permissão de escrita!")
