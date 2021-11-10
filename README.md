# Generateur-de-Charabia

## Utilisation de la matrice de transition
La matrice de probabilités générée dans mon programme a pour lignes la lettre et pour colonnes la probabilité de ce qui suit.
Afin d'obtenir la ligne, il faut multiplier une matrice ligne par cette matrice.
liste des caractères dans l'ordre : abcdefghijklmnopqrstuvwxyzàâéèêëîïôûüç '-

Afin de réutiliser la matrice dans un programme ultérieur, il faut à mon avis créer une fonction qui génère la matrice de transition à partir d'un fichier donné en argument. On peut ensuite importer cette fonction dans notre fichier car il semble difficile de stocker la matrice.

## Génération de la matrice de transition
On se positionne sur la première lettre du texte et on regarde quelle lettre la suit.
On implémente la case de la matrice correspondant à cette transition (cf plus huat pour déterminer ça).
La deuxième lettre (qualifiée auparavant de 'lettre qui suit') prend la place de la première lettre et on regarde sa propre successeure.
On continue jusqu'à arriver à la fin du texte.
Les deux extrêmes sont gérés en ajoutant symboliquement un espace au début et à la fin

On rend la matrice stochastique en divisant chaque ligne par la somme.

Problème :
Si on ne croise aucune occurence d'une lettre et qu'on a du coup une ligne nulle, est-ce qu'on peut vraiment parler de matrice stochastique ?
Il faudrait donc faire attention à n'avoir que des caractères spéciaux qu'on rencontrera ?

## Stockage et réutilisation de la matrice de transition
La fonction numpy.save prend en argument:
- un nom de fichier
- un ndarray
Elle crée un fichier nom_fichier.npy (non lisible pour nous autres simples mortels)
On peut y accéder plus tard grâce à la fonction numpy.load qui prend en argument un nom de fichier (avec le .npy, cette fois) et renvoie la matrice sous la forme array([...])