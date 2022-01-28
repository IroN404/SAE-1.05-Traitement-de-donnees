import pandas as pds

#La première chose que je faite est l'importation la librairie "pandas" qui me permettra d'étudier/importer le contenu d'un fichier excel ou csv externe.


#Ensuite j'ai défini une fonction que j'ai nommé "mise_en_forme" qui prend en compte un paramètre et celui-ci est le chemin d'accès vers le document csv.
#Cette fonction me permet de récupérer toutes les données du fichier csv et les répartir dans une variable liste.
#Chaque ligne du fichier csv est enregistrée dans la liste comme un élement string, où chaque variable de la ligne est séparé par un caractère "|" ce qui me permettra de traiter les différents élements plus tard dans mon programme.

def mise_en_forme(fichier_csv):
    x = pds.read_csv(fichier_csv)
    c = ['show_id|type|title|director|cast|country|date_added|release_year|rating|duration|listed_in|description']
    s = ""
    for i in range(0, 8807):
        for q in range(0, 12):
            s = s + str(x.iloc[i, q]) + "|"
        c.append(s)
        s = ""
    return c

#J'envoie ensuite cette variable liste que j'ai créé à ma deuxième fonction qui traitera la liste de facon a etudier toutes les différents variables pour voir celles qui manquent.

def is_float(x) -> bool:
    try:
        float(x)
        return True
    except ValueError:
        return False
#Les variables manquantes sont découverte en faisant une petite comparaison pour voir si la valeur de la variable est égale à 'nan'
#Pour les valeurs abérantes, je vérifie si la date est bien une valeure numérique, si non, j'ajoute 1 a une variable compteur "count"
#qui elle me permet de tenir compte des valeurs abérantes. Si la date est bel et bien une valeur numérique, je la compare a la date du premier film créé (1874).
#Si cette date est inférieure, elle est donc une valeur abbérante.
def var_manquante(liste):
    var = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    count = 0
    for i in range(1, len(liste)):
        L = liste[i].split("|")
        for q in range(0, len(L)):
            if L[q] == 'nan':
                var[q] += 1
            elif q == 0:
                if str(L[0])[:1] != "s":
                    count = count + 1
            elif q == 1:
                if L[q] != 'Movie' and L[q] != 'TV Show':
                    count = count + 1
            elif q == 2 or q == 3 or q == 4 or q == 5 or q == 6 or q == 8 or q == 9 or q == 10 or q == 11:
                if str(L[q]) != L[q]:
                    count = count + 1
                if L[q].isnumeric():
                    count = count + 1
            elif q == 7:
                if is_float(L[q]):
                    if float(L[q]) < 1874:
                        count = count + 1
                else:
                    count = count + 1
    L = liste[0].split("|")
    for i in range(0, len(var)):
        print("Pour la variable \"{}\" il manque {}% des valeurs ({} valeurs).".format(L[i], round(var[i]/(len(liste)-1)*100,2), var[i]))
    print("Il y a {} valeur(s) abérantes".format(count))

#Ensuite, j'affiche le résultat de facon lisible et compréhensible, en affichant le pourcentage de valeurs manquantes ainsi qu'en précisant le nom de la variable concernée.

var_manquante(mise_en_forme("../../data/processed/netflix.csv"))
#J'execute la fonction avec le chemin du fichier.

#L'affichage du programme est le suivant:
#Pour la variable "show_id" il manque 0.0% des valeurs (0 valeurs).
#Pour la variable "type" il manque 0.0% des valeurs (0 valeurs).
#Pour la variable "title" il manque 0.0% des valeurs (0 valeurs).
#Pour la variable "director" il manque 29.9% des valeurs (2633 valeurs).
#Pour la variable "cast" il manque 9.37% des valeurs (825 valeurs).
#Pour la variable "country" il manque 9.44% des valeurs (831 valeurs).
#Pour la variable "date_added" il manque 0.12% des valeurs (11 valeurs).
#Pour la variable "release_year" il manque 0.0% des valeurs (0 valeurs).
#Pour la variable "rating" il manque 0.05% des valeurs (4 valeurs).
#Pour la variable "duration" il manque 0.03% des valeurs (3 valeurs).
#Pour la variable "listed_in" il manque 0.0% des valeurs (0 valeurs).
#Pour la variable "description" il manque 0.0% des valeurs (0 valeurs).
#Il y a 15 valeur(s) abérantes
