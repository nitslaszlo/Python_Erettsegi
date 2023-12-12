from unittest import TestCase
from Jatekos import Jatekos


class TestJátékos(TestCase):
    @classmethod
    def setUpClass(cls):
        cls.jatekos1: Jatekos = Jatekos('Marci 3 12 1 8 5 8 1 2 1 4')
        cls.jatekos2: Jatekos = Jatekos('Gabi 4 7 5 6 13 9 5 4 1')

    def test_név(self):
        self.assertEqual(self.jatekos1.nev, 'Marci')
        self.assertEqual(self.jatekos2.nev, 'Gabi')

    def test_tippek_száma(self):
        self.assertEqual(self.jatekos1.tippek_szama, 10)
        self.assertEqual(self.jatekos2.tippek_szama, 9)

    def test_legnagyobb_tipp(self):
        self.assertEqual(self.jatekos1.legnagyobb_tipp, 12)
        self.assertEqual(self.jatekos2.legnagyobb_tipp, 13)

    def test_forduló_tippje(self):
        tippek_játékos1: list[int] = [3, 12, 1, 8, 5, 8, 1, 2, 1, 4]
        for forduló in range(1, self.jatekos1.tippek_szama + 1):
            self.assertEqual(self.jatekos1.fordulo_tippje(forduló), tippek_játékos1[forduló - 1])
        tippek_játékos2: list[int] = [4, 7, 5, 6, 13, 9, 5, 4, 1]
        for forduló in range(1, self.jatekos2.tippek_szama + 1):
            self.assertEqual(self.jatekos2.fordulo_tippje(forduló), tippek_játékos2[forduló - 1])

    def test_forduló_név_tip(self):
        tippek_játékos1: list[int] = [3, 12, 1, 8, 5, 8, 1, 2, 1, 4]
        for forduló in range(1, self.jatekos1.tippek_szama + 1):
            self.assertEqual(self.jatekos1.fordulo_nev_tip(forduló), f'Marci {tippek_játékos1[forduló - 1]}')
        tippek_játékos2: list[int] = [4, 7, 5, 6, 13, 9, 5, 4, 1]
        for forduló in range(1, self.jatekos2.tippek_szama + 1):
            self.assertEqual(self.jatekos2.fordulo_nev_tip(forduló), f'Gabi {tippek_játékos2[forduló - 1]}')
