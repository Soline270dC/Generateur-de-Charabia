import os
os.chdir(r"C:\Users\Aurelie\Desktop\Generateur-de-Charabia")

import codecs
fichier = codecs.open("Les miserables 1.txt","r","utf-8")
contenu = fichier.read()
fichier.close()

# contenu = "Formes que prend la souffrance pendant le sommeil\nTrois heures du matin venaient de sonner, et il y avait cinq heures
# qu'il marchait ainsi, presque sans interruption lorsqu'il se laissa
# tomber sur sa chaise.

# Il s'y endormit et fit un rêve."
print(contenu)

# ## Gérer les caractères spéciaux
# for carac in contenu :
#     if carac == "Ã©" :
#         contenu.replace(carac, "é")
# print(contenu)

# ## Générer la matrice de transition
# import numpy as np
# matrice = np.array(26*[26*[0]])
# print(matrice)

# for i in range(len(contenu)) :
#     matrice[i]

