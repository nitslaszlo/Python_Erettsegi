from unittest import TestCase
from Megoldás import Megoldás
import filecmp


class TestMegoldás(TestCase):
    @classmethod
    def setUpClass(cls):
        cls.megoldás1: Megoldás = Megoldás('utasadat.txt')

    def test_felszállók_száma(self):
        self.assertEqual(self.megoldás1.felszállók_száma, 699)

    def test_érvénytelen_felszállás(self):
        self.assertEqual(self.megoldás1.érvénytelen_felszállás, 21)

    def test_legtöbb_felszálló_fő(self):
        self.assertEqual(self.megoldás1.legtöbb_felszálló.felszálló_fő, 39)

    def test_legtöbb_felszálló_megálló(self):
        self.assertEqual(self.megoldás1.legtöbb_felszálló.megálló, 8)

    def test_ingyenes_utazás(self):
        self.assertEqual(self.megoldás1.ingyenes_utazás, 133)

    def test_kedvezményes_utazás(self):
        self.assertEqual(self.megoldás1.kedvezményes_utazás, 200)

    def test_figyelmeztetest_ír(self):
        self.megoldás1.figyelmeztetést_ír('figyelmeztetes.txt')
        self.assertTrue(filecmp.cmp('figyelmeztetes.txt', 'figyelmeztetesOH.txt', shallow=False))
