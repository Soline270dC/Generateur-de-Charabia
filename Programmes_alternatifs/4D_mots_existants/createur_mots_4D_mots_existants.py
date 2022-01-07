import numpy as np
import random
import codecs

# crée une liste de mots inventés de taille n (et l'écrit dans un fichier)
# prend en argument la matrice de transition 4D grpace à laquelle il construira les mots

def createur_mots_4D(n, Mat) : # O(max(n*len(ensemble_mots), n²))
    alphabet = 'abcdefghijklmnopqrstuvwxyzàâéèêëîïôûüç \'-'
    ind_esp = alphabet.index(' ')
    Mots = {''}
    for _ in range(n) : # O(n*(len(ensemble_mots) + n)) amorti
        # mot qui existe déjà dans ensemble_mot pour entrer dans la boucle
        mot = ''
        while mot.replace(' ','\n') in Mots : # test : O(len(ensemble_mot) + n)
            # le mot ne doit pas avoir déjà été créé : cela permet d'avoir exactement n mots inventés 
            mot = ''
            # on place les curseurs sur ' ' afin d'obtenir la première lettre
            x = y = z = ind_esp
            car = ''
            while car != ' ' : # O(1) (taille maximale des mots très faible)
                # marche aléatoire grâce à des probabilités pondérées (random.choices renvoie une liste de 1 élément)
                car = random.choices(alphabet, Mat[x][y][z])[0] # O(1)
                mot += car
                # après avoir ajouté le caractère, on décale les curseurs
                x = y
                y = z
                z = alphabet.index(car) # O(len(alphabet)) = O(1)
        Mots.add(mot.replace(' ','\n')) # O(len(mot)) = O(1) amorti
    
    f = codecs.open(f'liste_{n}_mots_4D.txt', 'w', 'utf-8')
    f.writelines(Mots)
    f.close()