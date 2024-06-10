def utworzMiejscaBaza():
    for i in range(2,10):
        x = 2
        miejsce = x
        miejsce = MiejsceZwykle(i,"tak","30",1, "nie")
        print (miejsce.id, miejsce.dostepne, miejsce.cena, miejsce.rzad, miejsce.miejsceNaKubek)
        x += 1
    for i in range(12,20):
        x = 12
        miejsce = x
        miejsce = MiejsceZwykle(i,"tak","35",2, "tak")
        print (miejsce.id, miejsce.dostepne, miejsce.cena, miejsce.rzad, miejsce.miejsceNaKubek)
        x += 1
    for i in range(22,25):
        x = 22
        miejsce = x
        miejsce = MiejsceZwykle(i,"tak","35",3, "tak")
        print (miejsce.id, miejsce.dostepne, miejsce.cena, miejsce.rzad, miejsce.miejsceNaKubek)
        x += 1
    for i in [1,11,21,10,20,25]:
        x = i
        miejsce = x
        miejsce = MiejsceDlaNiepelnosprawnych(i,"tak","35",2, "nie")
        print (miejsce.id, miejsce.dostepne, miejsce.cena, miejsce.rzad, miejsce.schody)
    for i in range(26,31):
        x = 26
        miejsce = x
        miejsce = MiejsceVIP(i,"tak","45",4, "rozkładane", "tak")
        print (miejsce.id, miejsce.dostepne, miejsce.cena, miejsce.rzad, miejsce.udogodnienia, miejsce.miejsceNaKubek)
        x += 1
    for i in range(31,36):
        x = 31
        miejsce = x
        miejsce = MiejsceVIP(i,"tak","45",5, "podwójne", "tak")
        print (miejsce.id, miejsce.dostepne, miejsce.cena, miejsce.rzad,miejsce.udogodnienia, miejsce.miejsceNaKubek)
        x += 1

utworzMiejscaBaza()