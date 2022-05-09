from cpf_cnpj import Documento


cpf = "15316264754"
cnpj = "35379838000112"


documento = Documento.cria_documento(cnpj)
documento_um = Documento.cria_documento(cpf)
print(documento)
print(documento_um)

