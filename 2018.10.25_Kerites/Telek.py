
class Telek(object):
    _házszám: int
    _szélesség: int
    _szín: str

    @property
    def ez_páros_telek(self) -> bool:
        return self._házszám % 2 == 0

    @property
    def ez_páratlan_telek(self) -> bool:
        return self._házszám % 2 == 1

    @property
    def oldal(self) -> str:
        return 'páros' if self.ez_páros_telek else 'páratlan'

    @property
    def házszám(self) -> int:
        return self._házszám

    @property
    def szín(self) -> str:
        return self._szín

    @property
    def szélesség(self) -> int:
        return self._szélesség

    def __init__(self, sor: str, házszám: int) -> None:
        self._házszám = házszám
        szélesség, szín = sor.split(' ')[1:]
        self._szélesség = int(szélesség)
        self._szín = szín
