import codecs
import random
import re

# lise de mots
def liste_mots_triee(nom_fichier, mode = 'ANSI') :
    f = codecs.open(nom_fichier, 'r', mode)
    str_mots = f.read()
    f.close()
    liste_mots = str_mots.split()
    liste_mots_triee = [[] for _ in range(26)]
    for mot in liste_mots :
        liste_mots_triee[len(mot)].append(mot)
    return liste_mots_triee

nom = input('nom de la liste de mots : ')
Liste_mots = liste_mots_triee(nom)

# texte (pas trop long siouplé)
fich = input('nom du fichier textuel : ')
f = codecs.open(fich, 'r', 'utf-8')
texte = f.read()
f.close()

# choix 1 : mots au hasard
def generateur_charabia_hasard(texte, Liste_mots, long_min = 5, long_max = 14) :
    sep = -1
    for i in range(len(texte)) :
        if texte[i] in [' ','"','(',')',',','?',';','.',':','!','_','»','«'] :
            long = i - (sep+1)
            if long >= long_min and long <= long_max:
                if Liste_mots[long] != [] :
                    n_nom = random.choice(Liste_mots[long])
                    texte = texte[:sep+1] + n_nom + texte[i:]
            sep = i
    return texte

# choix 2 : prmeière lettre identique et même nombre de lettres (possiblement inutile)

# choix 3 : distance d'édition la plus courte