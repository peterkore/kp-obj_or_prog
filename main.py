from JegyFoglalas import JegyFoglalas
from BelfoldiJarat import BelfoldiJarat
from NemzetkoziJarat import NemzetkoziJarat
from LegiTarsasag import LegiTarsasag

class RepuloJegyFoglalasiRendszer:
    def __init__(self):
        self._legiTarsasag = LegiTarsasag("British Airways")
        self._init_data()

    def _init_data(self):

        self._legiTarsasag.foglalasok = JegyFoglalas(1, "2024-11-10 10:00", 1)
        self._legiTarsasag.foglalasok = JegyFoglalas(2, "2024-11-10 10:01", 1)

        self._legiTarsasag.foglalasok = JegyFoglalas(3, "2024-11-11 11:00", 2)
        self._legiTarsasag.foglalasok = JegyFoglalas(4, "2024-11-11 11:01", 2)

        self._legiTarsasag.foglalasok = JegyFoglalas(5, "2024-11-12 20:00", 3)
        self._legiTarsasag.foglalasok = JegyFoglalas(6, "2024-11-12 20:01", 3)

        self._legiTarsasag.jaratok = BelfoldiJarat(3, "Debrecen", 55000)
        self._legiTarsasag.jaratok = BelfoldiJarat(2, "Budapest", 35000)
        self._legiTarsasag.jaratok = NemzetkoziJarat(1, "Miami USA", 400000)

# felhasználói interfész
    def user_interact(self):
        while True:
            print("1. Foglalások listázása")
            print("2. Jegy foglalása")
            print("3. Foglalás lemondása")
            print("4. Kilépés")

            menu = input("Válassz a fenti menüpontokból: ")

            if menu == "1":

                self._legiTarsasag.foglalasok
                self._legiTarsasag.jaratok

            elif menu == "2":
                jaratszam = input("Adja meg a járatszámot: ")
                self._legiTarsasag.jegy_foglalasa_jaratszam_szerint(jaratszam)
            elif menu == "3":
                jaratszam = input("Adja meg a járatszámot: ")
                self._legiTarsasag.jegy_lemondasa_jaratszam_szerint(jaratszam)
            elif menu == "4":
                break


repulojegy_foglalasi_rendszer = RepuloJegyFoglalasiRendszer()
repulojegy_foglalasi_rendszer.user_interact()