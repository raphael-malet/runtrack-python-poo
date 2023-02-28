#JOUR 2 JOB 3
#JOUR 2 JOB 2

class Livre:

    def __init__(self, titre , auteur, nb_page, disponible):
        self.__titre = titre
        self.__auteur = auteur
        self.__nb_page = nb_page
        self.__disponible = disponible

    def verification(self):
        if self.__disponible:
            return True
        else:
            return False
    def Emprunter(self):
        if self.verification():
            print('vous pouvez emprunter le livre')
            self.__disponible = False
        else:
            print('le livre est emprunter')
    def rendre(self):
        if not self.verification():
            print('vous rendez le livre')
            self.__disponible = True
        else:
            pass

    def __setTitre(self):
        self.__titre = input('Entre titre du livre : ')
        return self.__titre

    def __setAuteur(self):
        self.__auteur = input('Entrer auteur du livre :')
        return self.__auteur

    def __setPage(self):
        while True:
            self.__nb_page = input('Entrer le nombre de page :')
            if '.' in self.__nb_page:
                print('le nombre de page doit etre une nombre entier')
            elif self.__nb_page < str(0) or self.__nb_page.isalpha():
                print('le nombre de page entrée est incorrecte')
            else:
                return self.__nb_page

    def getTitre(self):
        self.__setTitre()

    def getAuteur(self):
        self.__setAuteur()

    def getpage(self):
        self.__setPage()

    def AfficherTitre(self):
        return self.__titre

    def AfficherAuteur(self):
        return self.__auteur
    def afficherNombrePage(self):
        return self.__nb_page


boukin = Livre('la parole de jul', 'Jul', 100, True)
boukin.Emprunter()
print('le Tire du livre est ', boukin.AfficherTitre())
print("l'auteur du livre est ", boukin.AfficherAuteur())
print("le nombre de page est de", boukin.afficherNombrePage())
boukin.Emprunter()
boukin.rendre()

#modifier les valeurs
boukin.getTitre()
boukin.getAuteur()
boukin.getpage()
boukin.Emprunter()

print('le Tire du livre est ', boukin.AfficherTitre())
print("l'auteur du livre est ", boukin.AfficherAuteur())
print("le nombre de page est de", boukin.afficherNombrePage())
boukin.Emprunter()
boukin.rendre()
boukin.Emprunter()
