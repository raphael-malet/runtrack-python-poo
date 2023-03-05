def longueur_chaine_de_caractere(chaine,x):
    chaine_longueur = chaine[0:-1]
    if chaine_longueur =='':
        print(x)
    else:
        x += 1
        return longueur_chaine_de_caractere(chaine_longueur, x)

chaine = input('Entrer une chaine de caractère :\n')
longueur_chaine_de_caractere(chaine,1)