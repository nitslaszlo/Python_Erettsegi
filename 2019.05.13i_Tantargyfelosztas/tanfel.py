from Megoldás import Megoldás


def main() -> None:
    m: Megoldás = Megoldás('beosztas.txt')

    print(f'2. feladat\nA fájlban {m.bejegyzések_száma} bejegyzés van.')

    print(f'3. feladat\nAz iskolában a heti összóraszám: {m.összóraszám}')

    input_név: str = input('4. feladat\nEgy tanár neve= ')
    print(f'A tanár heti óraszáma: {m.tanári_óraszám(input_név)}')

    # 5. feladat:
    m.ofőket_ír('of.txt')

    input_osztály: str = input('6. feladat\nOsztály= ')
    input_tantárgy: str = input('Tantárgy= ')
    print(f'Csoportbontás{"ban" if m.csoportbontás_van(input_osztály, input_tantárgy) else " nélkül"} tanulják.')

    print(f'7. feladat\nAz iskolában {m.tanárok_száma} tanár tanít.')


if __name__ == "__main__":
    main()
