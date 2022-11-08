# Créé par florentin.trotin, le 08/11/2022 en Python 3.7
def triangle (hauteur):
    for i in range(1,hauteur+2):
        for l in range(1,i):
            print("*", end="")
        print()

triangle(10)
