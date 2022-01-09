import codecs

# Choisir le mode d'utilisation (Au hasard/ Avec la distance d'édition de Levenshtein)
hasard = eval(input("Voulez-vous remplacer un mot par un mot inventé de même longueur choisi tout à fait au hasard ? (True/False) "))
levenshtein = eval(input("Voulez-vous remplacer un mot par un mot inventé qui lui est le plus proche par rapport à la distance d'édition de Levenshtein ? (True/False) "))

if hasard or levenshtein : 
    nom_liste = input("Veuillez noter le nom de la liste de mots inventés créée dans les étapes précédentes (avec extension txt): ")
    texte_fichier = eval(input("Voulez-vous modifier un texte stocké dans un fichier (True) ou écrire directement la phrase à modifier (False) ? "))
    if texte_fichier :
        nom_texte_a_modifier = input("Veuillez noter le nom du document à modifier (avec extension txt) : ")
        f = codecs.open(nom_texte_a_modifier, "r", "utf-8")
        texte = f.read()
        f.close()
    else :
        texte = input("Entrer un texte : ")

    # Création d'un fichier contenant le texte charabié
    ecrire_dans_un_fichier = eval(input("Voulez-vous écrire le charabia dans un fichier ? (True/False) "))
  
# Générer un texte nouveau suivant le mode au hasard
if hasard :
    from fonctions.Generateur_choix1_hasard import liste_mots_triee, generateur_charabia_hasard
    print("Génération de charabia en cours...")
    Liste_mots_triee = liste_mots_triee(nom_liste)
    nouveau_texte = generateur_charabia_hasard(texte, Liste_mots_triee, long_min = 5, long_max = 20)
    
    if ecrire_dans_un_fichier :
        f = codecs.open(nom_texte_a_modifier[:-4] + "_charabia_hasard.txt", "w", "utf-8")
        f.write(nouveau_texte)
        f.close()
    else :
        print(nouveau_texte)
  
# Générer un texte nouveau suivant le mode de la distance d'édition de Levenshtein
if levenshtein :
    from fonctions.Generateur_choix2_Levenshtein import liste_mots, generateur_charabia_levenshtein
    print("Génération de charabia en cours...")
    Liste_mots = liste_mots(nom_liste)
    nouveau_texte = generateur_charabia_levenshtein(texte, Liste_mots, long_min = 5, long_max = 20)
    
    if ecrire_dans_un_fichier :
        f = codecs.open(nom_texte_a_modifier[:-4] + "_charabia_levenshtein.txt", "w", "utf-8")
        f.write(nouveau_texte)
        f.close()
    else :
        print(nouveau_texte)