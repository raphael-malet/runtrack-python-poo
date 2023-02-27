#JOB07
class Personnage:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def gauche(self):
        self.x -= 1
    def droite(self):
        self.x += 1
    def haut(self):
        self.y += 1
    def bas(self):
        self.y -= 1
    def position(self):
        tuple_position = (self.x , self.y)
        return tuple_position

mouvement = Personnage(1,1)
mouvement.gauche()
print(mouvement.position())
mouvement.droite()
print(mouvement.position())
mouvement.haut()
print(mouvement.position())
mouvement.bas()
print(mouvement.position())

