class Rectangle:
    def __init__(self, longeur, largeur):
        self._longueur = longeur
        self._largeur = largeur

    def perimetre(self):
        perimetre_rectangle = (self._longueur + self._largeur) * 2
        print(perimetre_rectangle,'m')

    def surface(self):
        surface_rectangle = self._largeur * self._longueur
        print(surface_rectangle, 'm au carré')

    def __modifierLongeur(self):
        while True:
            self._longueur = input('Entrer longueur en m :')
            if self._longueur.isdigit():
                self._longueur = int(self._longueur)
                break
            else:
                continue
    def getModifierLongeur(self):
        self.__modifierLongeur()

    def __modifierLargeur(self):
        while True:
            self._largeur = input('Entrer longueur en m :')
            if self._largeur.isdigit():
                self._largeur = int(self._largeur)
                break
            else:
                continue
    def gerModifierLargeur(self):
        self.__modifierLargeur()


class Parallelepipede(Rectangle):
    def __init__(self, hauteur, largeur, longueur):
        self.hauteur = hauteur
        Rectangle.__init__(self, largeur, longueur)

    def volume(self):
        volume_parallelepipede = self.hauteur * self._largeur * self._longueur
        print('le volume du parallelepipde est de', volume_parallelepipede, 'm au cube')



para1 = Parallelepipede(10, 24,34)
para1.surface()
para1.perimetre()
para1.volume()
print('\n----modification des valeurs de base\n')
para1.gerModifierLargeur()
para1.gerModifierLargeur()
para1.surface()
para1.perimetre()
para1.volume()