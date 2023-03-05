
def factorielle(x):
    if x == 0:
        return 1
    else:
       return x*factorielle(x-1)

x = input('Entrer nombre entier :')
x = int(x)
print(factorielle(x))


