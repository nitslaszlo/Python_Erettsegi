from datetime import datetime


class ValasztasiEredmeny(object):
    _kerület: int
    _szavazatok: int
    _vnév: str
    _knév: str
    _párt_jel: str
    _foglalás_időpontja: datetime

    def __init__(self, sor: str) -> None:
        kerület, szavazatok, vnév, knév, párt_jel = sor.split(' ')
        self._kerület = int(kerület)
        self._szavazatok = int(szavazatok)
        self._vnév = vnév
        self._knév = knév
        self._párt_jel = párt_jel
