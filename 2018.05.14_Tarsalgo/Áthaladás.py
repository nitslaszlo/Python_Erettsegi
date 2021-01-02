from datetime import datetime


class Áthaladás(object):
    _idő: datetime
    _azon: str
    _irány: str

    @property
    def azon(self) -> str:
        return self._azon

    @property
    def idő(self) -> datetime:
        return self._idő

    @property
    def ez_kilépő(self) -> bool:
        return self._irány == 'ki'

    @property
    def ez_belépő(self) -> bool:
        return self._irány == 'be'

    def __init__(self, sor: str) -> None:
        idő_óra, idő_perc, azon, irány = sor.split(' ')
        self._idő = datetime.strptime(f'{idő_óra}:{idő_perc}', '%H:%M')  # str to datetime konverzió
        self._azon = azon
        self._irány = irány
