class Epizód:
    def __init__(self, adatok: list[str]) -> None:
        self.vetítés: str = adatok[0]
        self.cím: str = adatok[1]
        self.évad_epizód: str = adatok[2]
        self.hossz: int = int(adatok[3])
        self.megnézte: bool = adatok[4] == '1'

    @property
    def ismert_a_vetítés_dátuma(self) -> bool:
        return self.vetítés != 'NI'

    @property
    def vetítés_év(self) -> int:
        return int(self.vetítés.split('.')[0]) if self.ismert_a_vetítés_dátuma else -1

    @property
    def vetítés_hó(self) -> int:
        return int(self.vetítés.split('.')[1]) if self.ismert_a_vetítés_dátuma else -1

    @property
    def vetítés_nap(self) -> int:
        return int(self.vetítés.split('.')[2]) if self.ismert_a_vetítés_dátuma else -1
