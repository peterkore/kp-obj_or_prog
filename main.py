from datetime import datetime

from JegyFoglalas import JegyFoglalas
from BelfoldiJarat import BelfoldiJarat
from NemzetkoziJarat import NemzetkoziJarat
from LegiTarsasag import LegiTarsasag

class RepuloJegyFoglalasiRendszer:
    def __init__(self):
        self._legiTarsasag = LegiTarsasag("British Airways")
        self._init_data()


    def _init_data(self):

        self._legiTarsasag.foglalasok = JegyFoglalas( "2024-11-10 10:00", "1")
        self._legiTarsasag.foglalasok = JegyFoglalas( "2024-11-10 10:20", "1")

        self._legiTarsasag.foglalasok = JegyFoglalas( "2024-11-11 11:00", "2")
        self._legiTarsasag.foglalasok = JegyFoglalas("2024-11-11 11:20", "2")

        self._legiTarsasag.foglalasok = JegyFoglalas( "2024-11-12 20:00", "3")
        self._legiTarsasag.foglalasok = JegyFoglalas("2024-11-12 20:10", "3")

        self._legiTarsasag.jaratok = BelfoldiJarat( "1","Debrecen", "Budapest",  550, 1200)
        self._legiTarsasag.jaratok = BelfoldiJarat( "2","Budapest", "Győr",  35, 12000)
        self._legiTarsasag.jaratok = NemzetkoziJarat("3","Budapest", "Miami USA",  400, 12000)



# felhasználói interfész
    def user_interact(self):
        while True:
            print("1. Foglalások és Járatok listázása")
            print("2. Jegy foglalása")
            print("3. Foglalás lemondása")
            print("4. Kilépés")
            print(datetime.now())

            menu = input("Válassz a fenti menüpontokból: ")

            if menu == "1":
                print("******************Foglalások****************")
                self._legiTarsasag.foglalasok
                print("******************Járatok********************")
                self._legiTarsasag.jaratok

            elif menu == "2":
                jaratszam = input("Adja meg a járatszámot: ")
                self._legiTarsasag.jegy_foglalasa_jaratszam_szerint(jaratszam)
            elif menu == "3":
                idopont = "2024-11-11 11:00"
                jaratszam = input("Adja meg a járatszámot: ")
                self._legiTarsasag.jegy_lemondasa_jaratszam_szerint(idopont, jaratszam)
            elif menu == "4":
                break



repulojegy_foglalasi_rendszer = RepuloJegyFoglalasiRendszer()
repulojegy_foglalasi_rendszer.user_interact()