def var_manquante(string):
    count = 0
    for q in range(1, len(string), 1):
        L = string[q].split(",")
        for i in range(0, len(L), 1):
            if L[i] == "":
                count = count + 1
    print(count)

x = ["show_id,type,title,director,cast,country,date_added,release_year,rating,duration,listed_in,description",
     "s1,Movie,Dick Johnson Is Dead,Kirsten Johnson,,United States,\"September 25, 2021\",2020,PG-13,90 min,Documentaries,\"As her father nears the end of his life, filmmaker Kirsten Johnson stages his death in inventive and comical ways to help them both face the inevitable.",
     "s2,TV Show,Blood & Water,,\"Ama Qamata, Khosi Ngema, Gail Mabalane, Thabang Molaba, Dillon Windvogel, Natasha Thahane, Arno Greeff, Xolile Tshabalala, Getmore Sithole, Cindy Mahlangu, Ryle De Morny, Greteli Fincham, Sello Maake Ka-Ncube, Odwa Gwanya, Mekaila Mathys, Sandi Schultz, Duane Williams, Shamilla Miller, Patrick Mofokeng\",South Africa,\"September 24, 2021\",2021,TV-MA,2 Seasons,\"International TV Shows, TV Dramas, TV Mysteries","After crossing paths at a party, a Cape Town teen sets out to prove whether a private-school swimming star is her sister who was abducted at birth.\""]
var_manquante(x)

#ce programme sous forme de fonction compte le nombre de variables manquantes par rapport a une liste de données X