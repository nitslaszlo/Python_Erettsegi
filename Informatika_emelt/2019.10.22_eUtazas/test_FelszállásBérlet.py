from unittest import TestCase
from FelszállásBérlet import FelszállásBérlet


class TestFelszállásBérlet(TestCase):
    @classmethod
    def setUpClass(cls):
        cls.felszállás1: FelszállásBérlet = FelszállásBérlet('0 20190326-0700 4170861 NYB 20190404')
        cls.felszállás2: FelszállásBérlet = FelszállásBérlet('0 20190326-0700 2020534 TAB 20190328')
        cls.felszállás3: FelszállásBérlet = FelszállásBérlet('17 20190326-0722 2946924 FEB 20190325')
        cls.felszállás4: FelszállásBérlet = FelszállásBérlet('0 20190326-0700 4908462 NYP 20210101')

    def test_megálló_sorszáma(self):
        self.assertEqual(self.felszállás1.megálló_sorszáma, 0)
        self.assertEqual(self.felszállás2.megálló_sorszáma, 0)
        self.assertEqual(self.felszállás3.megálló_sorszáma, 17)
        self.assertEqual(self.felszállás4.megálló_sorszáma, 0)

    def test_kártya_azon(self):
        self.assertEqual(self.felszállás1.kártya_azon, '4170861')
        self.assertEqual(self.felszállás2.kártya_azon, '2020534')
        self.assertEqual(self.felszállás3.kártya_azon, '2946924')
        self.assertEqual(self.felszállás4.kártya_azon, '4908462')

    def test_érvényes_felszállás(self):
        self.assertEqual(self.felszállás1.érvényes_felszállás, True)
        self.assertEqual(self.felszállás2.érvényes_felszállás, True)
        self.assertEqual(self.felszállás3.érvényes_felszállás, False)
        self.assertEqual(self.felszállás4.érvényes_felszállás, True)

    def test_kedvezményes_utazás(self):
        self.assertEqual(self.felszállás1.kedvezményes_utazás, True)
        self.assertEqual(self.felszállás2.kedvezményes_utazás, True)
        self.assertEqual(self.felszállás3.kedvezményes_utazás, False)
        self.assertEqual(self.felszállás4.kedvezményes_utazás, False)

    def test_ingyenes_utazás(self):
        self.assertEqual(self.felszállás1.ingyenes_utazás, False)
        self.assertEqual(self.felszállás2.ingyenes_utazás, False)
        self.assertEqual(self.felszállás3.ingyenes_utazás, False)
        self.assertEqual(self.felszállás4.ingyenes_utazás, True)

    def test_lejár_három_nap(self):
        self.assertEqual(self.felszállás1.lejár_három_nap, False)
        self.assertEqual(self.felszállás2.lejár_három_nap, True)
        self.assertEqual(self.felszállás3.lejár_három_nap, False)
        self.assertEqual(self.felszállás4.lejár_három_nap, False)

    def test_lejárat(self):
        self.assertEqual(self.felszállás1.lejárat, '2019-04-04')
        self.assertEqual(self.felszállás2.lejárat, '2019-03-28')
        self.assertEqual(self.felszállás3.lejárat, '2019-03-25')
        self.assertEqual(self.felszállás4.lejárat, '2021-01-01')
