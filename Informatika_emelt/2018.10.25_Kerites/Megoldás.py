from Telek import Telek


class Megoldás:
    _telkek: list[Telek] = []

    @property
    def telkek_száma(self) -> int:
        return len(self._telkek)

    @property
    def utolsó_eladott_telek(self) -> Telek:
        return self._telkek[-1]

    @property
    def szomszédossal_azonos_szín(self) -> int:
        páratlan_telkek: list[Telek] = list(filter(lambda x: x.ez_páratlan_telek, self._telkek))
        for i in range(len(páratlan_telkek)-1):
            if str.isalpha(páratlan_telkek[i].szín) and páratlan_telkek[i].szín == páratlan_telkek[i+1].szín:
                return páratlan_telkek[i].házszám
        return -1

    def __init__(self, forrás: str) -> None:
        with open(forrás, 'r', encoding='utf-8') as sr:
            páratlan_házszám: int = 1
            páros_házszám: int = 2
            for sor in sr.read().splitlines():
                if sor[0] == '0':
                    self._telkek.append(Telek(sor, páros_házszám))
                    páros_házszám += 2
                if sor[0] == '1':  # állhatna else is, de így ellenőrizzük az adatsor első adatát is
                    self._telkek.append(Telek(sor, páratlan_házszám))
                    páratlan_házszám += 2

    def keresett_telek(self, házszám: int) -> Telek:
        return list(filter(lambda x: x.házszám == házszám, self._telkek))[0]

    def _létező_házszám(self, házszám: int) -> bool:
        return len(list(filter(lambda x: x.házszám == házszám, self._telkek))) > 0

    def lehetséges_szín(self, házszám: int) -> str:
        színek: set[str] = {'A', 'B', 'C', 'D'}
        for hsz in range(házszám - 2, házszám + 3, 2):  # pl.: ha a házszám=83, akkor: 81, 83, 85
            if self._létező_házszám(hsz):
                akt_telek: Telek = self.keresett_telek(hsz)
                if akt_telek.szín in színek:
                    színek.remove(akt_telek.szín)
        return színek.pop()

    def utcaképet_ír(self, fájl_neve: str) -> None:
        with open(fájl_neve, 'w', encoding='utf-8') as sw:
            sor1: str = ''
            sor2: str = ''
            for t in filter(lambda x: x.ez_páratlan_telek, self._telkek):
                sor1 += ''.ljust(t.szélesség, t.szín)
                # vagy:
                # sor1 += t.szín * t.szélesség
                sor2 += str(t.házszám).ljust(t.szélesség, ' ')
                # vagy:
                # sor2 += str(t.házszám)+' ' * (t.szélesség - len(str(t.házszám)))
            sw.write(f'{sor1}\n{sor2}\n')
