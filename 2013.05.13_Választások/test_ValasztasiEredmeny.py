from ValasztasiEredmeny import ValasztasiEredmeny
from unittest import TestCase


class TestÁthajtás(TestCase):
    @classmethod
    def setUpClass(cls):
        cls.eredmény1: ValasztasiEredmeny = ValasztasiEredmeny('5 19 Ablak Antal -')
        cls.eredmény2: ValasztasiEredmeny = ValasztasiEredmeny('1 120 Alma Dalma GYEP')
        cls.eredmény3: ValasztasiEredmeny = ValasztasiEredmeny('7 162 Bab Zsuzsanna ZEP')
        cls.eredmény4: ValasztasiEredmeny = ValasztasiEredmeny('1 154 Bors Botond HEP')
        cls.eredmény5: ValasztasiEredmeny = ValasztasiEredmeny('5 288 Joghurt Jakab TISZ')

    def test_név(self):
        self.assertEqual(self.eredmény1.név, 'Ablak Antal')
        self.assertEqual(self.eredmény2.név, 'Alma Dalma')
        self.assertEqual(self.eredmény3.név, 'Bab Zsuzsanna')
        self.assertEqual(self.eredmény4.név, 'Bors Botond')
        self.assertEqual(self.eredmény5.név, 'Joghurt Jakab')

    def test_szavazatok(self):
        self.assertEqual(self.eredmény1.szavazatok, 19)
        self.assertEqual(self.eredmény2.szavazatok, 120)
        self.assertEqual(self.eredmény3.szavazatok, 162)
        self.assertEqual(self.eredmény4.szavazatok, 154)
        self.assertEqual(self.eredmény5.szavazatok, 288)

    def test_kerület(self):
        self.assertEqual(self.eredmény1.kerület, 5)
        self.assertEqual(self.eredmény2.kerület, 1)
        self.assertEqual(self.eredmény3.kerület, 7)
        self.assertEqual(self.eredmény4.kerület, 1)
        self.assertEqual(self.eredmény5.kerület, 5)

    def test_párt_jel2(self):
        self.assertEqual(self.eredmény1.párt_jel2, 'Független')
        self.assertEqual(self.eredmény2.párt_jel2, 'GYEP')
        self.assertEqual(self.eredmény3.párt_jel2, 'ZEP')
        self.assertEqual(self.eredmény4.párt_jel2, 'HEP')
        self.assertEqual(self.eredmény5.párt_jel2, 'TISZ')

    def test_párt(self):
        self.assertEqual(self.eredmény1.párt, 'Független jelöltek')
        self.assertEqual(self.eredmény2.párt, 'Gyümölcsevők pártja')
        self.assertEqual(self.eredmény3.párt, 'Zöldségevők pártja')
        self.assertEqual(self.eredmény4.párt, 'Húsevők pártja')
        self.assertEqual(self.eredmény5.párt, 'Tejívók szövetsége')
