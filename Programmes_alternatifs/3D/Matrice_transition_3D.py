import numpy as np
import codecs

# Choisir la base de données parmi celles disponibles dans le dossier "Base de données"
nom = input('Veuillez noter le nom du fichier avec extension : ')
f = codecs.open(nom, 'r', 'utf-8')
texte = f.read()
f.close()

# Suppression de la ponctuation et de quelques caractères spéciaux
for c in ['"','(',')',',','?',';','.',':','!','--','_','»','«'] :
    texte = texte.replace(c,'')

for c in ' \t\n' :
    texte = texte.replace(c, '  ')

texte = texte.lower()

alphabet = 'abcdefghijklmnopqrstuvwxyzàâéèêëîïôûüç \'-'

Mat = np.zeros((len(alphabet), len(alphabet), len(alphabet)))
List_occ = np.zeros((len(alphabet), len(alphabet)))

# Création de la matrice de probabilité et comptage des occurences
x = y = 38 # = alphabet.index(' ') (on se place sur un espace)
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

# On procède à la normalisation de la matrice
for i in range(len(alphabet)) :
    for j in range(len(alphabet)) :
        if List_occ[i][j] != 0 :
            Mat[i][j] = Mat[i][j]/List_occ[i][j]

np.save(r'Programmes_alternatifs\3D\Matrice_probas_3D_liste', Mat)