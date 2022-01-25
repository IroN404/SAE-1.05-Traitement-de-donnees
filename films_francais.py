#cette fonction python permet de compter le nombre de films/séries sur le document CSV. 

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
    return var_manquante(c)

#J'envoie ensuite cette variable liste que j'ai créé à ma deuxième fonction qui traitera la liste de facon a etudier toutes les différents variables pour voir celles qui manquent.

#Les variables manquantes sont découverte en faisant une petite comparaison pour voir si la valeur de la variable est égale à 'nan'

def var_manquante(liste):
    francais = 0
    for i in range(1, len(liste)):
        L = liste[i].split("|")
        for q in range(0, len(L)):
            if L[q] == 'France':
                francais += 1
    print("Le pourcentage de films/séries francaises est de {}% ({} films/séries)".format(round(francais/8807*100,2), francais))

#Ensuite, j'affiche le résultat de facon lisible et compréhensible, en affichant le pourcentage de valeurs manquantes ainsi qu'en précisant le nom de la variable concernée.

chemin_csv = str(input("Merci de précisez le chemin absolu du document CSV: "))
mise_en_forme(chemin_csv)

#Je demande a l'utilisateur de préciser le chemin absolu du document CSV.


#L'affichage du résultat du programme ressemble à celui-ci:
#______
#Merci de précisez le chemin absolu du document CSV: U:\bureau\netflix.csv
#Le pourcentage de films/séries francaises est de 1.41%
