# Soline

import numpy as np
import codecs

nom = input("nom du ficher avec chemin d'accès absolu : ")

f = codecs.open(nom, 'r', 'utf-8')
texte = f.read()
f.close()

for c in '?,.;:!()-' :
    texte = texte.remove(c)

texte = texte.replace('\n', ' ')

ch = 'abcdefghijklmnopqrstuvwxyzàâéèêëîïôûü \'-'

Mat = np.zeros((len(ch), len(ch)))

ind_l = ch.index(' ')
for i in range(len(texte)-1) :
    ind_c = ch.index(texte[i])
    Mat[ind_l][ind_c] += 1
    ind_l = ind_c
ind_c = ch.index(' ')
Mat[ind_l][ind_c] += 1

for i in range(len(ch)) :
    s = sum(Mat[i])
    for j in range(len(ch)) :
        Mat[i][j] = Mat[i][j]/s