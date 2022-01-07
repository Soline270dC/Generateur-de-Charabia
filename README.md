# Generateur de Charabia
## 1 - Choisir la base de données
Un dossier contenant plusieurs bases de données est disponible

## 2 - Créer la matrice 4D
Il est aussi possible d'utiliser une matrice 3D ou 2D, mais les mots sont alors plus difficiles à lire et sonnent peu français pour la plupart

La fonction **mat_trans_4D** dans le fichier **Matrice_transition_4D.py** prend en entrée :
- le chemin d'accès d'un fichier, extension comprise (la base de donnée)
- le nom sans extension et avec chemin d'accès du fichier dans lequel sera stockée la matrice

La fonction analyse le texte et enregistre une matrice 4D des probabilités de transition dans un fichier .npy

## 3 - Créer l'ensemble de mots existants
Cette étape permettra, lorsque les mots seront crées, de ne prendre en compte que les mots réellement inventés par le générateur.

La fonction **ensemble_mots_existants** dans le fichier **ensemble_mots_existants.py** prend en entrée :
- le chemin d'accès de la base de donnée utilisée précédemment (avec extension)
- le nom (avec chemin d'accès et extension) du fichier dans lequel la base de données sera enregistrée

La fonction génère une liste sans répétition des mots rencontrés dans le texte et l'enregistre dans un fichier .txt

## 4 - Générer une liste de mots nouveaux
Deux étapes préliminaires :
1. Charger la matrice de transition adaptée (4D)
2. Faire appel à la fonction **creer_ensemble_mots** en passant en argument le nom du fichier dans lequel est stocké l'ensemble de mots

La fonction **createur_mots_4D** prend en entrée :
- le nombre *n* de mots à créer
- la matrice de transitions
- l'ensemble de mots

Elle génère par marche aléatoire *n* mots tous distincts et n'appartenant pas à l'ensemble de mots, puis enregistre cette liste dans un document .txt

## 5 - Utiliser le générateur de charabia
Les mots à remplacer sont choisis de la manière suivante : tous les mots dont la longueur est comprise entre *long_min* et *long_max* (par défaut 5 et 20) sont modifiés suivant le mode d'utilisation.

Deux modes d'utilisation :
### a) Au hasard
Ce mode permet de remplacer les mots choisis par un mot de même longueur pris au hasard.
1. Création d'une liste de listes où les mots inventés sont triés par nombres de caractères, grâce à la fonction **liste_mots_triee** qui prend en argument le nom du fichier où sont stockés les mots et renvoie la liste de listes en question
2. Import du texte sur lequel sera exécuté le générateur de charabia
3. Génération du charabia :
    La fonction **generateur_charabia_hasard** prend en entrée :
    - le texte à modifier
    - la liste de mots triée créée en 1.
    - les longueurs maximale et minimale des mots à modifier (arguments par mot-clé)
    
Elle renvoie le texte modifié

Sa complexité en temps est en \Theta(len(texte))

### b) Avec la distance d'édition de Levenshtein
Ce mode permet de remplacer les mots choisis par le mot de la liste de mots créés qui leur est le plus proche en distance d'édition (ou au hasard dans l'ensemble des mots les plus proches à distance égale).
1. Création d'une liste de mots inventés à partir du fichier .txt contenant la liste.
2. Import du texte sur lequel sera exécuté le générateur de charabia
3. Génération du charabia :
    La fonction **generateur_charabia_levenshtein** prend en entrée :
    - le texte à modifier
    - la liste de mots créée en 1.
    - les longueurs maximale et minimale des mots à modifier (arguments par mot-clé)

Elle renvoie le texte modifié

Cette fonction fait appel à la fonction **liste_d_l_min** du fichier **distance_levenshtein.py**.

Sa complexité en temps est en O(len(texte)*len(Liste_mots))
