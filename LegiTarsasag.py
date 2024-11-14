class LegiTarsasag:
    def __init__(self, legitarsasag_neve):
        self._legitarsasag_neve = legitarsasag_neve
        self._jaratok = []
        self._foglalasok = []


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
                jarat.jegy_foglalas()
                self.add_foglalas()


    def jegy_lemondasa_jaratszam_szerint(self, jaratszam):
        for jarat in self._jaratok:
            if jarat._jaratszam == jaratszam:
                jarat.jegy_foglalas_lemondasa()

    @property
    def foglalasok(self):
        #return self._foglalasok
        for foglalas in self._foglalasok:
            print(f" Járatszám: {foglalas._jaratszam} , Ár: {foglalas._jegyar} Célállomás: {foglalas._celallomas} ")

    @foglalasok.setter
    def add_foglalas(self, uj_foglalas):
        self._foglalasok.append(uj_foglalas)

    @property
    def foglalasok_listazasa(self):
        for foglalas in self._foglalasok:
            print(f" Járatszám: {foglalas._jaratszam} , Ár: {foglalas._jegyar} Célállomás: {foglalas._celallomas} ")




