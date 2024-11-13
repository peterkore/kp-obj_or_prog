from Jarat import Jarat

class BelfoldiJarat(Jarat):
    def __init__(self, jaratszam, honnan, hova, helyek_db, jegyar):
        super().__init__(jaratszam, honnan, hova, helyek_db, jegyar)
        self._extrak = ["elsőbbségi beszállás", "1 kisméretű poggyász"]

    @property
    def jaratszam(self):
        return self._jaratszam

    @property
    def honnan(self):
        return self._honnan

    @property
    def hova(self):
        return self._hova

    @property
    def helyek_db(self):
        return self._helyek_db

    @property
    def foglalt(self):
        return self._foglalt

    @property
    def jegyar(self):
        return self._jegyar

    def jegy_foglalas(self):
        if not self._foglalt_e:
            self._foglalt_e = True

        else:
            print("Hiba a jegy foglalt!")

    def jegy_foglalas_lemondasa(self):
        if self._foglalt_e:
            self._foglalt_e = False
        else:
            print("Hiba a jegy foglalt!")






