import codecs
import random

# Pour le générateur de charabia en lui-même, on propose deux possibilités à l'utilisateur : chaque mot de longueur >= 5 et <= 14 
# - choix 1 : est remplacé au hasard par un mot inventé de même longueur
# - choix 2 : est remplacé par un mot pas forcément de même longueur mais proche en termes de distance de Leveshtein : pour chaque mot à remplacer, on cherche les mots créés les plus proches et on en prend un aléatoirement (cf. fonction définie plus bas)

# Dans les deux cas, il faut commencer par générer une liste de mots créés à partir de la matrice de transition. Nous avons essayé successivement avec des listes de 100, 1000 et 5000 mots.

# cette fonction premet de lire une liste de mots dans un fichier et de la renvoyer sous la forme d'une list Python 
def liste_mots(nom_fichier_textuel, mode = 'utf-8') :
    f = codecs.open(nom_fichier_textuel, 'r', mode)
    str_mots = f.read()
    f.close()
    liste_mots = str_mots.split()  # C'est ici qu'on transforme le texte en list. 
    return liste_mots

# choix 2 : distance d'édition la plus courte
from fonctions.distance_levenshtein import liste_d_l_min 
#la fonction liste_d_l_min prend en argument une chaîne de caractères ch1 et une liste de chaînes de caractères, et renvoie une liste composée des chaînes issues de la liste telle que la distance de Levenshtein entre ces mots et ch1 soit minimale. 

def generateur_charabia_levenshtein(texte, Liste_mots, long_min = 5, long_max = 14) : # O(len(texte)*len(Liste_mots))
    #le fonctionnement de cette fonction est similaire à celle dans le cas du générateur-choix1
    sep = -1
    n_texte = ''
    dico = {}
    for i in range(len(texte)) : # O(len(texte)*len(Liste_mots))
        if texte[i] in [' ','"','(',')',',','?',';','.',':','!','_','»','«', '\n'] :
            long = i - (sep+1)
            if long >= long_min and long <= long_max : # environ 1/10 occurences
                if texte[sep+1:i] not in dico :
                    dico[texte[sep+1:i]] = liste_d_l_min(texte[sep+1:i], Liste_mots)              
                n_nom = random.choice(dico[texte[sep+1:i]]) # O(len(Liste_mots)*long*len_moyenne(mots in Liste_mots)) = O(len(Liste_mots)) car len_moyenne(mots in Liste_mots) = O(1) en pratique
                if texte[sep+1].upper() == texte[sep+1] :
                    n_texte += n_nom[0].upper() + n_nom[1:] + texte[i]
                else :
                    n_texte += n_nom + texte[i]
            else :
                n_texte += texte[sep+1:i+1]
            sep = i
    return n_texte