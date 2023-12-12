import datetime
from train import Train


class Solution:
    _trains_data: list[Train] = []
    _trains: set[int] = set()
    _stations: set[int] = set()
    _RUNNING_TIME: int = 2 * 60 + 22

    @property
    def num_of_trains(self) -> int:
        return len(self._trains)

    @property
    def num_of_stations(self) -> int:
        return len(self._stations)

    @property
    def max_downtime_data(self) -> Train:
        return max(self._trains_data, key=lambda x: x.downtime)

    def __init__(self, source_file: str) -> None:
        with open(source_file, 'r', encoding='UTF8') as sr:
            for line in sr.read().splitlines():
                current_train = Train(line)
                if current_train.time_is_depart and not current_train.is_first_station:
                    previous_data: list[Train] = list(filter(lambda x: x.id == current_train.id, self._trains_data))
                    current_train.calculate_downtime(previous_data[-1].time)
                self._trains_data.append(current_train)
        for e in self._trains_data:
            self._trains.add(e.id)
            self._stations.add(e.station)

    def train_running_time_check(self, train_id: int) -> str:
        train_data: list[Train] = list(filter(lambda x: x.id == train_id, self._trains_data))
        running_time = Train.calculate_running_time(train_data[0].time, train_data[-1].time)
        if running_time == self._RUNNING_TIME:
            return f'A(z) {train_id}. vonat útja pontosan az előírt ideig tartott'
        elif running_time > self._RUNNING_TIME:
            return f'A(z) {train_id}. vonat útja {running_time - self._RUNNING_TIME} perccel hosszabb volt az előírtnál'
        else:
            return f'A(z) {train_id}. vonat útja {self._RUNNING_TIME - running_time} perccel rövidebb volt az előírtnál'

    def write_data(self, train_id: int) -> None:
        train_data: list[Train] = list(filter(lambda x: x.id == train_id, self._trains_data))
        with open(f'halad{train_id}.txt', 'w', encoding='utf-8') as sw:
            for e in train_data:
                if not e.time_is_depart:
                    sw.write(f'{e.station}. állomás: {e.time.hour}:{e.time.minute}\n')

    def where_are_the_trains(self, time_string: str) -> str:
        output: str = ''
        input_time = datetime.datetime(2020, 1, 1, int(time_string.split(' ')[0]), int(time_string.split(' ')[1]))
        for e in self._trains:
            t: list[Train] = list(filter(lambda x: x.id == e, self._trains_data))
            for i in range(1, len(t)):
                p = i - 1  # index of previous event
                if t[p].time_is_depart:
                    if t[p].time <= input_time < t[i].time:
                        output += \
                            f'A(z) {t[i].id}. vonat a {t[p].station}. és a {t[i].station}. állomás között járt.\n'
                else:  # is_arrival
                    if t[p].time <= input_time < t[i].time:
                        output += f'A(z) {t[i].id}. vonat a {t[i].station}. állomáson állt.\n'
        return output
