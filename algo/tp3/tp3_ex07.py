# Créé par florentin.trotin, le 11/10/2022 en Python 3.7

def table(operande,valmin,valmax):
    for n in range(valmin,valmax+1):
        print(operande,"*",n,"=",n*operande)
table(5,0,10)