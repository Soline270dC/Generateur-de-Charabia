import numpy as np
import random
import codecs

f = codecs.open('ensemble_mots_français.txt','r', 'utf-8')
str_mot = f.read()
f.close()

liste_mot = str_mot.split()
liste_mot.append('')
ensemble_mot = set(liste_mot)

Mat = np.load(r'3D\Matrice_probas_3D_Miserables_1.npy')

alphabet = 'abcdefghijklmnopqrstuvwxyzàâéèêëîïôûüç \'-'

n = int(input('nombre de mots à créer : '))
Mots = set()

for _ in range(n) :
    mot = ''
    while mot[:-1] in ensemble_mot or mot.replace(' ','\n') in Mots:
        mot = ''
        x = y = 38 # = alphabet.index(' ')
        car = ''
        while car != ' ' :
            car = random.choices(alphabet, Mat[x][y])[0]
            mot += car
            x = y
            y = alphabet.index(car)
    Mots.add(mot.replace(' ','\n'))

f = codecs.open(f'3D\\liste_{n}_mots_3D_Miserables.txt', 'w', 'utf-8')
f.writelines(list(Mots))
f.close()