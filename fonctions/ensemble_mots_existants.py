import codecs

# O(len(texte)²)
def ensemble_mots_existants(nom_fichier, nom_ensemble, mode = 'utf-8') :
    f = codecs.open(nom_fichier, 'r', mode)
    texte = f.read()
    f.close()
    for c in ['"','(',')',',','?',';','.',':','!','--','_','»','«'] : # O(len(texte)²)
        texte = texte.replace(c,' ')
    texte = texte.lower()
    mots = texte.split()
    Ens_mots = set(mots)
    f = codecs.open(nom_ensemble, 'w', 'utf-8')
    f.write(repr(Ens_mots))
    f.close()
