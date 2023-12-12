import filecmp
from unittest import TestCase
from Megoldas import Megoldas


class TestMegoldás(TestCase):
    @classmethod
    def setUpClass(cls):
        cls.megoldás1: Megoldas = Megoldas('szavazatok.txt')

    def test_jelöltek_száma(self):
        self.assertEqual(self.megoldás1.jelöltek_száma, 40)

    def test_képviselő_keresése(self):
        self.assertEqual(self.megoldás1.képviselő_keresése('Fasirt Ferenc'), 'Fasirt Ferenc 143 szavazatot kapott.')
        self.assertEqual(self.megoldás1.képviselő_keresése('Kenyér Kálmán'), 'Ilyen nevű képviselőjelölt nem szerepel a nyilvántartásban!')

    def test_szavazatok_száma(self):
        self.assertEqual(self.megoldás1.szavazatok_száma, 4713)

    def test_szavazott_százalék(self):
        self.assertEqual(self.megoldás1.szavazott_százalék, '38.18%')

    def test_szavazat_stat(self):
        self.assertGreater(self.megoldás1.szavazat_stat.find('Független jelöltek 17.53 %'), -1)
        self.assertGreater(self.megoldás1.szavazat_stat.find('Gyümölcsevők pártja 16.36 %'), -1)
        self.assertGreater(self.megoldás1.szavazat_stat.find('Zöldségevők pártja 20.03 %'), -1)
        self.assertGreater(self.megoldás1.szavazat_stat.find('Húsevők pártja 24.59 %'), -1)
        self.assertGreater(self.megoldás1.szavazat_stat.find('Tejívók szövetsége 21.49 %'), -1)

    def test_győztes_képviselők(self):
        self.assertGreater(self.megoldás1.győztes_képviselők.find('Joghurt Jakab TISZ'), -1)
        self.assertGreater(self.megoldás1.győztes_képviselők.find('Narancs Edmond GYEP'), -1)
        self.assertGreater(self.megoldás1.győztes_képviselők.find('Vadas Marcell HEP'), -1)

    def test_allományt_ír(self):
        self.megoldás1.állományt_ír('kepviselok.txt')
        self.assertTrue(filecmp.cmp('kepviselok.txt', 'kepviselok_OH.txt', shallow=False))
