
with open('Les_Misérables.txt', 'r') as file:
    text = file.read().replace('\n', '').replace('  ', ' ')

# enlever les caractères génants :
caract_to_remove = {chr("."): None, chr("!"): None, chr("?") : None}
text.translate(caract_to_remove)
print(text)

transition_count = {}
# Le dictionnaire est composé de clé correspondant aux couples rencontrés dans le texte associé aux valeurs correspondant aux nombre de fois que le couple apparait
n = len(text)
for i in range(n-1):
    duo = text[i] + text[i+1]
    if duo in transition_count.keys():
        transition_count[duo] += 1
    else :
        transition_count[duo] = 1

# Je prends en compte la probabilité de chaque caractère en début de mot
Alphabet = abcdefghijklmnopqrstuvwxyzàâéèêëîïôûüç
for i in Alphabet :
    duo = " " + i
    if duo in transition_count.keys():
        transition_count[duo] += 1
    else :
        transition_count[duo] = 1

for k in transition_count.keys():
    transition_count[k] /= (n-1)*1.
    # multilier par "1." pour avoir un entier et dans un texte de n caractères, il y a n-1 couples

# for k,v in transition_count.items():
#     print(f"key : {k} value : {v}")


# def obtenirPos(c) :
#     alphabet = abcdefghijklmnopqrstuvwxyz
#     lettrespecial = àâéèêëîïôûüç
#     if c in alphabet :
#         p = ord(c) - 97
#         return p
#     else :
#         return len(alphabet) + index(lettrespecial)
#
# c = input("Donner une lettre : ")
# print("\nLa lettre est dans la", obtenirPos(c),"ème position dans l'alphabet.")
# # Construction du tableau de probabilité :
# TProba = [[0,0] for i in range(len(Alphabet))]
# for i in range (len(Alphabet)) :
#     for j in range(len(Alphabet)) :
#         Tproba[i,j] =


# Création de l'automate

lettre_depart = "p"
nombredecaractères = 6

subtransition_count = {}
for k,v in transition_count.items():
    if k.startswith(lettre_depart):
        subtransition_count[k] = v

