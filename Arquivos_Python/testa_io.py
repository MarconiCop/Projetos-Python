arquivo = open('dados/contatos-escrita.csv', encoding='latin_1', mode='a+')

print(type(arquivo.buffer))

texto_em_bytes = bytes('Este é um texto em bytes', 'latin_1')
# print(texto_em_bytes)
# print(type(texto_em_bytes))

contato = bytes('15,Veronica,veronica@veronica.com.br','latin_1')
arquivo.buffer.write(contato)


arquivo.close()
