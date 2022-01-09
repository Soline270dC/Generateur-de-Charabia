# Générateur de Charabia
Notre genérateur de charabia fonctionne en 5 étapes. Les 4 premières peuvent être réalisées depuis le fichier **Etapes_1_2_3_4.py** de ce dossier, et la dernière depuis le fichier **Etape_5.py**. Nous détaillons ici les différentes étapes, et nous avons également commenté les différentes fonctions utilisées et le code des fichier "étapes".

## 1 - Choisir la base de données
Un dossier contenant plusieurs bases de données est disponible. Pour plus de précisions, nous avons également mis en Readme dans ce dossier.

## 2 - Créer la matrice de transition 4D
Nous expliquons pourquoi et comment nous générons la matrice en commentaire dans le fichier **Matrice_transition_4D.py**. 
Il est aussi possible d'utiliser une matrice 3D ou 2D, mais les mots sont alors plus difficiles à lire et sonnent peu français pour la plupart. Les programmes des matrices 3D et 2D sont moins commentés mais le principe est le même que pour la 4D. 

La fonction **mat_trans_4D** dans le fichier **Matrice_transition_4D.py** prend en entrée :
- le chemin d'accès d'un fichier, extension comprise (la base de donnée)
- le nom sans extension et avec chemin d'accès du fichier dans lequel sera stockée la matrice

La fonction analyse le texte et enregistre une matrice 4D des probabilités de transition dans un fichier .npy

## 3 - Créer l'ensemble de mots existants en français
Cette étape permettra, lorsque les mots seront créés, de ne prendre en compte que les mots réellement inventés par le générateur.

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

**Remarque** : pour les étapes 3 et 4, nous avons choisi de faire en sorte de ne garder parmi les mots générés que ceux qui n'existent pas déjà en français. Mais dans le dossier **Programmes_alternatifs > 4D_mots_existants** nous avons mis des programmes et exemples où l'on ne prend pas en compte cet aspect.

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
    
Elle renvoie le texte modifié ou l'écrit dans un fichier selon le choix de l'utilisateur.

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

Elle renvoie le texte modifié ou l'écrit dans un fichier selon le choix de l'utilisateur.

Cette fonction fait appel à la fonction **liste_d_l_min** du fichier **distance_levenshtein.py**.

Sa complexité en temps est en O(len(texte)*len(Liste_mots))
