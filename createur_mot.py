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
    while car != ' ' : # on s'arrête quand on arrive à la fin d'un mot (signalé par ' ')
        car = random.choices(alphabet, Mat[i])[0] # random.choices renvoie une liste de 1 élément
        mot += car
        i = alphabet.index(car)
    Mots.append(mot.replace(' ','\n')) # on remplace l'espace final par un passage à la ligne

f = open(f'liste_{n}_mots.txt', 'w')
f.writelines(Mots)
f.close()