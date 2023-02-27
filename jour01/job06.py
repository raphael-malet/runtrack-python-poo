#JOB 06

class Animal:

    def __init__(self, age, prenom):
        self.age = age
        self.prenom = prenom

    def veillir(self):
        self.age += 1
        print("L'age de l'animal " + str(self.age) + ' ans')

    def nommer(self):
        print("l'animal se nom " + self.prenom)


age = 0
animal = Animal(age, 'Luna')
print("L'age de l'animal "+ str(age)+ ' ans')
animal.veillir()
animal.nommer()

