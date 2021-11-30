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

alphabet = 'abcdefghijklmnopqrstuvwxyzàâéèêëîïôûüç \'-'

Mat = np.zeros((len(alphabet), len(alphabet)))
List_occ = [0]*len(alphabet)

# création de matrice et remplissage des occurences
ind_l = 38 # = alphabet.index(' ')
for i in range(len(texte)-1) :
    car = texte[i]
    if car in alphabet :
        ind_c = alphabet.index(car)
        Mat[ind_l][ind_c] += 1
        List_occ[ind_c] += 1
        ind_l = ind_c
ind_c = 38
Mat[ind_l][ind_c] += 1

# normalisation
for i in range(len(alphabet)) :
    if List_occ[i] != 0 :
        Mat[i] = Mat[i]/List_occ[i]

np.save('Matrice_probas-2', Mat)