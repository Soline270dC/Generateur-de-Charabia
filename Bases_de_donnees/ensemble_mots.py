import codecs

f = codecs.open(r'Bases_de_donnees\Les_miserables_1.txt', 'r', 'utf-8')
texte = f.read()
f.close()

for c in ['"','(',')',',','?',';','.',':','!','--','_','»','«'] :
    texte = texte.replace(c,' ')
texte = texte.lower()

mots_misérables = texte.split()
Ens_mots_misérables = set(mots_misérables)

f = codecs.open(r'Bases_de_donnees\Liste_mots.txt', 'r', 'utf-8')
texte = f.read()
f.close()

texte = texte.lower()

mots_liste = texte.split()
Ens_mots_liste = set(mots_liste)

Ens_mots = Ens_mots_misérables|Ens_mots_liste

Liste = sorted(list(Ens_mots))
liste = '\n'.join(Liste)

f = codecs.open('ensemble_mots.txt', 'w', 'utf-8')
f.write(liste)
f.close()