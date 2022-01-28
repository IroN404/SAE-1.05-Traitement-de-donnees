import pandas as pds
import matplotlib.pyplot as plt
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
def duree_serie(x):
    Y = []
    X = []
    for i in range(1, len(x)):
        s = split(x, i, 9).split(" ")
        if split(x, i, 1) == "TV Show":
            if s[0].isdigit():
                Y.append(int(s[0]))
                X.append(int(float(split(x, i, 7))))
    return Y, X
L = mise_en_forme("../../data/processed/netflix.csv")
Axes = duree_serie(L)
Y = Axes[0]
#duree
X = Axes[1]
#dates
zipped_lists = zip(X, Y)
sorted_zipped_lists = sorted(zipped_lists)
Y = [element for _, element in sorted_zipped_lists]
X.sort()
plt.plot(X, Y)
plt.title("Durée des séries en fonction de leur date de diffusion.")
plt.xlabel("Date de sortie de la série (Années).")
plt.ylabel("Durée de la série (Saisons).")
plt.show()
