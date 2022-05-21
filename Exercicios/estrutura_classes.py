# 1. Classe Bola: Crie uma classe que modele uma bola:
class modela_bola:

    def __init__(self, cor, circunferencia, material):
        self.cor = cor
        self.circunferencia = circunferencia
        self.material = material

    def __str__(self):
        return "Bola {}, {}, {}".format(self.cor, self.circunferencia, self.material)

    def trocaCor(self, nova_cor):
        self.cor = nova_cor

    def mostraCor(self):
        print(self.cor)


# 2. Classe Quadrado: Crie uma classe que modele um quadrado:
class modela_quadrado:

    def __init__(self, lado):
        self.area = 0
        pergunta = input("Deseja trocar o lado do quadrado?").upper()

        if pergunta == "S":
            self.troca_lado(lado)
            self.calcula_area()
        else:
            self.lado = lado
            self.calcula_area()

    def __str__(self):
        return "O lado é  do quadrado é {} e a área é {}".format(self.lado, self.area)

    def mostra_lado(self):
        return self.lado

    def troca_lado(self, lado):
        lado = int(input("Digite o valor do lado:"))
        self.lado = lado
        return self.lado

    def calcula_area(self):
        self.area = self.lado * self.lado
        return self.area
