from __future__ import annotations
from megoldas import Megoldas


def main() -> None:
    m: Megoldas = Megoldas('tavirathu13.txt')

    input_telepules: str = input('2. feladat\nAdja meg egy település kódját! Település: ').upper()
    print(m.utolso_jelentes_ideje(input_telepules))

    print(f'3. feladat')
    print(f'A legalacsonyabb hőmérséklet:  {m.min_t_j()} fok.')
    print(f'A legmagasabb hőmérséklet: {m.max_t_j()} fok.')

    print('4. feladat')
    if len(m.szelcsendes) == 0:
        print('Nem volt szélcsend a mérések idején.')
    else:
        for i in m.szelcsendes:
            print(f'{i.telepuleskod} {i.idopont}')

    print(f'5. feladat\n{m.homerseklet_stat}')

    print('6. feladat\nA fáljok elkészültek.')
    m.write_data()


if __name__ == '__main__':
    main()
