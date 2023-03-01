class CompteBancaire:
    def __init__(self, numero_compte, nom, prenom, solde, decouvert):
        self.__numero_compte = numero_compte
        self.__nom = nom
        self.__prenom = prenom
        self.__solde = solde
        self.__decouvert = decouvert

    def afficher(self):
        print('Numéro de compte = ', self.__numero_compte)
        print('Nom = ', self.__nom)
        print('Pénom =', self.__prenom)
        print('Solde =',self.__solde,'€')
    def afficherSolde(self):
        print('Votre solde',self.__nom, 'est de ', self.__solde,'€')

    def versement(self, ajout_solde):
        self.__solde += ajout_solde
        print('votre nouveau solde',self.__nom ,'avec un beversement de' ,ajout_solde,'est de', self.__solde,'€')

    def retrait(self, retrait_solde):
        if self.__decouvert:
            self.__solde -= retrait_solde
            self.agios(retrait_solde)
            return True

        elif self.__solde < retrait_solde:
            print("Vous ne possédez pas assez d'argent sur votre solde actuelle",self.__nom)
            return False
        else:
            self.__solde -= retrait_solde
            print('Votre solde',self.__nom, 'après retrait est de',retrait_solde,'est de', self.__solde,'€')
            return True

    def agios(self,retrait):
        if self.__solde < 0:
            self.__solde -= 20
            print('Votre solde',self.__nom,'avec un retrait de ',retrait, 'apres agios est de', self.__solde,'€')
        else:
            print('votre solde',self.__nom,'avec un retrait de', retrait,'est de',self.__solde,'€')

    def virement(self, montant ,compte_destiantion):
        if self.retrait(montant):
            print(self.__nom,'Vous venez de virer un montant de', montant,'€')
            compte_destiantion.versement(montant)
        else:
            print("Vous ne pouvez pas faire de virement pas assez d'argent sur le compte de" ,self.__nom)





mon_compte = CompteBancaire(107, 'raphael', 'malet', 500, False)
compte_destitanation = CompteBancaire(109, 'Clement', 'Crippa', -100, True)

mon_compte.afficher()
mon_compte.afficherSolde()
mon_compte.versement(10)
mon_compte.retrait(300)
mon_compte.virement(100, compte_destitanation)

print('')
compte_destitanation.afficher()
print('')
mon_compte.afficher()