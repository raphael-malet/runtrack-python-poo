class Forme:
    def __init__(self):
        self.largeur = 0
        self.longueur = 0
    def aire(self):
        aire_rectangle = (self.largeur + self.longueur) * 2
        return aire_rectangle

class Rectangle(Forme):
    def __init__(self, largeur, longueur):
        Forme.__init__(self)
        self.largeur = largeur
        self.longueur = longueur

    def aire(self):
        aire_rectangle = (self.largeur + self.longueur)*2
        return aire_rectangle




forme1 = Forme()
print(forme1.aire())

rectangle1 = Rectangle(10, 10)
print(rectangle1.aire())