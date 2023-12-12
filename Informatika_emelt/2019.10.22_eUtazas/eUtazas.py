from Megoldás import Megoldás


def main() -> None:
    # 1. feladat: adatok beolvasása, tárolása
    m: Megoldás = Megoldás('utasadat.txt')

    print(f'2. feladat\nA buszra {m.felszállók_száma} utas akart felszállni.')

    print(f'3. feladat\nA buszra {m.érvénytelen_felszállás} utas nem szállhatott fel.')

    print(f'4. feladat\nA legtöbb utas ({m.legtöbb_felszálló.felszálló_fő} fő) a {m.legtöbb_felszálló.megálló}. megállóban próbált felszállni.')

    print('5. feladat')
    print(f'Ingyenes utazók száma: {m.ingyenes_utazás} fő')
    print(f'A kedvezményesen utazók száma: {m.kedvezményes_utazás} fő')

    m.figyelmeztetést_ír('figyelmeztetes.txt')


if __name__ == "__main__":
    main()
