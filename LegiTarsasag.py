import datetime
from datetime import datetime
from time import time
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







    @property
    def foglalasok(self):
        #return self._foglalasok
        for foglalas in self._foglalasok:
            print(f" Jegy id:{foglalas._jegy_id} Járatszám: {foglalas._jaratszam} ,  idő: {foglalas._foglalas_ideje} foglalt_e {foglalas.foglalt_e}")

    @foglalasok.setter
    def foglalasok(self, uj_foglalas):
        self._foglalasok.append(uj_foglalas)

    @property
    def foglalasok_listazasa(self):
        for foglalas in self._foglalasok:
            print(f" Járatszám: {foglalas._jaratszam} , ")

    def jegy_foglalas(self):
        if not self.foglalt_e:
            self._foglalt_e = True
        else:
            print("hiba a jegy már foglalt")

    def jegy_lemondas(self):
        if self.foglalt_e:
            self._foglalt_e = False
        else:
            print("hiba a jegy már szabad")

    def jegy_foglalasa_jegy_id_szerint(self, jegy_id):
        for foglalas in self._foglalasok:
            if foglalas.jegy_id == jegy_id:
                foglalas.jegy_foglalas()


    def jegy_lemondasa_jegy_id_szerint(self, jegy_id):

        for foglalas in self._foglalasok:
            if foglalas.jegy_id == jegy_id:
                foglalas.jegy_lemondas()

    def idopont_megfelelo(self, foglalas_ideje):
        ido = foglalas_ideje
        teszt = '2020-10-10'
        #teszt0 = '2020-10-11'
        date_now = datetime.now()
        #date_str = date0.strftime("%Y-%m-%d")
        #print(date_str)
        date_szam = datetime.strptime(ido,"%Y-%m-%d")
        #print(date_szam)
        if(date_now > date_szam):
            print("Hiba a ez a járat már nem foglalható")
            return False











