import numpy as np
import codecs

nom = input('nom du fichier + extension : ')
f = codecs.open(nom, 'r', 'utf-8') # utf-8 à adapter en fonction du document
texte = f.read()
f.close()

# fonction 'propre' (cf origin/Aurelie)
for c in '"(),?;.:!' : # cas des apostrophes à aviser ("c'", "l'", "d'")
    texte = texte.replace(c,'')

for c in '\t\n' :
    texte = texte.replace(c, ' ')

texte = texte.lower()

ch = 'abcdefghijklmnopqrstuvwxyzàâéèêëîïôûüç \'-'

Mat = np.zeros((len(ch), len(ch)))
List_occ = [0]*len(ch)

# création de matrice et remplissage des occurences
ind_l = 38 # = ch.index(' ')
for i in range(len(texte)-1) :
    ind_c = ch.index(texte[i])
    Mat[ind_l][ind_c] += 1
    List_occ[ind_c] += 1
    ind_l = ind_c
ind_c = 38
Mat[ind_l][ind_c] += 1

# normalisation
for i in range(len(ch)) :
    if List_occ[i] != 0 :
        Mat[i] = Mat[i]/List_occ[i]

np.save('Matrice_probas', Mat)