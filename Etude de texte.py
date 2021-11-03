# import os
# os.chdir(r"C:\Users\Aurelie\Desktop\Generateur-de-Charabia")

# import codecs
# fichier = codecs.open("Les miserables 1.txt","r","utf-8")
# contenu = fichier.read()
# fichier.close()

# Gérer les caractères spéciaux et la ponctuation sur un exemple (copié collé depuis fichier epub)
contenu = "En 1815, M. Charles-François-Bienvenu Myriel était évêque de Digne. C'était un vieillard d'environ soixante-quinze ans; il occupait le siège de Digne depuis 1806"
contenu = contenu.lower()  # J'ai vérifié : les chiffres ne posent pas pb qd on fait lower
A_enlever = ["c'","l'","d'","-",",",".",";","?","!"]
for i in range(len(contenu)) :
    if contenu[i] in A_enlever:
        contenu = contenu[:i]+ " " + contenu[i+1:]
print(contenu)


# contenu = "abcbd hdfh "


# Générer la matrice de transition
import numpy as np
matrice = np.float_(33*[34*[0]])

correspondance = {"a":0,"b":1,"c":2,"d":3,"e":4,"f":5,"g":6,"h":7,"i":8,"j":9,"k":10,"l":11,"m":12,"n":13,"o":14,"p":15,"q":16,"r":17,"s":18,"t":19,"u":20,"v":21,"w":22,"x":23,"y":24,"z":25,"é":26,"è":27,"ê":28,"ù":29,"à":30,"î":31," ":32}


for i in range(1,len(contenu)):
    if contenu[i-1] in correspondance and contenu[i] in correspondance :
        matrice[correspondance[contenu[i-1]]][correspondance[contenu[i]]]+=1
        # on va faire un compteur d'occurrences de chaque lettre
        matrice[correspondance[contenu[i-1]]][8] +=1

print(matrice)

for i in range(33):
    occ = matrice[i][33]
    if occ !=0 :
        for j in range(33):
            matrice[i][j] = float(matrice[i][j]) / float(occ)
print(str(matrice))

import os
os.chdir(r"C:\Users\Aurelie\Desktop\Generateur-de-Charabia")
fichier = open("matrice.txt","w")
fichier.write(str(matrice))
fichier.close()