import numpy as np
import random
import codecs

Mat = np.load(r'2D\Matrice_probas-2.npy')

f = codecs.open('ensemble_mots.txt','r', 'utf-8')
str_mot = f.read()
f.close()

liste_mot = str_mot.split()
liste_mot.append('')
ensemble_mot = set(liste_mot)

alphabet = 'abcdefghijklmnopqrstuvwxyzàâéèêëîïôûüç \'-'

n = int(input('nombre de mots à créer : '))
Mots = []
Mots2 = []

for _ in range(n) :
    mot = 'chat '
    while mot[:-1] in ensemble_mot :
        mot = ''
        i = 38 # = alphabet.index(' ')
        car = ''
        while car != ' ' :
            car = random.choices(alphabet, Mat[i])[0]
            mot += car
            i = alphabet.index(car)
    Mots.append(mot.replace(' ','\n'))

print(str(Mots2))
print('de' in ensemble_mot)

f = open(f'liste_{n}_mots_2D.txt', 'w')
f.writelines(Mots)
f.close()