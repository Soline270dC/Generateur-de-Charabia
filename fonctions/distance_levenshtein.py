def d_l(a,b) : # \Theta(len(a)*len(b))
    a = ' ' + a
    b = ' ' + b
    if a == b :
        return 0
    D = [[0 for _ in range(len(b))] for _ in range(len(a))]
    for i, car_a in enumerate(a) :
        for j, car_b in enumerate(b) :
            if j == 0 or i == 0 :
                D[i][j] = i + j
            else :
                D[i][j] = min(D[i-1][j] + 1, D[i][j-1] + 1, D[i-1][j-1] + int(car_a != car_b))
    return D[-1][-1]

def liste_d_l_min(nom, liste_mots) : # \Theta(len(nom)*len_moyenne(mots)*len(liste_mots)) = \theta(len(liste_mots)) car len(mot)<=30 ici
    d_min = float('inf')
    L = []
    for mot in liste_mots :
        d = d_l(mot,nom)
        if d < d_min :
            d_min = d
            L = [mot]
        elif d == d_min :
            L.append(mot)
    return L