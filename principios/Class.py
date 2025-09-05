#Classes em Python
class Cachorro:
    def __init__(self,nome,raca,idade,peso):
        self.nome = nome
        self.raca = raca
        self.idade = idade
        self.peso = peso

    def latir(self):
        print(f"Eu lati e me chamo {self.nome}")

cachorro1 = Cachorro("Billy","Bulldog", 8, 23.9)
cachorro1.latir()