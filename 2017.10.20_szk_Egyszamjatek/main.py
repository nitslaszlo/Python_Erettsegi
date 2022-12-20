from Megoldas import Megoldas


def main() -> None:
    # 2. feladat:
    m: Megoldas = Megoldas('egyszamjatek.txt')

    print(f'3. feladat: Játékosok száma: {m.jatekosok_szama}')

    print(f'4. feladat: Fordulók száma: {m.fordulok_szama}')

    print(f'5. feladat: Az első fordulóban {"" if m.volt_egyes_tipp else "nem "}volt egyes tipp!')

    print(f'6. feladat: Legnagyobb tipp a fordulók során: {m.jatek_legnagyobb_tipp}')

    input_fordulo: int = -1
    try:
        input_fordulo = int(input(f'7. feladat: Kérem a forduló sorszámát [1-{m.fordulok_szama}]: '))
    except ValueError:
        input_fordulo = 1

    if input_fordulo < 1 or input_fordulo > m.fordulok_szama:
        input_fordulo = 1

    print(f'8. feladat: {m.nyertes_tipp_szoveg(input_fordulo)}')

    print(f'9. feladat: {m.nyertes_jatekos_szoveg(input_fordulo)}')

    # 10. feladat:
    m.allomany_kezelese('nyertes.txt', input_fordulo)


if __name__ == "__main__":
    main()
