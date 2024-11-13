class LegiTarsasag:
    def __init__(self, legitarsasag_neve):
        self._legitarsasag_neve = legitarsasag_neve
        self._jaratok = []


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

    def jegy_lemondasa_jaratszam_szerint(self, jaratszam):
        for jarat in self._jaratok:
            if jarat._jaratszam == jaratszam:
                jarat.jegy_foglalas()




