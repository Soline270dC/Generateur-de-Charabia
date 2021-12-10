import numpy as np
import random

Mat = np.load('Matrice_probas_3D.npy')

alphabet = 'abcdefghijklmnopqrstuvwxyzàâéèêëîïôûüç \'-'

n = int(input('nombre de mots à créer : '))
Mots = []

for _ in range(n) :
    mot = ''
    x = y = 38 # = alphabet.index(' ')
    car = ''
    while car != ' ' :
        car = random.choices(alphabet, Mat[x][y])[0]
        mot += car
        x = y
        y = alphabet.index(car)
    Mots.append(mot.replace(' ','\n'))

f = open(f'liste_{n}_mots_3D.txt', 'w')
f.writelines(Mots)
f.close()