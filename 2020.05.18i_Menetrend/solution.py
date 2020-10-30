import datetime
from typing import List
from typing import Set
from train import Train


class Solution(object):
    _trains_data: List[Train] = list()
    _trains: Set[int] = set()
    _stations: Set[int] = set()
    _RUNNING_TIME: int = 2 * 60 + 22

    def __init__(self, source_file: str) -> None:
        with open(source_file, 'r', encoding='UTF8') as sr:
            for i in sr.read().splitlines():
                current_train = Train(i)
                if current_train.is_depart and not current_train.is_first_station:
                    previous_data: List[Train] = list(filter(lambda x: x.id == current_train.id, self._trains_data))
                    current_train.calculate_downtime(previous_data[-1].arrival_time)
                self._trains_data.append(current_train)
        for i in self._trains_data:
            self._trains.add(i.id)
            self._stations.add(i.station)

    def train_running_time_check(self, train_id: int) -> str:
        train_data: List[Train] = list(filter(lambda x: x.id == train_id, self._trains_data))
        running_time = Train.calculate_running_time(train_data[0].depart_time, train_data[-1].arrival_time)
        if running_time == self._RUNNING_TIME:
            return f'A(z) {train_id}. vonat útja pontosan az előírt ideig tartott'
        elif running_time > self._RUNNING_TIME:
            return f'A(z) {train_id}. vonat útja {running_time - self._RUNNING_TIME} perccel hosszabb volt az előírtnál'
        else:
            return f'A(z) {train_id}. vonat útja {self._RUNNING_TIME - running_time} perccel rövidebb volt az előírtnál'

    def write_data(self, train_id: int) -> None:
        train_data: List[Train] = list(filter(lambda x: x.id == train_id, self._trains_data))
        with open(f'halad{train_id}.txt', 'w', encoding='UTF8') as sw:
            for i in train_data:
                if i.is_arrival:
                    sw.write(f'{i.station}. állomás: {i.arrival_time.hour}:{i.arrival_time.minute}\n')

    def where_are_the_trains(self, time_string: str) -> str:
        output: str = ''
        input_time = datetime.datetime(2020, 1, 1, int(time_string.split(' ')[0]), int(time_string.split(' ')[1]))
        for i in self._trains:
            t: List[Train] = list(filter(lambda x: x.id == i, self._trains_data))
            for c in range(1, len(t)):
                p = c - 1  # index of previous event
                if t[p].is_depart:
                    if t[p].depart_time <= input_time < t[c].arrival_time:
                        output += \
                            f'A(z) {t[c].id}. vonat a {t[p].station}. és a {t[c].station}. állomás között járt.\n'
                else:  # is_arrival
                    if t[p].arrival_time <= input_time < t[c].depart_time:
                        output += f'A(z) {t[c].id}. vonat a {t[c].station}. állomáson állt.\n'
        return output

    @property
    def num_of_trains(self) -> int:
        return len(self._trains)

    @property
    def num_of_stations(self) -> int:
        return len(self._stations)

    @property
    def max_downtime_data(self) -> Train:
        return max(self._trains_data, key=lambda x: x.downtime)
