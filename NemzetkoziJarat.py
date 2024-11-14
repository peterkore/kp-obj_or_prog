from Jarat import Jarat

class NemzetkoziJarat(Jarat):
    def __init__(self, jaratszam, indulas, celallomas, helyek_db, jegyar):
        super().__init__(jaratszam, indulas, celallomas, helyek_db, jegyar)
        self._extrak = ["elsőbbségi beszállás", "1 kisméretű poggyász", "Gyors átjutás a biztonsági ellenőrzésen"]

    @property
    def jaratszam(self):
        return self._jaratszam

    @property
    def indulas(self):
        return self._indulas

    @property
    def celallomas(self):
        return self._celallomas

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




