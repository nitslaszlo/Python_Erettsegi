from Epizód import Epizód


class Megoldás:
    _epizódok: list[Epizód] = []

    def __init__(self, forras_file: str) -> None:
        with open(forras_file, 'r', encoding='UTF8') as sr:
            sorok: list[str] = sr.read().splitlines()
            for i in range(0, len(sorok), 5):
                self._epizódok.append(Epizód(sorok[i:i+5]))

    @property
    def ismert_a_vetítés_dátuma_darab(self) -> int:
        return len(list(filter(lambda x: x.ismert_a_vetítés_dátuma, self._epizódok)))

    @property
    def _megnézett_epizódok(self) -> list[Epizód]:
        return list(filter(lambda x: x.megnézte, self._epizódok))

    @property
    def megnézve_arány(self) -> float:
        return len(self._megnézett_epizódok) / len(self._epizódok)

    @property
    def össz_idő_perc(self) -> int:
        return sum(map(lambda x: x.hossz, self._megnézett_epizódok))

    @property
    def idő_nap(self) -> int:
        return self.össz_idő_perc // 1440

    @property
    def idő_óra(self) -> int:
        return (self.össz_idő_perc % 1440) // 60

    @property
    def idő_perc(self) -> int:
        return self.össz_idő_perc % 60

    @property
    def stat(self) -> list[str]:
        szótár_idő: dict[str, int] = dict()
        szótár_epizód_db: dict[str, int] = dict()
        for e in self._epizódok:
            if e.cím in szótár_idő:
                szótár_idő[e.cím] += e.hossz
                szótár_epizód_db[e.cím] += 1
            else:
                szótár_idő[e.cím] = e.hossz
                szótár_epizód_db[e.cím] = 1
        vissza: list[str] = []
        for key, value in szótár_idő.items():
            vissza.append(f'{key} {value} {szótár_epizód_db[key]}')
        return vissza

    def stat_ír(self, file_neve: str) -> None:
        with open(file_neve, 'w', encoding='UTF8') as sw:
            for sor in self.stat:
                sw.write(f'{sor}\n')

    def nem_látta_még(self, input_datum: str) -> list[str]:
        vissza: list[str] = list()
        for e in self._epizódok:
            if e.ismert_a_vetítés_dátuma and e.megnézte is False and e.vetítés <= input_datum:
                vissza.append(f'{e.évad_epizód}\t{e.cím}')
        return vissza

    def adott_napon_vetített(self, input_nap: str) -> list[str]:
        vissza: list[str] = list()
        for e in self._epizódok:
            if e.ismert_a_vetítés_dátuma:
                if Megoldás.hetnapja(e.vetítés_év, e.vetítés_hó, e.vetítés_nap) == input_nap:
                    if e.cím not in vissza:
                        vissza.append(f'{e.cím}')
        if len(vissza) == 0:
            vissza.append('Az adott napon nem kerül adásba sorozat.')
        return vissza

    @staticmethod
    def hetnapja(ev: int, ho: int, nap: int) -> str:
        napok: list[str] = ['v', 'h', 'k', 'sz', 'cs', 'p', 'szo']
        honapok: list[int] = [0, 3, 2, 5, 0, 3, 5, 1, 4, 6, 2, 4]
        if ho < 3:
            ev -= 1
        return napok[(ev + ev // 4 - ev // 100 + ev // 400 + honapok[ho - 1] + nap) % 7]
