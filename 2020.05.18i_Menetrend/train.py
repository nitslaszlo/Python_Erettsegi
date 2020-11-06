import datetime


class Train(object):
    @property
    def is_first_station(self) -> bool:
        return self.station == 0

    def __init__(self, line: str) -> None:
        tid, station, hour, minute, status = line.strip().split('\t')
        self.id = int(tid)
        self.station = int(station)
        self.time = datetime.datetime(2020, 1, 1, int(hour), int(minute))
        self.time_is_depart = status == 'I'  # False if time is arrival time
        self.downtime = -1

    def calculate_downtime(self, arrival: datetime.datetime) -> None:
        if self.time_is_depart:
            self.downtime = int((self.time - arrival).total_seconds()) // 60

    @staticmethod
    def calculate_running_time(first_depart: datetime.datetime, last_arrival: datetime.datetime) -> int:
        return int((last_arrival - first_depart).total_seconds()) // 60
