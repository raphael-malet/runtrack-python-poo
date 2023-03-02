import random

class Carte:
    def __init__(self):
        self.valeur = [2,3,4,5,6,7,8,9,10,'Valet','Dame','Roi','As']
        self.couleur = ['coeur', 'carreau', 'trefle', 'pique']
        self.paquet = []
        self.point =[]
        self.paquet_joueur =[]
        self.paquet_croupier = []

    def intitialisationPaquet(self):
        for couleur in self.couleur:
            for valeur in self.valeur:
                self.paquet.append((str(valeur)+' '+ couleur))

    def distribuer_carte_debut_partie(self):
        Carte.intitialisationPaquet(self)
        for i in range(2):

            tirage_joueur = random.randrange(len(self.paquet))
            carte = self.paquet[tirage_joueur]
            self.paquet.pop(tirage_joueur)
            self.paquet_joueur.append(carte)
            #-------------TIRAGE POUR LE CROUPIER ----------------
            tirage_croupier = random.randrange(len(self.paquet))
            carte_croupier = self.paquet[tirage_croupier]
            self.paquet.pop(tirage_croupier)
            self.paquet_croupier.append(carte_croupier)


    def tirage_carte(self, jeu ):
        tirage = random.randrange(len(self.paquet))
        carte = self.paquet[tirage]
        self.paquet.pop(tirage)
        jeu.append(carte)
        return jeu

    def additionner_point(self, point, i, croupier):
        if i[0:2] == '10':
            point += 10
        elif '1' in i[0:2]:
            point += 1
        elif '2' in i[0:2]:
            point += 2
        elif '3' in i[0:2]:
            point += 3
        elif '4' in i[0:2]:
            point += 4
        elif '5' in i[0:2]:
            point += 5
        elif '6' in i[0:2]:
            point += 6
        elif '7' in i[0:2]:
            point += 7
        elif '8' in i[0:2]:
            point += 8
        elif '9' in i[0:2]:
            point += 9
        elif 'Va' in i[0:2]:
            point += 10
        elif 'Da' in i[0:2]:
            point += 10
        elif 'Ro' in i[0:2]:
            point += 10
        elif 'As' in i[0:2]:
            if croupier:
                if point <= 10:
                    point += 10
                else:
                    point += 1
            else:
                while True:
                    choix = input('As tirer voulez vous la valeur 1 ou 11 ?\n1 = 1\n2 = 11 ')
                    if choix == '1':
                        point += 1
                        break
                    if choix == '2':
                        point += 11
                        break
                    else:
                        continue
        return point


class Jeu(Carte):
    def __init__(self):
        Carte.__init__(self)
        self.nombre_joueur = 0
        self.jeu_joueur = []
        self.point_joueur = 0
        self.jeu_croupier = []
        self.point_croupier = 0
        self.jeu_en_cours = True
        self.tirer_carte = True

    def addition_point_joueur_debut(self, carte, point, croupier):
        for i in carte:
           point = Carte.additionner_point(self, point, i, croupier)
        return point
    def Tour_joueur(self):
        while self.tirer_carte:
            choix = input("Voulez vous tirer une nouvelle carte ?\n1 = oui\n2 = non\n")
            if choix == '1':
                self.paquet_joueur = self.tirage_carte(self.paquet_joueur)
                carte = self.paquet_joueur[-1]
                carte_point = carte[0:2]
                self.point_joueur = self.additionner_point(self.point_joueur, carte_point, False)
                break
            if choix == '2':
                self.tirer_carte = False
                break
    def Tour_croupier(self):
        while True:
            if self.point_croupier >= 17:
                break
            else:
                self.paquet_croupier = self.tirage_carte(self.paquet_croupier)
                carte = self.paquet_croupier[-1]
                carte = carte[0:2]
                self.point_croupier = Carte.additionner_point(self, self.point_croupier, carte, True)
                break


    def Parite_en_cours(self):
        self.distribuer_carte_debut_partie()
        self.point_joueur = self.addition_point_joueur_debut(self.paquet_joueur, self.point_joueur, False)
        print('Votre jeu est :',', '.join(self.paquet_joueur))
        print('vos point =',self.point_joueur)
        print('----------------------------')
        self.point_croupier = self.addition_point_joueur_debut(self.paquet_croupier, self.point_croupier, True)
        print('Jeu du croupier est :', ', '.join(self.paquet_croupier))
        print('Point croupier = ', self.point_croupier)

        while self.jeu_en_cours:
            self.Tour_joueur()
            print('votre jeu est :',', '.join(self.paquet_joueur))
            print('Vos point =',self.point_joueur)
            if self.point_joueur > 21 or  self.point_joueur<self.point_croupier and not self.tirer_carte:
                print('vous avez perdu')
                break
            print('--------Tour Croupier-----------')
            self.Tour_croupier()
            print('Jeu croupier =', ', '.join(self.paquet_croupier))
            print('Point croupier = ', self.point_croupier)
            if self.point_croupier > 21 or self.paquet_croupier == 21 or self.point_croupier >= 17 and self.point_joueur > self.point_croupier:
                print('vous avez Gangé Bravo !!!!')
                break
            elif self.point_croupier >= 17 and self.point_croupier == self.point_joueur:
                print('Egalité')
                break

jeu = Jeu()
jeu.Parite_en_cours()

