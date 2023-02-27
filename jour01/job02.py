#JOB02

class Operation:
    def __init__(self,nombre1,nombre2):
        self.nombre1 = nombre1
        self.nombre2 = nombre2

    def afficher_nombre(self):
        print('Le nombre1 est ' + str(self.nombre1))
        print('le nombre2 est ' + str(self.nombre2))

nombre = Operation(12, 3)
nombre.afficher_nombre()
