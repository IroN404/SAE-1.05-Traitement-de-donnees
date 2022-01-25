def var_manquante(liste):
    L = []
    var = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    for i in range(1, len(liste)):
        L = liste[i].split(",")
        count = 0
        for q in range(0, len(L)):
            if L[q] == "":
                var[q] += 1
    for i in range(0, len(var)):
        print("Pour la variable {} il manque {}% des valeurs ({} valeurs). ".format(i+1, (int(var[i]/(len(liste)-1)*100)), var[i]))

fichier_csv = ['show_id,type,title,director,cast,country,date_added,release_year,rating,duration,listed_in,description',
               's1,Movie,Dick Johnson Is Dead,,,United States,"September 25, 2021",2020,PG-13,90 min,Documentaries,"As her father nears the end of his life, filmmaker Kirsten Johnson stages his death in inventive and comical ways to help them both face the inevitable."',
               's2,TV Show,Blood & Water,,"Ama Qamata, Khosi Ngema, Gail Mabalane, Thabang Molaba, Dillon Windvogel, Natasha Thahane, Arno Greeff, Xolile Tshabalala, Getmore Sithole, Cindy Mahlangu, Ryle De Morny, Greteli Fincham, Sello Maake Ka-Ncube, Odwa Gwanya, Mekaila Mathys, Sandi Schultz, Duane Williams, Shamilla Miller, Patrick Mofokeng",South Africa,"September 24, 2021",2021,TV-MA,2 Seasons,"International TV Shows, TV Dramas, TV Mysteries","After crossing paths at a party, a Cape Town teen sets out to prove whether a private-school swimming star is her sister who was abducted at birth."']
var_manquante(fichier_csv)

#cette fonction python "var_manquante(LISTE)" compte le nombre de variables manquantes par rapport a une liste de données X et précise la variable a laquelle cela correspond.
