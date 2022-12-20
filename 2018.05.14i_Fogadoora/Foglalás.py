from datetime import datetime


class Foglalás:
    _tanár_neve: str
    _időpont: datetime
    _foglalás_időpontja: datetime

    @property
    def tanár_neve(self) -> str:
        return self._tanár_neve

    @property
    def időpont(self) -> datetime:
        return self._időpont

    @property
    def időpont_str(self) -> str:
        return self._időpont.strftime('%H:%M')

    @property
    def foglalás_időpontja(self) -> datetime:
        return self._foglalás_időpontja

    @property
    def foglalás_időpontja_str(self) -> str:
        return self._foglalás_időpontja.strftime('%Y.%m.%d-%H:%M')

    def __init__(self, sor: str) -> None:
        vnév, knév, időpont, foglalás_időpontja = sor.split(' ')
        self._tanár_neve = f'{vnév} {knév}'
        self._időpont = datetime.strptime(időpont, '%H:%M')
        self._foglalás_időpontja = datetime.strptime(foglalás_időpontja, '%Y.%m.%d-%H:%M')
