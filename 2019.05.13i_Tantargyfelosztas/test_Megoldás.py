import filecmp
from unittest import TestCase
from Megoldás import Megoldás


class TestMegoldás(TestCase):
    @classmethod
    def setUpClass(cls):
        cls.megoldás1: Megoldás = Megoldás('beosztas.txt')

    def test_bejegyzések_száma(self):
        self.assertEqual(self.megoldás1.bejegyzések_száma, 329)

    def test_heti_összóraszám(self):
        self.assertEqual(self.megoldás1.összóraszám, 1016)

    def test_tanári_óraszám(self):
        self.assertEqual(self.megoldás1.tanári_óraszám('Albatrosz Aladin'), 24)

    def test_ofőket_ír(self):
        self.megoldás1.ofőket_ír('of.txt')
        self.assertTrue(filecmp.cmp('of.txt', 'of_OH.txt', shallow=False))

    def test_tanári_csoportbontás_van(self):
        self.assertEqual(
            self.megoldás1.csoportbontás_van('10.b', 'kemia'), True)

    def test_tanárok_száma(self):
        self.assertEqual(self.megoldás1.tanárok_száma, 49)
