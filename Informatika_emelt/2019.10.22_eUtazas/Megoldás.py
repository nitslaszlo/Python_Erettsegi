from FelszállásBérlet import FelszállásBérlet
from FelszállásJegy import FelszállásJegy
from Felszállás import Felszállás


class LegtöbbFelszálló:
    megálló: int
    felszálló_fő: int

    def __init__(self):
        self.megálló = -1
        self.felszálló_fő = -1


class Megoldás:
    _utasadatok: list[Felszállás] = []

    @property
    def felszállók_száma(self) -> int:
        return len(self._utasadatok)

    @property
    def érvénytelen_felszállás(self) -> int:
        return len(list(filter(lambda x: x.érvényes_felszállás is False, self._utasadatok)))

    @property
    def legtöbb_felszálló(self) -> LegtöbbFelszálló:
        megálló: dict[int, int] = {}
        for utasadat in self._utasadatok:
            if utasadat.megálló_sorszáma in megálló:
                megálló[utasadat.megálló_sorszáma] += 1
            else:
                megálló[utasadat.megálló_sorszáma] = 1
        legtöbb_fsz = LegtöbbFelszálló()
        legtöbb_fsz.felszálló_fő = max(megálló.values())
        for key, value in megálló.items():
            if value == legtöbb_fsz.felszálló_fő:
                legtöbb_fsz.megálló = key
                break
        return legtöbb_fsz

    @property
    def kedvezményes_utazás(self) -> int:
        return len(list(filter(lambda x: x.kedvezményes_utazás, self._utasadatok)))

    @property
    def ingyenes_utazás(self) -> int:
        return len(list(filter(lambda x: x.ingyenes_utazás, self._utasadatok)))

    # 6. feladat:
    @staticmethod
    def napokszama(e1: int, h1: int, n1: int, e2: int, h2: int, n2: int) -> int:
        h1 = (h1 + 9) % 12
        e1 = e1 - h1 // 10
        d1: int = 365 * e1 + e1 // 4 - e1 // 100 + \
            e1 // 400 + (h1 * 306 + 5) // 10 + n1 - 1
        h2 = (h2 + 9) % 12
        e2 = e2 - h2 // 10
        d2: int = 365 * e2 + e2 // 4 - e2 // 100 + \
            e2 // 400 + (h2 * 306 + 5) // 10 + n2 - 1
        return d2 - d1

    def __init__(self, forrás: str) -> None:
        with open(forrás, 'r', encoding='UTF8') as sr:
            for sor in sr.read().splitlines():
                típus = sor.split(' ')[3]
                if típus == 'JGY':
                    self._utasadatok.append(FelszállásJegy(sor))
                else:
                    self._utasadatok.append(FelszállásBérlet(sor))

    def figyelmeztetést_ír(self, file_neve: str) -> None:
        with open(file_neve, 'w', encoding='UTF8') as sw:
            for e in self._utasadatok:
                if isinstance(e, FelszállásBérlet) and e.lejár_három_nap:
                    sw.write(f'{e.kártya_azon} {e.lejárat}\n')
