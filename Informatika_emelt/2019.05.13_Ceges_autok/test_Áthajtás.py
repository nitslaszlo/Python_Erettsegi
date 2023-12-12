from unittest import TestCase
from Áthajtás import Áthajtás


class TestÁthajtás(TestCase):
    @classmethod
    def setUpClass(cls):
        cls.áthajtás1: Áthajtás = Áthajtás('1 08:45 CEG306 501 23989 0')
        cls.áthajtás2: Áthajtás = Áthajtás('29 14:03 CEG306 541 31154 1')

    def test_nap(self):
        self.assertEqual(self.áthajtás1.nap, '1')
        self.assertEqual(self.áthajtás2.nap, '29')

    def test_idő(self):
        self.assertEqual(self.áthajtás1.idő, '08:45')
        self.assertEqual(self.áthajtás2.idő, '14:03')

    def test_rendszám(self):
        self.assertEqual(self.áthajtás1.rendszám, 'CEG306')
        self.assertEqual(self.áthajtás2.rendszám, 'CEG306')

    def test_szem_azon(self):
        self.assertEqual(self.áthajtás1.szem_azon, '501')
        self.assertEqual(self.áthajtás2.szem_azon, '541')

    def test_km_számláló(self):
        self.assertEqual(self.áthajtás1.km_számláló, 23989)
        self.assertEqual(self.áthajtás2.km_számláló, 31154)

    def test_kihajtás(self):
        self.assertEqual(self.áthajtás1.kihajtás, True)
        self.assertEqual(self.áthajtás2.kihajtás, False)

    def test_behajtás(self):
        self.assertEqual(self.áthajtás1.behajtás, False)
        self.assertEqual(self.áthajtás2.behajtás, True)
