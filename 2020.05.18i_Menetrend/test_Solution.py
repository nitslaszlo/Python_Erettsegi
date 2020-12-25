from unittest import TestCase
from solution import Solution


class TestSolution(TestCase):
    @classmethod
    def setUpClass(cls):
        cls.solution: Solution = Solution('vonat.txt')

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
