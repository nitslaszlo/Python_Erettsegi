from Beosztás import Beosztás
from typing import List, OrderedDict, Set


class Megoldás(object):
    _beosztások: List[Beosztás] = []

    def __init__(self, forrás_file: str) -> None:
        with open(forrás_file, 'r', encoding='utf-8') as sr:
            sorok: List[str] = sr.read().splitlines()
            for i in range(0, len(sorok), 4):
                self._beosztások.append(Beosztás(sorok[i:i+4]))

    @property
    def bejegyzések_száma(self) -> int:
        return len(self._beosztások)

    @property
    def összóraszám(self) -> int:
        return sum(map(lambda x: x.óraszám, self._beosztások))

    def tanári_óraszám(self, név: str) -> int:
        tanár_bejegyzései: List[Beosztás] = list(filter(lambda x: x.név == név, self._beosztások))
        return sum(map(lambda x: x.óraszám, tanár_bejegyzései))

    def ofőket_ír(self, fájl_neve: str) -> None:
        osztalyok: OrderedDict[str, str] = OrderedDict()
        for beosztás in self._beosztások:
            if beosztás.tantárgy == 'osztalyfonoki' and beosztás.osztály not in osztalyok:
                osztalyok[beosztás.osztály] = beosztás.név
        with open(fájl_neve, 'w', encoding='utf-8') as sw:
            for osztály, ofő in osztalyok.items():
                sw.write(f'{osztály} - {ofő}\n')

    def csoportbontás_van(self, osztály: str, tantárgy: str) -> bool:
        bejegyzések_száma = 0
        for beosztás in self._beosztások:
            if beosztás.osztály == osztály and beosztás.tantárgy == tantárgy:
                bejegyzések_száma += 1
        return bejegyzések_száma == 2

    @property
    def tanárok_száma(self) -> int:
        tanárok: Set[str] = set()
        for beosztás in self._beosztások:
            tanárok.add(beosztás.név)
        return len(tanárok)
