import datetime
from unittest import TestCase
from train import Train
from solution import Solution


class TestTrain(TestCase):
    def setUp(self):
        self.train1: Train = Train('1	0	5	45	I')
        self.train2: Train = Train('1	1	6	0	E')

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


class TestSolution(TestCase):
    def setUp(self):
        self.solution: Solution = Solution('vonat.txt')

    def test_num_of_trains(self):
        self.assertEqual(self.solution.num_of_trains, 12)

    def test_num_of_stations(self):
        self.assertEqual(self.solution.num_of_stations, 11)

    def test_max_downtime_data(self):
        self.assertEqual(self.solution.max_downtime_data.id, 5)
        self.assertEqual(self.solution.max_downtime_data.station, 6)
        self.assertEqual(self.solution.max_downtime_data.downtime, 10)

    def test_train_running_time_check(self):
        self.assertEqual(self.solution.train_running_time_check(1),
                         'A(z) 1. vonat útja 5 perccel hosszabb volt az előírtnál')
        self.assertEqual(self.solution.train_running_time_check(2),
                         'A(z) 2. vonat útja 2 perccel hosszabb volt az előírtnál')
