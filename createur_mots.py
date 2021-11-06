# on essaye de se débrouiller pour ramener la matrice de probabilités Mat

import numpy as np
import random

ch = 'abcdefghijklmnopqrstuvwxyzàâéèêëîïôûüç \'-'
Mat = np.zeros((len(ch), len(ch)))
#Mat = np.array([0.5/8]*8 + [0.5])

#k = random.choices('abcdefghi', Mat)
#print(k[0])

n = int(input('nombre de mots : '))
L = []
for _ in range(n) :
    mot = ''
    i = ch.index(' ')
    car = ''
    while car != ' ' :
        car = random.choices(ch, Mat[i])[0]
        mot += car
        i = ch.index(car)
    L.append(mot)

f = open(f'{n}_mots_nouveaux.txt', 'w')
f.writelines(L)
f.close