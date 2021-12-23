import numpy as np
import codecs

f = codecs.open(r'Bases_de_donnees\Les_miserables_1.txt', 'r', 'utf-8') # utf-8 à adapter en fonction du document
texte = f.read()
f.close()

# fonction 'propre' (cf origin/Aurelie)
for c in ['"','(',')',',','?',';','.',':','!','--','_','»','«'] : # cas des apostrophes à aviser ("c'", "l'", "d'")
    texte = texte.replace(c,' ')
texte = texte.lower()

mots_mis = texte.split()
Ens_mots_mis = set(mots_mis)

f = codecs.open(r'Bases_de_donnees\Liste_mots.txt', 'r', 'utf-8') # utf-8 à adapter en fonction du document
texte = f.read()
f.close()

texte = texte.lower()

mots_list = texte.split()
Ens_mots_list = set(mots_list)

Ens_mots = Ens_mots_mis|Ens_mots_list

f = codecs.open('set_ensemble_mots.txt', 'w', 'utf-8')
f.write(repr(Ens_mots))
f.close()

Liste = sorted(list(Ens_mots))
liste = '\n'.join(Liste)

f = codecs.open('ensemble_mots.txt', 'w', 'utf-8')
f.write(liste)
f.close()