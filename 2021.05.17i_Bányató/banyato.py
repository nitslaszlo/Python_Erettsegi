from Megoldás import Megoldás


def main() -> None:
    m: Megoldás = Megoldás('melyseg.txt')
    print('2. feladat: ')
    input_sor: int = int(input('A mérés sorának azonosítója='))
    input_oszlop: int = int(input('A mérés sorának azonosítója='))
    print(f'A mért mélység az adott helyen {m.mélység(input_sor, input_oszlop)} dm')

    print(f'3. feladat\nA tó felszíne: {m.felszín} m2, átlagos mélysége: {m.átlagos_mélység_m:.2f} m')

    print(f'4. feladat\nA tó legnagyobb mélysége: {m.max_mélység} dm')
    print(f'A legmélyebb helyek sor-oszlop koordinátái:\n {m.legmélyebb_helyek}')

    print(f'5. feladat\nA tó partvonala {m.partvonal_hossza} m hosszú')



if __name__ == "__main__":
    main()
