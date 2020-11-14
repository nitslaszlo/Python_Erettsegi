from unittest import TestCase
from megoldas import Megoldas


class TestMegoldas(TestCase):
    def setUp(self):
        self.m: Megoldas = Megoldas('lista.txt')

    def test_ismert_a_vetítés_datuma_db(self):
        self.assertEqual(self.m.ismert_a_vetites_datuma_darab, 202)

    def test_megnezve_aranyszam(self):
        self.assertEqual(f'{self.m.megnezve_arany:.2%}', '45.66%')

    def test_eltoltott_ido(self):
        self.assertEqual(self.m.ido_nap, 2)
        self.assertEqual(self.m.ido_ora, 15)
        self.assertEqual(self.m.ido_perc, 32)
