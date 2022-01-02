import codecs
import random

# Pour le générateur de charabia en lui-même, on propose deux possibilités à l'utilisateur : chaque mot de longueur >= 5 et <= 14 
# - choix 1 : est remplacé au hasard par un mot inventé de même longueur
# - choix 2 : est remplacé par un mot pas forcément de même longueur mais proche en termes de distance de Leveshtein : pour chaque mot à remplacer, on cherche les mots créés les plus proches et on en prend un aléatoirement (cf. fonction définie plus bas)

# Dans les deux cas, il faut commencer par générer une liste de mots créés à partir de la matrice de transition. Nous avons essayé successivement avec des listes de 100, 1000 et 5000 mots.

# On propose à l'utilisateur de rentrer le texte à modifier dans un fichier .txt. La fonction suivante permet de lire ce fichier et d'en faire une liste de chaînes de caractères, chacune correspondant à un mot. 
def liste_mots(nom_fichier_textuel, mode = 'utf-8') :
    f = codecs.open(nom_fichier_textuel, 'r', mode)
    str_mots = f.read()
    f.close()
    liste_mots = str_mots.split()  # C'est ici qu'on sépare le texte en mots. 
    return liste_mots

#nom = input('nom de la liste de mots : ')
nom = r'4D\liste_5000_mots_4D.txt'
set_mots = set(liste_mots(nom))  # Pour améliorer la complexité de recherche dans la liste de mots inventés, on la transforme en set


# texte 
#fich = input('nom du fichier textuel : ')
fichier_textuel = r'Generateur_mot\fichier_textuel_2.txt'
fichier_textuel = codecs.open(fich, 'r', 'utf-8')
texte = fichier_textuel.read()
fichier_textuel.close()


# choix 2 : distance d'édition la plus courte
from distance_levenshtein import liste_d_l_min 
#la fonction liste_d_l_min prend en argument une chaîne de caractères ch1 et une liste de chaînes de caractères, et renvoie une liste composée des chaînes issues de la liste telle que la distance de Levenshtein entre ces mots et ch1 soit minimale. 

def generateur_charabia_levenshtein(texte, Liste_mots, long_min = 5, long_max = 14) : #le fonctionnement de cette fonction est similaire à celle dans le cas du générateur-choix1
    sep = -1
    n_texte = ''
    for i in range(len(texte)) :
        if texte[i] in [' ','"','(',')',',','?',';','.',':','!','_','»','«', '\n'] :
            long = i - (sep+1)
            if long >= long_min and long <= long_max:
                n_nom = random.choice(liste_d_l_min(texte[sep+1:i], Liste_mots))
                if texte[sep+1].upper() == texte[sep+1] :
                    n_texte += n_nom[0].upper() + n_nom[1:] + texte[i]
                else :
                    n_texte += n_nom + texte[i]
            else :
                n_texte += texte[sep+1:i+1]
            sep = i
    return n_texte

f = codecs.open(r'Generateur_mot\n_f_t.txt', 'w', 'utf-8')
f.write(generateur_charabia_levenshtein(texte, set_mots))
f.close()
