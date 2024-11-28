from datetime import datetime
from time import time
from JegyFoglalas import JegyFoglalas
from BelfoldiJarat import BelfoldiJarat
from NemzetkoziJarat import NemzetkoziJarat
from LegiTarsasag import LegiTarsasag

class RepuloJegyFoglalasiRendszer:
    def __init__(self):
        self._legiTarsasag = LegiTarsasag("British Airways")
        self._init_data()


    def _init_data(self):

        self._legiTarsasag.foglalasok = JegyFoglalas( "1","121",  "2024-10-21", True)
        self._legiTarsasag.foglalasok = JegyFoglalas( "1","122", "2024-10-22", False)


        self._legiTarsasag.foglalasok = JegyFoglalas( "2", "133", "2024-10-22", True)
        self._legiTarsasag.foglalasok = JegyFoglalas("2", "125","2024-10-22", False)


        self._legiTarsasag.foglalasok = JegyFoglalas( "3", "136",  "2024-10-22", True)
        self._legiTarsasag.foglalasok = JegyFoglalas("3", "137", "2024-10-22", False)


        self._legiTarsasag.jaratok = BelfoldiJarat( "1","Debrecen", "Budapest",  550, 1200)
        self._legiTarsasag.jaratok = BelfoldiJarat( "2","Budapest", "Győr",  35, 12000)
        self._legiTarsasag.jaratok = NemzetkoziJarat("3","Budapest", "Miami USA",  400, 12000)



# felhasználói interfész
    def user_interact(self):
        while True:
            print("1. Foglalások listázása")
            print("2. Járatok")
            print("3. Jegy foglalása")
            print("4. Foglalás lemondása")
            print("5. Kilépés")


            menu = input("Válassz a fenti menüpontokból: ")

            if menu == "1":

                print("******************Foglalások****************")
                self._legiTarsasag.foglalasok

                ido = "2024-12-12"
                x = self._legiTarsasag.idopont_megfelelo(ido)
                print(x)
            elif menu == "2":
                print("******************Járatok********************")
                self._legiTarsasag.jaratok
            elif menu == "3":
                foglalas_ideje = input("Adja meg a járat időpontját: ")
                if(self._legiTarsasag.idopont_megfelelo(foglalas_ideje)):
                 jegy_id = input("Adja meg a jegy_id-t: ")
                 self._legiTarsasag.jegy_foglalasa_jegy_id_szerint(jegy_id)
            elif menu == "4":
                foglalas_ideje = input("Adja meg a foglalás idejét: ev-honap-nap, 2022-01-01 ")
                if(self._legiTarsasag.idopont_megfelelo(foglalas_ideje)):
                    jegy_id = input("Adja meg a járatszámot: ")
                    self._legiTarsasag.jegy_lemondasa_jegy_id_szerint(jegy_id)

            elif menu == "5":
                break



repulojegy_foglalasi_rendszer = RepuloJegyFoglalasiRendszer()
repulojegy_foglalasi_rendszer.user_interact()
