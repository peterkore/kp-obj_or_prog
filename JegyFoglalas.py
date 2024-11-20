class JegyFoglalas:
    def __init__(self, foglalas_idopontja, jaratszam):
        self._foglalasok = []
        self._foglalas_idopontja = foglalas_idopontja
        self._jaratszam = jaratszam

    @property
    def foglalas_idopontja(self):
        return self._foglalas_idopontja

    @property
    def jarat_szam(self):
        return self._jaratszam



   # @property
   # def foglalasok(self):
    #    return self._foglalasok
        #for foglalas in self._foglalasok:
         #   print(f" Járatszám: {foglalas._jaratszam}  ")

    #@foglalasok.setter
    #def foglalasok(self, foglalas):
    #    self._foglalasok.append(foglalas)

    #@property
    #def foglalasok_listazasa(self):
    #    for foglalas in self._foglalasok:
    #        print(f" Járatszám: {foglalas._jaratszam}  ")

