# on essaye de se débrouiller pour ramener la matrice de probabilités Mat

import numpy as np
import random

ch = 'abcdefghijklmnopqrstuvwxyzàâéèêëîïôûüç \'-'

# on récupère la matrice
Mat = np.load('Matrice_probas.npy')

n = int(input('nombre de mots : '))
L = []
for _ in range(n) :
    mot = ''
    i = ch.index(' ')
    car = ''
    while car != ' ' : # on s'arrête quand on arrive à la fin d'un mot (signalé par ' ')
        car = random.choices(ch, Mat[i])[0] # random.choices renvoie une liste de 1 élément
        mot += car
        i = ch.index(car)
    L.append(mot.replace(' ','\n')) # on remplace l'espace final par un passage à la ligne

f = open(f'{n}_mots_nouveaux.txt', 'w')
f.writelines(L)
f.close