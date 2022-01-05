import numpy as np
import codecs

nom = input('nom du fichier + extension : ')
f = codecs.open(nom, 'r', 'utf-8') # utf-8 à adapter en fonction du document
texte = f.read()
f.close()

for c in ['"','(',')',',','?',';','.',':','!','--','_','»','«'] :
    texte = texte.replace(c,'')

for c in ' \t\n' :
    texte = texte.replace(c, '  ')

texte = texte.lower()

alphabet = 'abcdefghijklmnopqrstuvwxyzàâéèêëîïôûüç \'-'

Mat = np.zeros((len(alphabet), len(alphabet), len(alphabet)))
List_occ = np.zeros((len(alphabet), len(alphabet)))

# création de matrice et remplissage des occurences
x = y = 38 # = alphabet.index(' ')
for i in range(len(texte)) :
    car = texte[i]
    if car in alphabet :
        z = alphabet.index(car)
        Mat[x][y][z] += 1
        List_occ[x][y] += 1
        x = y
        y = z
z = 38
Mat[x][y][z] += 1

# normalisation
for i in range(len(alphabet)) :
    for j in range(len(alphabet)) :
        if List_occ[i][j] != 0 :
            Mat[i][j] = Mat[i][j]/List_occ[i][j]

np.save(r'3D\Matrice_probas_3D_liste', Mat)