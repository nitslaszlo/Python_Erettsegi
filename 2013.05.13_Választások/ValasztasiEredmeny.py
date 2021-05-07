class ValasztasiEredmeny(object):
    _kerület: int
    _szavazatok: int
    _vnév: str
    _knév: str
    _párt_jel: str

    @property
    def név(self) -> str:
        return f'{self._vnév} {self._knév}'

    @property
    def szavazatok(self) -> int:
        return self._szavazatok

    @property
    def kerület(self) -> int:
        return self._kerület

    @property
    def párt_jel2(self) -> str:
        return 'Független' if self._párt_jel == '-' else self._párt_jel

    @property
    def párt(self) -> str:
        párt_szótár: dict[str, str] = {
            'GYEP': 'Gyümölcsevők pártja',
            'HEP': 'Húsevők pártja',
            'TISZ': 'Tejívók szövetsége',
            'ZEP': 'Zöldségevők pártja',
            '-': 'Független jelöltek',
        }
        return párt_szótár[self._párt_jel]

    def __init__(self, sor: str) -> None:
        kerület, szavazatok, vnév, knév, párt_jel = sor.split(' ')
        self._kerület = int(kerület)
        self._szavazatok = int(szavazatok)
        self._vnév = vnév
        self._knév = knév
        self._párt_jel = párt_jel
