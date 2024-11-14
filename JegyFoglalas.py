class JegyFoglalas:
    def __init__(self, jegy_id, foglalas_idopontja, jarat_szam):
        self._jegy_id = jegy_id
        self._foglalas_idopontja = foglalas_idopontja
        self._jarat_szam = jarat_szam



    @property

    def jegy_id(self):
        return self._jegy_id

    @property
    def foglalas_idopontja(self):
        return self._foglalas_idopontja

    @property
    def jarat_szam(self):
        return self._jarat_szam

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

