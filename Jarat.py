from abc import ABC,abstractmethod

class Jarat(ABC):
    def __init__(self, jaratszam, celallomas, jegyar):
        self._jaratszam = jaratszam
        self._celallomas = celallomas
        self._jegyar = jegyar
        self._foglalt_e = False

    @abstractmethod
    def jegy_foglalas(self):
        pass

    @abstractmethod
    def jegy_foglalas_lemondasa(self):
        pass



