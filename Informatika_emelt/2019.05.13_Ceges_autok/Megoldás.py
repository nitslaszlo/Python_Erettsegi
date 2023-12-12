from Áthajtás import Áthajtás


class MaxÁthajtás:  # segéd osztály a 6. feladathoz
    megtett_km: int
    szem_azon: str


class Megoldás:
    _áthajtások: list[Áthajtás] = []

    @property
    def utolsó_kivitel(self) -> Áthajtás:
        return list(filter(lambda x: x.kihajtás, self._áthajtások))[-1]

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
            akt_rendszám: str = f'CEG30{jegy}'
            akt_áthajtások: list[Áthajtás] = self._auto_áthajtásai(
                akt_rendszám)
            számláló_diff: int = akt_áthajtások[-1].km_számláló - \
                akt_áthajtások[0].km_számláló
            vissza += f'CEG30{jegy} {számláló_diff} km\n'
        return vissza.strip()

    @property
    def max_áthajtás(self) -> MaxÁthajtás:
        max_áthajtás: MaxÁthajtás = MaxÁthajtás()
        max_áthajtás.megtett_km = 0
        for i, e1 in enumerate(self._áthajtások):
            if e1.kihajtás:
                # megkeressük, hogy mikor hozták vissza a kocsit:
                for e2 in self._áthajtások[i + 1:]:
                    if e2.rendszám == e1.rendszám:
                        megtett_km: int = e2.km_számláló - e1.km_számláló
                        if megtett_km > max_áthajtás.megtett_km:
                            max_áthajtás.megtett_km = megtett_km
                            max_áthajtás.szem_azon = e2.szem_azon
                        break  # "kilépünk" a belső (beágyazott) ciklusból
        return max_áthajtás

    def __init__(self, forrás: str) -> None:
        with open(forrás, 'r', encoding='utf-8') as sr:
            for sor in sr.read().splitlines():
                self._áthajtások.append(Áthajtás(sor))

    def _auto_áthajtásai(self, rendszám: str) -> list[Áthajtás]:
        return list(filter(lambda x: x.rendszám == rendszám, self._áthajtások))

    def menetlevelet_ír(self, rendszám: str) -> None:
        akt_áthajtások: list[Áthajtás] = list(
            filter(lambda x: x.rendszám == rendszám, self._áthajtások))
        with open('menetlevelek/' + rendszám + '_menetlevel.txt', 'w', encoding='utf-8') as sw:
            for e in akt_áthajtások:
                if e.kihajtás:
                    sw.write(
                        f'{e.szem_azon}\t{e.nap}. {e.idő}\t{e.km_számláló} km')
                else:
                    sw.write(f'\t{e.nap}. {e.idő}\t{e.km_számláló} km\n')
