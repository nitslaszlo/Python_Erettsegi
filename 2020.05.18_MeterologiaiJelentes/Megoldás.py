from Jelentés import Jelentés


class Megoldás(object):
    _LAST: int = -1
    _jelentések: list[Jelentés] = list()

    def __init__(self, source_file: str) -> None:
        with open(source_file, 'r', encoding='utf-8') as sr:
            for i in sr.read().splitlines():
                self._jelentések.append(Jelentés(i))

    @property
    def településkódok(self) -> set[str]:
        return set(i.településkód for i in self._jelentések)

    @property
    def hőmérséklet_stat(self) -> str:
        vissza: str = ''
        for tk in self.településkódok:
            akt_település = list(filter(lambda x: x.településkód == tk, self._jelentések))
            akt_település_átlaghoz = list(filter(lambda x: x.átlaghoz, akt_település))
            órák: set[int] = set(i.óra for i in akt_település_átlaghoz)
            if len(órák) == 4:  # Ha megvan mind a négy óra (1, 7, 13, 19) az átlaghoz:
                átlaghőmérséklet = sum(c.hőmérséklet for c in akt_település_átlaghoz) / len(akt_település_átlaghoz)
                vissza += f'{tk} Középhőmérséklet: {átlaghőmérséklet:.0f};'
            else:  # Egy vagy több óra hiányzik
                vissza += f'{tk} NA;'
            max_t = self.max_t_j(akt_település).hőmérséklet
            min_t = self.min_t_j(akt_település).hőmérséklet
            vissza += f'Hőmérséklet - ingadozás: {max_t - min_t}\n'
        return vissza

    @property
    def szélcsendes(self) -> list[Jelentés]:
        return list(filter(lambda x: x.szélcsend, self._jelentések))

    def max_t_j(self, jelentesek: list[Jelentés] = []) -> Jelentés:
        jelentesek = jelentesek or self._jelentések
        return max(jelentesek, key=lambda x: x.hőmérséklet)

    def min_t_j(self, jelentesek: list[Jelentés] = []) -> Jelentés:
        jelentesek = jelentesek or self._jelentések
        return min(jelentesek, key=lambda x: x.hőmérséklet)

    def utolsó_jelentés_ideje(self, telepuleskod: str) -> str:
        keresett_jelentések = list(filter(lambda x: x.településkód == telepuleskod, self._jelentések))
        if len(keresett_jelentések) > 0:  # Nem a feladat része!
            return str(keresett_jelentések[self._LAST].időpont)
        else:
            return 'Nincs ilyen település!'  # Nem a feladat része!

    def adatokat_ír(self) -> None:
        for i in self.településkódok:
            akt_település = list(filter(lambda x: x.településkód == i, self._jelentések))
            with open(f'txt_files/{i}.txt', 'w', encoding='utf-8') as sw:
                sw.write(f'{i}\n')
                for j in akt_település:
                    sw.write(f'{j.időpont} {"#" * j.erősség}\n')
