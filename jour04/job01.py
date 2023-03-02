class Personne:
    def __init__(self):
        self.age = 14

    def afficherAge(self):
        print(self.age, 'ans')

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
        Personne.__init__(self)

    def allerEnCours(self):
        print('Je vais en cours')

    def afficherAge(self):
        print("j'ai", self.age)

class Professeur:
    def __init__(self, matiere):
        self.__matiereEnseigné = matiere

    def enseigner(self):
        print('Le cours va commencer')


#instance Eleve
eleve1 = Eleve()
eleve1.afficherAge()
#instance Personne
personne1 = Personne()