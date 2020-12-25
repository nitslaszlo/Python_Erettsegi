from unittest import TestCase
from Epizód import Epizód


class TestEpizód(TestCase):
    def setUp(self):
        self.epizód1: Epizód = Epizód(['2017.07.16', 'Games', '7x01', '60', '1'])
        self.epizód2: Epizód = Epizód(['NI', 'The Fable', '7x12', '42', '0'])

    async def test_mezők(self):
        self.assertEqual(self.epizód1.vetítés, '2017.07.16')
        self.assertEqual(self.epizód1.cím, 'Games')
        self.assertEqual(self.epizód1.évad_epizód, '7x01')
        self.assertEqual(self.epizód1.hossz, 60)
        self.assertEqual(self.epizód1.megnézte, True)
        self.assertEqual(self.epizód2.vetítés, 'NI')
        self.assertEqual(self.epizód2.cím, 'The Fable')
        self.assertEqual(self.epizód2.évad_epizód, '7x12')
        self.assertEqual(self.epizód2.hossz, 42)
        self.assertEqual(self.epizód2.megnézte, False)

    async def test_ismert_a_vetítés_dátuma(self):
        self.assertEqual(self.epizód1.ismert_a_vetítés_dátuma, True)
        self.assertEqual(self.epizód2.ismert_a_vetítés_dátuma, False)

    async def test_dátum_mezők(self):
        self.assertEqual(self.epizód1.vetítés_év, 2017)
        self.assertEqual(self.epizód1.vetítés_hó, 7)
        self.assertEqual(self.epizód1.vetítés_nap, 16)
        self.assertEqual(self.epizód2.vetítés_év, -1)
        self.assertEqual(self.epizód2.vetítés_hó, -1)
        self.assertEqual(self.epizód2.vetítés_nap, -1)
