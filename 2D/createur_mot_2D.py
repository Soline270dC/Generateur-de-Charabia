import numpy as np
import random

# Importation de la matrice de probabilté de la base de donnée choisi nous permettant de générer des mots nouveaux
Mat = np.load('Matrice_probas-2.npy')

alphabet = 'abcdefghijklmnopqrstuvwxyzàâéèêëîïôûüç \'-'

n = int(input('nombre de mots à créer : '))
Mots = []

# Implémentation du générateur de nouveaux mots
for _ in range(n) :
    mot = ''
    i = 38 # Initialisation au caractère "espace" pour la première lettre (= alphabet.index(' '))
    car = ''
    while car != ' ' :
        car = random.choices(alphabet, Mat[i])[0]
        mot += car
        i = alphabet.index(car)
    Mots.append(mot.replace(' ','\n'))

#Création d'un fichier contenant la liste de mot généré
f = open(f'liste_{n}_mots_2D.txt', 'w')
f.writelines(Mots)
f.close()