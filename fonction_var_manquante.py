#cette fonction python permet de compter le nombre de variables manquantes par rapport a une liste de données et précise la variable a laquelle cela correspond. 
#Il renverra ensuite un pourcentage des valeurs manquantes.

import pandas as pds

#La première chose que je faite est l'importation la librairie "pandas" qui me permettra d'étudier/importer le contenu d'un fichier excel ou csv externe.


#Ensuite j'ai défini une fonction que j'ai nommé "mise_en_forme" qui prend en compte un paramètre et celui-ci est le chemin d'accès vers le document csv.
#Cette fonction me permet de récupérer toutes les données du fichier csv et les répartir dans une variable liste.
#Chaque ligne du fichier csv est enregistrée dans la liste comme un élement string, où chaque variable de la ligne est séparé par un caractère "|" ce qui me permettra de traiter les différents élements plus tard dans mon programme.

def mise_en_forme(fichier_csv):
    x = pds.read_csv(fichier_csv)
    c = ['show_id|type|title|director|cast|country|date_added|release_year|rating|duration|listed_in|description']
    s = ""
    for i in range(0, 8808):
        for q in range(0, 12):
            s = s + str(x.iloc[i, q]) + "|"
        c.append(s)
        s = ""
    return var_manquante(c)

#J'envoie ensuite cette variable liste que j'ai créé à ma deuxième fonction qui traitera la liste de facon a etudier toutes les différents variables pour voir celles qui manquent.

#Les variables manquantes sont découverte en faisant une petite comparaison pour voir si la valeur de la variable est égale à 'nan'

def var_manquante(liste):
    var = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    for i in range(1, len(liste)):
        L = liste[i].split("|")
        for q in range(0, len(L)):
            if L[q] == 'nan':
                var[q] += 1
    L = liste[0].split("|")
    for i in range(0, len(var)):
        print("Pour la variable \"{}\" il manque {}% des valeurs ({} valeurs).".format(L[i], round(var[i]/(len(liste)-1)*100,2), var[i]))


#Ensuite, j'affiche le résultat de facon lisible et compréhensible, en affichant le pourcentage de valeurs manquantes ainsi qu'en précisant le nom de la variable concernée.

chemin_csv = str(input("Merci de précisez le chemin absolu du document CSV: "))
mise_en_forme(chemin_csv)

#Je demande a l'utilisateur de préciser le chemin absolu du document CSV.


#L'affichage du résultat du programme ressemble à celui-ci:
#______
#Merci de précisez le chemin absolu du document CSV: U:\bureau\netflix.csv
#Pour la variable "show_id" il manque 0.0% des valeurs (0 valeurs).
#Pour la variable "type" il manque 0.01% des valeurs (1 valeurs).
#Pour la variable "title" il manque 0.01% des valeurs (1 valeurs).
#Pour la variable "director" il manque 29.9% des valeurs (2634 valeurs).
#Pour la variable "cast" il manque 9.38% des valeurs (826 valeurs).
#Pour la variable "country" il manque 9.45% des valeurs (832 valeurs).
#Pour la variable "date_added" il manque 0.14% des valeurs (12 valeurs).
#Pour la variable "release_year" il manque 0.01% des valeurs (1 valeurs).
#Pour la variable "rating" il manque 0.06% des valeurs (5 valeurs).
#Pour la variable "duration" il manque 0.05% des valeurs (4 valeurs).
#Pour la variable "listed_in" il manque 0.01% des valeurs (1 valeurs).
#Pour la variable "description" il manque 0.01% des valeurs (1 valeurs).
