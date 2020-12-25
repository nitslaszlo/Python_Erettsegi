from unittest import TestCase
from FelszállásJegy import FelszállásJegy


class TestFelszállásJegy(TestCase):
    @classmethod
    def setUpClass(cls):
        cls.felszállás1: FelszállásJegy = FelszállásJegy('22 20190326-0728 9084477 JGY 8')
        cls.felszállás2: FelszállásJegy = FelszállásJegy('26 20190326-0732 8885564 JGY 0')

    def test_megálló_sorszáma(self):
        self.assertEqual(self.felszállás1.megálló_sorszáma, 22)
        self.assertEqual(self.felszállás2.megálló_sorszáma, 26)

    def test_kártya_azon(self):
        self.assertEqual(self.felszállás1.kártya_azon, '9084477')
        self.assertEqual(self.felszállás2.kártya_azon, '8885564')

    def test_érvényes_felszállás(self):
        self.assertEqual(self.felszállás1.érvényes_felszállás, True)
        self.assertEqual(self.felszállás2.érvényes_felszállás, False)

    def test_kedvezményes_utazás(self):
        self.assertEqual(self.felszállás1.kedvezményes_utazás, False)
        self.assertEqual(self.felszállás2.kedvezményes_utazás, False)

    def test_ingyenes_utazás(self):
        self.assertEqual(self.felszállás1.ingyenes_utazás, False)
        self.assertEqual(self.felszállás2.ingyenes_utazás, False)

    def test_lejár_három_nap(self):
        self.assertEqual(self.felszállás1.lejár_három_nap, False)
        self.assertEqual(self.felszállás2.lejár_három_nap, False)
