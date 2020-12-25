from datetime import datetime


class Felszállás(object):
    _megálló_sorszáma: int
    _idő: datetime
    _azon: str

    def __init__(self, sor: str) -> None:
        sorszám, idő, azon = sor.split(' ')[0:3]
        self._megálló_sorszáma = int(sorszám)
        self._idő = datetime.strptime(idő, '%Y%m%d-%H%M')  # str to datetime konverzió
        self._azon = azon

    @property
    def érvényes_felszállás(self) -> bool:
        return False

    @property
    def megálló_sorszáma(self) -> int:
        return self._megálló_sorszáma

    @property
    def kedvezményes_utazás(self) -> bool:
        return False

    @property
    def ingyenes_utazás(self) -> bool:
        return False

    @property
    def lejár_három_nap(self) -> bool:
        return False

    @property
    def kártya_azon(self) -> str:
        return self._azon
