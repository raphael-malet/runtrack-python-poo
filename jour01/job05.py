#JOB05
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def afficherlespoints(self):
        print(str(self.x)+', '+str(self.y))

    def afficherX(self):
        print(self.x)
    def afficherY(self):
        print(self.y)
    def changerX(self, x):
        self.x = x
        print(self.x)
    def changerY(self, y):
        self.y = y
        print(self.y)


coordonee = Point(21, 11)
coordonee.afficherlespoints()
coordonee.afficherX()
coordonee.afficherY()
coordonee.changerX(35)
coordonee.changerY(34)