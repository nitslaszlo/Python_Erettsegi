from epizod import Epizod
from typing import Dict, List


class Megoldas(object):
    epizodok: List[Epizod] = list()

    def __init__(self, forras_file: str) -> None:
        with open(forras_file, 'r', encoding='UTF8') as sr:
            sorok: List[str] = sr.read().splitlines()
            for i in range(0, len(sorok), 5):
                self.epizodok.append(Epizod(sorok[i:i+5]))

    @property
    def ismert_a_vetites_datuma_darab(self) -> int:
        return len(list(filter(lambda x: x.ismert_a_vetites_datuma, self.epizodok)))

    @property
    def _megnezett_epizodok(self) -> List[Epizod]:
        return list(filter(lambda x: x.megnezte, self.epizodok))

    @property
    def megnezve_arany(self) -> float:
        return len(self._megnezett_epizodok) / len(self.epizodok)

    @property
    def ossz_ido_perc(self) -> int:
        return sum(map(lambda x: x.hossz, self._megnezett_epizodok))

    @property
    def ido_nap(self) -> int:
        return self.ossz_ido_perc // 1440

    @property
    def ido_ora(self) -> int:
        return (self.ossz_ido_perc % 1440) // 60

    @property
    def ido_perc(self) -> int:
        return self.ossz_ido_perc % 60

    @property
    def stat(self) -> List[str]:
        szotar_ido: Dict[str, int] = dict()
        szotar_epizod_db: Dict[str, int] = dict()
        for i in self.epizodok:
            if i.cim in szotar_ido:
                szotar_ido[i.cim] += i.hossz
                szotar_epizod_db[i.cim] += 1
            else:
                szotar_ido[i.cim] = i.hossz
                szotar_epizod_db[i.cim] = 1
        vissza: List[str] = list()
        for kulcs in szotar_ido:
            vissza.append(f'{kulcs} {szotar_ido[kulcs]} {szotar_epizod_db[kulcs]}')
        return vissza

    def write_stat(self, file_neve: str) -> None:
        with open(file_neve, 'w', encoding='UTF8') as sw:
            for sor in self.stat:
                sw.write(f'{sor}\n')

    @staticmethod
    def hetnapja(ev: int, ho: int, nap: int) -> str:
        napok: List[str] = ['v', 'h', 'k', 'sz', 'cs', 'p', 'szo']
        honapok: List[int] = [0, 3, 2, 5, 0, 3, 5, 1, 4, 6, 2, 4]
        if ho < 3:
            ev -= 1
        return napok[(ev + ev // 4 - ev // 100 + ev // 400 + honapok[ho - 1] + nap) % 7]

    def nem_latta_meg(self, input_datum: str) -> List[str]:
        vissza: List[str] = list()
        for i in self.epizodok:
            if i.ismert_a_vetites_datuma and i.megnezte is False and i.vetites <= input_datum:
                vissza.append(f'{i.evad_epizod}\t{i.cim}')
        return vissza

    def adott_napon_vetitett(self, input_nap: str) -> List[str]:
        vissza: List[str] = list()
        for i in self.epizodok:
            if i.ismert_a_vetites_datuma:
                if Megoldas.hetnapja(i.vetites_ev, i.vetites_ho, i.vetites_nap) == input_nap:
                    if i.cim not in vissza:
                        vissza.append(f'{i.cim}')
        if len(vissza) == 0:
            vissza.append('Az adott napon nem kerül adásba sorozat.')
        return vissza
