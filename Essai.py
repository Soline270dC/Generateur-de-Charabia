# Gérer les caractères spéciaux et la ponctuation
contenu = "En 1815, M. Charles-François-Bienvenu Myriel était évêque de Digne. C'était un vieillard d'environ soixante-quinze ans; il occupait le siège de Digne depuis 1806"
contenu = contenu.lower()
A_enlever = ["c'","l'","d'","-",",",".",";","?","!"]
for i in range(len(contenu)) :
    if contenu[i] in A_enlever:
        contenu = contenu[:i]+ " " + contenu[i+1:]
    
print(contenu)



contenu = "bcefa fg ad"

# Générer la matrice de transition
import numpy as np
matrice = np.array(9*[8*[0]])
print(matrice)

correspondance = {"a":0,"b":1,"c":2,"d":3,"e":4,"f":5,"g":6," ": 7}


for i in range(len(contenu)-1):
    matrice[correspondance[contenu[i]]][correspondance[contenu[i+1]]]+=1
    # on va faire un compteur d'occurrences de chaque lettre
    matrice[correspondance[contenu[i]]][8] +=1

print(matrice)

for i in range(9):
    occ = matrice[i][9]
    for j in range(8):
        matrice[i][j] / occ
print(matrice)


    





