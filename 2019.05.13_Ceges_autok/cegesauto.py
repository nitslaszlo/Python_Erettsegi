from Megoldás import Megoldás


def main() -> None:
    m: Megoldás = Megoldás('autok.txt')

    print(f'2. feladat\n{m.utolsó_kivitel.nap}. nap rendszám: {m.utolsó_kivitel.rendszám}')

    input_nap: str = input('3. feladat\nNap: ')
    print(f'Forgalom a(z) {input_nap}. napon:')
    print(m.forgalom(input_nap))

    print(f'4. feladat\nA hónap végén {m.kintlévő_autók_száma} autót nem hoztak vissza.')

    print(f'5.feladat\n{m.statisztika}')

    print(f'6. feladat\nLeghosszabb út: {m.max_áthajtás.megtett_km} km, személy: {m.max_áthajtás.szem_azon}')

    input_rendszám: str = input('7. feladat\nRendszám: ')
    m.menetlevelet_ír(input_rendszám)
    print('Menetlevél kész.')


if __name__ == "__main__":
    main()
