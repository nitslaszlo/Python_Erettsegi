import datetime
from unittest import TestCase
from train import Train


class TestTrain(TestCase):
    @classmethod
    def setUpClass(cls):
        cls.train1: Train = Train('1	0	5	45	I')
        cls.train2: Train = Train('1	1	6	0	E')

    def test_id(self):
        self.assertEqual(self.train1.id, 1)
        self.assertEqual(self.train2.id, 1)

    def test_station(self):
        self.assertEqual(self.train1.station, 0)
        self.assertEqual(self.train2.station, 1)

    def test_time(self):
        self.assertEqual(self.train1.time, datetime.datetime(2020, 1, 1, 5, 45))
        self.assertEqual(self.train2.time, datetime.datetime(2020, 1, 1, 6, 0))

    def test_arrival_time(self):
        self.assertEqual(self.train1.time_is_depart, True)
        self.assertEqual(self.train2.time_is_depart, False)

    def test_is_first_station(self):
        self.assertEqual(self.train1.is_first_station, True)
        self.assertEqual(self.train2.is_first_station, False)
