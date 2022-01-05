import codecs
import random

# Pour le générateur de charabia en lui-même, on propose deux possibilités à l'utilisateur : chaque mot de longueur >= 5 et <= 14 
# - choix 1 : est remplacé au hasard par un mot inventé de même longueur
# - choix 2 : est remplacé par un mot pas forcément de même longueur mais proche en termes de distance de Leveshtein : pour chaque mot à remplacer, on cherche les mots créés les plus proches et on en prend un aléatoirement (cf. fonction définie plus bas)

# Dans les deux cas, il faut commencer par générer une liste de mots créés à partir de la matrice de transition. Nous avons essayé successivement avec des listes de 100, 1000 et 5000 mots.

# Choix 1 : remplacement au hasard et de même nombre de caractères

# Liste de mots
# Comme on veut remplacer le mot initial par un mot créé de même longueur, on trie les mots créés selon leur longueur. Le tout est stocké dans une lsite de listes. Par exemple, liste_mots_triee[3] contient tous les mots inventés de longueur 3.
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

# On propose à l'utilisateur de rentrer le texte à modifier dans un fichier .txt. La fonction suivante permet de lire ce fichier et d'en faire une liste de chaînes de caractères, chacune correspondant à un mot. 
def liste_mots(nom_fichier_textuel, mode = 'utf-8') :
    f = codecs.open(nom_fichier_textuel, 'r', mode)
    str_mots = f.read()
    f.close()
    liste_mots = str_mots.split()  # C'est ici qu'on sépare le texte en mots. 
    return liste_mots

#nom = input('nom de la liste de mots : ')
nom = r'4D\liste_5000_mots_4D.txt'
set_mots = set(liste_mots(nom))
#Liste_mots_triee = liste_mots_triee(nom)

# texte (pas trop long siouplé)
#fich = input('nom du fichier textuel : ')
fich = r'Generateur_mot\fichier_textuel_2.txt'
f = codecs.open(fich, 'r', 'utf-8')
texte = f.read()
f.close()

# choix 1 : mots au hasard
def generateur_charabia_hasard(texte, Liste_mots_triee, long_min = 5, long_max = 14) :
    sep = -1
    n_texte = ''
    for i in range(len(texte)) :
        if texte[i] in [' ','"','(',')',',','?',';','.',':','!','_','»','«'] :
            long = i - (sep+1)
            if long >= long_min and long <= long_max:
                if Liste_mots_triee[long] != [] :
                    n_nom = random.choice(Liste_mots_triee[long])
                    if texte[sep+1].upper() == texte[sep+1] :
                        n_texte += n_nom[0].upper() + n_nom[1:] + texte[i]
                    else :
                        n_texte += n_nom + texte[i]
                else :
                    n_texte += texte[sep+1:i+1]
            else :
                n_texte += texte[sep+1:i+1]
            sep = i
    return n_texte



# choix 2 : distance d'édition la plus courte
from distance_levenshtein import liste_d_l_min

def generateur_charabia_levenshtein(texte, Liste_mots, long_min = 5, long_max = 14) :
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
