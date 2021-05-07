from Áthajtás import Áthajtás


class MaxÁthajtás(object):  # segéd osztály a 6. feladathoz
    megtett_km: int
    szem_azon: str


class Megoldás(object):
    _áthajtások: list[Áthajtás] = []

    def __init__(self, forrás: str) -> None:
        with open(forrás, 'r', encoding='utf-8') as sr:
            for sor in sr.read().splitlines():
                self._áthajtások.append(Áthajtás(sor))

    @property
    def utolsó_kivitel(self) -> Áthajtás:
        return list(filter(lambda x: x.kihajtás,  self._áthajtások))[-1]

    def forgalom(self, nap: str) -> str:
        return '\n'.join(e.forgalom for e in filter(lambda x: x.nap == nap, self._áthajtások))

    @property
    def kintlévő_autók_száma(self) -> int:
        db: int = 0
        for e in self._áthajtások:
            db += 1 if e.kihajtás else -1
        return db

    @property
    def statisztika(self) -> str:
        vissza: str = ''
        for jegy in range(10):
            akt_áthajtások: list[Áthajtás] = list(filter(lambda x: x.rendszám == f'CEG30{jegy}', self._áthajtások))
            számláló_diff: int = akt_áthajtások[-1].km_számláló - akt_áthajtások[0].km_számláló
            vissza += f'CEG30{jegy} {számláló_diff} km\n'
        return vissza.strip()

    @property
    def max_áthajtás(self) -> MaxÁthajtás:
        max: MaxÁthajtás = MaxÁthajtás()
        max.megtett_km = 0
        for i in range(len(self._áthajtások)):
            if self._áthajtások[i].kihajtás:
                for j in range(i+1, len(self._áthajtások)):  # megkeressük, hogy mikor hozták vissza a kocsit:
                    if self._áthajtások[j].rendszám == self._áthajtások[i].rendszám:
                        megtett_km: int = self._áthajtások[j].km_számláló - self._áthajtások[i].km_számláló
                        if megtett_km > max.megtett_km:
                            max.megtett_km = megtett_km
                            max.szem_azon = self._áthajtások[j].szem_azon
                        break  # "kilépünk" a belső (beágyazott) ciklusból
        return max

    def menetlevelet_ír(self, rendszám: str) -> None:
        akt_áthajtások: list[Áthajtás] = list(filter(lambda x: x.rendszám == rendszám, self._áthajtások))
        with open('menetlevelek/' + rendszám + '_menetlevel.txt', 'w', encoding='utf-8') as sw:
            for e in akt_áthajtások:
                if e.kihajtás:
                    sw.write(f'{e.szem_azon}\t{e.nap}. {e.idő}\t{e.km_számláló} km')
                else:
                    sw.write(f'\t{e.nap}. {e.idő}\t{e.km_számláló} km\n')
