import pandas as pds

def mise_en_forme(fichier_csv):
    x = pds.read_csv(fichier_csv)
    c = ['show_id|type|title|director|cast|country|date_added|release_year|rating|duration|listed_in|description']
    s = ""
    for i in range(0, 1999):
        for q in range(0, 12):
            s = s + str(x.iloc[i, q]) + "|"
        c.append(s)
        s = ""
    return var_manquante(c)

def var_manquante(liste):
    var = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    for i in range(1, len(liste)):
        L = liste[i].split("|")
        for q in range(0, len(L)):
            if L[q] == 'nan':
                var[q] += 1
    L = liste[0].split("|")
    for i in range(0, len(var)):
        print("Pour la variable \"{}\" il manque {}% des valeurs ({} valeurs).".format(L[i], (int(var[i]/(len(liste)-1)*100)), var[i]))

mise_en_forme('U:\Bureau\draw\dnetflix-1.csv')

#cette fonction python "var_manquante(LISTE)" compte le nombre de variables manquantes par rapport a une liste de données X et précise la variable a laquelle cela correspond.
#il l'affiche ensuite sous forme de (par exemple): "Pour la variable "show_id" il manque 0.26% des valeurs (26 valeurs)."
