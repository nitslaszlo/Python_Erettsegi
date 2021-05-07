from unittest import TestCase
from Megoldas import Megoldas
# import filecmp


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

    # def test_menetlevelek(self):
    #     for jegy in range(10):
    #         self.megoldás1.menetlevelet_ír(f'CEG30{jegy}')
    #         self.assertTrue(filecmp.cmp(f'menetlevelek/CEG30{jegy}_menetlevel.txt', f'menetlevelek_OH/CEG30{jegy}_menetlevel.txt', shallow=False))
