from __future__ import annotations


class Jelentes(object):
    def __init__(self, sor: str) -> None:
        telepuleskod, idopont, szelirany_erosseg, homerseklet = sor.strip().split(' ')
        self.telepuleskod = str(telepuleskod)
        self.idopont = f'{idopont[:2]}:{idopont[2:]}'
        self.szelirany = str(szelirany_erosseg[:3])
        self.erosseg = int(szelirany_erosseg[3:5])
        self.homerseklet = int(homerseklet)

    def __str__(self) -> str:
        return f'{self.telepuleskod} {self.idopont} {self.homerseklet}'

    # Unit teszthez kell, nem a megoldás része:
    def __eq__(self, other: Jelentes) -> bool:
        return self.telepuleskod == other.telepuleskod and \
               self.idopont == other.idopont and \
               self.szelirany == other.szelirany and \
               self.erosseg == other.erosseg and \
               self.homerseklet == other.homerseklet

    @property
    def atlaghoz(self) -> bool:
        return self.ora in (1, 7, 13, 19)

    @property
    def ora(self) -> int:
        return int(self.idopont[:2])

    @property
    def szelcsend(self) -> bool:
        # return self.szelirany == '000' and self.erosseg == 0
        return self.erosseg == 0
