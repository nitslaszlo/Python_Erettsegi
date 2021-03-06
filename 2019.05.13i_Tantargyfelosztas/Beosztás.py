from typing import List


class Beosztás(object):
    _név: str
    _tantárgy: str
    _osztály: str
    _óraszám: int

    def __init__(self, adatok: List[str]) -> None:
        név, tantárgy, osztály, óraszám = adatok
        self._név = név
        self._tantárgy = tantárgy
        self._osztály = osztály
        self._óraszám = int(óraszám)

    @property
    def óraszám(self) -> int:
        return self._óraszám

    @property
    def név(self) -> str:
        return self._név

    @property
    def osztály(self) -> str:
        return self._osztály

    @property
    def tantárgy(self) -> str:
        return self._tantárgy
