class MiejsceTeatralne:
    def __init__(self,id,dostepne,cena,rzad):
        self.id = id
        self.dostepne = dostepne
        self.cena = cena
        self.rzad = rzad

    def czyMiejsceDostepne(self):
        if self.dostepne == "tak":
            return True
        return False

class MiejsceZwykle(MiejsceTeatralne):
    def __init__(self,id,dostepne,cena,rzad,miejsceNaKubek):
        MiejsceTeatralne.__init__(self,id,dostepne,cena,rzad)
        self.miejsceNaKubek = miejsceNaKubek

class MiejsceVIP(MiejsceTeatralne):
    def __init__(self,id,dostepne,cena,rzad,udogodnienia,miejsceNaKubek):
        MiejsceTeatralne.__init__(self,id,dostepne,cena,rzad)
        self.udogodnienia = udogodnienia
        self.miejsceNaKubek = miejsceNaKubek

class MiejsceDlaNiepelnosprawnych(MiejsceTeatralne):
    def __init__(self,id,dostepne,cena,rzad,schody):
        MiejsceTeatralne.__init__(self,id,dostepne,cena,rzad)
        self.schody = schody

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

class Teatr:
    liczbaMiejsc = 40
    liczbaMiejscZwykluch = 26
    liczbaMiejscVIP = 10
    liczbaMiejscNiepelnosprawni = 4
    listaDostepnychMiejsc = []
    listaDostepnychMiejsc.extend(range(1, 41))

    @staticmethod
    def listaDostepnychMiejsc():
        if dostepne == "tak":
            listaDostepnychMiejsc.append(id)
            print (listaDostepnychMiejsc)


    @staticmethod
    def czyMiejsceDostepne(dostepne):
        if dostepne == "tak":
            return True
        return False

    @classmethod
    def utworzRezerwacje(cls,napis):
        if cls.czyMiejsceDostepne(id):
            return cls(imie,wiek,stypendium)

    print (listaDostepnychMiejsc)