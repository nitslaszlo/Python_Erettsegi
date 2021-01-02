from unittest import TestCase
from Telek import Telek


class TestFelszállásJegy(TestCase):
    @classmethod
    def setUpClass(cls):
        cls.telek1: Telek = Telek('0 10 P', 2)

    def test_ez_páros_telek(self):
        self.assertEqual(self.telek1.ez_páros_telek, True)

    def test_ez_páratlan_telek(self):
        self.assertEqual(self.telek1.ez_páratlan_telek, False)

    def test_oldal(self):
        self.assertEqual(self.telek1.oldal, 'páros')

    def test_házszám(self):
        self.assertEqual(self.telek1.házszám, 2)

    def test_szín(self):
        self.assertEqual(self.telek1.szín, 'P')

    def test_szélesség(self):
        self.assertEqual(self.telek1.szélesség, 10)
