# entrée : liste de mots (longue) et texte
# programme : parcourir la litse de mots pour leur trouver des potes
# sortie : texte charabié
# fréquence : tous les mots au dessus de 5 lettres ?
# choix du mot :    - un au pif du même nombre de lettres
#                   - même première lettre et même longueur
#                   - distance d'édition (/!\ complexité en temps)
# choix utilisateur : 2D/3D/4D - choix du mot - longueur de modification - toutes occurences/mot par mot
# essayer de se débrouiller pour la ponctuation

import codecs
import random

# lise de mots
nom = input('nom de la liste de mots : ')
f = codecs.open(nom, 'r', 'ANSI')
str_mots = f.read()
f.close()
liste_mots = str_mots.split()

# listes de mots par nombre de lettres :
Liste_mots = [[] for _ in range(26)]
for mot in liste_mots :
    Liste_mots[len(mot)].append(mot)

# texte (pas trop long siouplé)
#fich = input('nom du fichier textuel : ')
#f = codecs.open(fich, 'r', 'utf-8')
#texte = f.read()
#f.close()
texte = 'Tout est au mieux dans le meilleur des mondes, et je bois du chocolat chaud.'

# choix 1 : mots au hasard
sep = -1
for i in range(len(texte)) :
    if texte[i] in [' ','"','(',')',',','?',';','.',':','!','_','»','«'] :
        long = i - (sep+1)
        if long >= 5 and long < 15:
            if Liste_mots[long] != [] :
                n_nom = random.choice(Liste_mots[long])
                texte = texte[:sep+1] + n_nom + texte[i:]
        sep = i

print(texte)