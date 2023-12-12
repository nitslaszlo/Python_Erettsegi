from Beosztás import Beosztás


class Megoldás:
    _beosztások: list[Beosztás] = []

    def __init__(self, forrás_file: str) -> None:
        with open(forrás_file, 'r', encoding='utf-8') as sr:
            sorok: list[str] = sr.read().splitlines()
            for i in range(0, len(sorok), 4):
                self._beosztások.append(Beosztás(sorok[i:i+4]))

    @property
    def bejegyzések_száma(self) -> int:
        return len(self._beosztások)

    @property
    def összóraszám(self) -> int:
        # return sum(map(lambda x: x.óraszám, self._beosztások))
        return sum(e.óraszám for e in self._beosztások)

    def tanári_óraszám(self, név: str) -> int:
        return sum(e.óraszám for e in filter(lambda x: x.név == név, self._beosztások))

    def ofőket_ír(self, fájl_neve: str) -> None:
        with open(fájl_neve, 'w', encoding='utf-8') as sw:
            for e in filter(lambda x: x.tantárgy == 'osztalyfonoki', self._beosztások):
                sw.write(f'{e.osztály} - {e.név}\n')

    def csoportbontás_van(self, osztály: str, tantárgy: str) -> bool:
        beosztások_segéd: list[Beosztás] = list(filter(
            lambda x: x.osztály == osztály and x.tantárgy == tantárgy, self._beosztások))
        return len(beosztások_segéd) == 2

    @property
    def tanárok_száma(self) -> int:
        return len(set(map(lambda x: x.név, self._beosztások)))
