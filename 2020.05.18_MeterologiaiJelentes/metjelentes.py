from Megoldás import Megoldás


def main() -> None:
    m: Megoldás = Megoldás('tavirathu13.txt')

    input_település: str = input('2. feladat\nAdja meg egy település kódját! Település: ').upper()
    print(m.utolsó_jelentés_ideje(input_település))

    print(f'3. feladat')
    print(f'A legalacsonyabb hőmérséklet:  {m.min_t_j([])} fok.')
    print(f'A legmagasabb hőmérséklet: {m.max_t_j([])} fok.')

    print('4. feladat')
    if len(m.szélcsendes) == 0:
        print('Nem volt szélcsend a mérések idején.')
    else:
        for e in m.szélcsendes:
            print(f'{e.településkód} {e.időpont}')

    print(f'5. feladat\n{m.hőmérséklet_stat}')

    print('6. feladat\nA fájljok elkészültek.')
    m.adatokat_ír()


if __name__ == '__main__':
    main()
