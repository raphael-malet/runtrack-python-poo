#JOB04

class Personne:

    def __init__(self, nom, prenom):
        self.nom = nom
        self.prenom = prenom

    def SePresenter(self):
        print('je suis '+ self.prenom+ ' '+ self.nom)

john = Personne('Doe', 'John')
Jean = Personne('Dupond', 'Jean')

john.SePresenter()
Jean.SePresenter()