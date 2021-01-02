from unittest import TestCase
from Megoldás import Megoldás
import filecmp


class TestMegoldás(TestCase):
    @classmethod
    def setUpClass(cls):
        cls.megoldás1: Megoldás = Megoldás('ajto.txt')

    def test_első_belépő(self):
        self.assertEqual(self.megoldás1.első_belépő, '2')

    def test_statisztikát_ír(self):
        self.megoldás1.statisztikát_ír('athaladas.txt')
        self.assertTrue(filecmp.cmp('athaladas.txt', 'athaladas_OH.txt', shallow=False))

    def test_utolsó_kilépő(self):
        self.assertEqual(self.megoldás1.utolsó_kilépő, '6')

    def test_társalgóban_maradtak(self):
        self.assertEqual(self.megoldás1.társalgóban_maradtak, '1 11 22 24 29 30 35 37')

    def test_legtöbben_a_társalgóban(self):
        self.assertEqual(self.megoldás1.legtöbben_a_társalgóban.strftime("%H:%M"), '10:44')

    def test_mettől_meddig(self):
        self.assertEqual(self.megoldás1.mettől_meddig('22'), '11:22-11:27\n13:45-13:47\n13:53-13:58\n14:17-14:20\n14:57-')

    def test_eltöltött_idő_perc(self):
        self.assertEqual(self.megoldás1.eltöltött_idő_perc('22'), 18)
        self.assertEqual(self.megoldás1.eltöltött_idő_perc('39'), 39)

    def test_társalgóban_maradt(self):
        self.assertEqual(self.megoldás1.társalgóban_maradt('22'), True)
        self.assertEqual(self.megoldás1.társalgóban_maradt('39'), False)
