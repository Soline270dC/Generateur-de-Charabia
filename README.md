# Explication de ma matrice de transition
J'ai mis 33 lignes et 34 colonnes
Pour les lignes : les 26 lettres en minuscules + 6 caractères accentués (é,è,ê,ù,à,î) et le caractère espace (je viens de me rendre compte que j'ai oublié les ï je m'en occuperai !)
Pour les colonnes : les mêmes 33 caractères + une colonne supp qui sert à stocker au fur et à mesure du remplissage de la matrice le nb d'occurences de chaque lettre
Puis je compte les occurences de chaque succession
Puis je divise par le nb d'occurences pour avoir la probabilité

En revanche, 2 pb principaux :
- je n'ai pas encore vraiment réussi à utiliser les fichiers dispos sur le projet Gutenberg, notamment à cause de sauts de lignes ds le fichier txt, et je n'arrive pas à m'en débarasser
- comment afficher la matrice en entier ? le terminal affiche des pts de suspension... C'est pour ça que j'ai essayé d'écrire la matrice dans un fichier, mais pour l'instant ne marche pass
