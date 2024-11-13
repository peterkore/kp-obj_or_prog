from Jarat import Jarat

class BelfoldiJarat(Jarat):
    def __init__(self, jaratszam, celallomas, jegyar):
        super().__init__(jaratszam, celallomas, jegyar)
        self._extrak = ["elsőbbségi beszállás", "1 kisméretű poggyász"]

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





