from Megoldás import Megoldás


def main() -> None:
    m: Megoldás = Megoldás('melyseg.txt')
    print('2. feladat: ')
    input_sor: int = int(input('A mérés sorának azonosítója='))
    input_oszlop: int = int(input('A mérés sorának azonosítója='))
    print(f'A mért mélység az adott helyen {m.mélység(input_sor, input_oszlop)} dm')

    print(f'3. feladat\nA tó felszíne: {m.felszín} m2, átlagos mélysége: {m.átlagos_mélység:.2f} m')


if __name__ == "__main__":
    main()
