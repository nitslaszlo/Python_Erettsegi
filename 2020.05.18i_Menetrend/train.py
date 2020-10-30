import datetime


class Train(object):
    @property
    def is_depart(self) -> bool:
        return self.depart_time != -1

    @property
    def is_arrival(self) -> bool:
        return self.arrival_time != -1

    @property
    def is_first_station(self) -> bool:
        return self.station == 0

    def __init__(self, line: str) -> None:
        tid, station, hour, minute, status = line.strip().split('\t')
        self.id = int(tid)
        self.station = int(station)
        self.depart_time = datetime.datetime(2020, 1, 1, int(hour), int(minute)) if status == 'I' else -1
        self.arrival_time = datetime.datetime(2020, 1, 1, int(hour), int(minute)) if status == 'E' else -1
        self.downtime = -1

    def calculate_downtime(self, arrival: datetime.datetime) -> None:
        self.downtime = int((self.depart_time - arrival).total_seconds()) // 60

    @staticmethod
    def calculate_running_time(first_depart: datetime.datetime, last_arrival: datetime.datetime) -> int:
        return int((last_arrival - first_depart).total_seconds()) // 60
