#JOUR 2 JOB 4
class Student:
    def __init__(self, nom, prenom, id_etudiant, credit):
        self.__nom = nom
        self.__prenom = prenom
        self.__id_etudaint = id_etudiant
        self.__credit = credit
        self.__level = self.__setstudentEval()

    def add_credis(self):
        while True:
            ajout_credit = input('Entrer le nombre de crédit a ajouter')
            if ajout_credit < str(0) or ajout_credit.isalpha():
                print('la valeur entrer doit être un nombre supérieur a 0')
            else:
                self.__credit += int(ajout_credit)
                self.__level = self.__setstudentEval()
                break

    def __setstudentEval(self):
        if self.__credit >= 90:
            return 'Excellent'
        if self.__credit >= 80:
            return 'Très bien'
        if self.__credit >= 70:
            return 'Bien'
        if self.__credit >= 60:
            return 'Passable'
        if self.__credit <60:
            return 'Insuffisant'

    def studentInfo(self):
        print('nom =', self.__nom)
        print('Prénom =', self.__prenom)
        print('Id = ',self.__id_etudaint)
        print('Niveau =',self.__level)



    #metode afficher les attributs de la classe
    def afficherNom(self):
        return self.__nom
    def afficherPrenom(self):
        return self.__prenom
    def afficherID(self):
        return self.__id_etudaint
    def afficherCredit(self):
        return self.__credit




etudiant = Student('John', 'Doe', 145, 0)
#ajout 3 fois des credit a l'étudaint
etudiant.add_credis()
etudiant.add_credis()
etudiant.add_credis()

#resultat
print('le nombre de crédits de',etudiant.afficherNom(),etudiant.afficherPrenom(),'est de',etudiant.afficherCredit())
etudiant.studentInfo()