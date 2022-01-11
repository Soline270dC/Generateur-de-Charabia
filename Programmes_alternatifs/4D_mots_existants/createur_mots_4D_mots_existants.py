import numpy as np
import random
import codecs

# crée une liste de mots inventés de taille n (et l'écrit dans un fichier)
# prend en argument la matrice de transition 4D grpace à laquelle il construira les mots

def createur_mots_4D(n, Mat) :
    alphabet = 'abcdefghijklmnopqrstuvwxyzàâéèêëîïôûüç \'-'
    ind_esp = alphabet.index(' ')
    Mots = set()
    i = 0
    while i < n :
        mot = ''
        # on place les curseurs sur ' ' afin d'obtenir la première lettre
        x = y = z = ind_esp
        car = ''
        while car != ' ' :
            # marche aléatoire grâce à des probabilités pondérées (random.choices renvoie une liste de 1 élément)
            car = random.choices(alphabet, Mat[x][y][z])[0] # O(1)
            mot += car
            # après avoir ajouté le caractère, on décale les curseurs
            x = y
            y = z
            z = alphabet.index(car)
        mot = mot.replace(' ','\n')
        # le mot ne doit ni être français, ni avoir déjà été créé : cela permet d'avoir exactement n mots inventés 
        if not  mot in Mots :
            Mots.add(mot)
            i += 1
    f = codecs.open(f'liste_{n}_mots_4D.txt', 'w', 'utf-8')
    f.writelines(Mots)
    f.close()