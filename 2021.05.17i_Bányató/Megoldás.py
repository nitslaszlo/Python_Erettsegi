class Megoldás(object):
    _matrix: list[list[int]] = list()

    @property
    def legmélyebb_helyek(self) -> str:
        vissza: str = ''
        for sor_index in range(len(self._matrix)):
            for oszlop_index in range(len(self._matrix[0])):
                if self._matrix[sor_index][oszlop_index] == self.max_mélység:
                    vissza += f'({sor_index + 1}; {oszlop_index + 1}) '
        return vissza

    @property
    def max_mélység(self) -> int:
        return max([max(sor) for sor in self._matrix])

    @property
    def felszín(self) -> int:
        szum: int = 0
        for sor in self._matrix:
            for m in sor:
                if m > 0:
                    szum += 1
        return szum

    @property
    def átlagos_mélység_m(self) -> float:
        szum: int = 0
        for sor in self._matrix:
            for m in sor:
                szum += m
        return szum / self.felszín / 10

    def __init__(self, forrás: str) -> None:
        with open(forrás, 'r', encoding='UTF8') as sr:
            for sor in sr.read().splitlines()[2:]:
                self._matrix.append([int(szám) for szám in sor.split(' ')])

    def mélység(self, sor: int, oszlop: int) -> int:
        return self._matrix[sor - 1][oszlop - 1]
