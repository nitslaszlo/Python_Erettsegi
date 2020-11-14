from unittest import TestCase
from epizod import Epizod


class TestEpisode(TestCase):
    def setUp(self):
        self.epizod1: Epizod = Epizod(['2017.07.16', 'Games', '7x01', '60', '1'])
        self.epizod2: Epizod = Epizod(['NI', 'The Fable', '7x12', '42', '0'])

    def test_mezok(self):
        self.assertEqual(self.epizod1.vetites, '2017.07.16')
        self.assertEqual(self.epizod1.cim, 'Games')
        self.assertEqual(self.epizod1.evad_epizod, '7x01')
        self.assertEqual(self.epizod1.hossz, 60)
        self.assertEqual(self.epizod1.megnezte, True)
        self.assertEqual(self.epizod2.vetites, 'NI')
        self.assertEqual(self.epizod2.cim, 'The Fable')
        self.assertEqual(self.epizod2.evad_epizod, '7x12')
        self.assertEqual(self.epizod2.hossz, 42)
        self.assertEqual(self.epizod2.megnezte, False)

    def test_ismert_a_vetites_datuma(self):
        self.assertEqual(self.epizod1.ismert_a_vetites_datuma, True)
        self.assertEqual(self.epizod2.ismert_a_vetites_datuma, False)

    def test_datum_mezok(self):
        self.assertEqual(self.epizod1.vetites_ev, 2017)
        self.assertEqual(self.epizod1.vetites_ho, 7)
        self.assertEqual(self.epizod1.vetites_nap, 16)
        self.assertEqual(self.epizod2.vetites_ev, -1)
        self.assertEqual(self.epizod2.vetites_ho, -1)
        self.assertEqual(self.epizod2.vetites_nap, -1)
