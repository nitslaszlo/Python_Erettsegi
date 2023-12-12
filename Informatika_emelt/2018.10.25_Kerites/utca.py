from Megoldás import Megoldás


def main() -> None:
    # 1. feladat:
    m: Megoldás = Megoldás('kerites.txt')

    print(f'2. feladat\nAz eladott telkek száma: {m.telkek_száma}\n\n')

    print(f'3. feladat\nA {m.utolsó_eladott_telek.oldal} oldalon adták el az utolsó telket.')
    print(f'Az utolsó telek házszáma: {m.utolsó_eladott_telek.házszám}\n\n')

    print(f'4.feladat\nA szomszédossal egyezik a kerítés színe: {m.szomszédossal_azonos_szín}\n\n')

    input_házszám: int = int(input('5. feladat\nAdjon meg egy házszámot! '))
    print(f'A kerítés színe / állapota: {m.keresett_telek(input_házszám).szín}')
    print(f'Egy lehetséges festési szín: {m.lehetséges_szín(input_házszám)}')

    # 6. feladat:
    m.utcaképet_ír('utcakep.txt')


if __name__ == "__main__":
    main()
