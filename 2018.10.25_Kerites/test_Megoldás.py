from unittest import TestCase
from Megoldás import Megoldás
import filecmp


class TestMegoldás(TestCase):
    @classmethod
    def setUpClass(cls):
        cls.megoldás1: Megoldás = Megoldás('kerites.txt')

    def test_telkek_száma(self):
        self.assertEqual(self.megoldás1.telkek_száma, 98)

    def test_utolsó_eladott_telek_oldal(self):
        self.assertEqual(self.megoldás1.utolsó_eladott_telek.oldal, 'páros')

    def test_utolsó_eladott_telek_házszám(self):
        self.assertEqual(self.megoldás1.utolsó_eladott_telek.házszám, 78)

    def test_szomszédossal_azonos_szín(self):
        self.assertEqual(self.megoldás1.szomszédossal_azonos_szín, 73)

    def test_keresett_telek_szín(self):
        self.assertEqual(self.megoldás1.keresett_telek(83).szín, 'A')

    def test_lehetséges_szín(self):
        self.assertEqual(self.megoldás1.lehetséges_szín(83), 'D')

    def test_ofőket_ír(self):
        self.megoldás1.utcaképet_ír('utcakep.txt')
        self.assertTrue(filecmp.cmp('utcakep.txt', 'utcakep_OH.txt', shallow=False))
