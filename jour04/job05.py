class Forme:
    def __init__(self):
        self.largeur = 0
        self.longueur = 0
    def aire(self):
        return (self.largeur + self.longueur)*2

class Cercle(Forme):
    def __init__(self, radius):
        Forme.__init__(self)
        self.radius = radius


    def aire(self):
        aire_cercle = (self.radius**2)* 3.14
        return aire_cercle

class Rectangle(Forme):
    def __init__(self, largeur, longueur):
        Forme.__init__(self)
        self.largeur = largeur
        self.longueur = longueur

    def aire(self):
        aire_rectangle = (self.longueur + self.largeur)*2
        return aire_rectangle


forme1 = Forme()
print(forme1.aire())

cercle1 = Cercle(2)
print(cercle1.aire())

rectangle1 = Rectangle(10, 10)
print(rectangle1.aire())
