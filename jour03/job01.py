class Ville:
    def __init__(self, nom, habitant):
        self.__nom = nom
        self.__habitant = habitant

    #methode afficher le nombre d'habitant avant ajout
    def afficherHabitantBase(self):
        print("Population de la ville de", self.__nom,':', self.__habitant,'habitants')

    #methode qui ajoute 1 au nombre total de la ville
    def AjoutNbHabitant(self, AjoutHabiant):
        self.__habitant += AjoutHabiant

    #methode afficher le nombre d'ahibtant apres ajout
    def afficherMiseAjourHabitant(self):
        print("Mise a jour de la population de la ville de", self.__nom, self.__habitant, 'habitants')


class Personne:
    def __init__(self, nom, age):
        self.__nom = nom
        self.__age = age

    #methode pour ajouter 1 au nombre de la ville
    def AjoutHabitant(self,ville):
        self.__nbhabiatantville = 0
        self.__nbhabiatantville += 1
        ville.AjoutNbHabitant(self.__nbhabiatantville)


#initialisation des objets ville
ville1 = Ville('Paris', 1000000)
ville2 = Ville('Marseille', 861635)

#initialisagtion des objet personne
personne1 = Personne('John', 45)
personne2 = Personne('Myrtille', 4)
personne3 = Personne('Chloé', 18)

#afficher le nombre d'habitant de la ville
ville1.afficherHabitantBase()
ville2.afficherHabitantBase()

#ajouter les personnes au nombre de la ville
personne1.AjoutHabitant(ville1)
personne2.AjoutHabitant(ville1)
personne3.AjoutHabitant(ville2)

#afficher le nombre de personne de la ville apres ajout
ville1.afficherMiseAjourHabitant()
ville2.afficherMiseAjourHabitant()
