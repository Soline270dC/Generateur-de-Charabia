import random
import codecs

# crée un ensemble de mots à partir d'un fichier (permet d'éviter les doublons)
def creer_ensemble_mot(nom_fichier, mode = 'utf-8') :
    f = codecs.open(nom_fichier,'r', mode)
    E = eval(f.read())
    f.close()
    # on ajoute le mot vide pour qu'il ne soit pas créé
    E.add('')
    return E

# crée une liste de mots inventés de taille n (et l'écrit dans un fichier)
# prend en argument la matrice de transition 4D grpace à laquelle il construira les mots
# ainsi que l'ensemble de mots français pour ne pas créer de mots existants
def createur_mots_4D(n, Mat, ensemble_mots_existants, langue) :
    if langue == 'de' :
        alphabet = 'abcdefghijklmnopqrstuvwxyzäëïöü '
    elif langue == 'en' :
        alphabet = 'abcdefghijklmnopqrstuvwxyz '
    elif langue == 'es' :
        alphabet = 'abcdefghijklmnopqrstuvwxyzñáéíóú -'
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
            car = random.choices(alphabet, Mat[x][y][z])[0]
            mot += car
            # après avoir ajouté le caractère, on décale les curseurs
            x = y
            y = z
            z = alphabet.index(car)
        mot = mot.replace(' ','\n')
        # le mot ne doit ni être français, ni avoir déjà été créé : cela permet d'avoir exactement n mots inventés 
        if not (mot[:-1] in ensemble_mots_existants or mot in Mots) :
            Mots.add(mot)
            i += 1
    
    f = codecs.open(f'liste_{n}_mots_inventes_4D_{langue}.txt', 'w', 'utf-8')
    f.writelines(Mots)
    f.close()