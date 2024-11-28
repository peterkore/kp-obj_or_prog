class JegyFoglalas:
    def __init__(self, jaratszam, jegy_id, foglalas_ideje, foglalt_e):
        #self._foglalasok = []
      #  self._nev = nev
        self._jaratszam = jaratszam
        self._jegy_id = jegy_id
        self._foglalas_ideje = foglalas_ideje
        self._foglalt_e = foglalt_e

    @property
    def foglalas_ideje(self):
        return self._foglalas_ideje

    @property
    def jaratszam(self):
        return self._jaratszam

    @property
    def jegy_id(self):
        return self._jegy_id

    @property
    def foglalt_e(self):
        return self._foglalt_e

    def jegy_foglalas(self):
        if not self.foglalt_e:
            self._foglalt_e = True
        else:
            print("hiba a jegy már foglalt")

    def jegy_lemondas(self):
        if self.foglalt_e:
            self._foglalt_e = False
        else:
            print("hiba a jegy már szabad")



  #  @property
  #  def nev(self):
  #      return self._nev





