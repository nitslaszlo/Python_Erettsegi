from unittest import TestCase
from Beosztás import Beosztás


class TestFelszállásJegy(TestCase):
    @classmethod
    def setUpClass(cls):
        cls.beosztás1: Beosztás = Beosztás(
            ['Albatrosz Aladin', 'biologia', '9.a', '2'])

    def test_név(self):
        self.assertEqual(self.beosztás1.név, 'Albatrosz Aladin')

    def test_órszám(self):
        self.assertEqual(self.beosztás1.óraszám, 2)

    def test_tantárgy(self):
        self.assertEqual(self.beosztás1.tantárgy, 'biologia')

    def test_osztály(self):
        self.assertEqual(self.beosztás1.osztály, '9.a')
