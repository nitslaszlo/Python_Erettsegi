from __future__ import annotations  # Az __eq__() metódus Jelentés típusú other paraméteréhez kell


class Jelentés(object):
    def __init__(self, sor: str) -> None:
        településkód, időpont, szélirány_erősség, hőmérséklet = sor.strip().split(' ')
        self.településkód = str(településkód)
        self.időpont = f'{időpont[:2]}:{időpont[2:]}'
        self.szélirány = str(szélirány_erősség[:3])
        self.erősség = int(szélirány_erősség[3:5])
        self.hőmérséklet = int(hőmérséklet)

    def __str__(self) -> str:
        return f'{self.településkód} {self.időpont} {self.hőmérséklet}'

    # Unit teszthez kell, nem a megoldás része:
    def __eq__(self, other: Jelentés) -> bool:
        return self.településkód == other.településkód and \
            self.időpont == other.időpont and \
            self.szélirány == other.szélirány and \
            self.erősség == other.erősség and \
            self.hőmérséklet == other.hőmérséklet

    @property
    def átlaghoz(self) -> bool:
        return self.óra in (1, 7, 13, 19)

    @property
    def óra(self) -> int:
        return int(self.időpont[:2])

    @property
    def szélcsend(self) -> bool:
        # return self.szélirány == '000' and self.erősség == 0
        return self.erősség == 0
