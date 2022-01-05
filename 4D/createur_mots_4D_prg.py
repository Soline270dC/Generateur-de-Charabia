import numpy as np
import random
import codecs

f = codecs.open('ensemble_mots_français.txt','r', 'utf-8')
str_mot = f.read()
f.close()

liste_mot = str_mot.split()
liste_mot.append('')
ensemble_mot = set(liste_mot)

Mat = np.load(r'4D\Matrice_probas_4D.npy')

alphabet = 'abcdefghijklmnopqrstuvwxyzàâéèêëîïôûüç \'-'

n = int(input('nombre de mots à créer : '))
Mots = set()

for _ in range(n) :
    mot = ''
    while mot[:-1] in ensemble_mot :
        mot = ''
        x = y = z = 38 # = alphabet.index(' ')
        car = ''
        while car != ' ' :
            car = random.choices(alphabet, Mat[x][y][z])[0]
            mot += car
            x = y
            y = z
            z = alphabet.index(car)
    Mots.add(mot.replace(' ','\n'))

f = codecs.open(f'4D\\liste_{n}_mots_4D.txt', 'w', 'utf-8')
f.writelines(Mots)
f.close()