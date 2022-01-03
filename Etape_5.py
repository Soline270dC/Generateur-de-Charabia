import codecs

hasard = bool(input("Hasard ? (True/False) "))
levenshtein = bool(input("Levenshtein ? (True/False) "))

nom_liste = input("Nom de la liste de mots inventés (+ extension .txt) : ")

nom_texte_a_modifier = input("Nom du document à modifier (+ extension .txt) : ")
f = codecs.open(nom_texte_a_modifier, "r", "utf-8")
texte = f.read()
f.close()

ecrire_dans_un_fichier = bool(input("Voulez-vous écrire le charabia dans un fichier ? (True/False)"))

from Generateur_choix1_Hasard import liste_mots_triee, generateur_charabia_hasard

if hasard :
  Liste_mots_triee = liste_mots_triee(nom_liste)
  nouveau_texte = generateur_charabia_hasard(texte, Liste_mots_triee, long_min = 5, long_max = 20)
  if ecrire_dans_un_fichier :
    f = codecs.open(nom_texte_a_modifier[:-4] + "_charabia_hasard.txt", "w", "utf-8")
    f.write(nouveau_texte)
    f.close()
  else :
    print(nouveau_texte)

from Generateur_choix2_Levenshtein import liste_mots, generateur_charabia_levenshtein
    
if levenshtein :
  Liste_mots = liste_mots(nom_liste)
  nouveau_texte = generateur_charabia_levenshtein(texte, Liste_mots, long_min = 5, long_max = 20)
  if ecrire_dans_un_fichier :
    f = codecs.open(nom_texte_a_modifier[:-4] + "_charabia_levenshtein.txt", "w", "utf-8")
    f.write(nouveau_texte)
    f.close()
  else :
    print(nouveau_texte)