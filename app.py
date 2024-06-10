#################################### Typy danych i zmienne w Python
# wiek = 20
# print (type(wiek))
# cena = 32.45
# print (type(cena))
# c = 23-2j
# print (type(c))
# imie = "Janek"
# print (type(imie))
# b = b"x"
# print (b)
# print (type(b))
# czyPelnoletni = True
# print (type(czyPelnoletni))
# n = None
# print (type(n))

#ctrl + /   - komentarz wieloliniowy

####################################Liczby
# cena = 7.6
# cena2 = 7
# print (round(cena))
# print (isinstance(cena,(str,int)))


# #przekonwertowanie, nie zaokrąglenie!
# print (int(cena))

# x = 4
# print (type(x))
# y = ('%.2f' % x)
# print (type(y))

# x = 0.1
# y = 0.1
# #print (x*y)
#
# from decimal import Decimal
# print (type(int(Decimal(str(x))*Decimal(str(y)))))
# print (round(x*y, 2))


############# zmienne proste i przypisywanie id
#zmiennych prostych nie można zmieniać - immutable
# a = "Jan"
# b = a
#
# print (a)
# print (id(a))
#
# print (b)
# print (id(b))

# a = 10
# print (a)
# print (id(a))
# a = 20
# print (a)
# print (id(a))

#Praca domowa
#Za pomocą Python odwołaj się do wartości zapisanej w komórce pamięci (wyszukaj po id)
#zamiana systemó binarnych na dziesiętne i odwrotnie

#należy rozróżnić wynik dizałania funkcji od wyniki zwracaneo przez funkcję

# a=[1,5,2,0]
# #a.sort()
# print (a)
# print(a.sort())

#import sys
#https://bulldogjob.pl/readme/funkcja-id-w-6-kluczowych-koncepcjach-pythona
# wartosc = 25
# komorka = id(wartosc)
# print (komorka)

############# 20240415
############### zmienne jako obiekt
# liczby = [2,6,2,8,5]
# # print(type(liczby))
# # print(isinstance(liczby,int))
#
# ### operacje/metody - jak znaleźć dostępne metody/operacje
# ## dir - dla obiektu
# print(dir(liczby))
# ### help działa bez printa, dla każdej klasy
# help(list)
#
# ##metoda pop
# ##usuwa wartości i ją zwraca

#################typy zmiennych w python - sugestia
#można zasugerować typ zmiennej, ale i tak ją można  zmienić - python nie reaguje
# cena:float
# cena = 34,56
# print(cena)
#
# def (suma(x:int,y:str)):

############Komentarze w Python
#komentarz jednoliniowy
# """
# Komenatrze
# wielliniowe
# """
#
# # komentarze wieloliniowe służą również do zmiennych tekstowych wieloliniowych
# zdanie = """Python jest super
# Python jest super
# Python jest superPython jest super
# Python jest superPython jest super
# Python jest super.
# Python jest super
# """
# print (zdanie)


# ### słowa kluczowe - nie powinno się ich stosować
# #lista słów kluczowych
# import keyword
# print (keyword.kwlist)

# ################## TYP STR
# dane = "Jan Kowalski 20-400"
# # #pojedyncze znaki
# # print(dane[0])
# # #dane[0]="a"
# # #### zakres znaków (zawsze o jedno więcej)
# # print(dane[0:3])
# # #### od końca
# # print(dane[-6:])
# # print(dane[-6:-1])
# # ### od początku bez ostatnich znaków
# # print(dane[0:-7])
# # print(dane[:-3])
# # ## od początku do końca - odwrócenie tekstu - palindromy
# # print (dane[::-1])
#
# # funkcja - obliczanie długości
# print(len(dane))

##### metody na STR
#dane = "PRZYKLADOWY tekst"
#print(dane.lower())

# dane ="jan Kowalski"
# dane1 = dane[0].upper() + dane[1:]
# print (dane1)
#
# print(dane.isupper())

# kodPocztowy = "20)400"
# dowolnyZnak =
# print(kodPocztowy.replace(")","-"))

# dane = "Jan Kowalski Szkola 20 Krakow"
# print(dane.split())
# # dane = "Jan-Kowalski-Szkola-20-Krakow"
# print(dane.split(" ", 2))

# dane = ["mleko","chleb","cebula","pieprz"]
# #doklejenie do spacji kolejne wartości z listy
# daneTekstowe = " ".join(dane)
# print(daneTekstowe)

#usunięcie białych znaków
# dane = " Jan "
# print(dane.strip())

###sprawdzenie czy tekst zaczyna się/kończy na
# dane = "Jan Kowalski."
# # #true or fales - endswitch
# #print(dane.startswith(".",-1))
# print (dane.find("an"))

### wyszukiwanie i pozycja
# dane = "Jan Kowalski"
# # #metoda find zwraca pierwszą szukaną pozycję
# # #znajdzie=index, nie znajdzie=-1
# # print(dane.find("a",5))
# #pozcyja szukanej wartości, ale tylko jak istnieje, w przeciwnym razie wywala błąd
# print(dane.index("a"))

# wiek = "20"
# # #wiek = "20a"
# wiek = "Janek"
##sprawdzenie czy tekst is alpha
# print(wiek.isalpha())
# ##sprawdzenie czy liczba isdigit
# print(wiek.isdigit())
# test = (int(wiek))
# print(type(test))

###OPERATORY
###ARYTMETYCZNE
# x = 5
# y = 3
# print (x+y)
# print (x-y)
# print (x*y)
# #operator * można używać również do serializacji danych
# print(x*"SOS ")
# #dzielenie
# print(x/y)
# #dzielenie całkowite
# print(x//y)
# #potęgowanie
# print(2**3)
# #uwaga (3 i 2 to sa potegi)
# print(2**3**2)
# #reszta z dzielenia
# print(10%4)
# #można wyszukać liczby parzyste/nieparzyste
# #dzielenie przez dwa - wynik 1 nieparzyste, wynik 0 parzyste
# print(12%2)
# print(11%2)
# # print(10%2)
# # #czy liczba jest podzielna przez ...
# print(15%5)
# print(11%2)

#PRZYPISANIA
# x = 5
# #zwiększenie wartości o ...
# #ikrementacja
# x = x + 1
# x += 1
# print (x)
# #dekrementacja
# x -= 1
# print(x)
# x/=2
# print(x)
# x**=2


#PORÓWNANIA
# a=5
# b=10
# print(a>b)
# print(a<=b)
# #porównanie
# print(a==b)
# #różne
# print(a!=b)
# x ="Jan"
# c = x
# print (x)
# print (c)
# print (x==c)
# print (x is c)
# print(id(x))
# print(id(c))
# c = c+"ina"
# print (c)
# c = c[:-3]
# print (x)
# print (c)
# print (x==c)
# print (x is c)
# print(id(x))
# print(id(c))

# #PRZYNALEŻNOŚĆ
#
# print("admin"=="admin" and "12"=="123")
# print("admin"=="admin" or "12"=="123")
#
# print ("cytryna" not in "banan pieprz")
# print ("cytryna" in "banan pieprz")

#BITOWE (TRUE OR FALSE)
# a = 5           #0101
# b = 8           #1000
# print (5&8)     #0000
# print (5|8)     #1101
# print (5^8)     #1101
#
# #negacja bitowa
# print(~0)   #0      0
# print(~1)   #1     10
# print(~2)   #10    11
# print(~3)   #11   100




#https://bulldogjob.pl/readme/funkcja-id-w-6-kluczowych-koncepcjach-pythona
# import ctypes
# szukana_wartosc = 5
# pamiec = id(szukana_wartosc)
#ctypes bibilitema, cast funkcja, atrybut py_object (wyłąniamy obiekt)
# wynik = ctypes.cast(pamiec, ctypes.py_object).value
# print (wynik)

## trwałe usunięcie obiekut
#del szukana_wartosc

## przekompiluj program app.py do pliku app.exe
## w cmd
# pip install pyinstaller
#do zmiennych środowiskowych dodać ścieżkę
## w cmd
##pyinstaller -onefile app.py
## w folderze dist plik exe


#####################znaki uft8
#aby wstawić kod znaku "\u"
# print("\u03A9")
# #funkcja zmiana liczby na znak
# print (chr(126))

#ćwiczenie 1
#zaokrąglanie round liczb
# decimal_number = 10.7865512345
# print (type(decimal_number))
# #from decimal import Decimal
# print (round(decimal_number, 2))
# print ('%.2f' % decimal_number)

#ćwiczenie 2
# x = 5
# y = 2
# z = 10
#
# a = (x+y)*z
# print (a)
# b = x*z+y*z
# print (b)
#
# c = ((x+y)*z) == (x*z+y*z)
#
# print (c)
# #czy ten sam obiekt
# print (a is b)
# #czy ta sama wartość
# print (a==b)

#ćwiczenie 3
# length = 4
# width = 2
# pole = 4*2
# print (pole)
# print ("Pole prostokąta wynosi: ", pole)
#
# import math
# radius = 2
# obwod = round(2*math.pi*radius,2)
# print ("Obwód koła wynosi: ", obwod)
#
# a = 2
# b = 3
# srednia = (a+b)/2
# print ("Średnia arytmetyczna wynosi: ", srednia)


#ćwiczenie 4
#konwersja liczb
# num = 4
# numFloat = float(num)
# print ("Liczba zmiennoprzecinkowa: ", numFloat)
#
# float_num = 10.12
# int_num = int(float_num)
# print ("Liczba całkowita: ", int_num)

#Wyświetlanie informacji na ekranie
# wiek = 20
# imie = "Jan"
#
# #wyświetlanie bez formatowania. Spacje po zmiennych...
# print("Nazywam się",imie,". Mam", wiek,"lat")
# #podstawianie zmiennych w tekście %s - formatowanie
# print("Nazywam się %s. Mam %s lat." %(imie,wiek))
# #formaotowanie za pomocą funkcji formant (wstawiania args [same wartości] lub kwargs[elementy nazwanne z wartościami])
# print("Nazywam się {0}. Mam {1} lat.".format(imie,wiek))
# print("Nazywam się {0}. Mam {wiek} lat.".format(imie,wiek=wiek))
# print("Nazywam się {0}. Mam {wiek} lat.".format(imie,wiek=50))
# #interpolacja
# print(f"Nazywam się {imie}. Mam {wiek} lat")
# print(f"Nazywam się {imie}. Mam {wiek+1} lat")
# #konkatonacja
# print("Nazywam się "+imie+". Mam "+str(wiek)+" lat.")

# #ćwiczenie 6
# #data urodzenia a rok przestępny
# bicieMinuta = 72
# wiek = 70
# dniRok = 365
# godzinaDzien = 24
# minutaGodzina = 60
# bicieSerca = bicieMinuta*wiek*dniRok*godzinaDzien*minutaGodzina
# print (f"Serce 70-latka ma za sobą {bicieSerca} uderzeń")

#ćwiczenie 7
# cenaPizzy1 = 5
# cenaPizzy2 = 20
# radiusPizzy1 = 2
# radiusPizzy2 = 5
# import math
# polePizzy1 = math.pi*radiusPizzy1**2
# polePizzy2 = math.pi*radiusPizzy2**2
# wynikPizza1 = polePizzy1/cenaPizzy1
# wynikPizza2 = polePizzy2/cenaPizzy2
#
# oplacalnoscPizzy1 = wynikPizza1>wynikPizza2
# print (f"Pizza nr 1 jest bardziej opłacalna: {oplacalnoscPizzy1}")

# #Ćwiczenie 8
# wyraz = "czyJestemPalindromem"
# Palindrom = wyraz == (wyraz[::-1])
# print (f"Wyraz {wyraz} jest palindromem: {Palindrom}")

#Ćwiczenie 9
# kodPocztowy = "123456"
# poprawnyKodPoczotwy = (kodPocztowy.replace(kodPocztowy[2],"-"))
# print (poprawnyKodPoczotwy)

# #Ćwiczenie 10
# zdanie = "jan Kowalski"
# print(zdanie[0].isupper())


#### Instrukcja if
# if warunek:
#     #Blok kod
# else:
#     #Blok kod

#Instrukcje warunkowe = IF
#wiek = 10
#brak operator -> zmiana zmiennej na bool, sprawdzenie czy wartość T czy F.
# W przypadku liczb: 0 != True
# if wiek:
#     print("Osoba pełnoletnia")

# if wiek>=18:
#     print("Osoba pełnoletnia")
#     print ("Osoba ma 18 lat")
#
# elif wiek>0 and wiek<18:
#     print("Osoba niepełnoletnia")
#
# else:
#     print ("Nieprawidłowe dane")

# x=4.1874
# print(x)
# print ('%.20f' % x)
# y = "testowy tekst"
# print ('Odpowiedż to % s' % y)
# import math
# c1 = 5
# c2 = 10
# r1 = 5
# r2 = 5
# p1 = math.pi*r1**2
# p2 = math.pi*r2**2
# s1 = p1/c1
# s2 = p2/c2
# # if (s1> s2):
# #     print ("pizza1 tańsza od pizza2");
# # else:
# #     print("pizza2 tańsza od pizza1");
# slownik = dict();
# slownik['pizza1'] = s1
# slownik['pizza2'] = s2
# print (slownik)

# kod = 123456
# zmiana = str(kod).replace(str(kod)[2], "-")
# print (zmiana)

# zdanie = "to Jest przykład"
# print (zdanie[0].isupper())

##########################Pętle while
#każda zmienna, która jest równa 0 lub wartość pusta "" jest FALSE
#licznik/counter
# a = 0
# while a<10:
#     print (a)
#     a+=1

# login = input("Podaj login")
# while login != "admin":
#     login = input("Podaj poprawny login")
#     #break
# else:
#     print ("Login prawidłowy")

###########pętle for
#iteracja/powtarzanie po jakiejś sekwencji
# dane = "Jan Kowalski"
#
# for litera in dane:
#     print (litera)

# produkty =["mleko", "pieprz", "cytryna", "pomidor"]
# for produkt in produkty:
#     print (produkt)

#funkcja range - zakresy
# print(list(range(10)))
# print(list(range(5,10)))
# print(list(range(5,20,3)))

#kolejny licznik
# for i in range(10):
#     print (i,"Python")

# produkty =["mleko", "pieprz", "cytryna", "pomidor"]
# for produkt in produkty:
#     if produkt in ("cytryna", "pieprz"):
# #         #zakońćzenie pętli
# #         #break
# #         #pomijanie danych instrukcji
#         continue
#     print (produkt)

# #pętla zagnieżdżona
# for x in range(5):
#     #end - usunięcie tworzenia nowego wiersza
#     print (x, end=" ")
#     for y in range(5):
#         print (y, end="")
#     #przejście do nowego wiersza
#     print()

#analiza dynamiczna kodów - wartości i typów zmiennyc - debuger

# #listy wielowymiarowe
# listaWielowymiarowa = [[1,2,3],[4,5,6],[7,8,9]]
# for x in listaWielowymiarowa:
#     print (x)
#     for y in x:
#         print(y)



#praca domowa
#Utwórz tabliczkę mnożenia za pomocą pętli zagnieżdżonej
# 1   2   3   4
# 2   4   6   8
# 3   6   9   12
# 4   8   12  16

#Pętla i funkcja enumerate()
# produkty = ["mleko","papier","cukier","pieprz"]
# print (len(produkty))
#
# for p in range (len(produkty)):
#     print(p,produkty[p])
#
# #tutaj brak indexu, potrzebny inny licznik
# for p in produkty:
#     print(p)

# tupla - indeks:element
# print (list(enumerate(produkty)))
# print (enumerate(produkty))

# lista = ['a', 'b', 'c', 'd']
# for indeks, element in enumerate(lista):
#     print(indeks, element)
#
# for x,y in enumerate(produkty):
#     print (x,y)

#listy składane
# liczby = [1,2,3,4,5]
# parzyste = [x*2 for x in liczby if x%2==0]
# print (parzyste)

# slowo = "python"
# duze_litery = [litera.upper() for litera in slowo]
# print(duze_litery)

#print([x for x in range(1,6)])
#
#print([[y for y in range (1,4)] for x in range(5)])

#praca domowa
#napisz generator losowych haseł - pętla, tabel ascii, potrzebny moduł

# cyfry = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
# for a in cyfry:
#     for b in cyfry:
#         print (a, "*", b, "=", a*b)

# liczby = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# nieparzyste = [x for x in liczby if x % 2]
# print(nieparzyste)

# for i in range (10,0,-3):
#     print (i)


#Ćwiczenie 11
# a = 10
# licznik = 0
# while a<=10 and a>0:
#     licznik += 1
#     #print(f"To jest licznik {licznik}")
#     if licznik == 3:
#         licznik = 0
#     else:
#         print(a)
#     a-=1
#
# licznik = 0
# for x in range (10,0,-1):
#     licznik+=1
#     if licznik == 3:
#         licznik = 0
#         continue
#     print (x)

# izogram = input("Podaj słowo, a my sprawdzimy czy to słowo jest izogramem: ")
# listaUnikalna = list(set(izogram))
# if len(list(izogram)) == len(list(set(izogram))):
#     print ("Tak")
# else:
#     print ("Nie")

#ćwiczenie 12
# izogram = "skrzynia"
#można tez sprawdzić czy znak jest unikatowy
# izogram = input("Podaj słowo, a my sprawdzimy czy to słowo jest izogramem: ")
#
# for x in izogram:
#     liczbaPowtorzen = izogram.count(x)
#     if liczbaPowtorzen > 1:
#         print(f"Słowo {izogram} nie jest izogramem. Litera {x} się powtarza")
#         break
# else:
#     print(f"Słowo {izogram} jest izogramem.")

#Ćwiczenie 13
# waga = input("Podaj swoją wagę: ")
# wzrost = input("Podaj swój wzrost: ")
# BMI = float(waga)/(float((wzrost))**2)
# if BMI <=18:
#     print(f"Niedowaga")
# elif BMI > 17 and BMI <=24:
#     print(f"Norma")
# elif BMI > 24 and BMI <=29:
#     print(f"Nadwaga")
# elif BMI > 29 and BMI <=39:
#     print(f"Otyłość")
# else:
#     print(f"Poważna otyłość")
#
#Praca domowa 5
#Pobierz cenę netto od użytkownika i wyświetl cenę brutto
#zabezpiecz program przed podaniem błędnej ceny (operacja na tekście i instrukcje warunkowe)

#Ćwiczenie 14
# lista = [42, 13, 5, 7, 12, 3, 8]
# licznik = 0
# dlugosc = len(lista)
# for i in lista:
#     for j in lista:
#         if i > j:
#             licznik = 0
#             break
#         licznik += 1
#         if licznik == dlugosc:
#             print (lista.index(i))

# for i in range (10,0,-3):
#     print (i)

#ZMIENNE ZŁOŻONE
#LISTY (LIST) TABLICE []
# dane = []
# print (dane)
# print (type(dane))
#dane = [1,2,3,4,"A","Jan",["ser", "mąka"]]
# print (dane)
# #wynik to string
# print (dane[5])
# #wynik to int
# print (dane[1])
# #wynik to lista
# print (dane[6])
# #wynik to string z podlisty
# print (dane[6][0])
# #sprawadzanie czy element z listy jest listą
# if isinstance(dane[1], list):
#     for i in dane[1]:
#         print(i)

# dane[0]=10
# print (dane)

#LISTY (LIST) metody na listac
# produkty = ["mleko","chleb","cebula","czosnek","papier"]
# nowa = sorted(produkty)
# print (produkty)
# print (nowa)
# #dodanie elementu do listy - metody zawszez coś zwracają, jeśli metoda jest działaniem, to zawsze zwraca None
# produkty.append("mleko")
# print (produkty.index("cebula"))
# # #usuwanie i zwrocenie elemntu
#print(produkty.pop(1))
#
# #tworzenie kopii
#kopia = produkty.copy()
# print(kopia)
# #czyszczenie kopii
#kopia.clear()
# print(kopia)
#
# #liczenie ile razy dany element jest na liście
#
# print(produkty.count("papier"))
#
# #iteracja, łaczenie dwóch list
# produkty2 = ["banan","kiwi"]
# #produkty.extend(produkty2)
# nowe = list(zip(produkty,produkty2))
# print (nowe)
# # produkty.extend([produkty2[1]])
# print(produkty)

# #dodanie elementu na konkretne miejsce na liście
# produkty.insert(2,"rolka")
# print (produkty)
#
# #usuwanie
# produkty.remove("rolka")
# print (produkty)
#
# #sortowanie
# produkty.sort()
# print (produkty)
# produkty.sort(reverse=True)
# print (produkty)
#
# #funkcja sorted, sortuje w danym miejscu, nie na trwale, tak jak metoda
# posortowanaLista = sorted(produkty)
# print (posortowanaLista)

#funkcja zip - 2 lub wiecej list i tworzy sekwencje, tuple, zip tworzy obiekt tupli
# miesiace = ["I", "II", "III", "IV"]
# dni = [31,28,31]
# miesiaceDni = zip(miesiace,dni)
# print (miesiaceDni)
# print(list(miesiaceDni))
# print (type(miesiaceDni))
# for i in miesiaceDni:
#     print(i)

# liczby = [1,2,3,4,5]
# print(3 in liczby)

#słowniki
#listy słownikowe nie maja indeksu, mamy klucze
# produktyCeny = {}
# produktyCeny = {0:5,"chleb":7,"Ser":2,"nabiał":[{"a":1},"mleko","śmietana"]}
# print(produktyCeny["chleb"])
# print(produktyCeny["nabiał"][0])
# print(produktyCeny["nabiał"][0]["a"])
#
# #dodanie nowego klucza - TYLKO JEŚLI TEGO PRODUKTU NIE MA, JAK JEST TO AKTUALIZACJA DANYCH
# produktyCeny["nowe"]=10
# print(produktyCeny)
# #zwraca wartości dla klucza, jak nie ma klucza, to zwraca None
# print(produktyCeny.get("mleko"))
#
# #lista kluczy ze słownika
# print (list((produktyCeny.keys())))
# #lista wartości ze słownika
# print (produktyCeny.values())
# #lista wartości i kluczy ze słownika
# print (produktyCeny.items())
#

# # Iteracja po kluczach
# slownik = {1:23, 2:22, 3:33}
#
# for klucz in slownik:
#     print(klucz)
# # Iteracja po wartościach
# for wartosc in slownik.values():
#     print(wartosc)
# # Iteracja po parach klucz-wartość
# for klucz, wartosc in slownik.items():
#     print(f'Klucz: {klucz}, Wartość: {wartosc}')

# for i in produktyCeny:
#     print(i, produktyCeny[i])
#
# for i in produktyCeny.keys():
#     print(i)
#
# for i in produktyCeny.values():
#     print(i)
#
# for i in produktyCeny.items():
#     print(i)
#
# for i,z in produktyCeny.items():
#     print(i,z)

#produktyCeny = {0:5,"chleb":7,"Ser":2,"nabiał":[{"a":1},"mleko","śmietana"]}
# # #dodawanie do listy, jesli nie ma klucza na liscie
# produktyCeny.setdefault("chleb",10)
# produktyCeny.setdefault("cytryny",10)
# print(produktyCeny)
#
# # usuwanie całego elementu/parę z listy
#print(produktyCeny.pop(0))
#print(produktyCeny.popitem())
#print(produktyCeny)
# #
# #lista
# produkty = ["mleko","ser","masło"]
# # # tworzenie słownika z lisy kluczy
# produktyCeny = dict.fromkeys(produkty,None)
# print (produktyCeny)

#wyznaczenie liczb pierwszych, to te co dzielą się przez 1 i przez same siebie

# # praca domowa 3
# #tabliczka mnożenia
# zakres = range(1,11)
# for x in zakres:
#     for y in zakres:
#         wynik = y*x
#         print(wynik, end="\t")
#     print()

# praca domowa
# #napisz generator losowych haseł - pętla, tabel ascii, potrzebny moduł
# import string
# import random
# dlugosc_hasla = 10
# zestaw_znakow = string.ascii_letters
#
# haslo =""
# for x in range (dlugosc_hasla):
#     x = random.choice(zestaw_znakow)
#     haslo += x
# print(f"Twoje nowe hasło to: {haslo}")

# lista = []
# wynik =""
# for x in range (dlugosc_hasla):
#     x = random.choice(zestaw_znakow)
#     lista.append(x)
#     wynik = "".join(lista)
# print(f"Twoje nowe hasło to: {wynik}")

# praca domowa 5
#metody na tekscie
#właściwość tekstu
#instrukcja warunkowa
#bazowanie na tym że tekst
# vat = 23
# cena_netto = input("Podaj cenę netto")

# while True:
#     try:
#         stawka_vat = (float(cena_netto) * vat) / 100
#         cena_brutto = round(float(cena_netto) + stawka_vat,2)
#         print(f"Cena brutto produktu wynosi: {cena_brutto} złotych.")
#         break
#     except:
#         cena_netto = input("Podałeś cenę netto w złym formacie. Przykładowy format to 5.5. Spróbuj podać jeszcze raz cenę: ")

#zmienna  KROTKA TUPLE jest stała! nie można jej zmieniać
#tupla z lub bez ()
#jak stowrzymy pustą tuplę,  to nie będzi emożna jej zmodyfikwoać
# dane = ("lp","imie","nazwisko")
# print (dane)
# print (type(dane))
# #indeks
# print (dane[1])
#
# pi = (3.14,)
# print (pi)
# print (type(pi[0]))

#możliwość podmiany wartości bez tworzenia zmiennej pomocniczej
#wykorzystanie typu tupli w locie
# x = 10
# y = 20
# x,y = y,x

# rozpakowana_krotka = (4, 5, 6)
# x, y, z = rozpakowana_krotka
# print (x)

#rozpakowywanie tupli - unpacking - przypisywanie wartości krotki do zmiennych
#pierwszy sposób
# dane = (4,5,6)
# x,y,z = dane
# print (x,y,z)
# #drugi sposób
# def wartosci():
#     return 3,4,5
#
# x,y,z = wartosci()

# dane = 1,2,3,4,5
# #tworzenie listy z tupli
# x,*y,z = dane
# print (x)
# print (type(y))
# print (y)


# #pakowanie tupli - z wykorzystaniem *
# # * daje nam wiele danych
# dodatkoweDane = 6,7,8
# noweDane = (1,2,3, *dodatkoweDane)
# print (noweDane)
# print (*dodatkoweDane)

#funkcja set - zbiór danych - wyszukanie unikatowych danych
# imiona = set()
# print(type(imiona))

# imiona = {"Jan", "Ola", "Jan", "Ola", "Ela", "Adam"}
# print (imiona)
# print(type(imiona))

# dane = {1,2,3,4,5}
# # print (dane)
# #
# dane.remove(8)
# print (dane)
#
# dane.add(5)
# print(dane)

# #operacje na zbiorach
# klasaA = {"Jan", "Ola", "Jan", "Adam"}
# klasaB = {"Jan", "Ula", "Ola", "Tomasz", "Ewa"}

# print(klasaA)
# print(klasaB)
# #część wspólna zbiorów (elementy powtarzające się w dwóch zbiorach)
# print(klasaA & klasaB)
# #unikalna lista, suma zbiorów
# print(klasaA | klasaB)
# #element z A, którego nie ma w B
# print(klasaA - klasaB)
# #eleemnty unikalne z dwóch list / róznica zbiorów, róznica symetryczna
# print(klasaA ^ klasaB)
# print (klasaA.symmetric_difference(klasaB))

#Ćwiczenie18
# kraje = {"PL":"Duda","USA":"Trump"}
# for x,y in kraje.items():
#     print(x,y)
#
# for i in kraje:
#     print(i, kraje[i])
#
# for x in kraje.values():
#     print(x)

#Ćwiczenie19
# wyniki = [['Kowalski', 90, 86, 93],['Nowak', 76, 64, 78],['Kwiatkowski', 82, 82, 87]]
# print (wyniki[0])
#
# for x in wyniki:
#     print (x[0])
#
# print (wyniki[1][1:])
#


#Ćwiczenie20
# mojaLista = [22,26,159]
# listaZnakow = []
# for x in mojaLista:
#     znaki = list(str(x))
#     listaZnakow.extend(znaki)
# print (listaZnakow)

# Ćwiczenie 21
# liczby = [[1, 2, 3, 4], [5, 6], [7, 8, 9]]
# suma = 0
# for i in liczby:
#     for j in i:
#         suma += j
# print (suma)

# suma = 0
# for i in liczby:
#     if len(i)>=3:
#         suma+=i[2]
# print (suma)

#Ćwiczenie 22
# zakupy = ["mleko", "chleb", "jajka"]
# zakupy.append("cytryna")
# zakupy.remove("mleko")
# zakupy.pop(1)
# print (zakupy)

#flynerd

#Ćwiczenie 23
# ocenyFilmow = {"Film1":4, "Film2":7, "Film3":10, "Film4":1}
# dobreFilmy = {}
# for i in ocenyFilmow:
#     print (i, ocenyFilmow[i])
#     if ocenyFilmow[i] > 5:
#         #dodawanie do ????????????
#         dobreFilmy[i] = ocenyFilmow[i]
# print (dobreFilmy)

#praca domowa 5
# vat = 23
# cena_netto = input("Podaj cenę netto")
# while True:
#     if cena_netto.isdigit():
#         cena_netto_float = float(cena_netto)
#         stawka_vat = (cena_netto_float * vat) / 100
#         cena_brutto = round(cena_netto_float + stawka_vat,2)
#         print(f"Cena brutto produktu wynosi: {cena_brutto} złotych.")
#         break
#     elif "." in cena_netto:
#         cena_netto_kropka = cena_netto.replace(".","")
#         if cena_netto_kropka.isdigit():
#             cena_netto_float = float(cena_netto)
#             stawka_vat = (cena_netto_float * vat) / 100
#             cena_brutto = round(cena_netto_float + stawka_vat, 2)
#             print(f"Cena brutto produktu wynosi: {cena_brutto} złotych.")
#             break
#     else:
#         cena_netto = input("Podałeś cenę netto w złym formacie. Przykładowy format to 5.5. Spróbuj podać jeszcze raz cenę: ")



# wyniki = [['Kowalski', 90, 86, 93],[88,'Nowak', 76, 64.5, 78],['Kwiatkowski', 82, 82, 87]]
# for x in wyniki[1]:
#     if str(x).isdigit():
#         print(x)
#     elif "." in str(x):
#         y = str(x).replace(".","")
#         if y.isdigit():
#             print (x)

# #Ćwiczenie 24
# infoGeograficzne = ("Warszawa", 52.1, 21.2)
# nazwa, szerGeogr, dlGeogr = infoGeograficzne
# print (f"Informacje o mieście {nazwa}: szerokość geograficzna {szerGeogr}, długość geograficzna {dlGeogr}")

# #Ćwiczenie 25
# #(miasto, temperatura, warunki atmosferyczne)
# waw = ("Warszawa", 21, "dobre")
# lbn = ("Lublin", 25, "bardzo dobre")
# krk = ("Kraków", 18, "złe")
#
# listaMiast = [waw, lbn, krk]
# listaTemp = [waw[1], lbn[1], krk[1]]
# listaTemp.sort()
# for i in listaMiast:
#     if i[1] == listaTemp[0]:
#         print (f"{i[0]} jest najchłodniejszym miejscem")
#     elif i[1] == listaTemp[2]:
#         print (f"{i[0]} jest najcieplejszym miejscem")

# #Ćwiczenie 26
# katalog = {"Pan Tadeusz":"Mickiewicz"}
# katalog.update({"Potop":"Sienkiewicz"})
# katalog.setdefault("Lalka","Prus")
# katalog.pop("Potop")
# print (katalog)

#Ćwiczenie 27
# zadania = {"sprzątanie":"do wykonania", "gotowanie":"do wykonania","nauka":"do wykonania"}
# zadania["nauka"] = "wykonane"
# zadania["basen"] = "do wykonania"
# for i in zadania:
#     if zadania[i] == "do wykonania":
#         print (i)
# for i, j in zadania.items():
#     if j == "do wykonania": print (i)

# #Ćwiczenia 28
# lista = ["chleb", "jabłko", "chleb", "banan", "mleko"]
# elementDoUsuniecia = "chleb"
# for i in lista:
#     if i == elementDoUsuniecia:
#         lista.remove(i)
# print (lista)

# #Ćwiczenie 29
# z1 = set()
# z2 = set()
# z1_nowe = ("chleb","masło","mleko")
# z2_nowe = ("chleb", "masło", "cukier", "sól")
# z1.update(z1_nowe)
# z2.update(z2_nowe)
# print (z1.intersection(z2))
# print (z1.difference(z2))
# print (z1.union(z2))

#drukowanie danych w konsoli print
# sep = ","
# end = "!\n"
# tekst = "Dziś, jest ładny dzień"
# a=10
# b=20
# print (tekst, a, b, sep = ", ", end = "!\n")
#interpolacja stringów
#dowania pustych znaków, wyrównanie tekstu
# name = "Alicja"
# print (f"|{name:10}|")
# print (f"|{name:2}|")
# print (f"|{name:>10}|")
# print (f"|{name:^10}|")

# pi = 3.143543453543
# #wartosci  z przecinkiem
# print (f"{pi:.3}")
# #wartosci po przecinku
# print (f"{pi:.3f}")

# procent = 0.75
# print (f"{procent:.2%}")
# print (f"{procent:.0%}")

#wprowadzanie danych
#parametry listy poleceń
# import sys
# parametry = sys.argv[0]
# print(parametry)

#funkcje
#argument to wartosc
#parametr to nazwa
# def suma ():
#     print (10+20)
# suma()
# suma()

# def suma (x,y):
#     print (x+y)
#
# print (suma (5,10))

#funkcje kończy się na return

# def suma(x,y):
#     suma = x+y
#     return suma
# print(suma(10,20))

#parametry funkcji
# def pokaz(x,y,z):
#     print (x,y,z)
# pokaz(10,20,30)
# pokaz(y=20,x=10, z=30)
# pokaz(10,20, z= 30)

#parametry domyślne
# def os (x,y,z=0):
#     print(x,y,z)
#
# os (1,2)

#funkcje z dowolną liczbą argumentow args
#wynik to tupla
# def suma(*x):
#     print (x)
# suma(1,2)

#funkcja z dowolną liczbą argumentów nazwanych kwargs
#wynik to słownik
# def suma (**x):
#     print(x)
# suma(mleko=10,chleb=8)

# napisz funkcję pobierającą jako argymenty ceny oraz nazwy i ceny a następnie zliczającą sumę wszystkich
# def sumaCen(*x,**y):
#     wynik = 0
#     for i in x:
#         wynik += i
#     for j,k in y.items():
#         wynik += k
#     print (wynik)
# sumaCen(5,10,mleko=2, cukier=5)

#zasiegi funkcji: lokalny, zagnieżdżony i globalny
#lokalny x
# def pokaz():
#     x = 10 #zasieg lokalny
#     print (x)
# pokaz()
#
# #globalny x
# def pokaz():
#     global x #utworzenie zasiegu globalnego
#     x = 10 #zasieg globalnego
#     print (x)
# pokaz()
#
# x = 10 #zasieg globalnego
# def pokaz():
#     print (x)
# pokaz()

#zasieg zagniezdzony x
# def zew():
#     x = 10
#     def wew():
#         print (x)
#     wew ()
# zew()

#funkcje zagnieżdżone
# def funkcja_a():
#     print ("To jest funkcja A")
#
# def funkcja_b():
#     print("To jest funkcja B")
#
# def wybierz_funkcje(flaga):
#     if flaga:
#         return funkcja_a
#     else:
#         return funkcja_b
#
# wybrana_funkcja = wybierz_funkcje(True)
# wybrana_funkcja()
# wybierz_funkcje(True)()

# def generuj_funkcje(mnoznik):
#     def funkcja_wew(x):
#         return x*mnoznik
#     return funkcja_wew

#print(generuj_funkcje(2)(4))
# podwojenie = generuj_funkcje(2)
# print(podwojenie(4))

# x = 5 # Zmienna globalna
# def moja_funkcja():
#     global x # Deklaracja, że będziemy modyfikować globalną zmienną x
#     x = 10 # Modyfikacja zmiennej globalnej
#
# moja_funkcja()
# print(x)


# #Ćwiczenie 37
# def sumaWartosci (*wartosci, **wartosciOpis):
#     wynik = 0
#     for x in wartosci:
#         wynik += x
#     for y in wartosciOpis:
#         wynik += wartosciOpis[y]
#     print (wynik)
# sumaWartosci(1,2,3,4, mleko = 5, papier = 10)
# #
# #Ćwiczenie 38
# def suma (*wartosci):
#     wynik = 0
#     for x in wartosci:
#         wynik += x
#     print (wynik)
# suma(1,2,3,4,5,6,7,8,9)
#
# #Ćwiczenie 40
# def policzSamogloski (tekst):
#     samogloski = set("aeoiu")
#     licznik = 0
#     for i in tekst.lower():
#         print (i)
#         if i in samogloski:
#             licznik += 1
#     print (licznik)
# policzSamogloski("hejA")
#
# #Ćwiczenie 41
# def losowanie ():
#     import random
#     wylosowane = []
#     for x in range (10):
#         x = random.choice(range(0,10))
#         if x not in wylosowane:
#             wylosowane.append(x)
#         else:
#             print("Oh no! I repeated myself!")
#             break
# losowanie()

#wbudowane funkcje:eval(), exec(), globals(),compile()
#eval()
#interpretacja tekstu jednoliniowego jako kodu pythona i jej wykonanie
# a = 10
# zrodlo = "a+2"
# wynik = eval(zrodlo)
# print (wynik)
#globals()
# #słownik zmiennych z modułu
# #bepieczeństwo aplikacji
#print(globals())

#exec() - interpretacja tekstu wielliniowego jako kody pythona i jej wykonanie
# zrodlo = """
# a = 10
# print ("Python")
# """
# exec(zrodlo)
# print (a)

#compile() - zwiekszenie wydajnosci, zmiana na postac bajtowa
# import time #jak długo będzie wykonywało się źródło
# zrodlo = "a+=1"
# a = 0
# start = time.time()
# for i in range(100000):
#     exec(zrodlo)
# stop = time.time()
# czas1 = stop-start
# print(czas1)
#
# start2 = time.time()
# zrodloKompilowanie = compile(zrodlo,"opcja","exec")
# for i in range(100000):
#     exec(zrodloKompilowanie)
# stop2 = time.time()
# czas2 = stop2-start2
# print(czas2)

#Cwiczenie 42
# def liczenie (operator: str,*wartosci):
#     wynik = 0
#     if operator == "+":
#         for x in wartosci:
#             wynik += x
#     elif operator == "-":
#         wynik = wartosci[0]
#         for x in wartosci[1:]:
#             wynik -= x
#     else:
#         print ("Błędny operator")
#     print (wynik)
# liczenie ("-",2,3)

#Ćwiczenie 43
# import random #losowanie wartosci/liczb
# haslo = ""
# for i in range(10):
#     #chr zmiana liczby na znaki
#     haslo += (chr(random.randint(33,126)))
# print (haslo)

#Importowanie modułów i pakietów
# import matematyka.dzialania as dz #z aliasem
# print (dz.suma(5,6))
# dz.roznica(5,6)
# print(dz.autor)


#import wszystkiego
#import wybranych funkcji///
# from  dzialania import suma,autor
# print(suma(5,6)

#gdzie suzkac modulow
# import sys
# #lista sciezek w ktorych szuka python - kolejnosc
# print (sys.path)
#
# import random
# print (random.__file__)

#pakiet (jak folder) -> moduły (jak pliki)
# import matematyka.dzialania
# from  matematyka import dzialania
# import matematyka.dzialania as md
# md.suma()

#pip instal flask - w terminalu
#import flask

#wyjatki
#przyklady bledow
# a = 10
# liczby = [1,0,3]
# for i in liczby:
#     print(a/i)

# imie = "Jan"
# print(imie1)
#
# class OSOBA:
#     pass
# print (OSOBA.imie)

#oblsuga wyjatkow
#try except
# a = 10
# liczby = [1,0,3]
# for i in liczby:
#     try:
#         wynik = a/i
#     except (ZeroDivisionError,NameError):
#         print("błąd dzielenia przez 0")
#         continue
#     print (wynik)


# a = 10
# liczby = [1,0,3]
# for i in liczby:
#     try:
#         wynik = a/i
#         print(wynik)
#         liczby[10]
#         B
#     except ZeroDivisionError:
#         print("błąd dzielenia przez 0")
#         continue
#     except NameError:
#         print("Brak zmiennej")
#         continue
#     except:
#         continue

# a = 10
# liczby = [1,0,3]
# for i in liczby:
#     try:
#         wynik = a/i
#         print(wynik)
#     except ZeroDivisionError:
#         print("błąd dzielenia przez 0")
#         continue
#     except ArithmeticError:
#         print("błąd")
#         continue


# try:
#     10/0
# except Exception as err:
#     print(err.__reduce__())

#jak sprawzic w ktorej liii pojawil sie blad
# import sys
# import os
# try:
#     raise ValueError("Błedna wartosc")
# except ValueError as e:
#     typ, obiekt, obiekt2 = sys.exc_info()
#     print (typ, obiekt, obiekt2)
#
#     nazwaPliku = os.path.split(obiekt2.tb_frame.f_code.co_filename)[1]
#     print(nazwaPliku)
#     numerLinii = obiekt2.tb_lineno
#     print(numerLinii)

#finaly - mimo  błedu program pojdzie
# try:
#     file = open("dane.txt","w")
#     file.write("Jan Kowalski")
# except IOError:
#     print("Wystąpił błąd podczas przetwarzania pliku")
# #zawsze zostanie wykonane
# finally:
#     print ("plik został zamknięty")
#     file.close()

# raise, nie obsługuje wyjątków, ale powiadomienie o wyjątku
# a=10
# liczby = [1,0,3]
# for i in liczby:
#     if i == 0:
#         raise ValueError("Błąd - dzielnik nie może byc 0")
#     print (a/i)

#Ćwiczenie 45
# from datetime import datetime
# wprowadzonaData = input("Wprowadź datę w formacie dd.mm.rrrr")
# if len(wprowadzonaData) != 10 or wprowadzonaData[2]!= "." or wprowadzonaData[5]!= ".":
#     raise ValueError("Błędny format daty")
# try:
#     dzien = int(wprowadzonaData[:2])
#     miesiac = int(wprowadzonaData[3:5])
#     rok = int(wprowadzonaData[6:])
#     print (datetime(rok,miesiac,dzien))
# except:
#     raise ValueError("Błędne dane w dacie")

#operacje na plikach
#odczyt danych z pliku
#wymaga zamkniecia
# f = open("dane.txt")
# f.close()

#automatycmie sie zamknie
# with open("dane.txt", encoding="UTF-8") as f:
#     #print(f) #dane o obiekcie
#     #czytanie linii
#     print(f.readline(), end="")
#     print(f.readline(), end="")
#     print(f.readline(), end="")
#     print(f.readline(), end="")
#
# with open("dane.txt", encoding="UTF-8") as f:
#     linia = f.readline()
#     while linia:
#         print (linia, end="")
#         linia= f.readline()


# with open("dane.txt", encoding="UTF-8") as f:
#     linia = f.readline()
#     licznik = 0
#     while linia:
#         if licznik == 2:
#             print(linia[2])
#         print (linia, end="")
#         linia= f.readline()
#         licznik += 1

#praca domowa - ćwiczenie 47
#Napisz funkcję, która zwróci 5 najczęstszych słów z dzieła Mickiewicza.
# https://pastebin.com/raw/aAHeW5Pt (przekopiuj i zapisz do pliku tekstowego to,
# co znajdziesz pod tym linkiem).
#Podpowiedź: skorzystaj z funkcji open(), metody split(), słownika oraz pętli.

# import cwicz44
# print (cwicz44.lista)
# print(cwicz44.check_list(5))

# def liczenieSlow (nazwaPliku):
#     listaSlow = []
#     slownik = {}
#     listaNowa = []
#     with open(nazwaPliku, encoding="UTF-8") as f:
#         linia = f.readline()
#         while linia:
#             listaSlow.extend(linia.split())
#             linia= f.readline()
#     unikalnaListaSlow = set(listaSlow)
#     for slowo in unikalnaListaSlow:
#         liczbaPowtorzen = listaSlow.count(slowo)
#         slownik[slowo] = liczbaPowtorzen
#     for i,j in slownik.items():
#         if j in sorted(list(slownik.values()),reverse=True)[:5]:
#             x = (j,i)
#             listaNowa.append(x)
#     for i,j in sorted(listaNowa, reverse=True):
#         print (j)
# liczenieSlow("Mickiewicz.txt")

#wczytanie pliku/txt - drugi sposób
# with open("dane.txt", encoding = "UTF8") as f:
#     linie = f.readlines()
#     print (linie)
#     for i in linie:
#         print (i.rstrip())

# #wczytanie pliku/txt - trzeci sposób
# with open ("dane.txt", encoding = "UTF8") as f:
#     for linia in f:
#         print (linia.rstrip())

#zapis danych do pliku
#w - nadpisywanie danych w pliku
#a - aktualizacja danych w pliku - tryb przyrostowy
# with open ("dane.txt", "a", encoding = "UTF8") as f:
#     f.write("\nAdam Cichosz")

# lista = ["trener", "informatyk", "nauczyciel"]
# with open ("dane.txt", "w", encoding = "UTF8") as f:
#     f.writelines ("\n".join(lista))
#
# slownik = {"trener":1, "informatyk":2, "nauczyciel":3}
# with open ("dane.txt", "w", encoding = "UTF8") as f:
#     f.writelines (slownik)

# #Ćwiczenie 46
# zawody = ["trener", "informatyk", "nauczyciel"]
# with open ("zawody.txt", "w", encoding = "UTF8") as f:
#     f.writelines (", ".join(zawody))

#Programowanie obiektowe - łaczy ze sobą stan obiektu i metody (możliwości działania na obiekcie)
#bez konstruktora -  nie można podać od razu wartości
# class OSOBA:
#     imie = ""
#     nazwisko = ""
#     wiek = ""
#     gatunek = ""
#
# o1 = OSOBA()
# o1.imie  = "Jan"
# o1.nazwisko = "Kowalski"
# o1.wiek = 45
#
# o2 = OSOBA()
# o2.imie  = "Ola"
# o2.nazwisko = "Nowak"
# o2.wiek = 30
#
# #nadpisanie
# o1.imie = "Adam"
# print (o1)
# print (o1.imie)

#z konstruktorem
# class OSOBA:
#     #metoda instancyjna SPECJALNA - musi istnieć obiekt klasy, wywoływana autoamtycznie
#     #jak ma wygladac obiekt, towrzenie obiektu
#     def __init__(self,imie,nazwisko,wiek):
#         #self - ddostępne z zewnątrz funkcji
#         self.imie = imie
#         self.nazwisko = nazwisko
#         self.wiek = wiek
#         print ("Utworzyłeś obiekt klasy OSOBA")
#
#     #metoda specjalna, wyśiwetlanie wartosci obiektu
#     def __str__(self):
#         return f"{self.imie}, {self.nazwisko}, {self.wiek}"
#
#     #zwykła metoda, automatycznie się wywołą
#     def pokazDane (self):
#         print(self.imie,self.nazwisko,self.wiek)
#
#     def zwiekszWiek(self):
#         self.wiek += 1
# #
# #
# o1 = OSOBA("Jan","Kowalski",25)
# o2 = OSOBA("Ola","Nowak",40)
# print(o1)
# o1.pokazDane()
# o1.zwiekszWiek()
# o1.pokazDane()

#ćwiczenie dla chęntnych
#napisz metodę, która wyświetli atrybuty klasy w sposób dynamiczny

#Ćwiczenie 48
# class OSOBA:
#     def __init__(self,imie,nazwisko):
#         self.imie = imie
#         self.nazwisko = nazwisko
#
#     def __str__(self):
#         return f"{self.imie},{self.nazwisko}"
#
# o1 = OSOBA("Jan","Kowalski")
# print (o1)

#dostep do danych
#pola chronione i prywatne, metoda seters
#pole chronione _nazwaPola -informacja dla innych, modyfikacja tego pola tylko przez metody z klasy (np. set...)
# class OSOBA:
#     def __init__(self,imie,nazwisko,pesel):
#         self.imie = imie
#         self.nazwisko = nazwisko
#         #atrybut chroniony
#         self._pesel = pesel
#
#     def pokazDane (self):
#         print (self.imie,self.nazwisko,self._pesel)
#
#     def setPesel(self, nowyPesel):
#         self._pesel = nowyPesel
#
# o1 = OSOBA("Ola","Nowak",1234565)
# o1.pokazDane()
# o1._pesel = 12
# o1.setPesel(9999)
# print(o1._pesel)



#pole prywatne
# class OSOBA:
#     def __init__(self,imie,nazwisko,pesel):
#         self.imie = imie
#         self.nazwisko = nazwisko
#         #pole prywatne __xxxxxx, nie można modyfikować spoza klasy
#         self.__pesel = pesel
#
#     def setPesel(self, nowyPesel):
#         self._pesel = nowyPesel
#
#     def getPesel(self):
#         return self.__pesel
#
# o1 = OSOBA("Ola","Nowak",1234565)
# o1._pesel = 12
# o1.setPesel(9999)
# print(o1.getPesel())
#
# print(dir(o1))
#
# o1._OSOBA__pesel = 121212
# print(o1.getPesel())

#ćwiczenie dla chętnych
#zdefiniuj stałą za pomocą programowania obiektowego np. pi=3,14
# class METODY:
#     def __init__(self,wartoscPI=3.14):
#         self.__wartoscPI = wartoscPI
#
#     def __str__(self):
#         return f"{self.__wartoscPI}"
#
# m1 = METODY()
# print (m1)


#wartosc a referencja
#kopia obiektu jest referenecją obiektu, ma wpływ na źródło, potrzebny deep copy

##dziedziczenie pass
# class OSOBA:
#     def __init__ (self,imie,nazwisko):
#         self.imie = imie
#         self.nazwisko = nazwisko
#
#     def pokaz_dane(self):
#         print(self.imie, self.nazwisko)
#
# class STUDENT(OSOBA):
#     pass
#
# o1 = OSOBA("Jan","Kowalski")
# s1 = STUDENT("Ola", "Nowak")
# s1.pokaz_dane()

#dziedziczenie - super()
#dzieiczy z klady podrzędnej
#wada - jak wiele klas, problem z hierarchią, metoda super nie wskazuje do której klasy idziemy
# class OSOBA:
#     def __init__ (self,imie,nazwisko,wiek,pesel):
#         self.imie = imie
#         self.nazwisko = nazwisko
#         self.wiek = wiek
#         self.__pesel = pesel
#
#     def przedstaw_sie(self):
#         print(f"Cześć jestem {self.imie} {self.nazwisko} i mam {self.wiek} lat.")
#
# class STUDENT(OSOBA):
#     def __init__(self,imie,nazwisko,wiek,pesel,numer_albumu):
#         #musimy jawnie wywołać konstruktor z klasy nadrzędnej
#         #metoda super przekazuje obiekt domyślnie - nie trzeba self podawać
#         super().__init__(imie,nazwisko,wiek,pesel)
#         self.numer_albumu = numer_albumu
#
#     def przedstaw_sie(self):
#         super().przedstaw_sie()
#         print (f"Numer indeksu {self.numer_albumu}")
#
# s1 = STUDENT("Jan","Kowalski",20,123456,999)
# s1.przedstaw_sie()

#dziedziczenie z klasy nadrzędnej - wskazujemy jawnie z której klasy pobieramu
# class OSOBA:
#     def __init__ (self,imie,nazwisko):
#         self.imie = imie
#         self.nazwisko = nazwisko
#
#     def __str__(self):
#         return f"{self.imie} {self.nazwisko}"
#
# class STUDENT(OSOBA):
#     def __init__(self,imie,nazwisko,album):
#         OSOBA.__init__(self,imie,nazwisko)
#         self.album = album
#
# s1 = STUDENT("Jan","Kowalski",1234)
# print(s1)

#wielodziedziczenie
# class OSOBA:
#     def __init__(self,imie,nazwisko):
#         self.imie = imie
#         self.nazwisko = nazwisko
#
# class STUDENT(OSOBA):
#     def __init__(self,imie,nazwisko,stypendium):
#         OSOBA.__init__(self,imie,nazwisko)
#         self.stypendium = stypendium
#     def pokazFinanse(self):
#         print(self.stypendium)
#
# class PRACOWNIK(OSOBA):
#     def __init__(self,imie,nazwisko,wynagrodzenie):
#         OSOBA.__init__(self,imie,nazwisko)
#         self.wynagrodzenie=wynagrodzenie
#     def pokazFinanse(self):
#         print(self.wynagrodzenie)
#
# #konflikty
# class PRACUJACY_STUDENT(STUDENT,PRACOWNIK):
#     def __init__(self,imie,nazwisko,stypendium,wynagrodzenie):
#         STUDENT.__init__(self,imie,nazwisko,stypendium)
#         PRACOWNIK.__init__(self,imie,nazwisko,wynagrodzenie)
#
#     def pokazFinanse(self):
#         print("?")
#
#     def pokazDane(self):
#         print(self.imie,self.nazwisko,self.stypendium,self.wynagrodzenie)
#
# ps = PRACUJACY_STUDENT("Jan","Kowalski",500,1000)
# ps.pokazDane()
# ps.pokazFinanse()

# class OSOBA:
#     def __init__(self,imie):
#         self.imie = imie
#
#     def pokaz(self):
#         print(self.imie)
#
# class STUDENT(OSOBA):
#     pass
#
# class PRACOWNIK:
#     def pokaz1(self):
#         print("Klasa pracownik")
#
# class CZLOWIEK(STUDENT,PRACOWNIK):
#     pass
#
# c1 = CZLOWIEK("Jan")
# c1.pokaz()

#przeciążanie konstruktora - w pythonie nie ma czegoś takiego, ale mozna zasymulować
# class OSOBA:
#     #parametr domyślny = nieobowiązkowy
#     def __init__(self,imie,nazwisko,pesel=""):
#         self.imie = imie
#         self.nazwisko = nazwisko
#         self.pesel = pesel
#
#
# o1 = OSOBA("Jan","Kowalski",123)

#Ćwiczenie 49
# class UCZELNIA:
#     def __init__(self,nazwa_uczelni=None,ulica=None,miejscowosc=None,kod_pocztowy=None,liczba_studentow=None):
#         self.nazwa_uczelni = nazwa_uczelni
#         self.ulica = ulica
#         self.miejscowosc = miejscowosc
#         self.kod_pocztowy = kod_pocztowy
#         self.liczba_studentow = liczba_studentow
#
#     def pokazDane (self):
#         print (self.nazwa_uczelni,self.ulica,self.miejscowosc,self.kod_pocztowy,self.liczba_studentow)
#
#     def setLiczbaStudentow(self,liczba_studentow):
#         self.liczba_studentow = liczba_studentow
#
# class STUDENT(UCZELNIA):
#     def __init__(self,imie,nazwisko,nr_albumu,__pesel,nazwa_uczelni):
#         UCZELNIA.__init__(self,nazwa_uczelni)
#         self.imie = imie
#         self.nazwisko = nazwisko
#         self.nr_albumu = nr_albumu
#         self.__pesel = __pesel
#
#     def pokazDane(self):
#         print(self.imie,self.nazwisko,self.nr_albumu,self.__pesel,self.nazwa_uczelni)
#
#     def setPesel(self,__pesel):
#         self.__pesel = __pesel
#
# u1 = UCZELNIA("PW","Nowa","Warszawa","02-594",1000)
# u1.pokazDane()
# u1.setLiczbaStudentow(2000)
# u1.pokazDane()
#
# s1 = STUDENT ("Jan", "Kowalski", 9999, 123456789, "UW")
# s1.pokazDane()
# s1.setPesel(987654321)
# s1.pokazDane()

# #wyjątki są klasami
# try:
#     int("Python")
# except Exception as e:
#     print(e)
#     print(e.__str__())

#tworzenie własnych wyjątków
# class NASZ_WYJATEK(Exception):
#     pass
#
# a = 10
# liczby = [1,0,9]
# for e in liczby:
#     if e==0:
#         raise NASZ_WYJATEK("Dzielnik nie może być równy 0")
#     print(a/e)

# class NASZ_WYJATEK(Exception):
#     def __init__(self):
#         komunikat = "Dzielnik nie może być równy 0"
#         super().__init__(komunikat)
#
# a = 10
# liczby=[1,0,3]
#
# for i in liczby:
#     try:
#         if i==0:
#             raise NASZ_WYJATEK()
#         print(a/i)
#     except NASZ_WYJATEK:
#         continue

#praca domowa
#zamień dowolny dokument tekstowy na dokument pdf
#odpowiednia czcionka!
#pip install fpdf
# from fpdf import FPDF
#
# pdf = FPDF()
# pdf.add_page()
# pdf.set_font("Arial", size=10)
# content = ""
#
# with open(txt_file, 'r') as file:
#     for linia in file:
#         content += linia
#     print (content)
#     #content = file.read()
#     pdf.multi_cell(0, 10, content)
#
# pdf.output(pdf_file)


#Ćwiczenie 31
# imiona = ["Jan", "Janina", "Anna", "Piotr", "Kasia"]
# noweImiona = input("Podaj dwa imiona:")
# imiona.extend((noweImiona.split()))
# print (imiona)
# imiona.insert(3, "Olaf")
# print (imiona)
# print(imiona.index("Olaf"))
# imiona.remove("Olaf")
# imiona.sort(reverse = True)
# print(imiona)
# kopiaListy = imiona.copy()
# print (kopiaListy)

# #Ćwiczenie 33
# slownik = {1:"jeden", 2:"dwa", 3:"trzy", 4:"cztery", 5:"pięć", 6:"sześć", 7:"siedem", 8:"osiem", 9:"dziewięc"}
# dane = input ("Wprowadź ciąg cyfr")
# for i in dane:
#     numer = int(i)
#     if numer in slownik.keys():
#         print (slownik.get(numer))

#Ćwiczenie 34
# slownik = ["0","1","2","3","4","5","6","7","8","9","."]
# cena = input ("Podaj cenę:")
# sprawdzenie = True
# licznik = 0
# for i in cena:
#     if i not in slownik:
#         print(f"Niepoprawny format")
#         sprawdzenie = False
#         break
#     elif i == ".":
#         licznik += 1
#         if licznik > 1:
#             print(f"Niepoprawny format")
#             sprawdzenie = False
#             break
# if sprawdzenie:
#     nowyWynik = float(cena)+float(cena)*0.1
#     print (nowyWynik)

# #Ćwiczenie 35
# pin = str(123)
# licznik = 1
# blad = 0
# while licznik < 4:
#     podanyPIN = input("Podaj kod PIN")
#     licznik += 1
#     if podanyPIN != pin:
#         blad += 1
#     if blad == 3:
#         print ("Podano 3 razy nieprawidłowy PIN")
#         break

#Ćwiczenie 36
# login = "Ja"
# haslo = "123"
# licznik = 0
# while True:
#     podanyLogin = input("Podaj login")
#     podaneHaslo = input("Podaj hasło")
#     if podanyLogin != login or podaneHaslo != haslo:
#         licznik += 1
#         print (f"Błędny login lub hasło. Błędne dane podano {licznik} razy.")
#     else:
#         print ("Podano poprawne hasło")
#         break

#abstrakcja - uproszczenie jednego problemu
#hermetyzajca = ukrywanie pewnych danych
#dziedziczenie - dziedziczenie pewnych/wsyztskich cech i dodanie nowych
#polimorfizm (wielopostaciowość) - zapisywanie jednej funkcji (metody) pod różnymi postaciami

#klasa abstrakcyjna - sama w sobie nie istnieje, uogolnienie innych klas
#koło, kwadrat, trójkąt realny obiekt, a figura to klasa abstrakcyjna
#kl abstrakcyjna uniemożliwia utworzenie własnych obiektów, wymsza dodanie metody w klasach potomnych

# from abc import ABC,abstractmethod
# from math import pi
#
# class FIGURA(ABC):
#     # @ dekorator, zwykła funkcja
#     @abstractmethod
#     def obwod(self):
#         pass
#     @abstractmethod
#     def pole(self):
#         pass
# #
# class PROSTOKAT(FIGURA):
#     def __init__(self,a,b):
#         self.a = a
#         self.b = b
#     def obwod(self):
#         return 2*self.a+2*self.b
#     def pole(self):
#         return self.a * self.b
# #
# P1 = PROSTOKAT(5,8)
# print (P1.pole())
# #
# class KOLO(FIGURA):
#     def __init__(self,r):
#         self.r = r
#
#     def pole(self):
#         return pi*self.r**2
#     def obwod(self):
#         return 2*pi*self.r
#
# O1 = KOLO(5)
# print (O1.obwod())

#polimorfizm, wielopostaciowosć, dla róznych typów danych możemy wywołać jedną funkcję
# def suma (a,b):
#     print (a+b)
# suma(1,5)
# suma(1.5,5.4)
# suma("Jan", " Kowalski")

# class OSOBA:
#     def __init__(self,imie,nazwisko):
#         self.imie = imie
#         self.nazwisko = nazwisko
#
# class PRACOWNIK(OSOBA):
#     def __init__(self,imie,nazwisko,stawka,liczba_godzin):
#         OSOBA.__init__(self,imie,nazwisko)
#         self.stawka = stawka
#         self.liczba_godzin = liczba_godzin
#     def pokaz_finanse(self):
#         return self.stawka*self.liczba_godzin
#
# class STUDENT(OSOBA):
#     def __init__(self,imie,nazwisko,stypendium):
#         OSOBA.__init__(self,imie,nazwisko)
#         self.stypendium = stypendium
#     def pokaz_finanse(self):
#         return self.stypendium
# # #wspolna funkcja - analiza finansow
# def sprawdz_finanse(obj):
#     print(obj.pokaz_finanse())
# P1 = PRACOWNIK("Jan","Kowalski",30,160)
# S1 = STUDENT("Ola","Nowak",650)
# #
# sprawdz_finanse(P1)
# sprawdz_finanse(S1)

# class ZWIERZE():
#     def __init__(self,nazwa,wiek,waga):
#         self.nazwa =  nazwa
#         self.wiek = wiek
#         self.waga = waga
#
#     def przedstaw_sie(self):
#         print(f"Jestem {self.nazwa} i mam {self.wiek} lat")
#
#     def urodziny(self):
#         self.wiek += 1
#
# class SLON(ZWIERZE):
#     def __init__(self,nazwa,wiek,waga):
#         ZWIERZE.__init__(self,nazwa,wiek,waga)
#
#     def przedstaw_sie(self):
#         print(f"Jestem {self.nazwa} i mam {self.wiek} lat")
#
# class LEW(ZWIERZE):
#     def __init__(self,nazwa,wiek,waga):
#         ZWIERZE.__init__(self,nazwa,wiek,waga)
#
#     def przedstaw_sie(self):
#         print(f"Jestem {self.nazwa} i mam {self.wiek} lat")
#
# slon = SLON("słon",10,100)
# lew = LEW("lew",5,50)
# listaZwierzat = [slon,lew]
#
# def zmien_wiek(obj):
#     obj.urodziny()

#
# for z in listaZwierzat:
#     zmien_wiek(z)
#     z.przedstaw_sie()

#metody i pola statyczne
# class OSOBA:
#     #pole statyczne, bez parametru self
#     licznik = 0
#     def __init__(self,imie,nazwisko):
#         self.imie = imie
#         self.nazwisko = nazwisko
#         OSOBA.licznik+=1
#
#     @staticmethod
#     def pokaz():
#         print(OSOBA.licznik)
#
# OSOBA.pokaz()
# print(OSOBA.licznik)
# OSOBA("Jan","Kowalski")
# OSOBA("Ola","Nowak")
# print(OSOBA.licznik)
# OSOBA.pokaz()

#metoda klasowa i statyczna
# class STUDENT():
#     def __init__(self,imie,wiek,stypendium):
#         if self.czyImiePoprawne(imie):
#             self.imie = imie
#             self.wiek = wiek
#             self.stypendium = stypendium
#
#     @classmethod
#     def stworzZeStringa(cls,napis):
#         imie,wiek,stypendium = napis.split()
#         wiek,stypendium = int(wiek),float(stypendium)
#         if cls.czyImiePoprawne(imie):
#

#
#     @staticmethod
#     def czyImiePoprawne(imie):
#         if imie[0].isupper() and len(imie)>2:
#             return True
#         return False
#
# x = STUDENT.stworzZeStringa("Ola 2 25")
# print (x.imie, x.wiek, x.stypendium)

#praca domowa
#napisz program, który zwraca True/Komunikat, jesli dany proces jest aktywny w systemie

# import subprocess
# def czyProcesAktywny(nazwaProcesu):
#     aktywneProcesy = str(subprocess.check_output("tasklist"))
#     if nazwaProcesu in aktywneProcesy:
#         print (f"Proces aktywny")
#         return True
#     else:
#         print(f"Proces nieaktywny")
#         return False
# czyProcesAktywny("pycharm64.exe")

#praca domowa
#napisz program, który wyśle mejla z dowolnym powiadomieniem (wykorzystac serwer wp...)
# import smtplib
# from email.message import EmailMessage
# import ssl
#
# port = 465
# host = "smtp.poczta.onet.pl"
# login = "hkuc@onet.pl"
# #password = input("Wpisz hasło: ")
#
# from_email = 'hkuc@onet.pl'
# to_email = 'hkucharzyk@gmail.com'
# tytul = 'Testowa wysyłka'
# message = 'Pozdrawiam! /n H'
# print ("Start -2")
# smtp = smtplib.SMTP('smtp.gmail.com',587)
# status_code, response = smtp.ehlo()
# print(f"[*] Echoing the server: {status_code} {response}")
# status_code, response = smtp.starttls()
# print(f"[*] Starting TLS connection: {status_code} {response}")
# status_code, response = smtp.login('hkucharzyk@gmail.com', 'Misiulec89!!!')
# print(f"[*] Logging in: {status_code} {response}")
#
# smtp.sendmail('hkucharzyk@gmail.com','hkuc@onet.pl',message)
# smtp.quit()

#serializacja - zapisanie obiektu w pamięci trwałej -  do pliku/bazy danych
#seria bytów - moduł pickle - zapisyniae dowolnego obiektu
# import pickle
# data = {
#     "a": [1,2.0,4+6j],
#     "b":("Python", "Java", "C++"),
#     "c":[False,True,False]
# }
#
# with open ("data.pickle","wb") as f:
#     pickle.dump(data, f)

#deserializacja
# import pickle
# with open ("data.pickle", "rb") as f:
#     data = pickle.load(f)
# print (data)

#pliki csv
# import csv
# with open ("dane.csv", encoding="UTF8") as f:
#     #funkcja reader tworzy obiekt
#     dane = csv.reader(f)
#     print (dane)
#     for i in dane:
#         print (i)
#

#import pliku z csv rozdzielonego średnikiem
# import csv
# with open("daneSrednik.csv", encoding="UTF8") as f:
#     #funkcja reader tworzy obiekt
#     dane = csv.reader(f, delimiter=";")
#     print (dane)
#     for i in dane:
#         print (i)

#zapis pliku do csv
# import csv
# # with open ("dane.csv", "a", newline="") as f:
# #     dane = csv.writer(f)
# #     dane.writerow([])
# #     dane.writerow(["Zbyszek","Nowak",30])

#pliki json
#odczyt danych json
# import json
# with open ("dane.json") as f:
#     dane = json.load(f)
#     #to jest słownik
#     print (dane)
#     print (dane["dogs"][1])
#     print(dane["dogs"][1]["name"])

#zapis danych do jsona
# dane = {}
# dane["ludzie"] = []
# dane["ludzie"].append([{"imie":"Jan","nazwisko":"Ćma","wiek":20}])
# dane["ludzie"].append([{"imie":"Ola","nazwisko":"Nowak","wiek":30}])
#
# import json
# with open ("zapis.json", "w", encoding="UTF8") as f:
#     json.dump(dane,f,ensure_ascii=False)

#Ćwiczenie
# import json
# def prognoza(miejscowosc):
#     with open("imgw.json") as f:
#         lista = json.load(f)
#         for i in lista:
#             if i["stacja"] == miejscowosc:
#                 print(f"""W miejscowości {i["stacja"]} (stacja nr {i["id_stacji"]}), w dniu {i["data_pomiaru"]} o godzinie {i["godzina_pomiaru"]} były poniższe warunki pogodowe:
# temperatura: {i["temperatura"]}
# predkość wiatru: {i["predkosc_wiatru"]}
# kierunek wiatru: {i["kierunek_wiatru"]}
# wilgotność względna: {i["wilgotnosc_wzgledna"]}
# suma opadu: {i["suma_opadu"]}
# ciśnienie: {i["cisnienie"]}""")
#                 break
#         else:
#             print("Wprowadzona nazwa miejscowosci jest niepoprawna")
#
# prognoza("Lublin")


#moduł datetime
# from datetime import datetime,date,time
# #
# # aktulany_czas = datetime.now()
# # print(aktulany_czas)
# # print(aktulany_czas.time().minute)
# # print(aktulany_czas.date().month)
#
# #określona data i godzina
# data = date(2000,3,28)
# print (data)
#
# czas = time(12,30,58)
# print (czas)

#ćwiczenie - uzyskaj z aktualnej daty: rok, miesiac i dzień w formacie: Miesiac:dzien:token
# from datetime import datetime,date
# rok = datetime.now().year
# miesiac = datetime.now().month
# dzien = datetime.now().day
# dataFormat = f"{miesiac}:{dzien}:{rok}"
# print(dataFormat)
# dataFormat2 = date(rok,miesiac,dzien)
# print(dataFormat2)

#dodawanie/odejmowanie czasu
# from datetime import datetime,timedelta
# now = datetime.now()
# print(now)
# new_now = now+timedelta(days=10)
# print(new_now)
#
# now_minus = now - timedelta(hours=1)
# print (now_minus)

#formatowanie daty i czasu
from datetime import datetime,time,date
# now = datetime.now()
# print (now)
#
# data = date(2000,1,10)
# czas = time(18,25)
# print (data)
# print (czas)
#
# #okreslona data i czas
# okreslony_czas = datetime.combine(data,czas)
# print (okreslony_czas)
#
# #formatowanie daty, godziny jako ciąg znaków
# print(now.strftime("%d/%m: %A"))

# format = datetime.strptime("2023:03:01","%Y:%m:%d")
# nowyFormat = format.strftime("%d/%m/%Y")
# print (nowyFormat)


#ćwiczenie - napisz program który formatuje podaną przez użytkownika datę w postaci: Dzień:miesiac:rok do postaci rok:miesiac:dzien
# from datetime import datetime, date, time
# podanaData = input("Podaj datę wejściową dzień:miesiac:rok: ")
#
# dzien = int(podanaData[:2])
# miesiac = int(podanaData[3:5])
# rok = int(podanaData[6:])
# data = date(rok,miesiac,dzien)
# dataFormat = data.strftime("%Y/%m/%d")
# print (dataFormat)

# import calendar
# print(calendar.month(2024,6))
# print(calendar.month_name[6],2024)
# print(calendar.day_name[0],2024)
# print(calendar.MAY)
# print(calendar.TextCalendar().formatyear(2024))

#środowisko uruchomieniowe
#zmienna specjalna name
#czy dany skrypt uruchamiany bezpośrednio ze skryptu czy z importu
#main to wartość __name__ == __main__
import nowe

#xampp

#narzędzie PIP