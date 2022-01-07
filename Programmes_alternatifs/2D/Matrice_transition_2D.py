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

for c in '\t\n' :
    texte = texte.replace(c, ' ')

texte = texte.lower()

alphabet = 'abcdefghijklmnopqrstuvwxyzàâéèêëîïôûüç \'-'

Mat = np.zeros((len(alphabet), len(alphabet)))
List_occ = np.zeros(len(alphabet))

# Création de la matrice de probabilité et comptage des occurences
x = 38 # Au départ on se place sur un caractère "espace" pour la première lettre (= alphabet.index(' '))
for i in range(len(texte)) :
    car = texte[i]
    if car in alphabet :
        y = alphabet.index(car)
        Mat[x][y] += 1
        List_occ[x] += 1
        x = y
y = 38
Mat[x][y] += 1

# On procède à la normalisation de la matrice
for i in range(len(alphabet)) :
    if List_occ[i] != 0 :
        Mat[i] = Mat[i]/List_occ[i]

np.save(r'Programmes_alternatifs\2D\Matrice_probas_2D_liste', Mat)