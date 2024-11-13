from abc import ABC,abstractmethod

class Jarat(ABC):
    def __init__(self, jaratszam, honnan, hova, helyek_db, jegyar):
        self._jaratszam = jaratszam
        self._honnan = honnan
        self._hova = hova
        self._helyek_db = helyek_db
        self._jegyar = jegyar
        self._foglalt_e = False

    @abstractmethod
    def jegy_foglalas(self):
        pass

    @abstractmethod
    def jegy_foglalas_lemondasa(self):
        pass



