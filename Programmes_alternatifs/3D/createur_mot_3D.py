import numpy as np
import random
import codecs

f = codecs.open('ensemble_1.txt','r', 'utf-8')
ensemble_mot = eval(f.read())
f.close()
ensemble_mot.add('')

Mat = np.load(r'Programmes_alternatifs\3D\Matrice_probas_3D_Miserables_1.npy')

alphabet = 'abcdefghijklmnopqrstuvwxyzàâéèêëîïôûüç \'-'

n = int(input('nombre de mots à créer : '))
Mots = set()
ind_esp = alphabet.index(' ')

# Implémentation du générateur de nouveaux mots
i = 0
while i < n :
    mot = ''
    x = y = ind_esp
    car = ''
    while car != ' ' :
        car = random.choices(alphabet, Mat[x][y])[0]
        mot += car
        x = y
        y = alphabet.index(car)
    mot = mot.replace(' ','\n')
    if mot not in Mots and mot[:-1] not in ensemble_mot :
        Mots.add(mot)
        i += 1

f = codecs.open(f'Programmes_alternatifs\\3D\\liste_{n}_mots_3D_Miserables_.txt', 'w', 'utf-8')
f.writelines(list(Mots))
f.close()