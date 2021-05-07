from datetime import datetime
from datetime import timedelta
from Foglalás import Foglalás


class Megoldás(object):
    _foglalások: list[Foglalás] = list()

    @property
    def foglalások_száma(self) -> int:
        return len(self._foglalások)

    @property
    def első_foglalás(self) -> str:
        f: Foglalás = sorted(self._foglalások, key=lambda x: x.foglalás_időpontja)[0]
        return f'Tanár neve: {f.tanár_neve}\nFoglalt időpont: {f.időpont_str}\nFoglalás ideje: {f.foglalás_időpontja_str}\n'

    def __init__(self, forrás: str) -> None:
        with open(forrás, 'r', encoding='utf-8') as sr:
            for sor in sr.read().splitlines():
                self._foglalások.append(Foglalás(sor))

    def időpontfoglalások_száma(self, tanár_neve: str) -> int:
        return len(list(filter(lambda x: x.tanár_neve == tanár_neve, self._foglalások)))

    def foglalt_tanárok(self, időpont: str) -> str:
        idő: datetime = datetime.strptime(időpont, '%H:%M')
        nevek: set[str] = set(e.tanár_neve for e in filter(lambda x: x.időpont == idő, self._foglalások))
        ki: str = '\n'.join(sorted(nevek))
        with open(f'foglalt_tanárok/{időpont.replace(":", "")}.txt', 'w', encoding='utf-8') as sw:
            sw.write(f'{ki}\n')
        return ki

    def tanár_szabad(self, tanár_neve: str) -> str:
        szabad_időpontok: list[str] = []
        for óra in range(16, 18):
            for perc in range(0, 60, 10):
                szabad_időpontok.append(f'{óra}:{str(perc).zfill(2)}')
        for foglalás in filter(lambda x: x.tanár_neve == tanár_neve, self._foglalások):
            szabad_időpontok.remove(foglalás.időpont_str)
        return '\n'.join(sorted(szabad_időpontok))

    def tanár_legkorábban_távozhat(self, tanár_neve: str) -> str:
        tanár_foglalások: list[Foglalás] = list(filter(lambda x: x.tanár_neve == tanár_neve, self._foglalások))
        return (sorted(tanár_foglalások, key=lambda x: x.időpont)[-1].időpont + timedelta(minutes=10)).strftime('%H:%M')
