#JOB08

class Cercle:
    def __init__(self, rayon):
        self.rayon = rayon

    def changerRayon(self, rayon):
        self.rayon = rayon
        print("le rayon est désormais égale a "+ str(self.rayon))


    def circonference(self):
        circonf = (self.rayon*2)*3.14
        return circonf
    def aire(self):
        calcul_aire = (self.rayon**2)*3.14
        return calcul_aire

    def diametre(self):
        calcul_diametre = self.rayon*2
        return calcul_diametre

    def afficherInfos(self):
        print("le rayon du cercle est de " + str(self.rayon))
        print( 'diamètre du cercle de rayon '+ str(self.rayon)+ ' est de ' + str(self.diametre()))
        print("l'aire du cercle de rayon "+ str(self.rayon)+ ' est de ' + str(self.aire()))
        print("la circonférence du cercle de rayon "+ str(self.rayon)+ ' est de ' + str(self.circonference())+'\n')



cercle1 = Cercle(4)
cercle2 = Cercle(7)

#cercle avec 4 de rayon
cercle1.afficherInfos()

#cercle avec 7 de rayon
cercle2.afficherInfos()

#cercle avec rayon changer
cercle2.changerRayon(10)
cercle2.afficherInfos()
