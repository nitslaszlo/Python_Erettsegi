from typing import List
from Áthajtás import Áthajtás


class Megoldás(object):
    _áthajtások: List[Áthajtás] = []

    def __init__(self, forrás: str) -> None:
        with open(forrás, 'r', encoding='utf-8') as sr:
            for sor in sr.read().splitlines():
                self._áthajtások.append(Áthajtás(sor))

    @property
    def utolsó_kivitel(self) -> Áthajtás:
        return list(filter(lambda x: x.kihajtás,  self._áthajtások))[-1]
