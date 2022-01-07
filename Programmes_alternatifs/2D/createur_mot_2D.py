import numpy as np
import random
import codecs

f = codecs.open('ensemble_1.txt','r', 'utf-8')
ensemble_mot = eval(f.read())
f.close()
ensemble_mot.add('')

# Importation de la matrice de probabilté de la base de donnée choisi nous permettant de générer des mots nouveaux
Mat = np.load(r'Programmes_alternatifs\2D\Matrice_probas_2D_Miserables_1.npy')

alphabet = 'abcdefghijklmnopqrstuvwxyzàâéèêëîïôûüç \'-'

n = int(input('nombre de mots à créer : '))
Mots = set()
ind_esp = alphabet.index(' ')

# Implémentation du générateur de nouveaux mots
i = 0
while i < n :
    mot = ''
    x = ind_esp # Initialisation au caractère "espace" pour la première lettre
    car = ''
    while car != ' ' :
        car = random.choices(alphabet, Mat[x])[0]
        mot += car
        x = alphabet.index(car)
    mot = mot.replace(' ','\n')
    if mot not in Mots and mot[:-1] not in ensemble_mot :
        Mots.add(mot)
        i += 1

#Création d'un fichier contenant la liste de mot généré
f = codecs.open(f'liste_{n}_mots_2D.txt', 'w', 'utf-8')
f.writelines(Mots)
f.close()