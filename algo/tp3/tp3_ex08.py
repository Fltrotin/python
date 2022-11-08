# Créé par florentin.trotin, le 08/11/2022 en Python 3.7
def rectangle (hauteur, largeur):
    for i in range(1,hauteur+1):
        for l in range(1,largeur+1):
            print("*", end="")
        print()

rectangle(6,5)
