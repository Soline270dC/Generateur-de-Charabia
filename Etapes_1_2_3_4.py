import numpy as np

#1 Choisir la base de données parmi celles disponibles dans le dossier "Base de données"
base_donnee = input("Nom de la base de données avec chemin d'accès relatif : ")

#2 Créer la matrice 4D
from mat_trans_4D import mat_trans_4D
nom_matrice = input("Nom à donner à la matrice (sans extension) : ")
print("Création de la matrice en cours...")
mat_trans_4D(base_donnee, nom_matrice)

#3 Créer l'ensemble de mots existants
from ensemble_mots import ensemble_mots_existants
nom_ensemble = input("Nom à donner à l'ensemble de mots existants (avec extension txt) : ")
ensemble_mots_existants(base_donnee, nom_ensemble)

#4 Générer une liste de mots nouveaux
from createur_mots_4D import creer_ensemble_mot, createur_mots_4D
Mat = np.load(nom_matrice + ".npy")
ensemble_mot = creer_ensemble_mot(nom_ensemble)

n = int(input("Nombre de mots à créer : ")) # Conseils de nombre de mots : entre 5000 et 10 000
breakpoint()
createur_mots_4D(n, Mat, ensemble_mot)