import codecs

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

Liste_mots = sorted(list(Ens_mots)) # O(len(Ens_mots)*log(len(Ens_mots)))
ch = '\n'.join(Liste_mots) # O(len(Ens_mots))

f = codecs.open('ensemble_mots_français.txt', 'w', 'utf-8')
f.write(ch)
f.close() # O(len(ch))

# O(len(texte)²)