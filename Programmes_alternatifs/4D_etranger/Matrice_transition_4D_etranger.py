import numpy as np
import codecs

# crée une matrice de transition en 4 dimensions à partir d'un fichier textuel
# 4D : considère la possibilité d'avoir le caractère c4 sachant que les caractères précédents sont c1, c2 et c3
def mat_trans_4D(nom_fichier, nom_matrice, langue, mode = 'utf-8') :
    f = codecs.open(nom_fichier, 'r', mode)
    texte = f.read()
    f.close()
    # l'étude des signes de ponctuation n'est pas pertinente, donc ils sont supprimés
    for c in ['"','(',')',',','?',';','.',':','!','--','_','»','«'] :
        texte = texte.replace(c,'')
    for c in ' \t\n' :
        texte = texte.replace(c, '   ')

    texte = texte.lower()

    if langue == 'de' :
        alphabet = 'abcdefghijklmnopqrstuvwxyzäëïöü '
    elif langue == 'en' :
        alphabet = 'abcdefghijklmnopqrstuvwxyz '
    elif langue == 'es' :
        alphabet = 'abcdefghijklmnopqrstuvwxyzñáéíóú -'

    Mat = np.zeros((len(alphabet), len(alphabet), len(alphabet), len(alphabet)))
    List_occ = np.zeros((len(alphabet), len(alphabet), len(alphabet)))

    ## création de matrice et remplissage des occurences
    ind_esp = alphabet.index(' ')
    x = y = z = ind_esp
    for i in range(len(texte)) :
        car = texte[i]
        # on ne prend pas en compte les nombres
        if car in alphabet :
            t = alphabet.index(car)
            # incrémentation de la matrice de transition et de la matrice d'occurences
            Mat[x][y][z][t] += 1
            List_occ[x][y][z] += 1
            # déplacement du curseur
            x = y
            y = z
            z = t
    # la dernière transition (de fin de mot) est gérée en ajoutant un espace fictif à la fin du texte
    t = ind_esp
    Mat[x][y][z][t] += 1

    ## normalisation de la matrice pour transformer les nombres d'occurences en probabilités de transition
    for i in range(len(alphabet)) :
        for j in range(len(alphabet)) :
            for k in range(len(alphabet)):
                if List_occ[i][j][k] != 0 :
                    Mat[i][j][k] = Mat[i][j][k]/List_occ[i][j][k]
    # stockage de la matrice au format .npy
    np.save(nom_matrice, Mat)