def var_manquante(liste):
    L = []
    var = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    for i in range(1, len(liste)):
        L = liste[i].split(",")
        count = 0
        for q in range(0, len(L)):
            if L[q] == "":
                var[q] += 1
    L = liste[0].split(",")
    for i in range(0, len(var)):
        print("Pour la variable \"{}\" il manque {}% des valeurs ({} valeurs).".format(L[i], (int(var[i]/(len(liste)-1)*100)), var[i]))

fichier_csv = ['show_id,type,title,director,cast,country,date_added,release_year,rating,duration,listed_in,description',',,,,,,,,,,,']
var_manquante(fichier_csv)

#cette fonction python "var_manquante(LISTE)" compte le nombre de variables manquantes par rapport a une liste de données et précise le nom de la variable a laquelle cette valeur manquante correspond.
#il l'affiche ensuite sous forme de (par exemple): "Pour la variable "show_id" il manque 0.26% des valeurs (26 valeurs)."
