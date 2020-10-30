import os
from solution import Solution


def main():
    os.system('cls||clear')
    sol: Solution = Solution('vonat.txt')

    print(f'2. feladat\nAz állomások száma: {sol.num_of_stations}\nA vonatok száma: {sol.num_of_trains}')

    print(f'3. feladat\nA(z) {sol.max_downtime_data.id}. vonat a(z) {sol.max_downtime_data.station}. állomáson '
          f'{sol.max_downtime_data.downtime} percet állt.')

    input_train_id: int = int(input('4. feladat\nAdja meg egy vonat azonosítóját! '))
    input_time: str = input('Adjon meg egy időpontot (óra perc)! ')

    print(f'5. feladat\n{sol.train_running_time_check(input_train_id)}.')

    # 6. feladat
    sol.write_data(input_train_id)

    print(f'7. feladat\n{sol.where_are_the_trains(input_time)}')


if __name__ == '__main__':
    main()
