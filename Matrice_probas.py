# Soline

import numpy as np
import codecs

nom = input("nom du ficher avec chemin d'accès absolu : ")
# lecture du fichier
f = codecs.open(nom, 'r', 'utf-8')
texte = f.read()
f.close()

# on efface la ponctuation
for c in '?,.;:!()' :
    texte = texte.replace(c, '')

# on enlève les sauts de ligne et on baisse la casse
texte = texte.replace('\n', ' ')
texte = texte.lower()

# ch correspond à l'ordre des caractères dans la matrice de transition
# J'ai inclus l'apostrophe et le tiret (mots composés)
ch = 'abcdefghijklmnopqrstuvwxyzàâéèêëîïôûüç \'-'

# on crée une matrice de zéros
Mat = np.zeros((len(ch), len(ch)))

# on garde en note l'indice de la ligne (lettre initiale)
# puis on cherche l'indice de la colonne (lettre suivante)
# on implémente la matrice à la case ind_l, ind_c
# l'indice de la colonne devient celiu de la ligne
# (on considère maintenant cette lettre comme lettre initiale)
# au début, on met l'indice de la ligne sur espace pour compter le début du mot
# on fait de même à la fin pour compter la fin du mot
ind_l = ch.index(' ')
for i in range(len(texte)-1) :
    ind_c = ch.index(texte[i])
    Mat[ind_l][ind_c] += 1
    ind_l = ind_c
ind_c = ch.index(' ')
Mat[ind_l][ind_c] += 1

# maintenant que la matrice contient le nombre de transitions,
# on la ramène à une matrice stochastique en divisant chaque ligne par la somme des lignes
for i in range(len(ch)) :
    s = sum(Mat[i])
    if s != 0 :
        for j in range(len(ch)) :
            Mat[i][j] = Mat[i][j]/s