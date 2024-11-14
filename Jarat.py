from abc import ABC,abstractmethod

class Jarat(ABC):
    def __init__(self, jaratszam, indulas, celallomas, helyek_db, jegyar):
        self._jaratszam = jaratszam
        self._indulas = indulas
        self._celallomas = celallomas
        self._helyek_db = helyek_db
        self._jegyar = jegyar
        self._foglalt_e = False

    @abstractmethod
    def jegy_foglalas(self):
        pass

    @abstractmethod
    def jegy_foglalas_lemondasa(self):
        pass



