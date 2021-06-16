class Megoldás(object):
    matrix: list[int][int] = list()

    def __init__(self, forrás: str) -> None:
        sor_index: int = 1
        with open(forrás, 'r', encoding='UTF8') as sr:
            for sor in sr.read().splitlines():
                adatok = sor.split(' ')
                for adat in adatok:
                    

