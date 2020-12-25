from unittest import TestCase
from Jelentés import Jelentés


class TestJelentes(TestCase):
    def setUp(self):
        self.jel1: Jelentés = Jelentés('BP 0000 VRB02 23')
        self.jel2: Jelentés = Jelentés('BP 0100 00000 22')

    def test_atlaghoz(self):
        self.assertEqual(self.jel1.átlaghoz, False)
        self.assertEqual(self.jel2.átlaghoz, True)

    def test_ora(self):
        self.assertEqual(self.jel1.óra, 0)
        self.assertEqual(self.jel2.óra, 1)

    def test_szelcsend(self):
        self.assertEqual(self.jel1.szélcsend, False)
        self.assertEqual(self.jel2.szélcsend, True)
