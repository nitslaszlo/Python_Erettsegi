class Áthajtás:
    _nap: str
    _idő: str
    _rendszám: str
    _szem_azon: str
    _km_számláló: int
    _behajtás: bool

    def __init__(self, sor: str) -> None:
        nap, idő, rendszám, szem_azon, km_számláló, behajtás = sor.split(' ')
        self._nap = nap
        self._idő = idő
        self._rendszám = rendszám
        self._szem_azon = szem_azon
        self._km_számláló = int(km_számláló)
        self._behajtás = behajtás == '1'

    @property
    def behajtás(self) -> bool:
        return self._behajtás

    @property
    def kihajtás(self) -> bool:
        return not self._behajtás

    @property
    def nap(self) -> str:
        return self._nap

    @property
    def rendszám(self) -> str:
        return self._rendszám

    @property
    def forgalom(self) -> str:
        return f'{self._idő} {self.rendszám} {self._szem_azon} {"be" if self.behajtás else "ki"}'

    @property
    def km_számláló(self) -> int:
        return self._km_számláló

    @property
    def szem_azon(self) -> str:
        return self._szem_azon

    @property
    def idő(self) -> str:
        return self._idő
