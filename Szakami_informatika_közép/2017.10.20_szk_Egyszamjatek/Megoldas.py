import os
from Jatekos import Jatekos


class Megoldas:
    _jatekosok: list[Jatekos]

    @property
    def jatekosok_szama(self) -> int:
        return len(self._jatekosok)

    @property
    def fordulok_szama(self) -> int:
        return self._jatekosok[0].tippek_szama

    @property
    def jatek_legnagyobb_tipp(self) -> int:
        # Megoldás max() függvénnyel:
        # return max(jatekos.legnagyobb_tipp for jatekos in self._jatekosok)
        max_tipp: int = self._jatekosok[0].legnagyobb_tipp
        for jatekos in self._jatekosok[1:]:
            if jatekos.legnagyobb_tipp > max_tipp:
                max_tipp = jatekos.legnagyobb_tipp
        return max_tipp

    @property
    def volt_egyes_tipp(self) -> bool:
        volt_egyes: bool = False
        for jatekos in self._jatekosok:
            if jatekos.fordulo_tippje(1) == 1:
                volt_egyes = True
                break
        return volt_egyes

    def __init__(self, forras: str):
        self._jatekosok = []
        with open(forras, 'r', encoding='utf-8') as file:
            for sor in file.read().splitlines():
                self._jatekosok.append(Jatekos(sor))

    # segéd fg a 8. feladathoz
    def _fordulo_szotar(self, fordulo_sorszama: int) -> dict[int, int]:
        szotar: dict[int, int] = dict()
        for j in self._jatekosok:
            jatekos_tippje: int = j.fordulo_tippje(fordulo_sorszama)
            if jatekos_tippje in szotar:  # ha a kulcs megtalálható a szótárba
                szotar[jatekos_tippje] += 1
            else:
                szotar[jatekos_tippje] = 1  # új kulcs (key) létrehozása 1-es kezdőértékkel (value)
        return szotar

    # segéd fg a 8. feladathoz
    def _nyertes_tipp(self, fordulo_sorszama: int) -> int:
        # felad: megkeresni a legkisebb kulcsot, ahol a value 1-es értékű
        tipp: int = -1  # visszatérési érték, ha nincs egyedi tipp
        szotar: dict[int, int] = self._fordulo_szotar(fordulo_sorszama)
        for vizsgalt_tipp in range(1, 100):
            if vizsgalt_tipp in szotar and szotar[vizsgalt_tipp] == 1:
                tipp = vizsgalt_tipp
                break  # az első legkisebb egyedi tippet keressük, ezért a keresést be kell fejezni
        return tipp

    def nyertes_tipp_szoveg(self, fordulo_sorszama: int) -> str:
        nyertes_tipp: int = self._nyertes_tipp(fordulo_sorszama)
        if nyertes_tipp == -1:
            return 'Nem volt egyedi tipp a megadott fordulóban!'
        else:
            return f'A nyertes tipp a megadott fordulóban: {nyertes_tipp}'

    def _nyertes_jatekos(self, fordulo_sorszama: int, nyertes_tipp: int) -> str:
        for j in self._jatekosok:
            if j.fordulo_tippje(fordulo_sorszama) == nyertes_tipp:
                return j.nev
        return "Hiba!"  # Technikai return, elvileg nem kerülhet erre a vezérlés

    def nyertes_jatekos_szoveg(self, fordulo_sorszama: int) -> str:
        nyertes_tipp: int = self._nyertes_tipp(fordulo_sorszama)
        if nyertes_tipp == -1:
            return 'Nem volt nyertes a megadott fordulóban!'
        else:
            return f'A megadott forduló nyertese: {self._nyertes_jatekos(fordulo_sorszama, nyertes_tipp)}'

    def _allomany_torlese(self, file_neve: str) -> None:
        if os.path.exists(file_neve):
            os.remove(file_neve)  # illene try-except blokk

    def _allomany_irasa(self, file_neve: str, fordulo_sorszama: int, nyertes_tipp: int) -> None:
        with open(file_neve, 'w', encoding='UTF8') as sw:
            sw.write(f'Forduló sorszáma: {fordulo_sorszama}.\n')
            sw.write(f'Nyertes tipp: {nyertes_tipp}\n')
            sw.write(f'Nyertes játékos: {self._nyertes_jatekos(fordulo_sorszama, nyertes_tipp)}\n')

    def allomany_kezelese(self, file_neve: str, fordulo_sorszama: int) -> None:
        nyertes_tipp: int = self._nyertes_tipp(fordulo_sorszama)
        try:
            if nyertes_tipp == -1:
                self._allomany_torlese(file_neve)
            else:
                self._allomany_irasa(file_neve, fordulo_sorszama, nyertes_tipp)
        except FileNotFoundError as ex:
            print(ex)
