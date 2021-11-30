import numpy as np
import random

Mat = np.load('Matrice_probas.npy')

alphabet = 'abcdefghijklmnopqrstuvwxyzàâéèêëîïôûüç \'-'

n = int(input('nombre de mots à créer : '))
Mots = []

for _ in range(n) :
    mot = ''
    i = 38 # = alphabet.index(' ')
    car = ''
    while car != ' ' :
        car = random.choices(alphabet, Mat[i])[0]
        mot += car
        i = alphabet.index(car)
    Mots.append(mot.replace(' ','\n'))

f = open(f'liste_{n}_mots.txt', 'w')
f.writelines(Mots)
f.close()