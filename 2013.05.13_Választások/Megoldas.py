from ValasztasiEredmeny import ValasztasiEredmeny


class Megoldas(object):
    _eredmények: list[ValasztasiEredmeny] = []

    @property
    def jelöltek_száma(self) -> int:
        return len(self._eredmények)

    @property
    def szavazatok_száma(self) -> int:
        szum: int = 0
        for e in self._eredmények:
            szum += e.szavazatok
        return szum

    @property
    def szavazott_százalék(self) -> str:
        return f'{self.szavazatok_száma / 12345:.2%}'

    @property
    def _eredmeny_stat(self) -> dict[str, int]:
        stat: dict[str, int] = {}
        for e in self._eredmények:
            if e.párt in stat:
                stat[e.párt] += e.szavazatok
            else:
                stat[e.párt] = e.szavazatok
        return stat

    @property
    def szavazat_stat(self) -> str:
        vissza: str = ''
        szavazatok_száma: int = self.szavazatok_száma
        stat: dict[str, int] = self._eredmeny_stat
        # Ha nem kell szóköz a százalék jel elé:
        # for key, value in stat.items():
        #     vissza += f'{key} {value / szavazatok_száma:.2%}\n'

        # Szóközös megoldás:
        for key, value in stat.items():
            vissza += f'{key} {value / szavazatok_száma * 100:.2f} %\n'

        return vissza

    @property
    def _legtöbb_szavazat(self) -> int:
        max: int = -1
        for e in self._eredmények:
            if e.szavazatok > max:
                max = e.szavazatok
        return max

    @property
    def győztes_képviselők(self) -> str:
        vissza: str = ''
        max: int = self._legtöbb_szavazat
        for e in self._eredmények:
            if e.szavazatok == max:
                vissza += f'{e.név} {e.párt_jel2}\n'
        return vissza

    @property
    def _kerület_stat(self) -> dict[int, ValasztasiEredmeny]:
        stat: dict[int, ValasztasiEredmeny] = {}
        for e in self._eredmények:
            if e.kerület in stat:
                if e.szavazatok > stat[e.kerület].szavazatok:
                    stat[e.kerület] = e
            else:
                stat[e.kerület] = e
        return stat

    def __init__(self, forrás: str) -> None:
        with open(forrás, 'r', encoding='utf-8') as sr:
            for sor in sr.read().splitlines():
                self._eredmények.append(ValasztasiEredmeny(sor))

    def _képviselő_indexe(self, képviselő_neve: str) -> int:
        ind: int = -1
        for index, item in enumerate(self._eredmények):
            if item.név == képviselő_neve:
                ind = index
                break
        return ind

    def képviselő_keresése(self, képviselő_neve: str) -> str:
        ind: int = self._képviselő_indexe(képviselő_neve)
        if ind == -1:
            return "Ilyen nevű képviselőjelölt nem szerepel a nyilvántartásban!"
        else:
            return f'{képviselő_neve} {self._eredmények[ind].szavazatok} szavazatot kapott.'

    def állományt_ír(self, állomány_neve: str) -> None:
        with open(állomány_neve, 'w', encoding='utf-8') as sw:
            ks: dict[int, ValasztasiEredmeny] = self._kerület_stat
            for kerület in range(1, 9):
                sw.write(f'{kerület}.kerület: {ks[kerület].név} {ks[kerület].párt_jel2}\n')
