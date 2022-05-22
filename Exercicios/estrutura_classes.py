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

    def troca_lado(self, lado):
        lado = int(input("Digite o valor do lado:"))
        self.lado = lado
        return self.lado

    def calcula_area(self):
        self.area = self.lado * self.lado
        return self.area


# 3. Classe Retangulo: Crie uma classe que modele um retangulo:
class modela_retangulo:

    def __init__(self, base, altura):
        self.area = 0
        self.perimetro = 0

        pergunta = input("Deseja trocar os lados do retângulo?").upper()

        if pergunta == "S":
            self.troca_lados(base, altura)
            self.calcula_area()
            self.calcula_perimetro()
        else:
            self.base = base
            self.altura = altura
            self.calcula_area()
            self.calcula_perimetro()

    def __str__(self):
        return "A base do Retângulo é {}, A altura do retângulo é {}, A área do retângulo é {}, O perímetro do " \
               "Retângulo é {}.".format(self.base, self.altura, self.area, self.perimetro)

    def troca_lados(self, base, altura):
        base = int(input("Digite o valor da base: "))
        self.base = base
        altura = int(input("Digite o valor da altura: "))
        self.altura = altura
        return self.base, self.altura

    def calcula_area(self):
        self.area = self.base * self.altura
        return self.area

    def calcula_perimetro(self):
        self.perimetro = (self.base * 2) + (self.altura * 2)
        return self.perimetro
