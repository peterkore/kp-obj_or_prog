from Jarat import Jarat

class NemzetkoziJarat(Jarat):
    def __init__(self, jaratszam, celallomas, jegyar):
        super().__init__(jaratszam, celallomas, jegyar)
        self._extrak = ["elsőbbségi beszállás", "1 kisméretű poggyász", "Gyors átjutás a biztonsági ellenőrzésen"]

    @property
    def jaratszam(self):
        return self._jaratszam

    @property
    def celallomas(self):
        return self._celallomas

    @property
    def foglalt(self):
        return self._foglalt

    @property
    def jegyar(self):
        return self._jegyar




