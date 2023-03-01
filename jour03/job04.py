class Joueur:
    def __init__(self, nom, numero, postion, nb_but, passe, jaune, rouge):
        self.nom = nom
        self.numero = numero
        self.position = postion
        self.nb_but = nb_but
        self.passe = passe
        self.jaune = jaune
        self.rouge = rouge

    def marquerBut(self):
        self.nb_but +=1

    def effectuerUnePasseDecisive(self):
        self.passe +=1

    def recevoirUnCartonJaune(self):
        self.jaune += 1
    def recevoirUnCartonRouge(self):
        self.rouge += 1

    def afficherStatistique(self):
        print('nom joueur = ',self.nom)
        print('numero du joueur = ', self.numero)
        print('poste = ',self.position)
        print('nombre de but = ', self.nb_but)
        print('passe décisive = ', self.passe)
        print('carton jaune = ', self.jaune)
        print('carton rouge = ', self.rouge)
        print('')


class Equipe:
    def __init__(self, nom):
        self.nom = nom
        self.liste_joueur = []


    def ajouterJoueur(self, joueur):
        self.liste_joueur += [joueur.nom]

    def afficherListeJoueur(self):
        print(self.liste_joueur)

    def AfficherStatistiquesJoueurs(self):

        if self.nom == 'France':
            print('Equipe =',self.nom)
            benzema.afficherStatistique()
            zizou.afficherStatistique()
            mbappe.afficherStatistique()
            print('-------------------')
        else:
            print('Equipe =', self.nom)
            messi.afficherStatistique()
            aguero.afficherStatistique()
            maradona.afficherStatistique()
            print('----------------------')

    def mettreAJourStatistiqueJoueur(self):
        if self.nom == 'France':
            print('Equipe =',self.nom)
            benzema.afficherStatistique()
            zizou.afficherStatistique()
            mbappe.afficherStatistique()
            print('-------------------')
        else:
            print('Equipe =', self.nom)
            messi.afficherStatistique()
            aguero.afficherStatistique()
            maradona.afficherStatistique()
            print('----------------------')



benzema = Joueur('benzema',10,'attaquant',0, 0, 0 , 0)
zizou = Joueur('zizou',9,'milieu',0,0, 0, 0)
mbappe = Joueur('mbappe',7,'attaquant',0,0, 0, 0)


messi = Joueur('messi','milieu',10,  0,0, 0, 0)
aguero = Joueur('aguero',9,'attaquand',  0,0, 0, 0)
maradona = Joueur('maradona',7,'milieu', 0,0, 0, 0)


france = Equipe('France')
argentine = Equipe('Argentine')

france.ajouterJoueur(benzema)
france.ajouterJoueur(zizou)
france.ajouterJoueur(mbappe)

argentine.ajouterJoueur(messi)
argentine.ajouterJoueur(aguero)
argentine.ajouterJoueur(maradona)

france.AfficherStatistiquesJoueurs()
argentine.AfficherStatistiquesJoueurs()

print('-------DEBUT DU MATCH--------')


mbappe.recevoirUnCartonJaune()
messi.marquerBut()
zizou.effectuerUnePasseDecisive()
benzema.marquerBut()
maradona.recevoirUnCartonRouge()
zizou.marquerBut()
zizou.effectuerUnePasseDecisive()
mbappe.marquerBut()
aguero.recevoirUnCartonJaune()
aguero.recevoirUnCartonJaune()

print('--------FIN DU MATCH---------')

france.mettreAJourStatistiqueJoueur()
argentine.mettreAJourStatistiqueJoueur()
