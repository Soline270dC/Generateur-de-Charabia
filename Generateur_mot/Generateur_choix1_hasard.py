import codecs
import random

# Pour le générateur de charabia en lui-même, on propose deux possibilités à l'utilisateur : chaque mot du texte qu'on veut remplacer est soit remplacé :
# - choix 1 : au hasard par un mot inventé de même longueur : pour chaque mot à remplacer, on cherche les mots créés de même longueur et on en prend un aléatoirement 
# - choix 2 : par un mot pas forcément de même longueur mais proches en termes de distance de Leveshtein : pour chaque mot à remplacer, on cherche les mots créés les plus proches et on en prend un aléatoirement 
# Dans les deux cas, il faut commencer par générer une liste de mots créés à partir de la matrice de transition. Nous avons essayé successivement avec des listes de 100, 1000 et 5000 mots.

# Dans les deux cas, nous avons choisi de ne remplacer que les mots de longueur supérieur ou égale à 5 et inférieure ou égale à 20. 
# En effet, avec les mots trop courts, il y a deux problèmes :
# - nous avons décidé de garder dans les listes de mots inventés que les mots créés qui n'existent pas déjà en français, ce qui fait qu'il y a assez peu de mots courts dans nos listes car de nombreux mots de deux ou trois lettres existent déjà.  
# - de plus, garder les mots courts permet que le texte reste lisible et garde une certaine structure


# Choix 1 : remplacement au hasard et de même nombre de caractères

# Listes de mots : mots créés et mots à changer
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

#nom = input('nom de la liste de mots inventés à utiliser : ')
nom_de_la_liste_mots_inventés = r'4D\liste_5000_mots_4D.txt'
Liste_mots_triee = liste_mots_triee(nom_de_la_liste_mots_inventés)

# texte
#fichier_texte = input('nom du fichier textuel : ')
fichier_texte = r'Generateur_mot\fichier_textuel_2.txt'
fichier_texte = codecs.open(fichier_texte, 'r', 'utf-8')
texte = fichier_texte.read()
fichier_texte.close()

def generateur_charabia_hasard(texte, Liste_mots_triee, long_min = 5, long_max = 20) : # O(len(texte))
    sep = -1
    # sep correspondra dans la suite du programme à la position du dernier séparateur de mots dans le texte
    n_texte = ''
    for i in range(len(texte)) : # O(len(texte))
        if texte[i] in [' ','"','(',')',',','?',';','.',':','!','_','»','«'] :
            # on considère que lorsque l'on rencontre un de ces signes, il s'agit de la fin d'un mot.
            # Remarque : on ne prend pas en compte l'apostrophe pour que le programme considère les mots avec apostrophe comme un seul mot
            long = i - (sep+1) # long correspond à la longueur du dernier mot lu
            if long >= long_min and long <= long_max: # on regarde si on veut remplacer le mot lu
                if Liste_mots_triee[long] != [] : # O(1)
                    # on choisit ici un des mots de même longueur de la liste triéee par longueur 
                    n_nom = random.choice(Liste_mots_triee[long])
                    # on fait en sorte de garder les majuscules pour faciliter la lecture du texte final
                    if texte[sep+1].upper() == texte[sep+1] :
                        n_texte += n_nom[0].upper() + n_nom[1:] + texte[i]
                    else :
                        n_texte += n_nom + texte[i]
                # si jamais il n'y a pas de mot de même longueur dans la liste triée, on garde le mot sans le remplacer
                else :
                    n_texte += texte[sep+1:i+1]
            # de même, si le mot est trop court ou trop long, on le garde
            else :
                n_texte += texte[sep+1:i+1]
            sep = i
    return n_texte


