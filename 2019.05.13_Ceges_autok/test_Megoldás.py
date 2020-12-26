from unittest import TestCase
from Megoldás import Megoldás


class TestMegoldás(TestCase):
    @classmethod
    def setUpClass(cls):
        cls.megoldás1: Megoldás = Megoldás('autok.txt')

    def test_utolsó_kivitel_nap(self):
        self.assertEqual(self.megoldás1.utolsó_kivitel.nap, '30')

    def test_utolsó_kivitel_rendszám(self):
        self.assertEqual(self.megoldás1.utolsó_kivitel.rendszám, 'CEG300')
