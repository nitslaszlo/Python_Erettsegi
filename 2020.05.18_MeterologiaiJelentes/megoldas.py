from jelentes import Jelentes
from typing import List
from typing import Set


class Megoldas(object):
    _LAST: int = -1
    _jelentesek: List[Jelentes] = list()

    def __init__(self, source_file: str) -> None:
        with open(source_file, 'r', encoding='utf-8') as sr:
            for i in sr.read().splitlines():
                self._jelentesek.append(Jelentes(i))

    @property
    def telepuleskodok(self) -> Set[str]:
        return set(i.telepuleskod for i in self._jelentesek)

    @property
    def homerseklet_stat(self) -> str:
        output: str = ''
        for tk in self.telepuleskodok:
            akt_telepules = list(filter(lambda x: x.telepuleskod == tk, self._jelentesek))
            akt_telepules_atlaghoz = list(filter(lambda x: x.atlaghoz, akt_telepules))
            orak = set(i.ora for i in akt_telepules_atlaghoz)
            if len(orak) == 4:  # Ha megvan mind a négy óra (1, 7, 13, 19) az átlaghoz:
                atlaghomerseklet = sum(c.homerseklet for c in akt_telepules_atlaghoz) / len(akt_telepules_atlaghoz)
                output += f'{tk} Középhőmérséklet: {atlaghomerseklet:.0f};'
            else:  # Egy vagy több óra hiányzik
                output += f'{tk} NA;'
            max_t = self.max_t_j(akt_telepules).homerseklet
            min_t = self.min_t_j(akt_telepules).homerseklet
            output += f'Hőmérséklet - ingadozás: {max_t - min_t}\n'
        return output

    @property
    def szelcsendes(self) -> List[Jelentes]:
        return list(filter(lambda x: x.szelcsend, self._jelentesek))

    def max_t_j(self, jelentesek: List[Jelentes] = []) -> Jelentes:
        jelentesek = jelentesek or self._jelentesek
        return max(jelentesek, key=lambda x: x.homerseklet)

    def min_t_j(self, jelentesek: List[Jelentes] = []) -> Jelentes:
        jelentesek = jelentesek or self._jelentesek
        return min(jelentesek, key=lambda x: x.homerseklet)

    def utolso_jelentes_ideje(self, telepuleskod: str) -> str:
        keresett_jelentesek = list(filter(lambda x: x.telepuleskod == telepuleskod, self._jelentesek))
        if len(keresett_jelentesek) > 0:  # Nem a feladat része!
            return str(keresett_jelentesek[self._LAST].idopont)
        else:
            return 'Nincs ilyen település!'  # Nem a feladat része!

    def write_data(self) -> None:
        for i in self.telepuleskodok:
            akt_telepules = list(filter(lambda x: x.telepuleskod == i, self._jelentesek))
            with open(f'txt_files/{i}.txt', 'w', encoding='utf-8') as sw:
                sw.write(f'{i}\n')
                for j in akt_telepules:
                    sw.write(f'{j.idopont} {"#" * j.erosseg}\n')
