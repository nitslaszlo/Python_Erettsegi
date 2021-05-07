from datetime import datetime
from Áthaladás import Áthaladás


class Megoldás(object):
    _áthaladások: list[Áthaladás] = []
    _MEGFIGYELÉS_VÉGE_PERC: int = 15 * 60

    @property
    def első_belépő(self) -> str:
        return self._áthaladások[0].azon

    @property
    def utolsó_kilépő(self) -> str:
        return list(filter(lambda x: x.ez_kilépő, self._áthaladások))[-1].azon

    @property
    def _statisztika(self) -> dict[str, int]:
        stat: dict[str, int] = dict()
        for áthaladás in self._áthaladások:
            if áthaladás.azon in stat:
                stat[áthaladás.azon] += 1
            else:
                stat[áthaladás.azon] = 1
        return dict(sorted(stat.items(), key=lambda t: int(t[0])))

    @property
    def társalgóban_maradtak(self) -> str:
        páratlan_értékkel = dict(filter(lambda x: x[1] % 2 == 1,  self._statisztika.items()))
        return ' '.join(páratlan_értékkel.keys())

    @property
    def legtöbben_a_társalgóban(self) -> datetime:
        akt_létszám: int = 1
        max_létszám: int = 1
        max_létszám_idő: datetime = self._áthaladások[0].idő
        for áthaladás in self._áthaladások[1:]:
            akt_létszám += 1 if áthaladás.ez_belépő else -1
            if akt_létszám > max_létszám:
                max_létszám = akt_létszám
                max_létszám_idő = áthaladás.idő
        return max_létszám_idő

    def __init__(self, forrás: str) -> None:
        with open(forrás, 'r', encoding='utf-8') as sr:
            for sor in sr.read().splitlines():
                self._áthaladások.append(Áthaladás(sor))

    def statisztikát_ír(self, fájlnév: str) -> None:
        with open(fájlnév, 'w', encoding='utf-8') as sw:
            for azon, db in self._statisztika.items():
                sw.write(f'{azon} {db}\n')

    def mettől_meddig(self, azon: str) -> str:
        mm: str = ''
        for áthaladás in self._áthaladások:
            if áthaladás.azon == azon:
                mm += áthaladás.idő.strftime('%H:%M')
                mm += '-' if áthaladás.ez_belépő else '\n'
        return mm

    def társalgóban_maradt(self, azon: str) -> bool:
        return azon in self.társalgóban_maradtak.split(' ')

    def eltöltött_idő_perc(self, azon: str) -> int:
        akt_belép_perc: int = 0
        akt_kilép_perc: int = 0
        eltöltött_perc: int = 0
        for áthaladás in self._áthaladások:
            if áthaladás.azon == azon and áthaladás.ez_belépő:
                akt_belép_perc = áthaladás.idő.hour * 60 + áthaladás.idő.minute
            if áthaladás.azon == azon and áthaladás.ez_kilépő:
                akt_kilép_perc = áthaladás.idő.hour * 60 + áthaladás.idő.minute
                eltöltött_perc += akt_kilép_perc - akt_belép_perc
        if self.társalgóban_maradt(azon):
            eltöltött_perc += self._MEGFIGYELÉS_VÉGE_PERC - akt_belép_perc
        return eltöltött_perc
