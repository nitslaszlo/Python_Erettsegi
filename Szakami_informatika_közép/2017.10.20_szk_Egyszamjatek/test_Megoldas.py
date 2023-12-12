import filecmp
import pathlib as pl
from unittest import TestCase
from Megoldas import Megoldas


class TestMegoldás(TestCase):
    @classmethod
    def setUpClass(cls):
        cls.megoldás1: Megoldas = Megoldas('egyszamjatek.txt')

    def test_játékosok_száma(self):
        self.assertEqual(self.megoldás1.jatekosok_szama, 9)

    def test_fordulók_száma(self):
        self.assertEqual(self.megoldás1.fordulok_szama, 10)

    def test_játék_legnagyobb_tipp(self):
        self.assertEqual(self.megoldás1.jatek_legnagyobb_tipp, 13)

    def test_volt_egyes_tipp(self):
        self.assertEqual(self.megoldás1.volt_egyes_tipp, True)

    def test_nyertes_tipp_szöveg(self):
        fordulok_nyertes_tippek: list[int] = [1, 3, 3, 1, 1, 8, 3, 1, 3]
        self.assertEqual(self.megoldás1.nyertes_tipp_szoveg(
            10), "Nem volt egyedi tipp a megadott fordulóban!")
        for forduló in range(1, self.megoldás1.fordulok_szama):
            self.assertEqual(self.megoldás1.nyertes_tipp_szoveg(
                forduló), f'A nyertes tipp a megadott fordulóban: {fordulok_nyertes_tippek[forduló - 1]}')

    def test_nyertes_játékos_szöveg(self):
        fordulok_nyertes_nevek: list[str] = [
            'Lili', 'Tibi', 'Andi', 'Bence', 'Mari', 'Marci', 'Andi', 'Andi', 'Lili']
        self.assertEqual(self.megoldás1.nyertes_jatekos_szoveg(
            10), "Nem volt nyertes a megadott fordulóban!")
        for forduló in range(1, self.megoldás1.fordulok_szama):
            self.assertEqual(self.megoldás1.nyertes_jatekos_szoveg(
                forduló), f'A megadott forduló nyertese: {fordulok_nyertes_nevek[forduló - 1]}')

    def test_állomány_kezelése(self):
        for forduló in range(1, self.megoldás1.fordulok_szama):
            self.megoldás1.allomany_kezelese('nyertes.txt', forduló)
            self.assertTrue(filecmp.cmp(
                'nyertes.txt', f'Nyertes_OH/nyertes_OH_{forduló}.txt', shallow=False))

        # törlés ellenőrzése:
        self.megoldás1.allomany_kezelese('nyertes.txt', 10)
        path = pl.Path("nyertes.txt")
        self.assertTrue(not path.is_file())
