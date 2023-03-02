class Personne:
    def __init__(self, age):
        self.age = age

    def afficherAge(self):
        print("j'ai", self.age, 'ans')

    def bonjour(self):
        print("Hello")

    def modifierAge(self):
        while True:
            self.age = input('Entrer age :')
            if self.age.isdigit():
                break
            else:
                continue


class Eleve(Personne):
    def __init__(self):
        Personne.__init__(self, 14)

    def allerEnCours(self):
        print('Je vais en cours')

class Professeur(Personne):
    def __init__(self, matiere):
        self.__matiereEnseigné = matiere
        Personne.__init__(self, 40)

    def enseigner(self):
        print('Le cours va commencer')


#instance Eleve
eleve1 = Eleve()
eleve1.afficherAge()
eleve1.bonjour()
eleve1.allerEnCours()
eleve1.modifierAge()
eleve1.afficherAge()
print('--------')
#instance Professeur
prof1 = Professeur('math')
prof1.afficherAge()
prof1.bonjour()
prof1.enseigner()
