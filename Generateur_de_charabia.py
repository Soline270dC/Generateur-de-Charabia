#1 Choisir la base de données parmi celles disponibles dans le dossier "Base de données"
base_donnee = input("Nom de la base de données avec chemin d'accès relatif : ")

#2 Créer la matrice 4D
from mat_trans_4D_fct import mat_trans_4D
nom_matrice = input("Nom à donner à la matrice (sans extension) : ")
mat_trans_4D(base_donnee, nom_matrice)

#3 Créer l'ensemble de mots existants
from ensemble_mots import ensemble_mots_existants
nom_ensemble = input("Nom à donner à l'ensemble (avec extension) : ")
ensemble_mots_existants(base_donnee, nom_ensemble)

#4 Générer une liste de mots nouveaux
