from datetime import datetime, timedelta
from Felszállás import Felszállás


class FelszállásBérlet(Felszállás):
    _típus: str
    _érvényes_idő: datetime

    def __init__(self, sor: str) -> None:
        super().__init__(sor)
        típus, érvényes_idő = sor.split(' ')[3:5]
        self._típus = típus
        self._érvényes_idő = datetime.strptime(érvényes_idő + '-23:59', '%Y%m%d-%H:%M')

    @property
    def érvényes_felszállás(self) -> bool:
        return self._idő <= self._érvényes_idő

    @property
    def kedvezményes_utazás(self) -> bool:
        return self.érvényes_felszállás and self._típus in ["TAB", "NYB"]

    @property
    def ingyenes_utazás(self) -> bool:
        return self.érvényes_felszállás and self._típus in ["NYP", "RVS", "GYK"]

    @property
    def lejár_három_nap(self) -> bool:
        tdiff: timedelta = self._érvényes_idő - self._idő
        return self.érvényes_felszállás and tdiff.days <= 3

    @property
    def lejárat(self) -> str:
        return self._érvényes_idő.strftime('%Y-%m-%d')
