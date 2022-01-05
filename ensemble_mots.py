import codecs

# supprimer ce qui n'est pas la fonction
f = codecs.open(r'Bases_de_donnees\Les_miserables_1.txt', 'r', 'utf-8')
texte = f.read()
f.close()

for c in ['"','(',')',',','?',';','.',':','!','--','_','»','«'] : # O(len(texte)²)
    texte = texte.replace(c,' ')
texte = texte.lower() # O(len(texte))

mots_misérables = texte.split() # O(len(texte))
Ens_mots_misérables = set(mots_misérables) # O(len(mots_misérables))

f = codecs.open(r'Bases_de_donnees\Liste_mots.txt', 'r', 'utf-8')
texte = f.read()
f.close()

texte = texte.lower() # O(len(texte))

mots_liste = texte.split() # O(len(texte))
Ens_mots_liste = set(mots_liste) # O(len(mots_liste))

Ens_mots = Ens_mots_misérables|Ens_mots_liste # O(len(mots-liste) + len(mots_misérables))

f = codecs.open('ensemble_mots_français.txt', 'w', 'utf-8')
f.write(repr(Ens_mots))
f.close() # O(len(ch))

# O(len(texte)²)

def ensemble_mots_existants(nom_fichier, nom_ensemble, mode = 'utf-8') :
    f = codecs.open(nom_fichier, 'r', mode)
    texte = f.read()
    f.close()
    for c in ['"','(',')',',','?',';','.',':','!','--','_','»','«'] :
        texte = texte.replace(c,' ')
    texte = texte.lower()
    mots = texte.split()
    Ens_mots = set(mots)
    f = codecs.open(nom_ensemble, 'w', 'utf-8')
    f.write(repr(Ens_mots))
    f.close()
