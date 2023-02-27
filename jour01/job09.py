class Produit:
    def __init__(self, nom, prixHT, TVA):
        self.nom = nom
        self.prixHT = prixHT
        self.TVA = TVA

    def changer_prix_nom(self, nom, prixHT):
        self.nom = nom
        self.prixHT = prixHT

    def nom_produit(self):
        return self.nom

    def prixHT_produit(self):
        return self.prixHT

    def TVA_produit(self):
        self.TVA = self.TVA
        return self.TVA

    def CalculerPrixTTC(self):
        prixTTC = self.prixHT + (self.prixHT * self.TVA)
        return prixTTC

    def afficher(self):
        liste_produit = (self.nom, self.prixHT, str(self.TVA), self.CalculerPrixTTC())
        return liste_produit



patate= Produit('patate', 10, 0.20)
ps5 = Produit('PS5', 400, 0.20)
tele = Produit('télé', 250, 0.20)
print(patate.afficher())
print(ps5.afficher())
print(tele.afficher())

print(patate.nom_produit())
print(str(patate.prixHT_produit())+'€ HT')
print(str(patate.TVA_produit()*100)+'%','TVA')
print(str(patate.CalculerPrixTTC())+ '€ TTC\n')

print(ps5.nom_produit())
print(str(ps5.prixHT_produit())+'€ HT')
print(str(ps5.TVA_produit()*100)+'%','TVA')
print(str(ps5.CalculerPrixTTC())+ '€ TTC\n')

print(tele.nom_produit())
print(str(tele.prixHT_produit())+'€ HT')
print(str(tele.TVA_produit()*100)+'%','TVA')
print(str(tele.CalculerPrixTTC())+ '€ TTC\n')

patate.changer_prix_nom('pomme', 5)
print(patate.afficher())
print(patate.nom_produit())
print(str(patate.prixHT_produit())+'€ HT')
print(str(patate.TVA_produit()*100)+'%','TVA')
print(str(patate.CalculerPrixTTC())+ '€ TTC\n')

ps5.changer_prix_nom('xbox', 300)
print(ps5.afficher())
print(ps5.nom_produit())
print(str(ps5.prixHT_produit())+'€ HT')
print(str(ps5.TVA_produit()*100)+'%','TVA')
print(str(ps5.CalculerPrixTTC())+ '€ TTC\n')

tele.changer_prix_nom('voiture', 25000)
print(tele.afficher())
print(tele.nom_produit())
print(str(tele.prixHT_produit())+'€ HT')
print(str(tele.TVA_produit()*100)+'%','TVA')
print(str(tele.CalculerPrixTTC())+ '€ TTC\n')
