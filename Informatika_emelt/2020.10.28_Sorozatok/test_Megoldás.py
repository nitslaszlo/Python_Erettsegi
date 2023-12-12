from unittest import TestCase
from Megoldás import Megoldás
import filecmp


class TestMegoldás(TestCase):
    def setUp(self):
        self.m: Megoldás = Megoldás('lista.txt')

    async def test_ismert_a_vetítés_dátuma_db(self):
        self.assertEqual(self.m.ismert_a_vetítés_dátuma_darab, 202)

    async def test_megnézve_arányszám(self):
        self.assertEqual(f'{self.m.megnézve_arány:.2%}', '45.66%')

    async def test_eltöltött_idő(self):
        self.assertEqual(self.m.idő_nap, 2)
        self.assertEqual(self.m.idő_óra, 15)
        self.assertEqual(self.m.idő_perc, 32)

    async def test_nem_látta_még(self):
        self.assertListEqual(self.m.nem_látta_még('2017.10.18'),
                             ['7x01\tThe Fable',
                              '7x02\tThe Fable',
                              '15x04\tMilitary Police',
                              '5x03\tSpy School',
                              '5x04\tSpy School',
                              '4x04\tThe Elite Minds'])

    async def test_adott_napon_vetített(self):
        self.assertListEqual(self.m.adott_napon_vetített('cs'),
                             ['The Hospital',
                              'Spectacular Power',
                              'Upper Story',
                              'Chicago Flame',
                              'Shrinktime'])

    async def test_summa_txt(self):
        self.m.stat_ír('summa.txt')
        self.assertTrue(filecmp.cmp('summa_OH.txt', 'summa.txt', shallow=False))
