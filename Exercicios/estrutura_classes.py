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
