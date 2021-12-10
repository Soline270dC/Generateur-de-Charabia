import numpy as np
import random

Mat = np.load('Matrice_probas_4D.npy')

alphabet = 'abcdefghijklmnopqrstuvwxyzàâéèêëîïôûüç \'-'

n = int(input('nombre de mots à créer : '))
Mots = []

for _ in range(n) :
    mot = ''
    x = y = z = 38 # = alphabet.index(' ')
    car = ''
    while car != ' ' :
        car = random.choices(alphabet, Mat[x][y][z])[0]
        mot += car
        x = y
        y = z
        z = alphabet.index(car)
    Mots.append(mot.replace(' ','\n'))

f = open(f'liste_{n}_mots_4D.txt', 'w')
f.writelines(Mots)
f.close()