from unittest import TestCase
from Megoldás import Megoldás
import filecmp


class TestMegoldás(TestCase):
    @classmethod
    def setUpClass(cls):
        cls.megoldás1: Megoldás = Megoldás('autok.txt')

    def test_utolsó_kivitel_nap(self):
        self.assertEqual(self.megoldás1.utolsó_kivitel.nap, '30')

    def test_utolsó_kivitel_rendszám(self):
        self.assertEqual(self.megoldás1.utolsó_kivitel.rendszám, 'CEG300')

    def test_forgalom(self):
        self.assertEqual(self.megoldás1.forgalom('4'), '12:50 CEG303 561 ki\n19:17 CEG308 552 be')

    def test_kintlévő_autók_száma(self):
        self.assertEqual(self.megoldás1.kintlévő_autók_száma, 4)

    def test_statisztika(self):
        self.assertEqual(self.megoldás1.statisztika, 'CEG300 6751 km\nCEG301 5441 km\nCEG302 5101 km\nCEG303 7465 km\nCEG304 6564 km\nCEG305 5232 km\nCEG306 7165 km\nCEG307 6489 km\nCEG308 6745 km\nCEG309 1252 km')

    def test_max_áthajtás(self):
        self.assertEqual(self.megoldás1.max_áthajtás.megtett_km, 1551)
        self.assertEqual(self.megoldás1.max_áthajtás.szem_azon, '506')

    def test_menetlevelek(self):
        for jegy in range(10):
            self.megoldás1.menetlevelet_ír(f'CEG30{jegy}')
            self.assertTrue(filecmp.cmp(f'menetlevelek/CEG30{jegy}_menetlevel.txt', f'menetlevelek_OH/CEG30{jegy}_menetlevel.txt', shallow=False))
