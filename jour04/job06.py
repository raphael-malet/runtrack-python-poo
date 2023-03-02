class Vehicule:
    def __init__(self, marque, annee, prix):
        self.marque = marque
        self.annee = annee
        self.prix = prix

    def informationsVehicule(self, modele):
        print('Marque =', self.marque)
        print('Modele =', modele)
        print('Année =', self.annee)
        print('Prix =', self.prix)

    def demarrer(self):
        print('Attention je roule')


class Voiture(Vehicule):
    def __init__(self, marque, modele, annee, prix):
        Vehicule.__init__(self, marque, annee, prix)
        self.portes = 4
        self.modele = modele


    def informationsVehicule(self):
        Vehicule.informationsVehicule(self,self.modele)
        print('Nombre de portes =',self.portes)
    def demarrer(self):
        Vehicule.demarrer(self)
        print('Les 100 sont en Y')

class Moto(Vehicule):
    def __init__(self, marque, modele, annee, prix):
        Vehicule.__init__(self, marque, annee, prix)
        self.roue = 2
        self.modele = modele


    def informationsVehicule(self):
        Vehicule.informationsVehicule(self, self.modele)
        print('Nombre de roue', self.roue)

    def demarrer(self):
        Vehicule.demarrer(self)
        print('En Y le 100')


voiture1 = Voiture('Mercedes','Classe A', 2010, 100000)
voiture1.informationsVehicule()
voiture1.demarrer()

print('--------------------')

moto1 = Moto('Yamaha', '1200 Vmax', 1987, 4500)
moto1.informationsVehicule()
moto1.demarrer()