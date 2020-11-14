from typing import List


class Epizod(object):
    def __init__(self, adatok: List[str]) -> None:
        self.vetites: str = adatok[0]
        self.cim: str = adatok[1]
        self.evad_epizod: str = adatok[2]
        self.hossz: int = int(adatok[3])
        self.megnezte: bool = adatok[4] == '1'

    @property
    def ismert_a_vetites_datuma(self) -> bool:
        return self.vetites != 'NI'

    @property
    def vetites_ev(self) -> int:
        return int(self.vetites.split('.')[0]) if self.ismert_a_vetites_datuma else -1

    @property
    def vetites_ho(self) -> int:
        return int(self.vetites.split('.')[1]) if self.ismert_a_vetites_datuma else -1

    @property
    def vetites_nap(self) -> int:
        return int(self.vetites.split('.')[2]) if self.ismert_a_vetites_datuma else -1
