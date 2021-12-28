import numpy as np
import random
import codecs

def creer_ensemble_mot(nom_fichier, mode = 'utf-8') :
    f = codecs.open(nom_fichier,'r', mode)
    str_mot = f.read()
    f.close()
    liste_mot = str_mot.split()
    liste_mot.append('')
    return set(liste_mot)

Mat = np.load(r'4D\Matrice_probas_4D_Miserables_tot.npy')
ensemble_mot = creer_ensemble_mot("ensemble_mots.txt")

def createur_mots_4D(n, Mat = Mat, ensemble_mot = ensemble_mot) :
    alphabet = 'abcdefghijklmnopqrstuvwxyzàâéèêëîïôûüç \'-'
    n = int(input('nombre de mots à créer : '))
    Mots = []
    for _ in range(n) :
        mot = 'chat '
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
        Mots.append(mot.replace(' ','\n'))
    f = codecs.open(f'4D\\liste_{n}_mots_4D.txt', 'w', 'utf-8')
    f.writelines(Mots)
    f.close()