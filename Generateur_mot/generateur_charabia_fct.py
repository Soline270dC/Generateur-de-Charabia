import codecs
import random
import re

# lise de mots
def liste_mots_triee(nom_fichier, mode = 'utf-8') :
    f = codecs.open(nom_fichier, 'r', mode)
    str_mots = f.read()
    f.close()
    liste_mots = str_mots.split()
    liste_mots_triee = [[] for _ in range(26)]
    for mot in liste_mots :
        if len(mot) < 26 :
            liste_mots_triee[len(mot)].append(mot)
    return liste_mots_triee

def liste_mots(nom_fichier, mode = 'utf-8') :
    f = codecs.open(nom_fichier, 'r', mode)
    str_mots = f.read()
    f.close()
    liste_mots = str_mots.split()
    return liste_mots

#nom = input('nom de la liste de mots : ')
nom = r'4D\liste_5000_mots_4D.txt'
set_mots = set(liste_mots(nom))
#Liste_mots_triee = liste_mots_triee(nom)

# texte (pas trop long siouplé)
#fich = input('nom du fichier textuel : ')
fich = r'Generateur_mot\fichier_textuel.txt'
f = codecs.open(fich, 'r', 'utf-8')
texte = f.read()
f.close()

# choix 1 : mots au hasard
def generateur_charabia_hasard(texte, Liste_mots_triee, long_min = 5, long_max = 14) :
    sep = -1
    for i in range(len(texte)) :
        if texte[i] in [' ','"','(',')',',','?',';','.',':','!','_','»','«'] :
            long = i - (sep+1)
            if long >= long_min and long <= long_max:
                if Liste_mots_triee[long] != [] :
                    texte = texte[:sep+1] + random.choice(Liste_mots_triee[long]) + texte[i:]
            sep = i
    return texte

# choix 2 : prmeière lettre identique et même nombre de lettres (possiblement inutile)

# choix 3 : distance d'édition la plus courte
from distance_levenshtein import liste_d_l_min

def generateur_charabia_levenshtein(texte, Liste_mots, long_min = 5, long_max = 14) :
    sep = -1
    n_texte = ''
    for i in range(len(texte)) :
        if texte[i] in [' ','"','(',')',',','?',';','.',':','!','_','»','«'] :
            long = i - (sep+1)
            if long >= long_min and long <= long_max:
                n_texte += random.choice(liste_d_l_min(texte[sep+1:i], Liste_mots)) + texte[i]
            else :
                n_texte += texte[sep+1:i+1]
            sep = i
    return n_texte

print(generateur_charabia_levenshtein(texte, set_mots))