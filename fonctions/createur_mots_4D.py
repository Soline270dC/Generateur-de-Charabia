import numpy as np
import random
import codecs

# crée un ensemble de mots à partir d'un fichier (permet d'éviter les doublons)
def creer_ensemble_mot(nom_fichier, mode = 'utf-8') : # O(len(E)) en moyenne
    f = codecs.open(nom_fichier,'r', mode)
    E = eval(f.read()) # O(len(E))
    f.close()
    # on ajoute le mot vide pour qu'il ne soit pas créé
    E.add('') # O(1) en moyenne
    return E

# crée une liste de mots inventés de taille n (et l'écrit dans un fichier)
# prend en argument la matrice de transition 4D grpace à laquelle il construira les mots
# ainsi que l'ensemble de mots français pour ne pas créer de mots existants
def createur_mots_4D(n, Mat, ensemble_mots_existants) : # O(max(n*len(ensemble_mots), n²))
    alphabet = 'abcdefghijklmnopqrstuvwxyzàâéèêëîïôûüç \'-'
    ind_esp = alphabet.index(' ')
    Mots = set()
    i = 0
    while i < n :# O(n*(len(ensemble_mots) + n))
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
        mot = mot.replace(' ','\n')
        
        # le mot ne doit ni être français, ni avoir déjà été créé : cela permet d'avoir exactement n mots inventés. 
        # De plus, on choisit de ne garder que les mots de longueur inférieure ou égale à 30 (dans les générateurs 
        # de charabia utilisés ensuite, on ne remplacera en effet que les mots de longueur comprise en 5 et 20)
        if not (mot[:-1] in ensemble_mots_existants or mot in Mots) and len(mot[:-1]) <= 30 : # test : O(len(ensemble_mot) + n)
            Mots.add(mot) # O(1) en moyenne
            i += 1
    
    f = codecs.open(f'liste_{n}_mots_inventes_4D.txt', 'w', 'utf-8')
    f.writelines(Mots)
    f.close()