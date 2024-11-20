from datetime import datetime

from BelfoldiJarat import BelfoldiJarat
from JegyFoglalas import JegyFoglalas
from NemzetkoziJarat import NemzetkoziJarat


class LegiTarsasag():
    def __init__(self, legitarsasag_neve):
        self._legitarsasag_neve = legitarsasag_neve
        self._jaratok = []
        self._foglalasok = []

    @property
    def indulas(self):
        return self._indulas




    @property
    def legitarsasag_neve(self):
        return self._legitarsasag_neve


    @property
    def jaratok(self):
        for jarat in self._jaratok:
            print(f" Járatszám: {jarat._jaratszam} , Ár: {jarat._jegyar} Célállomás: {jarat._celallomas} ")


    @jaratok.setter
    def jaratok(self, uj_jarat):
        self._jaratok.append(uj_jarat)

    def jegy_foglalasa_jaratszam_szerint(self, jaratszam):
        for jarat in self._jaratok:
            if jarat._jaratszam == jaratszam:
                #print(lefoglal._foglalas_idopontja)
                lefoglal = JegyFoglalas(datetime.now(), jaratszam)
                print(lefoglal._foglalas_idopontja)
                #return print(f" {lefoglal._jaratszam}")
                self._foglalasok.append(lefoglal)
            else:
                print("Hiba a járatszám vagy a helyek darabszámát illetően")



    idopont = "2024-11-11 11:00"
    def jegy_lemondasa_jaratszam_szerint(self, idopont, jaratszam):
        for jarat in self._jaratok:
            if jarat._jaratszam == jaratszam:
                lemond = JegyFoglalas(idopont, jaratszam)
                print(lemond._foglalas_idopontja)
                self._foglalasok.remove(lemond)
            else:
                print("hiba az időpont vagy járatszám körül")

    @property
    def foglalasok(self):
        #return self._foglalasok
        for foglalas in self._foglalasok:
            print(f" Járatszám: {foglalas._jaratszam} ,  idő: {foglalas._foglalas_idopontja}")

    @foglalasok.setter
    def foglalasok(self, uj_foglalas):
        self._foglalasok.append(uj_foglalas)

    @property
    def foglalasok_listazasa(self):
        for foglalas in self._foglalasok:
            print(f" Járatszám: {foglalas._jaratszam} , jegyszám: ")




