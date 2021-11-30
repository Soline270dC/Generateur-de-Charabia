import numpy as np

Mat = np.load('Matrice_probas.npy')

alphabet = 'abcdefghijklmnopqrstuvwxyzàâéèêëîïôûüç \'-'

n = int(input('nombre de mots à créer : '))
Mots = []

for _ in range(n) :
    mot = ''
    i = 38 # = alphabet.index(' ')
    car = ''
    