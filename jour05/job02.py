def fonction(x):
    n = input('Entrer nombre entier')
    if not n.isdigit():
        return fonction(x)
    else:
        n = int(n)
        print(x**n)


fonction(10)