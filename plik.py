###############################################################################################################################

import random

###############################################################################################################################

zaloga = 0
pieniadze = 0
dzien = 0
x = 0
y = 39
energia = 0
gra1 = True
gra2 = True
km = 0
pogoda = 0
poziom_trudnosci = 0
jaka_pogoda = 0
jedzenie = 10
spragnienie = 0

woda = 0
mienso = 0
jabka = 0
cytryny = 0
podpiwek = 0
sul = 0
szpada = 0
armata = 0
amunicja_do_armaty = 0
kusza_z_amunicjom = 0
sztylet = 0
zapasowy_zagiel = 0
kompas_magnetyczny = 0
narzedzia_do_naprawy_okretu = 0

###############################################################################################################################
# Funkcje ogólne:

def powitanie():
    print()
    print("/" * 100)
    print()
    print("Ahoj kamracie, witam ciebie w 'SIMULATOR Columbus.\nW tym symulatorze wcielisz się w Krzysztofa Kolumba, który ma za zadanie odkryć Amerykę.\nInstrukcja: Działaj według poleceń i zatwierdź wybór przyciskiem 'ENTER'.")
    print("Ps: Wszystkie odległości i spółrzędne są wzorowane na prawdziwych.")


def ustawienia():
    global jedzenie, zaloga, pieniadze

    print()
    print("=" * 100)
    print()
    print("Wybierz poziom trudności:")
    print("+" * 25)
    print("1) ŁATWY - W tym trybie gry masz: 3kg mięsa, 2kg soli, 6L wody na start | 50 załogi z wyposażeniem: 1 sztylet na osobę | nieograniczone pieniądze | niską szanse na wystąpienie sztormu itd. | nie będziesz atakowany przez wrogich piratów i plemiona.")
    print("." * 100)
    print("2) NORMALNY - W tym trybie gry masz: 1kg mięsa, 3L wody na start | 25 załogi z wyposażeniem: 10 sztyletów | 5000 pieniędzy | średnią szansę na wystąpienie sztormu itd. | średnią szansę na to że ktoś cię zaatakuję.")
    print("." * 100)
    print("3) TRUDNY - W tym trybie gry masz: 0 jedzenia na start | 10 załogi| 1000 pieniędzy| wysoką szansę na wystąpienie sztormu itd. | wysoką szansę na atak przeciwnika.")
    print("." * 100)

    while True:
        global zaloga, pieniadze, sztylet, mienso, sul, woda
        poziom_trudnosci = input("Wybierz jedną z opcji 1-3: ")

        if poziom_trudnosci == "1":
            zaloga += 50
            pieniadze = 100000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000
            sztylet += 50
            mienso += 3
            sul += 2
            woda += 6
            break

        elif poziom_trudnosci == "2":
            zaloga += 25
            pieniadze += 5000
            sztylet += 10
            mienso += 1
            woda += 3
            break

        elif poziom_trudnosci == "3":
            zaloga += 10
            pieniadze += 1000
            break

        else:
            print()
            print("BŁĄD!!! Musisz podać liczbę 1-3. Spróbuj ponownie.")


def powitanie_sklep():
    print()
    print("&" * 100)
    print()
    print("Ahoj, witaj w sklepie 'Pirackie Potrzeby'.\nW tym sklepie nie kupisz tylko rzeczy z jednego rodzaju, więc co chcesz kupić ?\nPs: Ostatnio uciekło nam dużo bydła z zagrody, więc mięso troche podrożało, a i filter wody się popsuł i został nam 1.")


def ekwipunek():
    print()
    print("Ekwipunek:")
    print()
    print(f"woda: {woda}L")
    print(f"mięso: {mienso}kg")
    print(f"jabka: {jabka}kg")
    print(f"cytryny: {cytryny}kg")
    print(f"podpiwek: {podpiwek}L")
    print(f"sól: {sul}kg")
    print(f"szpada: {szpada}")
    print(f"armata: {armata}")
    print(f"amunicja do armaty: {amunicja_do_armaty}")
    print(f"kusza z amunicjom: {kusza_z_amunicjom}")
    print(f"sztylet: {sztylet}")
    print(f"zapasowy żagiel: {zapasowy_zagiel}")
    print(f"kompas magnetyczny: {kompas_magnetyczny}")
    print(f"narzedzia do naprawy okretuy: {narzedzia_do_naprawy_okretu}")


def jedzenie_sklep():
    global pieniadze, woda, mienso, jabka, cytryny, podpiwek, sul

    print()
    print("____________________________________")
    print("| Produkty: | Ceny: | Ilość: | Nr. |")
    print("|----------------------------------|")
    print("|   woda    |  50$  |   1L   |  1  |")
    print("|   mięso   |  50$  |   1kg  |  2  |")
    print("|  jabłka   |  10$  |   1kg  |  3  |")
    print("|  cytryny  |  50$  |   1kg  |  4  |")
    print("| podpiwek  |  40$  |   1L   |  5  |")
    print("|   sól     |  70$  |   1kg  |  6  |")
    print("|__________________________________|")
    print("7) Wyjdź ze sklepu z jedzeniem/piciem.")
    print("Ps: Pamiętaj, że jak Ty jesz, to Twoja załoga też.")
    
    while True:
        wybor_kupionego_jedzenia = input("\nWybierz JEDEN przedmiot, wybierz opcję 1-7: ")
        
        if wybor_kupionego_jedzenia == "7":
            print("Wychodzisz ze sklepu.")
            wybor_rodzaju_rzeczy_w_sklepie()
            break
            
        elif wybor_kupionego_jedzenia == "1":
            try:
                ilosc_kupionego_jedzenia = int(input("Podaj ilość wybranego produktu: "))
                if pieniadze >= ilosc_kupionego_jedzenia * 50:
                    if ilosc_kupionego_jedzenia <= 0:
                        print("\nBŁĄD!!! Ilość produktu nie może być równa lub mniejsza od 0. Spróbuj ponownie.")
                    else:
                        woda += ilosc_kupionego_jedzenia
                        pieniadze -= 50
                else:
                    print("\nBŁĄD!!! Masz za mało pieniędzy. Spróbuj ponownie.")
            except ValueError:
                print("\nBŁĄD!!! Musisz wpisać liczbę cyframi! Spróbuj ponownie.")
        
        elif wybor_kupionego_jedzenia == "2":
            try:
                ilosc_kupionego_jedzenia = int(input("Podaj ilość wybranego produktu: "))
                if pieniadze >= ilosc_kupionego_jedzenia * 50:
                    if ilosc_kupionego_jedzenia <= 0:
                        print("\nBŁĄD!!! Ilość produktu nie może być równa lub mniejsza od 0. Spróbuj ponownie.")
                    else:
                        mienso += ilosc_kupionego_jedzenia
                        pieniadze -= 50
                else:
                    print("\nBŁĄD!!! Masz za mało pieniędzy. Spróbuj ponownie.")
            except ValueError:
                print("\nBŁĄD!!! Musisz wpisać liczbę cyframi! Spróbuj ponownie.")

        elif wybor_kupionego_jedzenia == "3":
            try:
                ilosc_kupionego_jedzenia = int(input("Podaj ilość wybranego produktu: "))
                if pieniadze >= ilosc_kupionego_jedzenia * 10:
                    if ilosc_kupionego_jedzenia <= 0:
                        print("\nBŁĄD!!! Ilość produktu nie może być równa lub mniejsza od 0. Spróbuj ponownie.")
                    else:
                        jabka += ilosc_kupionego_jedzenia
                        pieniadze -= 10
                else:
                    print("\nBŁĄD!!! Masz za mało pieniędzy. Spróbuj ponownie.")
            except ValueError:
                print("\nBŁĄD!!! Musisz wpisać liczbę cyframi! Spróbuj ponownie.")

        elif wybor_kupionego_jedzenia == "4":
            try:
                ilosc_kupionego_jedzenia = int(input("Podaj ilość wybranego produktu: "))
                if pieniadze >= ilosc_kupionego_jedzenia * 50:
                    if ilosc_kupionego_jedzenia <= 0:
                        print("\nBŁĄD!!! Ilość produktu nie może być równa lub mniejsza od 0. Spróbuj ponownie.")
                    else:
                        cytryny += ilosc_kupionego_jedzenia
                        pieniadze -= 50
                else:
                    print("\nBŁĄD!!! Masz za mało pieniędzy. Spróbuj ponownie.")
            except ValueError:
                print("\nBŁĄD!!! Musisz wpisać liczbę cyframi! Spróbuj ponownie.")

        elif wybor_kupionego_jedzenia == "5":
            try:
                ilosc_kupionego_jedzenia = int(input("Podaj ilość wybranego produktu: "))
                if pieniadze >= ilosc_kupionego_jedzenia * 40:
                    if ilosc_kupionego_jedzenia <= 0:
                        print("\nBŁĄD!!! Ilość produktu nie może być równa lub mniejsza od 0. Spróbuj ponownie.")
                    else:
                        podpiwek += ilosc_kupionego_jedzenia
                        pieniadze -= 40
                else:
                    print("\nBŁĄD!!! Masz za mało pieniędzy. Spróbuj ponownie.")
            except ValueError:
                print("\nBŁĄD!!! Musisz wpisać liczbę cyframi! Spróbuj ponownie.")

        elif wybor_kupionego_jedzenia == "6":
            try:
                ilosc_kupionego_jedzenia = int(input("Podaj ilość wybranego produktu: "))
                if pieniadze >= ilosc_kupionego_jedzenia * 70:
                    if ilosc_kupionego_jedzenia <= 0:
                        print("\nBŁĄD!!! Ilość produktu nie może być równa lub mniejsza od 0. Spróbuj ponownie.")
                    else:
                        sul += ilosc_kupionego_jedzenia
                        pieniadze -= 70
                else:
                    print("\nBŁĄD!!! Masz za mało pieniędzy. Spróbuj ponownie.")
            except ValueError:
                print("\nBŁĄD!!! Musisz wpisać liczbę cyframi! Spróbuj ponownie.")

        else:
            print("\nBŁĄD!!! Nie ma opcji o takim numerze. Wybierz 1-7.")

    print()
    print(f"Pieniądze: {pieniadze}")
    print("Ekwipunek:")
    ekwipunek()


def minus_mienso():
    pass


def bron_sklep():
    global ekwipunek, pieniadze, szpada, armata, amunicja_do_armaty, kusza_z_amunicjom, sztylet

    print()
    print("___________________________________________")
    print("|    Produkty:     | Ceny: | Ilość: | Nr. |")
    print("|-----------------------------------------|")
    print("|     szpada       | 100$  |    1   |  1  |")
    print("|     armata       | 500$  |    1   |  2  |") 
    print("|amunicja do armaty|  25$  |   10   |  3  |")
    print("| kusza z amunicją | 150$  |    1   |  4  |")
    print("|     sztylet      |  50$  |    1   |  5  |")
    print("|_________________________________________|")
    print("6) Wyjdź ze sklepu z bronią.")
    print("Ps: Załoga nie jest zazwyczaj uposażona w broń.")

    while True:
        wybor_kupionego_jedzenia = input("\nWybierz JEDEN przedmiot, wybierz opcję 1-7: ")
        
        if wybor_kupionego_jedzenia == "6":
            print("Wychodzisz ze sklepu.")
            wybor_rodzaju_rzeczy_w_sklepie()
            break
            
        elif wybor_kupionego_jedzenia == "1":
            try:
                ilosc_kupionego_jedzenia = int(input("Podaj ilość wybranego produktu: "))
                if pieniadze >= ilosc_kupionego_jedzenia * 100:
                    if ilosc_kupionego_jedzenia <= 0:
                        print("\nBŁĄD!!! Ilość produktu nie może być równa lub mniejsza od 0. Spróbuj ponownie.")
                    else:
                        szpada += ilosc_kupionego_jedzenia
                        pieniadze -= 100
                else:
                    print("\nBŁĄD!!! Masz za mało pieniędzy. Spróbuj ponownie.")
            except ValueError:
                print("\nBŁĄD!!! Musisz wpisać liczbę cyframi! Spróbuj ponownie.")
        
        elif wybor_kupionego_jedzenia == "2":
            try:
                ilosc_kupionego_jedzenia = int(input("Podaj ilość wybranego produktu: "))
                if pieniadze >= ilosc_kupionego_jedzenia * 500:
                    if ilosc_kupionego_jedzenia <= 0:
                        print("\nBŁĄD!!! Ilość produktu nie może być równa lub mniejsza od 0. Spróbuj ponownie.")
                    else:
                        armata += ilosc_kupionego_jedzenia
                        pieniadze -= 500
                else:
                    print("\nBŁĄD!!! Masz za mało pieniędzy. Spróbuj ponownie.")
            except ValueError:
                print("\nBŁĄD!!! Musisz wpisać liczbę cyframi! Spróbuj ponownie.")

        elif wybor_kupionego_jedzenia == "3":
            try:
                ilosc_kupionego_jedzenia = int(input("Podaj ilość wybranego produktu: "))
                if pieniadze >= ilosc_kupionego_jedzenia * 25:
                    if ilosc_kupionego_jedzenia <= 0:
                        print("\nBŁĄD!!! Ilość produktu nie może być równa lub mniejsza od 0. Spróbuj ponownie.")
                    else:
                        amunicja_do_armaty = amunicja_do_armaty + ilosc_kupionego_jedzenia * 10
                        pieniadze -= 25
                else:
                    print("\nBŁĄD!!! Masz za mało pieniędzy. Spróbuj ponownie.")
            except ValueError:
                print("\nBŁĄD!!! Musisz wpisać liczbę cyframi! Spróbuj ponownie.")

        elif wybor_kupionego_jedzenia == "4":
            try:
                ilosc_kupionego_jedzenia = int(input("Podaj ilość wybranego produktu: "))
                if pieniadze >= ilosc_kupionego_jedzenia * 150:
                    if ilosc_kupionego_jedzenia <= 0:
                        print("\nBŁĄD!!! Ilość produktu nie może być równa lub mniejsza od 0. Spróbuj ponownie.")
                    else:
                        kusza_z_amunicjom += ilosc_kupionego_jedzenia
                        pieniadze -= 150
                else:
                    print("\nBŁĄD!!! Masz za mało pieniędzy. Spróbuj ponownie.")
            except ValueError:
                print("\nBŁĄD!!! Musisz wpisać liczbę cyframi! Spróbuj ponownie.")

        elif wybor_kupionego_jedzenia == "5":
            try:
                ilosc_kupionego_jedzenia = int(input("Podaj ilość wybranego produktu: "))
                if pieniadze >= ilosc_kupionego_jedzenia * 50:
                    if ilosc_kupionego_jedzenia <= 0:
                        print("\nBŁĄD!!! Ilość produktu nie może być równa lub mniejsza od 0. Spróbuj ponownie.")
                    else:
                        sztylet += ilosc_kupionego_jedzenia
                        pieniadze -= 50
                else:
                    print("\nBŁĄD!!! Masz za mało pieniędzy. Spróbuj ponownie.")
            except ValueError:
                print("\nBŁĄD!!! Musisz wpisać liczbę cyframi! Spróbuj ponownie.")

        else:
            print("\nBŁĄD!!! Nie ma opcji o takim numerze. Wybierz 1-7.")

    print()
    print(f"Pieniądze: {pieniadze}")
    print("Ekwipunek:")
    ekwipunek()


def rzeczy_do_okretu_sklep():
    global ekwipunek, pieniadze, zapasowy_zagiel, kompas_magnetyczny, narzedzia_do_naprawy_okretu

    print()
    print("____________________________________________________")
    print("|         Produkty:         | Ceny: | Ilość: | Nr. |")
    print("|--------------------------------------------------|")
    print("|      zapasowy żagiel      | 500$  |    1   |  1  |")
    print("|    kompas magnetyczny     | 150$  |    1   |  2  |")
    print("|narzędzia do naprawy okrętu| 100$  |    1   |  3  |")
    print("|__________________________________________________|")
    print("4) Wyjdź ze sklepu z rzeczami do okrętu.")

    while True:
        wybor_kupionego_jedzenia = input("\nWybierz JEDEN przedmiot, wybierz opcję 1-7: ")
        
        if wybor_kupionego_jedzenia == "4":
            print("Wychodzisz ze sklepu.")
            wybor_rodzaju_rzeczy_w_sklepie()
            break
            
        elif wybor_kupionego_jedzenia == "1":
            try:
                ilosc_kupionego_jedzenia = int(input("Podaj ilość wybranego produktu: "))
                if pieniadze >= ilosc_kupionego_jedzenia * 500:
                    if ilosc_kupionego_jedzenia <= 0:
                        print("\nBŁĄD!!! Ilość produktu nie może być równa lub mniejsza od 0. Spróbuj ponownie.")
                    else:
                        zapasowy_zagiel += ilosc_kupionego_jedzenia
                        pieniadze -= 500
                else:
                    print("\nBŁĄD!!! Masz za mało pieniędzy. Spróbuj ponownie.")
            except ValueError:
                print("\nBŁĄD!!! Musisz wpisać liczbę cyframi! Spróbuj ponownie.")
        
        elif wybor_kupionego_jedzenia == "2":
            try:
                ilosc_kupionego_jedzenia = int(input("Podaj ilość wybranego produktu: "))
                if pieniadze >= ilosc_kupionego_jedzenia * 150:
                    if ilosc_kupionego_jedzenia <= 0:
                        print("\nBŁĄD!!! Ilość produktu nie może być równa lub mniejsza od 0. Spróbuj ponownie.")
                    else:
                        kompas_magnetyczny += ilosc_kupionego_jedzenia
                        pieniadze -= 150
                else:
                    print("\nBŁĄD!!! Masz za mało pieniędzy. Spróbuj ponownie.")
            except ValueError:
                print("\nBŁĄD!!! Musisz wpisać liczbę cyframi! Spróbuj ponownie.")

        elif wybor_kupionego_jedzenia == "3":
            try:
                ilosc_kupionego_jedzenia = int(input("Podaj ilość wybranego produktu: "))
                if pieniadze >= ilosc_kupionego_jedzenia * 100:
                    if ilosc_kupionego_jedzenia <= 0:
                        print("\nBŁĄD!!! Ilość produktu nie może być równa lub mniejsza od 0. Spróbuj ponownie.")
                    else:
                        narzedzia_do_naprawy_okretu += ilosc_kupionego_jedzenia
                        pieniadze -= 100
                else:
                    print("\nBŁĄD!!! Masz za mało pieniędzy. Spróbuj ponownie.")
            except ValueError:
                print("\nBŁĄD!!! Musisz wpisać liczbę cyframi! Spróbuj ponownie.")
        else:
            print("\nBŁĄD!!! Nie ma opcji o takim numerze. Wybierz 1-7.")

    print()
    print(f"Pieniądze: {pieniadze}")
    print("Ekwipunek:")
    ekwipunek()


def wybor_rodzaju_rzeczy_w_sklepie():
    print()
    print("1) Jedzenie/picie.\n2) Broń.\n3) Rzeczy do okrętów.\n4) Wyjdź.")
    print()
    
    while True:
        wybor_sklepu = input("Wybierz jedną z opcji 1-3: ")

        if wybor_sklepu == "1":
            jedzenie_sklep()
            break
        elif wybor_sklepu == "2":
            bron_sklep()
            break
        elif wybor_sklepu == "3":
            rzeczy_do_okretu_sklep()
            break
        elif wybor_sklepu == "4":
            wybor_na_morzu()
            break
        else:
            print()
            print("BŁĄD!!! Musisz podać liczbę 1-4. Spróbuj ponownie.")


def wybor_na_morzu():
    global ekwipunek
    print()
    print(":" * 100)
    print()
    print("Ekwipunek: ")
    print(ekwipunek)
    print()
    print("WYPŁYWAMY!!!")


def info_koniec():
    print()
    print("$" * 100)
    print()
    print("Twórca: Ja, czyli Ada, lat 12!!!")
    print("Podziękowania: dla całej blższej rodzinki (:")
    print("Testerzy: moja mama, brat i babacia")
    print("Sponsor: moja babcia, bo bez niej by mnie tu nie było <3")
    print()
    print("%" * 100)
    print()


def koniec():
    global wybor_koniec_czy_gra, gra1, gra2

    print()
    print("^" * 100)
    print()
    print("Gratulacj, udało Ci się odkryć jedno z wielu zakończeń.")
    print("Teraz możesz zagrać ponownie, aby odkryć kolejne zakończenia albo zakończyć rozgryfkę na dziś.")
    print()
    print("1) Graj dalej.")
    print("2) Zakończ na dziś.")
    print()
    wybor_koniec_czy_gra = input("Wybierz jedną z opcji 1-2: ")

    if wybor_koniec_czy_gra == "2":
        gra1 = False
        gra2 = False
        info_koniec()

    elif wybor_koniec_czy_gra == "1":
        gra1 = True
        gra2 = False

###############################################################################################################################
# Zakończenia:

def zakonczenie_energia():
    global gra1, gra2

    print()
    print("<" * 100)
    print()
    print("The end.")
    print("Zakończenie numer 1. Śmierć przez zbyt duże zmęczenie.")
    print()
    print("Końcowe wyniki:")
    print("(" * 15)
    ekwipunek()
    print()
    print(f"Dzien: {dzien}")
    print(f"Pozycja: x:{x}, y:{y}")
    print(f"Poziom zmęczenia: {energia}%")
    print(f"Poziom głodu: {jedzenie}%")
    print(f"Załoga: {zaloga}.")
    print()
    print("@" * 100)
    print()
    gra1 = False
    gra2 = False


def zakonczenie_km():
    global gra1, gra2

    print()
    print("<" * 100)
    print()
    print("The end.")
    print("Zakończenie numer 2. Udało Ci się dopłynąć do Ameryki.")
    print()
    print("Końcowe wyniki:")
    print("(" * 15)
    ekwipunek()
    print()
    print(f"Dzien: {dzien}")
    print(f"Pozycja: x:{x}, y:{y}")
    print(f"Poziom zmęczenia: {energia}%")
    print(f"Poziom głodu: {jedzenie}%")
    print(f"Załoga: {zaloga}.")
    print()
    print("@" * 100)
    print()
    gra1 = False
    gra2 = False


def zakonczenie_spanie():
    global gra1, gra2

    print()
    print("<" * 100)
    print()
    print("The end.")
    print("Zakończenie numer 3. Śmierć przez zbyt dużą ilość snu.")
    print()
    print("Końcowe wyniki:")
    print("(" * 15)
    ekwipunek()
    print()
    print(f"Dzien: {dzien}")
    print(f"Pozycja: x:{x}, y:{y}")
    print(f"Poziom zmęczenia: {energia}%")
    print(f"Poziom głodu: {jedzenie}%")
    print(f"Załoga: {zaloga}.")
    print()
    print("@" * 100)
    print()
    gra1 = False
    gra2 = False

def zakonczenie_glod():
    global gra1, gra2

    print()
    print("<" * 100)
    print()
    print("The end.")
    print("Zakończenie numer 4. Śmierć przez za duży głud.")
    print()
    print("Końcowe wyniki:")
    print("(" * 15)
    ekwipunek()
    print()
    print(f"Dzien: {dzien}")
    print(f"Pozycja: x:{x}, y:{y}")
    print(f"Poziom zmęczenia: {energia}%")
    print(f"Poziom głodu: {jedzenie}%")
    print(f"Załoga: {zaloga}.")
    print()
    print("@" * 100)
    print()
    gra1 = False
    gra2 = False

def zakonczenie_jedzenie():
    global gra1, gra2

    print()
    print("<" * 100)
    print()
    print("The end.")
    print("Zakończenie numer 5. Śmierć z przejedzenia.")
    print()
    print("Końcowe wyniki:")
    print("(" * 15)
    ekwipunek()
    print()
    print(f"Dzien: {dzien}")
    print(f"Pozycja: x:{x}, y:{y}")
    print(f"Poziom zmęczenia: {energia}%")
    print(f"Poziom głodu: {jedzenie}%")
    print(f"Załoga: {zaloga}.")
    print()
    print("@" * 100)
    print()
    gra1 = False
    gra2 = False

def zakonczenie_samotnosc():
    global gra1, gra2

    print()
    print("<" * 100)
    print()
    print("The end.")
    print("Zakończenie numer 6. Śmierć przez samotnosc.")
    print()
    print("Końcowe wyniki:")
    print("(" * 15)
    ekwipunek()
    print()
    print(f"Dzien: {dzien}")
    print(f"Pozycja: x:{x}, y:{y}")
    print(f"Poziom zmęczenia: {energia}%")
    print(f"Poziom głodu: {jedzenie}%")
    print(f"Załoga: {zaloga}.")
    print()
    print("@" * 100)
    print()
    gra1 = False
    gra2 = False

def zakonczenie_spragnienie():
    global gra1, gra2

    print()
    print("<" * 100)
    print()
    print("The end.")
    print("Zakończenie numer 7. Śmierć przez odwodnienia.")
    print()
    print("Końcowe wyniki:")
    print("(" * 15)
    ekwipunek()
    print()
    print(f"Dzien: {dzien}")
    print(f"Pozycja: x:{x}, y:{y}")
    print(f"Poziom zmęczenia: {energia}%")
    print(f"Poziom głodu: {jedzenie}%")
    print(f"Załoga: {zaloga}.")
    print()
    print("@" * 100)
    print()
    gra1 = False
    gra2 = False

def zakonczenie_alkohol():
    global gra1, gra2

    print()
    print("<" * 100)
    print()
    print("The end.")
    print("Zakończenie numer 8. Śmierć przez utopienie, ponieważ upiłeś się i nie chcąco wypadłeś za burtę.")
    print()
    print("Końcowe wyniki:")
    print("(" * 15)
    ekwipunek()
    print()
    print(f"Dzien: {dzien}")
    print(f"Pozycja: x:{x}, y:{y}")
    print(f"Poziom zmęczenia: {energia}%")
    print(f"Poziom głodu: {jedzenie}%")
    print(f"Załoga: {zaloga}.")
    print()
    print("@" * 100)
    print()
    gra1 = False
    gra2 = False

###############################################################################################################################
# Funkcje konkretne:

def poczatkowe_informacje():
    powitanie()
    ustawienia()
    print()
    
    while True:
        nazwa_okretu = input("Podaj nazwę swojego okrętu: ")
        if nazwa_okretu != "":
            break
        else:
            print()
            print("BŁĄD!!! Nie możesz nic nie wpisać. Musisz wpisać nazwę okrętu!")

    print()
    print(f"Twój okręt to: {nazwa_okretu}")
    print(f"Stan początkowy -> Załoga: {zaloga} | Pieniądze: {pieniadze if pieniadze < 9000000 else 'nieskończoność'} | Współrzędne x:{x}, y:{y} | Poziom zmęczenia: {energia}.")

    print()
    print("-" * 30, "Koniec konfiguracji początkowej. Gra się rozpoczyna!", "-" * 30)


def sklep():
    powitanie_sklep()
    wybor_rodzaju_rzeczy_w_sklepie()


def wybor_akcji_sklep():
    print()
    print("Ahoj! Za chwile wyruszamy w morze kamracie, więc masz jeszcze czas pójść do sklepu.")
    print()

    print("Wybierz jedną z akcji którą wykonasz:")
    print()
    print("1) Idź do sklepu.")
    print("2) Wypłyń na ocean.")
    print()

    while True:
        wybor_akcji = input("Wybierz opcję 1-2: ") 

        if wybor_akcji == "1":
            sklep()
            break

        elif wybor_akcji == "2":
            wybor_na_morzu()#################################################################
            break

        else:
            print()
            print("BŁĄD!!! Musisz wpisać liczbę 1-2. Spróbuj ponownie.")

def akcja():
    global ekwipunek, x, y, wybor_akcji_na_morzu, pogoda, dzien, energia, km, zaloga, poziom_trudnosci, jaka_pogoda, jedzenie, spragnienie, jabka, mienso
    dzien += 1

    # if poziom_trudnosci == "1":
    #     pogoda = random.randint(1, 10)
    #     if pogoda == "10":
    #         jaka_pogoda = random.randint(1, 2)
    #         if jaka_pogoda == "1":
    #             print()
    #             print("UWAGA!!! SZTORM!!!")
    #             print("15 minut później...")
                

    # elif poziom_trudnosci == "2":
    #     pogoda = random.randint(1, 5)
    #     if pogoda == "5":
    #         pass

    # elif poziom_trudnosci == "3":
    #     pogoda = random.randint(1, 3)
    #     if pogoda == "3":
    #         pass

    print()
    ekwipunek()
    print()
    print(f"Dzien: {dzien}.")
    print(f"Pozycja: x:{x}, y:{y}.")
    print(f"Poziom zmęczenia: {energia}%.")
    print(f"Poziom głodu: {jedzenie}%")
    print(f"Poziom spragnienia: {spragnienie}%")
    print(f"Załoga: {zaloga}.")
    print()
    print("Co teraz zrobisz?")
    print("1) Idź spać.")
    print("2) Płyń 500km.")
    print("3) Jedz mięso.")
    print("4) Jedz jabka.")
    print("5) Pij wodę.")
    print("6) Pij podpiwek.")
    print()

    wybor_akcji_na_morzu = input("Wybierz opcję 1-6: ")

    if energia == 100:
        zakonczenie_energia()
    else:
        if wybor_akcji_na_morzu != "1":
            energia += 5
        elif wybor_akcji_na_morzu == "1":
            energia -= 5

    if km == 8:
        zakonczenie_km()
    else:
        if wybor_akcji_na_morzu == "2":
            km += 1
            x -= 4.9
            y -= 1.5

    if energia < 0:
        zakonczenie_spanie()

    if zaloga <= 0:
        zakonczenie_samotnosc()

    if wybor_akcji_na_morzu == "6":
        zakonczenie_alkohol()

    if jedzenie <= 0:
        zakonczenie_jedzenie()

    if jedzenie >= 100:
        zakonczenie_glod()
    else:
        if wybor_akcji_na_morzu != "3" and wybor_akcji_na_morzu != "4":
            jedzenie += 5
        elif wybor_akcji_na_morzu == "3":
            jedzenie -= 15
            mienso -= 1

        if wybor_akcji_na_morzu != "4" and wybor_akcji_na_morzu != "3":
            jedzenie += 5
        elif wybor_akcji_na_morzu == "4":
            jedzenie -= 5
            jabka -= 1

    if spragnienie >= 100:
        zakonczenie_spragnienie()
    else:
        if wybor_akcji_na_morzu != "5":
            spragnienie += 5
        elif wybor_akcji_na_morzu =="5":
            spragnienie -= 5

###############################################################################################################################
# Główna pętla:

while gra1:
    poczatkowe_informacje()
    wybor_akcji_sklep()
    gra2 = True

    while gra2:
        akcja()
    
    koniec()

###############################################################################################################################