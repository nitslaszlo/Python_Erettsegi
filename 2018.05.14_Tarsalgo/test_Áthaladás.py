from unittest import TestCase
from Áthaladás import Áthaladás
from datetime import datetime


class TestFelszállásJegy(TestCase):
    @classmethod
    def setUpClass(cls):
        cls.áthaladás1: Áthaladás = Áthaladás('9 1 2 be')
        cls.áthaladás2: Áthaladás = Áthaladás('14 42 11 ki')

    def test_azon(self):
        self.assertEqual(self.áthaladás1.azon, '2')
        self.assertEqual(self.áthaladás2.azon, '11')

    def test_idő(self):
        self.assertEqual(self.áthaladás1.idő, datetime.strptime(f'9:1', '%H:%M'))
        self.assertEqual(self.áthaladás2.idő, datetime.strptime(f'14:42', '%H:%M'))

    def test_ez_kilépő(self):
        self.assertEqual(self.áthaladás1.ez_kilépő, False)
        self.assertEqual(self.áthaladás2.ez_kilépő, True)

    def test_ez_belépő(self):
        self.assertEqual(self.áthaladás1.ez_belépő, True)
        self.assertEqual(self.áthaladás2.ez_belépő, False)
