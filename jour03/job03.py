class Tache:
    def __init__(self, titre, description, status):
        self.titre = titre
        self.description = description
        self.status = status


class ListeDeTaches:
    def __init__(self):
        self.tache = []

    def ajouterTache(self, tache):
        self.tache += [tache.titre, tache.description, tache.status]

    def supprimerTache(self, tache):
        for i in self.tache:
            if i == tache.titre:
                position = self.tache.index(i)
                self.tache.pop(position)
                self.tache.pop(position)
                self.tache.pop(position)

    def marquerCommeFinie(self, tache):
        for i in self.tache:
            if i == tache.titre:
                position = self.tache.index(i)
                if self.tache[position+2] == 'en cours':
                    self.tache.pop(position+2)
                    self.tache.insert(position+2, 'terminer')
                    tache.status = 'terminer'



    def afficherListe(self):
        print(self.tache)

    def filtrerListe(self, tache):
        liste_filtrer = []
        for i in range(len(self.tache)):
            if self.tache[i] == tache.status:
                liste_filtrer.append(self.tache[i - 2])
                liste_filtrer.append(self.tache[i - 1])
                liste_filtrer.append(self.tache[i])
        print(liste_filtrer)


#initialisation des taches
tache1 = Tache('Job1', 'ajout personne a une ville', 'en cours')
tache2 = Tache('Job2', 'création compte bancaire' , 'terminer')
tache3 = Tache('job3', 'To do liste', 'en cours')
tache4 = Tache('job4', 'equipe de foot', 'en cours')
tache5 = Tache('job5', 'mini jeu', 'en cours')

#ensemble des methode de la classe ListeDeTache
liste = ListeDeTaches()
liste.ajouterTache(tache1)
liste.ajouterTache(tache2)
liste.ajouterTache(tache3)
liste.ajouterTache(tache4)
liste.ajouterTache(tache5)
liste.afficherListe()
liste.marquerCommeFinie(tache1)
liste.afficherListe()
liste.supprimerTache(tache3)
liste.afficherListe()
liste.filtrerListe(tache1)
liste.filtrerListe(tache4)