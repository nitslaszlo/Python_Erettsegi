from unittest import TestCase
from megoldas import Megoldas
import filecmp


class TestMegoldas(TestCase):
    def setUp(self):
        self.m: Megoldas = Megoldas('lista.txt')

    async def test_ismert_a_vetítés_datuma_db(self):
        self.assertEqual(self.m.ismert_a_vetites_datuma_darab, 202)

    async def test_megnezve_aranyszam(self):
        self.assertEqual(f'{self.m.megnezve_arany:.2%}', '45.66%')

    async def test_eltoltott_ido(self):
        self.assertEqual(self.m.ido_nap, 2)
        self.assertEqual(self.m.ido_ora, 15)
        self.assertEqual(self.m.ido_perc, 32)

    async def test_nem_latta_meg(self):
        self.assertListEqual(self.m.nem_latta_meg('2017.10.18'),
                             ['7x01\tThe Fable',
                              '7x02\tThe Fable',
                              '15x04\tMilitary Police',
                              '5x03\tSpy School',
                              '5x04\tSpy School',
                              '4x04\tThe Elite Minds'])

    async def test_adott_napon_vetitett(self):
        self.assertListEqual(self.m.adott_napon_vetitett('cs'),
                             ['The Hospital',
                              'Spectacular Power',
                              'Upper Story',
                              'Chicago Flame',
                              'Shrinktime'])

    async def test_summa_txt(self):
        self.m.write_stat('summa.txt')
        self.assertTrue(filecmp.cmp('summa_OH.txt', 'summa.txt', shallow=False))
