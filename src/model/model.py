import pandas as pds

def mise_en_forme(fichier_csv):
    x = pds.read_csv(fichier_csv)
    c = ['show_id|type|title|director|cast|country|date_added|release_year|rating|duration|listed_in|description']
    for i in range(0, 8807):
        s = ""
        for q in range(0, 12):
            s = s + str(x.iloc[i, q]) + "|"
        c.append(s)
    return c

def split(x, i, n):
    r = x[i].split("|")
    return r[n]

def France_film(x):
    francais = 0
    f = [0, 0]
    for i in range(1, len(x)):
        movie = 0
        L = x[i].split("|")
        for q in range(0, len(L)):
            if L[q] == 'Movie':
                movie = 1
            if L[q] == 'France':
                francais += 1
                if movie == 1:
                    f[0] += 1
                else:
                    f[1] += 1
    print("Le pourcentage de films/séries francais est de {}% ({} films/séries).".format(round(francais/8807*100,2),francais))
    print("Le nombre de films francais est {}.".format(f[0]))
    print("Le nombre de séries francaises est {}.".format(f[1]))

def duree_film_serie(x, test):
    MO = []
    TV = []
    for i in range(1, len(x)):
        s = split(x, i, 9).split(" ")
        if s[0].isdigit():
            if split(x, i, 1) == "Movie":
                MO.append(int(s[0]))
            else:
                TV.append(int(s[0]))
    MO.sort()
    TV.sort()
    if test == 0:
        return MO
    if test == 1:
        return TV

def ComputeMean(x):
    print("La moyenne de la durée des films est de {} minute(s)".format(round(sum(duree_film_serie(x, 0))/(len(duree_film_serie(x, 0))+1),2)))
    print("La moyenne de la durée des séries est de {} saison(s)".format(round(sum(duree_film_serie(x, 1))/(len(duree_film_serie(x, 1))+1),2)))
    mean = [round(sum(duree_film_serie(x, 0))/(len(duree_film_serie(x, 0))+1), 2), round(sum(duree_film_serie(x, 1))/(len(duree_film_serie(x, 1))+1),2)]
    return mean

def ComputeMedian(x):
    print(duree_film_serie(x, 0)[int(len(duree_film_serie(x, 0))/2)])
    print(duree_film_serie(x, 1)[int(len(duree_film_serie(x, 1)) / 2)])
    median = [duree_film_serie(x, 0)[int(len(duree_film_serie(x, 0))/2)], duree_film_serie(x, 1)[int(len(duree_film_serie(x, 1)) / 2)]]
    return median

L = mise_en_forme("../../data/processed/netflix.csv")
print("_____________________")
France_film(L)
print("_____________________")
ComputeMean(L)
print("_____________________")
ComputeMedian(L)
