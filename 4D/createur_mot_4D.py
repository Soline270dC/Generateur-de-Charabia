import numpy as np
import random

# Importation de la matrice de probabilité de la base de donnée choisi nous permettant de générer des nouveaux mots
Mat = np.load('Matrice_probas_4D_Miserables_tot.npy')

alphabet = 'abcdefghijklmnopqrstuvwxyzàâéèêëîïôûüç \'-'

n = int(input('nombre de mots à créer : '))
Mots = []

# Implémentation du générateur de mot
for _ in range(n) :
    mot = ''
    x = y = z = 38 # On initialise au caractère "espace" pour la première lettre (= alphabet.index(' '))
    car = ''
    while car != ' ' :
        car = random.choices(alphabet, Mat[x][y][z])[0]
        mot += car
        x = y
        y = z
        z = alphabet.index(car)
    Mots.append(mot.replace(' ','\n'))

# Création d'un fichier contenant la liste de mot généré
f = open(f'liste_{n}_mots_4D.txt', 'w')
f.writelines(Mots)
f.close()