import numpy as np
import codecs

def mat_trans_4D(nom_fichier, alphabet = 'abcdefghijklmnopqrstuvwxyzàâéèêëîïôûüç \'-') :
    f = codecs.open(nom_fichier, 'r', 'utf-8') # utf-8 à adapter en fonction du document
    texte = f.read()
    f.close()

    for c in ['"','(',')',',','?',';','.',':','!','--','_','»','«'] :
        texte = texte.replace(c,'')

    for c in ' \t\n' :
        texte = texte.replace(c, '   ')

    texte = texte.lower()

    Mat = np.zeros((len(alphabet), len(alphabet), len(alphabet), len(alphabet)))
    List_occ = np.zeros((len(alphabet), len(alphabet), len(alphabet)))

    # création de matrice et remplissage des occurences
    x = y = z = 38 # = alphabet.index(' ')
    for i in range(len(texte)) :
        car = texte[i]
        if car in alphabet :
            t = alphabet.index(car)
            Mat[x][y][z][t] += 1
            List_occ[x][y][z] += 1
            x = y
            y = z
            z = t
    t = 38
    Mat[x][y][z][t] += 1

    # normalisation
    for i in range(len(alphabet)) :
        for j in range(len(alphabet)) :
            for k in range(len(alphabet)):
                if List_occ[i][j][k] != 0 :
                    Mat[i][j][k] = Mat[i][j][k]/List_occ[i][j][k]

    np.save(r'4D\Matrice_probas_villages', Mat)