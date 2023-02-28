#JOUR 2 JOB 5

class Voiture:
    def __init__(self, marque, modele, annee, kilometrage, reservoir):
        self.__marque = marque
        self.__modele = modele
        self.__annee = annee
        self.__kilometrage = kilometrage
        self.__en_marche = False
        self.__reservoir = reservoir


    def __setArreter(self):
        self.__en_marche = False

    def getArreter(self):
        return self.__setArreter()

    def __setVerifier_plein(self):
        return self.__reservoir

    def __setModel(self):
        self.__modele = input('Modele = ')

    def getModel(self):
        self.__setModel()

    def __setMarque(self):
        self.__marque = input('Marque = ')

    def getMarque(self):
        self.__setMarque()

    def __setAnnee(self):
        while True:
            self.__annee = input('Année = ')
            if not self.__annee.isalpha():
                break

    def getAnnee(self):
        self.__setAnnee()
    def __setKilometre(self):
        while True:
            self.__kilometrage = input('nombre de kilomètre = ')
            if not self.__kilometrage.isalpha():
                break
    def getKilometrage(self):
        self.__setKilometre()

    def __setReservoire(self):
        while True:
            self.__reservoir = input('niveau du reservoire = ')
            if not self.__reservoir.isalpha():
                break
    def getReservoire(self):
        self.__setReservoire()

    def __setDemarrer(self):
        if int(self.__setVerifier_plein())>5:
            self.__en_marche = True
            return 'La voiture démarre'
        else:
            self.__en_marche = False
            return "/!\ Il n'y a pas assez d'essence dans le reservoir"
    def getDemarrer(self):
        return self.__setDemarrer()


    def InfoVoiture(self):
        print('marque =', self.__marque)
        print('modele =', self.__modele)
        print('Annee = ',self.__annee)
        print('kilometrage =', self.__kilometrage)
        print('Quantité réservoire =', self.__reservoir)



ma_voitrure = Voiture('fiat', 'panda', 2010, 50000, 50)
ma_voitrure.getMarque()
ma_voitrure.getModel()
ma_voitrure.getAnnee()
ma_voitrure.getKilometrage()
ma_voitrure.getReservoire()
ma_voitrure.InfoVoiture()
print(ma_voitrure.getDemarrer())
