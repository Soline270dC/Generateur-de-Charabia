import numpy as np
import random
import codecs

Mat = np.load(r'2D\Matrice_probas_2D_liste_mots.npy')

f = codecs.open('ensemble_mots_français.txt','r', 'utf-8')
str_mot = f.read()
f.close()

liste_mot = str_mot.split()
liste_mot.append('')
ensemble_mot = set(liste_mot)

alphabet = 'abcdefghijklmnopqrstuvwxyzàâéèêëîïôûüç \'-'

n = int(input('nombre de mots à créer : '))
Mots = set()

for _ in range(n) :
    mot = ''
    while mot[:-1] in ensemble_mot and mot.replace(' ','\n') in Mots:
        mot = ''
        i = 38 # = alphabet.index(' ')
        car = ''
        while car != ' ' :
            car = random.choices(alphabet, Mat[i])[0]
            mot += car
            i = alphabet.index(car)
    Mots.add(mot.replace(' ','\n'))

f = codecs.open(f'2D\\liste_{n}_mots_2D.txt', 'w', 'utf-8')
f.writelines(list(Mots))
f.close()