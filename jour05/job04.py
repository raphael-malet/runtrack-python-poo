def plus_grand_chiffre_liste(liste):
    if len(liste) == 1:
        return liste[0]
    else:
        return max(liste[0], plus_grand_chiffre_liste(liste[1:]))






liste = [1,2,3,45,6,43,2,4,6,465,5,321,321,322]
print(plus_grand_chiffre_liste(liste))